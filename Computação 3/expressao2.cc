#include <cstdlib>
#include <ctime>
#include <iostream>
#include <sys/timeb.h>
#include <vector>
#include <memory>
#include <type_traits>

using namespace std;

template <int L, int C>
void inicializa( double (&m)[L][C] ) {
	for( int i = 0; i < L; i++ )
		for( int j = 0; j < C; j++ )
			m[i][j] = rand() / (double) RAND_MAX;
}

template <int L, int CL, int C>
void mult( double (&res)[L][C], const double (&a)[L][CL], const double (&b)[CL][C] ) {
	for( int i = 0; i < L; i++ )
		for( int j = 0; j < C; j++ )
			res[i][j] = 0;

	for( int i = 0; i < L; i++ )
		for( int j = 0; j < C; j++ )
			for( int k = 0; k < CL; k++ )
				res[i][j] += a[i][k] * b[k][j];
}

template <int L, int C>
void somam( double (&res)[L][C], const double (&a)[L][C], const double (&b)[L][C] ) {
	for( int i = 0; i < L; i++ )
		for( int j = 0; j < C; j++ )
			res[i][j] = a[i][j]+b[i][j];
}

template <class M1, class M2>
class Otimizador;

template <int L, int C>
class Matriz {
	public:
	Matriz(){inicializa(m);}
	template<class Otm>
	Matriz(Otm otm) {
		m = otm.otimiza().m;
	}
	
	constexpr int nLin() {
		return L;
	}
	constexpr int nCol() {
		return C;
	}
	
	template< int C2>
	Matriz<L, C2> mul(const Matriz<C, C2>& m2) const {
		Matriz<L, C2> ret;
		mult(ret.m, m, m2.m);
		return ret;
	}
	
	Matriz<L, C> soma(const Matriz<L, C>& m2) const {
		Matriz<L, C> ret;
		somam(ret.m, m, m2.m);
		return ret;
	}
	
	void print () {
		cout <<  "[";
		for (int i = 0; i < L; i++){
			cout << " ";
			for (int j = 0; j < C; j++) {
				cout << m[i][j] << " ";
			}
			if (i != L-1 ) cout << endl;
		}
		cout << "]";
	}
	auto otimiza() { 
		return *this;
	}
	double m[L][C];
	
	template < class Otm >
	auto operator = (Otm otm) {
		cout << "asjiash" << endl;
		m = otm.otimiza().m;
		return *this;
	}
	
};

template <int L, int LC, int C>
Matriz<L,C> operator * (const Matriz<L, LC>& a , const Matriz<LC, C>& b ) {
	return a.mul(b);
}

template <int L, int C>
Matriz<L,C> operator + (const Matriz<L, C>& a , const Matriz<L, C>& b ) {
	return a.soma(b);
}



template <typename F>
class Apply {
public:
  Apply( F f ): f(f) {}
  
	template< int L, int C>
	Matriz<L,C> apply(const Matriz<L,C>& m) const {
		Matriz<L,C> res;
		for (int i = 0; i < L; i ++)
			for (int j = 0; j < C; j++) 
				res.m[i][j] = f(m.m[i][j]);
		return res;

	}
	
	template< int L, int C>
	void applyVoid(const Matriz<L,C>& m) const {
		Matriz<L,C> res;
		for (int i = 0; i < L; i ++)
			for (int j = 0; j < C; j++) 
				f(m.m[i][j]);
	}
  
	template <int L, int C>
	auto operator()( const Matriz<L,C>& m ) const {
		if constexpr (is_same<void, decltype(f(m.m[0][0]))>::value ) {
			applyVoid(m);
		}
		else {
			return apply(m);
		}
	}
private:
  F f;
};

template <typename F> Apply<F> apply( F f ) { return Apply<F>(f); }
int main () {
Matriz<100,1> a;
  Matriz<1,100> b;
	auto tamanho = apply([](auto x){cout << x;});
  auto x = a * b;
  tamanho(x);
  //x.print();
  auto y = a + a;
  //y.print();
}
