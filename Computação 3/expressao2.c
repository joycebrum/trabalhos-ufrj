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
	Matriz<L, C2> mul(Matriz<C, C2> m2) {
		Matriz<L, C2> ret;
		mult(ret.m, m, m2.m);
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

template <class M1, class M2>
class Otimizador {
	public:
	template<class T1, class T2>
	Otimizador(const Otimizador<T1, T2>& a, const M2& b): a(a), b(b) { }
	template<int L, int C>
	Otimizador(const Matriz<L, C>& a , const M2& b ): a(a), b(b) { }
	
	
	constexpr int nLin() {
		return a.nLin();
	}
	constexpr int nCol() {
		return b.nCol();
	}
	
	M1 getFirst() const { return a; }
	M2 getSecond() const { return b; }
	
	template <class T>
	auto mul(T sec) {
		return a.mul(b).mul(sec);
	}

	auto otimiza() {
		cout << "otimiza";
		return a.mul(b.otimiza());
	}
	void print () {
		otimiza().print();
	}
	
	private:
	M1 a;
	M2 b;
	
};



template <int L, int LC, int C>
Otimizador<Matriz<L, LC>, Matriz<LC, C>> operator * (const Matriz<L, LC>& a , const Matriz<LC, C>& b ) {
	return Otimizador<Matriz<L, LC>, Matriz<LC, C>>(a,b);
}

template <typename M1, typename M2, int LC, int C>
auto operator * (const Otimizador<M1, M2>& a , const Matriz<LC, C>& b ) {
	M2 second  = a.getSecond();
	if constexpr (second.nLin() == 1) { // matriz linha
		Otimizador<M2, Matriz<LC, C>> otm(second, b);
		M1 first = a.getFirst();
		return Otimizador<M1, Otimizador<M2, Matriz<LC, C> > >(first, otm);
	}  
	else {
		return Otimizador<Otimizador<M1, M2>, Matriz<LC, C>>(a,b);
	}
}

template <typename F>
class Apply {
public:
  Apply( F f ): f(f) {}
  
  template< int L, int C>
  Matriz<L, C> apply(const Matriz<L,C>& m) const {
	  Matriz<L,C> res;
		for (int i = 0; i < L; i ++)
			for (int j = 0; j < C; j++) 
				res.m[i][j] = f(m.m[i][j]);
		return res;
  }
  
  template <int L, int C>
  Matriz<L,C> operator()( const Matriz<L,C>& m ) const {
		return apply(m);
  }
  template <class M1, class M2>
  auto operator()( const Otimizador<M1, M2>& otm ) const {
		auto res = otm.otimiza();
		return apply(res);
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
  auto y = b * a;
  //y.print();
}
