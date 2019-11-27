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
void mult( vector<vector<double>> &res, const vector<vector<double>> &a, const vector<vector<double>> &b ) {
	for( int i = 0; i < res.size(); i++ )
		for(unsigned int j = 0; j < res[i].size(); j++ )
			res[i][j] = 0;

	for( unsigned int i = 0; i < res.size(); i++ )
		for(unsigned int j = 0; j < res[i].size(); j++ )
			for( unsigned int k = 0; k < a[i].size(); k++ )
				res[i][j] += a[i][k] * b[k][j];
}

void somam( vector<vector<double>> &res, const vector<vector<double>> &a, const vector<vector<double>> &b  ) {
	for( unsigned int i = 0; i < a.size(); i++ )
		for( unsigned int j = 0; j < a[i].size(); j++ )
			res[i][j] = a[i][j]+b[i][j];
}

template <class M1, class M2>
class Otimizador;

template <int L, int C>
class Matriz {
	public:
	Matriz(){
		m.resize(L);
		for(int i = 0; i < L; i++) {
			m[i].resize(C);
		}
	}
	template<class Otm>
	Matriz(Otm otm) {
		m.resize(L);
		auto otm_m = otm.otimiza().m;
		for(int i = 0; i < L; i++) {
			m[i].resize(C);
			for (int j = 0; j < C; j++)
				m[i][j] = otm_m[i][j];
		}
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
		//mult(ret.m, m, m2.m);
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
	auto otimiza() const{ 
		return *this;
	}
	vector<vector<double>> m;
	
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

	auto otimiza() const{
		return a.mul(b.otimiza());
	}
	void print () {
		otimiza().print();
	}
	
	private:
	M1 a;
	M2 b;
	
};

/*
template <int L, int LC, int C>
Matriz<L,C> operator * (const Matriz<L, LC>& a , const Matriz<LC, C>& b ) {
	return a.mul(b);
}*/

template <int L, int C>
Matriz<L,C> operator + (const Matriz<L, C>& a , const Matriz<L, C>& b ) {
	return a.soma(b);
}

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
	
	template <class M1, class M2>
	auto operator()( const Otimizador<M1, M2>& otm ) const {
		auto res = otm.otimiza();
		if constexpr (is_same<void, decltype(f(res.m[0][0]))>::value) {
			applyVoid(res);
		}
		else {
			return apply(res);
		}
	}
private:
  F f;
};

template <typename F> Apply<F> apply( F f ) { return Apply<F>(f); }
int main () {
	auto tamanho = [](auto m){return m.nLin() * m.nCol();};
  Matriz<1000,1> a;
  Matriz<1,1000> b;
  Matriz<1000,1000> c;
  int tempo = 0, lapso1, lapso2;
  

  tempo = clock();

  Matriz<1000,1000> x1 = a * b;
  Matriz<1000,1000> x2 = x1 * c;

  cout << tamanho(x1) << endl;
  cout << tamanho(x2) << endl;

	lapso1 = clock() - tempo;

  tempo = clock();

  Matriz<1000,1000> y = a * b * c;

  lapso2 = clock() - tempo;
  cout << tamanho(y) << endl;

  if( lapso1/lapso2 > 10 )
    cout << "Otimizou" << endl;
  else
    cout << "Não otimizou" << endl;
}
