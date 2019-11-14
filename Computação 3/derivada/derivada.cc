#include <iostream>
#include <math.h>
#include <type_traits>
#include <sstream>

using namespace std;

template<typename F>
class Seno;
template<typename F>
class Cosseno;


template< typename T>
string monta_parenteses_str(T v) {
	if (v.parenteses_str()) {
		return "("+v.str()+")";
	}
	return v.str();
}
template< typename T>
string monta_parenteses_dx(T v) {
	if (v.parenteses_dx()) {
		return "("+v.dx_str()+")";
	}
	return v.dx_str();
}

class Cte {
public:
  Cte( double c ): c(c) {}
  
  double operator()( double v ) {
    return c;
  }
  double dx(double v) {
	  return 0;
  }
	string str() const {		
		ostringstream strs;
		strs << c;
		return strs.str();
	}
	string dx_str() const {
		return "0";
	}
	Cte v_dx() {
		return Cte(0);
	}
	bool parenteses_str() { return false; }
	bool parenteses_dx() { return false; }
  
private:
  double c;
};
class X {
public:
	double operator()( double v ) {
		return v;
	}
	double e(double v) {
		return v;
	} 
	double dx(double v) {
		return 1;
	}
	
	Cte v_dx() {
		return Cte(1);
	}
	string str() const {
		return "x";
	}
	string dx_str() const {
		return "1";
	}
	bool parenteses_str() { return false; }
	bool parenteses_dx() { return false; }
};
X x;

class String {
public:
	String( string c ): c(c) {}
  
	string operator()( double v ) {
		return c;
	}
	string str() const {		
		return c;
	}
	string dx_str() const {
		return c;
	}
	bool parenteses_str() { return c.length() > 1; }
	bool parenteses_dx() { return c.length() > 1; }
  
private:
  string c;
};


template <typename F1, typename F2>
class Soma {
public:
	Soma( F1 f1, F2 f2 ): f1(f1), f2(f2) {}
	  
	double operator()( double v ) {
		return f1(v) + f2( v );
	}
	template< typename D1, typename D2>
	auto v_dx() {
		return Soma<D1, D2>(f1.v_dx, f2.v_dx);
	}
	double e( double v ) {
		return f1(v) + f2(v);
	}
	  
	double dx( double v ) {
		return f1.dx(v) + f2.dx(v);
	}
	string str() const {
		if (f1.str() == "0" || f2.str() == "0") {
			if (f1.str() == "0" && f2.str() == "0") {
				return "0";
			}
			if (f1.str() == "0") {
				return f2.str();
			}
			return f1.str();
		}
		return f1.str() + "+" + f2.str();
	}
	string dx_str() const {
		if (f1.dx_str() == "0" || f2.dx_str() == "0") {
			if (f1.dx_str() == "0" && f2.dx_str() == "0") {
				return "0";
			}
			if (f1.dx_str() == "0") {
				return f2.dx_str();
			}
			return f1.dx_str();
		}
		return f1.dx_str() + "+" + f2.dx_str();
	}
	
	bool parenteses_str() { 
		if (f1.str() == "0" || f2.str() == "0") {
			return false;
		}
		return true;
	}
	bool parenteses_dx() { 
		if (f1.dx_str() == "0" || f2.dx_str() == "0") {
			return false;
		}
		return true;
	}
  
private:
	F1 f1;
	F2 f2;
};



template <typename F1, typename F2>
class Multiplica {
public:
  Multiplica( F1 f1, F2 f2 ): f1(f1), f2(f2) {}
  
