#include <iostream>
#include <math.h>
#include <type_traits>

using namespace std;

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
};
X x;

class Cte {
public:
  Cte( double c ): c(c) {}
  
  double operator()( double v ) {
    return c;
  }
  double dx(double v) {
	  return 0;
  }
  
private:
  double c;
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
	private:
	F f;
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
  
private:
	F1 f1;
	F2 f2;
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
  
private:
	F1 f1;
	F2 f2;
};

template <typename F1, typename F2>
class Soma {
public:
	Soma( F1 f1, F2 f2 ): f1(f1), f2(f2) {}
	  
	double operator()( double v ) {
		return f1(v) + f2( v );
	}
	double e( double v ) {
		return f1(v) + f2(v);
	}
	  
	double dx( double v ) {
		return f1.dx(v) + f2.dx(v);
	}
	
  
private:
	F1 f1;
	F2 f2;
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
	private:
	F f;
	int potencia;
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
	double v = 3;
	auto f =  2 * x->*1.1;

	cout << "f(" << v<< ")= " << f.e(v) << " f'("<< v << ")= " << f.dx(v) << "   ";// << x->*2;
  
  return 0;
}