	double operator()( double v ) {
		return f1(v) * f2( v );
	}
	double e( double v ) {
		return f1(v) * f2(v);
	}
	double dx( double v ) {
		return f1(v)*f2.dx(v) + f1.dx(v)*f2(v);
	}
	template< typename D1, typename D2>
	auto v_dx() {
		return Soma< Multiplica<D1,F2>, Multiplica<F1, D2> >(Multiplica<D1, F2>(f1.v_dx, f2), Multiplica<F1, D2>(f1, f2.v_dx));
	}
	string str() const {
		if (f1.str() == "0") {
			return "0";
		}
		if (f2.str() == "0") {
			return "0";
		}
		if (f1.str() == "1") {
			if (f2.str() == "1") {
				return "1";
			}
			return f2.str();
		}
		if (f2.str() == "1") {
			return f1.str();
		}
		if (f1.str() == "-1") {
			if (f2.str() == "-1") {
				return "1";
			}
			return "-"+f2.str();
		}
		if (f2.str() == "-1") {
			return "-"+f1.str();
		}
		return monta_parenteses_str(f1) + "*" + monta_parenteses_str(f2);
	}
	
	
	
	string dx_str() const {
		Multiplica<String, F2> fator1( String(f1.dx_str()), f2 );
		Multiplica<F1, String> fator2 (f1, String(f2.dx_str()));
		Soma<Multiplica<String, F2>, Multiplica<F1, String>> soma (fator1,fator2);
		return soma.str();
	}
	
	bool parenteses_str() { 
		if (f1.str() == "0" || f2.str() == "0" || f1.str() == "1" || f2.str() == "1") {
			return false;
		}
		return true;
	}
	bool parenteses_dx() { 
		if (f1.str() == "0" || f2.str() == "0" || f1.dx_str() == "0" || f2.dx_str() == "0") {
			return false;
		}		
		return true;
	}
  
private:
	F1 f1;
	F2 f2;
	string getStr(string v1, string v2) {
		if (v1 == "0") {
			return "0";
		}
		if (v2 == "0") {
			return "0";
		}
		if (v1 == "1") {
			if (v2 == "1") {
				return "1";
			}
			return f2.str();
		}
		if (v2 == "1") {
			return f1.str();
		}
		return "(" + v1 + ")*(" + v2 + ")";
	}
};


template<typename F>
class Cosseno {
	public:
	Cosseno(F f): f(f) {}
	double operator () (double v) {
		return cos(f(v));
	}
	double e(double v) {
		return sin(f(v));
	}
	double dx(double v) {
		return -1*sin(f.e(v))*f.dx(v);
	}
	string str() const {
		return "cos(" + f.str() + ")";
	}
	string dx_str() const {
		Multiplica<String, String> fator2 (String("-sin(" + f.str() + ")"), String(f.dx_str()));
		return fator2.str();
	}
	template<typename D2>
	auto v_dx() {
		return Multiplica<Multiplica<Cte, Seno<F>>, D2>(Multiplica<Cte, Seno<F>>(Cte(-1), Seno<F>(f)), f.v_dx());
	}
	bool parenteses_str() { return false; }
	bool parenteses_dx() { 
		if (f.dx_str() == "0" || f.dx_str() == "1") {
			return false;
		}		
		return true;
	}
	private:
	F f;
};

template<typename F>
class Seno {
	public: 
	Seno(F f):f (f) {}
	
	double operator() (double v) {
		return sin(f(v));
	}
	double e(double v) {
		return sin(f(v));
	}
	double dx(double v) {
		return cos(f.e(v))*f.dx(v);
	}
	string str() const {
		return "sin(" + f.str() + ")";
	}
	string dx_str() const {
		Multiplica<String, String> fator2 (String("cos(" + f.str() + ")"), String(f.dx_str()));
		return fator2.str();
	}
	template<typename D2>
	auto v_dx() {
		return Multiplica< Cosseno<F>, D2>(Cosseno<F>(f), f.v_dx());
	}
	bool parenteses_str() { return false; }
	bool parenteses_dx() { 
		if (f.dx_str() == "0" || f.dx_str() == "1") {
			return false;
		}		
		return true;
	}
	private:
	F f;
};


template <typename F1, typename F2>
class Subtracao {
public:
	Subtracao( F1 f1, F2 f2 ): f1(f1), f2(f2) {}
	  
	double operator()( double v ) {
		return f1(v) - f2( v );
	}
	
	double e( double v ) {
		return f1(v) - f2(v);
	}
	  
	double dx( double v ) {
		return f1.dx(v) - f2.dx(v);
	}
	string str() const {
		if (f1.str() == "0" || f2.str() == "0") {
			if (f1.str() == "0" && f2.str() == "0") {
				return "0";
			}
			if (f1.str() == "0") {
				return "-" + f2.str();
			}
			return f1.str();
		}
		return monta_parenteses_str(f1) + "-" + monta_parenteses_str(f2);
	}
	string dx_str() const {
		if (f1.dx_str() == "0" || f2.dx_str() == "0") {
			if (f1.dx_str() == "0" && f2.dx_str() == "0") {
				return "0";
			}
			if (f1.dx_str() == "0") {
				return f2.dx_str();
			}
			return f1.dx_str();
		}
		return monta_parenteses_dx(f1) + "-" + monta_parenteses_dx(f2);
	}
	template<typename D1, typename D2>
	auto v_dx() {
		return Subtracao< D1, D2>(f1.v_dx(), f2.v_dx());
	}
	bool parenteses_str() { 
		if (f1.str() == "0" || f2.str() == "0") {
			return false;
		}
		return true;
	}
	bool parenteses_dx() { 
		if (f1.dx_str() == "0" || f2.dx_str() == "0") {
			return false;
		}
		return true;
	}
  
private:
	F1 f1;
	F2 f2;
};


template <typename F>
class Potencia {
	public:
	Potencia(F f, int potencia): f(f), potencia(potencia) {}
	double operator () (double v) {
		return pow(f(v), potencia);
	}
	double e(double v) {
		return pow( f(v), potencia );
	}
	double dx(double v) {
		return potencia * pow( f(v), potencia-1 ) * f.dx(v);
	}
	template<typename D>
	auto v_dx() {
		return Multiplica< Multiplica< Cte, D >, Potencia<F> >(Multiplica< Cte, D >(potencia, f.v_dx()), Potencia<F>(f, potencia-1));
	}
	string str() const {
		if (potencia == 0) {
			return "1";
		}
		else if (potencia == 1) {
			return f.str();
		}
		ostringstream strs;
		strs << potencia;
		return monta_parenteses_str(f) + "^" + strs.str();
	}
	string dx_str() const {
		ostringstream strs;
		strs << potencia-1;
		ostringstream strs2;
		strs2 << potencia;
		if (potencia == 0 || f.dx_str() == "0") {
			return "0";
		}
		else if (potencia ==1){
			return "1";
		}
		else if (potencia == 2) {
			return "2*" + monta_parenteses_dx(f)  + "*" + monta_parenteses_str(f);
		}
		Multiplica<String, F> fator1( String(f.dx_str()), f );
		return strs2.str() + "*" + fator1.str() + "^" + strs.str();
	}
	
	bool parenteses_str() { return false; }
	bool parenteses_dx() { 
		if (potencia == 0 || potencia == 1 || f.dx_str() == "0") {
			return false;
		}	
		return true;
	}
	private:
	F f;
	int potencia;
};


template <typename F1, typename F2>
class Divide {
public:
	Divide( F1 f1, F2 f2 ): f1(f1), f2(f2) {}
	  
	double operator()( double v ) {
		return f1(v) / f2( v );
	}
	double e( double v ) {
		return f1(v) / f2(v);
	}
	  
	double dx( double v ) {
		return (f1(v)*f2.dx(v) - f1.dx(v)*f2(v)) / (f2(v) * f2(v));
	}
	template<typename D1, typename D2>
	auto v_dx() {
		Potencia <F2> pot (f2, 2);
		Subtracao< Multiplica<D1,F2>, Multiplica<F1, D2> > subs (Multiplica<D1, F2>(f1.v_dx, f2), Multiplica<F1, D2>(f1, f2.v_dx));
		return Divide<Subtracao< Multiplica<D1,F2>, Multiplica<F1, D2> >, Potencia <F2>>(subs, pot);
	}
	string str() const {
		if (f2.str()=="1") {
			return f1.str();
		}
		return monta_parenteses_str(f1) + "/" + monta_parenteses_str(f2);
	}
	string dx_str() const {
		Multiplica<decltype(f1.v_dx()), F2> fator1 (f1.v_dx, f2);
		Multiplica<F1, decltype(f2.v_dx())> fator2 (f1, f2.v_dx());
		Subtracao<Multiplica<decltype(f1.v_dx()), F2>, Multiplica<F1, decltype(f2.v_dx())>> subs (fator1, fator2);
		Potencia<F2> pot (f2, 2);
		if (f2.str()=="1") {
			return subs.str();
		}
		return monta_parenteses_str(subs) + "/" + pot.str();
	}
	bool parenteses_pot() { return true; }
	
	bool parenteses_str() { return false; }
	bool parenteses_dx() { 
		Multiplica<decltype(f1.v_dx()), F2> fator1 (f1.v_dx, f2);
		Multiplica<F1, decltype(f2.v_dx())> fator2 (f1, f2.v_dx());
		if (f2.str() == "1" && (fator1.str() == "0" || fator2.str() == "0")) {
			return false;
		}		
		return true;
	}
  
private:
	F1 f1;
	F2 f2;
};
template <typename F>
class Exponencial {
	public:
	Exponencial(F f): f(f) {}
	double operator () (double v) {
		return exp( f(v) );
	}
	double e (double v) {
		return exp( f(v) );
	}
	double dx (double v) {
		return exp( f(v) )*f.dx(v);
	}
	template<typename D>
	auto v_dx() {
		return Multiplica< Exponencial<F>, D > (Exponencial<F>(f), f.v_dx());
	}
	string str() const {
		return "exp(" + f.str() + ")";
	}
	string dx_str() const {
		Multiplica<Exponencial<F>, String> fator1( Exponencial<F>(f), String(f.dx_str()) );
		return fator1.str();
	}
	bool parenteses_str() { return false; }
	bool parenteses_dx() { 
		if (f.dx_str() == "1" || f.dx_str() == "0" ) { return false; } 
		Multiplica<Exponencial<F>, String> fator1( Exponencial<F>(f), String(f.dx_str()) );
		return fator1.parenteses_dx();
	}
	private:
	F f;
};


template <typename F>
class Logaritmo {
	public:
	Logaritmo(F f): f(f) {}
	double operator () (double v) {
		return log( f(v) );
	}
	double e (double v) {
		return log( f(v) );
	}
	double dx (double v) {
		return (1/f(v)) * f.dx(v);
	}
	template<typename D>
	auto v_dx() {
		return Multiplica< Divide<Cte, F>, D > (Divide<Cte, F>(Cte(1), f), f.v_dx());
	}
	string str() const {
		return "log(" + f.str() + ")";
	}
	string dx_str() const {
		Divide<Cte, F> div (Cte(1), f);
		Multiplica<Divide<Cte, F>, String> fator1(div, String(f.dx_str()) );
		return fator1.str();
	}
	bool parenteses_str() { return false; }
	bool parenteses_dx() { 
		Divide<Cte, F> div (Cte(1), f);
		Multiplica<Divide<Cte, F>, decltype(f.v_dx())> fator1(div, f.v_dx() );
		return fator1.parenteses_dx();
	}
	private: 
	F f;
};

template <typename F1, typename F2> 
Multiplica<F1,F2> operator * ( F1 f1, F2 f2 ) {
   return Multiplica<F1,F2>( f1, f2 );
}

template <typename F2> 
Multiplica<Cte,F2> operator * ( double n, F2 f2 ) {
   return Multiplica<Cte,F2>( n, f2 );
}

template <typename F1> 
Multiplica<F1,Cte> operator * ( F1 f1, double n ) {
   return Multiplica<F1,Cte>( f1, n );
}

template <typename F2> 
Multiplica<Cte,F2> operator * ( int n, F2 f2 ) {
   return Multiplica<Cte,F2>( n, f2 );
}

template <typename F1> 
Multiplica<F1,Cte> operator * ( F1 f1, int n ) {
   return Multiplica<F1,Cte>( f1, n );
}

template <typename F1, typename F2> 
Divide<F1,F2> operator / ( F1 f1, F2 f2 ) {
   return Divide<F1,F2>( f1, f2 );
}

template <typename F2> 
Divide<Cte,F2> operator / ( double n, F2 f2 ) {
   return Divide<Cte,F2>( n, f2 );
}

template <typename F1> 
Divide<F1,Cte> operator / ( F1 f1, double n ) {
   return Divide<F1,Cte>( f1, n );
}

template <typename F2> 
Divide<Cte,F2> operator / ( int n, F2 f2 ) {
   return Divide<Cte,F2>( n, f2 );
}

template <typename F1> 
Divide<F1,Cte> operator / ( F1 f1, int n ) {
   return Divide<F1,Cte>( f1, n );
}
template <typename F1, typename F2> 
Soma<F1,F2> operator + ( F1 f1, F2 f2 ) {
   return Soma<F1,F2>( f1, f2 );
}

template <typename F2> 
Soma<Cte,F2> operator + ( double n, F2 f2 ) {
   return Soma<Cte,F2>( n, f2 );
}

template <typename F1> 
Soma<F1,Cte> operator + ( F1 f1, double n ) {
   return Soma<F1,Cte>( f1, n );
}

template <typename F2> 
Soma<Cte,F2> operator + ( int n, F2 f2 ) {
   return Soma<Cte,F2>( n, f2 );
}

template <typename F1> 
Soma<F1,Cte> operator + ( F1 f1, int n ) {
   return Soma<F1,Cte>( f1, n );
}

template <typename F1, typename F2> 
Subtracao<F1,F2> operator - ( F1 f1, F2 f2 ) {
   return Subtracao<F1,F2>( f1, f2 );
}

template <typename F2> 
Subtracao<Cte,F2> operator - ( double n, F2 f2 ) {
   return Subtracao<Cte,F2>( n, f2 );
}

template <typename F1> 
Subtracao<F1,Cte> operator - ( F1 f1, double n ) {
   return Subtracao<F1,Cte>( f1, n );
}

template <typename F2> 
Subtracao<Cte,F2> operator - ( int n, F2 f2 ) {
   return Subtracao<Cte,F2>( n, f2 );
}

template <typename F1> 
Subtracao<F1,Cte> operator - ( F1 f1, int n ) {
   return Subtracao<F1,Cte>( f1, n );
}

template<typename F, typename Pot>
Potencia<F> operator ->* (F f, Pot valor) {
	//constexpr auto inteiro = is_same_v< int, Pot>::value;
	static_assert( !std::is_same<Pot , double>::value, "Operador de potenciação definido apenas para inteiros" );
	return Potencia<F>(f, valor);
}

template<typename F>
Seno<F> sin(F f) {
	return Seno<F>(f);
}

template<typename F>
Cosseno<F> cos(F f) {
	return Cosseno<F>(f);
}

template<typename F>
Exponencial<F> exp(F f) {
	return Exponencial<F>(f);
}

template<typename F>
Logaritmo<F> log(F f) {
	return Logaritmo<F>(f);
}

int main() {
	auto f = exp( x * log( x - 8.0 ) + 1.0 );
	//auto f =  1.0 / (sin(x)->*2 + cos(x)->*2)->*4 ;
	cout << f.str() <<  endl << f.dx_str();
  return 0;
}

