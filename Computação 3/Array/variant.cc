#include <iostream>
#include <string>
#include <type_traits>
#include <vector>
#include <map>
#include <memory>
#include <sstream>

using namespace std;

class Var {
public:
  // === Exceções ==========
	class Erro {
	public:
	Erro( string msg ): msg(msg) {}

		string operator()() const {
		  return msg;
		}

		private:
		string msg;
	};

	enum TYPE { UNDEFINED = 0, CHAR, BOOL, INT, DOUBLE, STRING, OBJECT, FUNCTION, ARRAY }; 

	class Undefined {
		public:
		Undefined( TYPE type = UNDEFINED ): type(type) {}
		virtual ~Undefined() {}

		virtual void print( ostream& o ) const { o << "undefined"; }

		virtual Var rvalue( const string& st ) const { throw Erro( "Essa variável não é um objeto" ); }
		virtual Var& lvalue( const string& st ) { throw Erro( "Essa variável não é um objeto" ); }
		virtual Var rvalue( const int i ) const { throw Erro( "Essa variável não é um array" ); }
		virtual Var& lvalue( const int i ) { throw Erro( "Essa variável não é um array" ); }
		virtual Var rvalue( const Var var ) const { throw Erro( "Essa variável não é um array" ); }
		virtual Var& lvalue( const Var var ) { throw Erro( "Essa variável não é um array" ); }

		virtual Var func( const Var& arg ) const { 
			throw Erro( "Essa variável não pode ser usada como função" ); 
		} 

		public:
			const TYPE type;
	};

	// === Tipos internos =======================
	template <typename T, typename tipo=void>
	class Type: public Undefined {
		public:
		Type( const T& v ): Undefined( sel_type() ), v(v) {}

		virtual void print( ostream& o ) const { 
		  if constexpr( is_same_v< bool, T > )
			o << (v? "true" : "false"); 
			  else
			o << v;
		}
		
		const T& value() const { return v; }

		static constexpr TYPE sel_type() {
			if constexpr ( is_same_v<int, T> ) return INT;
			else if constexpr ( is_same_v<char, T> ) return CHAR;
			else if constexpr ( is_same_v<bool, T> ) return BOOL;
			else if constexpr ( is_same_v<double, T> ) return DOUBLE;
			else if constexpr ( is_same_v<string, T> ) return STRING;
			else if constexpr ( is_same_v<vector<tipo>, T> ) return ARRAY;
			else return UNDEFINED;
		}
		private:
		T v;
	};

	class Object: public Undefined {
		public:
		Object(): Undefined( OBJECT ) {}
		Object(TYPE t): Undefined(t) {}

		virtual void print( ostream& o ) const { o << "object"; }

		virtual Var& lvalue( const string& st ) { return atr[st]; }
		virtual Var rvalue( const string& st ) const { 
			if( auto x = atr.find( st ); x != atr.end() )
				return x->second;
			else
				return Var(); 
		}

		private:
		map<string,Var> atr; 
	};

	template <typename F>
	class Func: public Object {
		public:
		Func( F f ): Object( FUNCTION ), f(f) {}

		virtual void print( ostream& o ) const { o << "function"; }

		virtual Var func( const Var& arg ) const { return invoke( f, arg ); }  

		private:
		F f;
	};
	
	class Array: public Object {
		public:
		Array(vector<Var> v): Object(ARRAY), v(v) {}
		Array(): Object(ARRAY) {}
		
		virtual void print (ostream& o ) const;
		virtual Var& lvalue( const int i ) { return v[i]; }
		virtual Var rvalue( const int i ) const { return v[i]; }
		/*virtual Var& lvalue( const Var var ) { 
			switch(var.valor->type) {
				case INT: 
					return ((const Int*) valor.get())->value();
				default:
					throw Erro( "Essa variável não é um array" );
					break;
					
			}
		}
		virtual Var rvalue( const Var var ) const { return v[i]; }*/
		
		private:
		vector<Var> v;
	};

	typedef Type<bool> Bool;
	typedef Type<char> Char;
	typedef Type<int> Int;
	typedef Type<double> Double;
	typedef Type<string> String;
  
private:
  // === Operações ================================   
	template <typename A, typename B>
	static Var adicao( const Undefined* a, const Undefined* b ) { 
		return ((const A*) a)->value() + ((const B*) b)->value(); 
	}

	template <typename A, typename B>
	static Var subtracao( const Undefined* a, const Undefined* b ) { 
		return ((const A*) a)->value() - ((const B*) b)->value(); 
	}

	template <typename A, typename B>
	static Var multiplicacao( const Undefined* a, const Undefined* b ) { return ((const A*) a)->value() * ((const B*) b)->value(); }

	template <typename A, typename B>
	static Var divisao( const Undefined* a, const Undefined* b ) { return ((const A*) a)->value() / ((const B*) b)->value(); }

	template <typename A, typename B>
	static Var menor( const Undefined* a, const Undefined* b ) { return ((const A*) a)->value() < ((const B*) b)->value(); }
    
public:

	static Var sel_adicao( const Var& a, const Var& b );
	static Var sel_subtracao( const Var& a, const Var& b );
	static Var sel_multiplicacao( const Var& a, const Var& b );
	static Var sel_divisao( const Var& a, const Var& b );
	static Var sel_menor( const Var& a, const Var& b );
	static Var sel_and( const Var& a, const Var& b );
	static Var sel_or( const Var& a, const Var& b );
	static Var sel_not( const Var& a );
  
// === Construtores ================================
public:
	Var(): valor( new Undefined() ) {}
	Var( bool v ): valor( new Bool( v ) ) {}
	Var( char v ): valor( new Char( v ) ) {}
	Var( int v ): valor( new Int( v ) ) {}
	Var( double v ): valor( new Double( v ) ) {}
	Var( const string& st ): valor( new String( st ) ) {}
	Var( const char* st ): valor( new String( st ) ) {}
	Var(  Object *o ): valor( o ) {}

	template <typename F>
	Var( const enable_if_t< is_invocable_r<Var, F, Var>::value, F>&& f ): valor( shared_ptr<Undefined>( new Func<F>( f ) ) ) {}
  
	const Var& operator = ( bool v ) { valor = shared_ptr<Undefined>( new Bool( v ) ); return *this; }
	const Var& operator = ( char v ) { valor = shared_ptr<Undefined>( new Char( v ) ); return *this; }
	const Var& operator = ( int v ) { valor = shared_ptr<Undefined>( new Int( v ) ); return *this; }
	const Var& operator = ( double v ) { valor = shared_ptr<Undefined>( new Double( v ) ); return *this; }
	const Var& operator = ( const string& st ) { valor = shared_ptr<Undefined>( new String( st ) ); return *this; }
	const Var& operator = ( const char* st ) { valor = shared_ptr<Undefined>( new String( st ) ); return *this; }
  
	const Var& operator = ( Object *o ) { 
		valor = shared_ptr<Undefined>( o ); 
		return *this;
	}
  
	template <typename F>
	auto operator = ( const F& f ) -> const enable_if_t< is_invocable_r<Var, F, Var>::value, Var>& {
		valor = shared_ptr<Undefined>( new Func<F>( f ) );
		return *this;
	}
  
	void print( ostream& o ) const { valor->print( o ); }

	/*Var& operator[]( const string& st ) { return valor->lvalue( st ); }
	Var  operator[]( const string& st ) const { return valor->rvalue( st ); }
	Var& operator[]( int i) { return valor->lvalue(i); }
	Var  operator[]( int i) const { return valor->rvalue(i); }*/
	
	Var  operator[]( Var a) { 
		cout << "ola";
		cout  << " tipo; " << a.valor->type << endl;
		switch (a.valor->type) {
			case STRING:
				return valor->rvalue( ((const String*) valor.get())->value() );
			case INT:
				return valor->rvalue( ((const Int*) valor.get())->value() );
			default: 
				throw Erro( "Operação inválida." );
		}
	}
  
	Var operator()( const Var& arg ) const { return valor->func( arg ); }
  
// === Metodos ============================================
	bool asBool() {
		switch(valor->type) {
			case BOOL:
				return ((const Bool*) valor.get())->value();
			case INT:
				return ((const Int*) valor.get())->value() != 0;
			case DOUBLE:
				return ((const Double*) valor.get())->value() != 0;
			default: 
				return false;
		}
	}
	
	string asString() {
		ostringstream strs;
		switch(valor->type) {
			case BOOL:
				strs << ((const Bool*) valor.get())->value();
				return strs.str();
			case INT:
				return to_string(((const Int*) valor.get())->value());
			case DOUBLE:
				strs << ((const Double*) valor.get())->value();
				return strs.str();
			case CHAR:
				strs << ((const Char*) valor.get())->value();
				return strs.str();
			default :
				return "";
		}
	}
	bool isNumber() {
		switch(valor->type) {
			case INT:
			case DOUBLE:
				return true;
			default:
				return false;
		}
	}
   
public:
  shared_ptr<Undefined> valor;
};

inline constexpr int tipo_args( Var::TYPE tipo_a, Var::TYPE tipo_b ) { return (tipo_a << 3) | tipo_b; }  

inline Var Var::sel_adicao( const Var& a, const Var& b ) {
  switch( tipo_args( a.valor->type, b.valor->type ) ) {
    case tipo_args( CHAR, CHAR ): 	return string("") + ((const Char*) a.valor.get())->value() + ((const Char*) b.valor.get())->value(); 
    case tipo_args( INT, INT ): 	return adicao<Int,Int>( a.valor.get(), b.valor.get() );
    case tipo_args( DOUBLE, DOUBLE ): 	return adicao<Double,Double>( a.valor.get(), b.valor.get() ); 
    case tipo_args( STRING, STRING): 	return adicao<String,String>( a.valor.get(), b.valor.get() ); 

    case tipo_args( INT, CHAR ): 	return adicao<Int,Char>( a.valor.get(), b.valor.get() );
    case tipo_args( CHAR, INT ): 	return adicao<Char,Int>( a.valor.get(), b.valor.get() );

    case tipo_args( INT, DOUBLE ): 	return adicao<Int,Double>( a.valor.get(), b.valor.get() ); 
    case tipo_args( DOUBLE, INT ): 	return adicao<Double,Int>( a.valor.get(), b.valor.get() ); 
    
    case tipo_args( STRING, CHAR ): 	return adicao<String,Char>( a.valor.get(), b.valor.get() ); 
    case tipo_args( CHAR, STRING): 	return adicao<Char,String>( a.valor.get(), b.valor.get() ); 
    
    default:
      return Var();
   }
}

Var Var::sel_subtracao( const Var& a, const Var& b ) {
  switch( tipo_args( a.valor->type, b.valor->type ) ) {
    case tipo_args( CHAR, CHAR ): 	return subtracao<Char,Char>( a.valor.get(), b.valor.get() ); ; 
    case tipo_args( INT, INT ): 	return subtracao<Int,Int>( a.valor.get(), b.valor.get() );
    case tipo_args( DOUBLE, DOUBLE ): 	return subtracao<Double,Double>( a.valor.get(), b.valor.get() ); 

    case tipo_args( INT, CHAR ): 	return subtracao<Int,Char>( a.valor.get(), b.valor.get() );
    case tipo_args( CHAR, INT ): 	return subtracao<Char,Int>( a.valor.get(), b.valor.get() );

    case tipo_args( INT, DOUBLE ): 	return subtracao<Int,Double>( a.valor.get(), b.valor.get() ); 
    case tipo_args( DOUBLE, INT ): 	return subtracao<Double,Int>( a.valor.get(), b.valor.get() ); 
    
    default:
      return Var();
   }
}

Var Var::sel_multiplicacao( const Var& a, const Var& b ) {
    switch( tipo_args( a.valor->type, b.valor->type ) ) {
    case tipo_args( INT, INT ): 	return multiplicacao<Int,Int>( a.valor.get(), b.valor.get() );
    case tipo_args( DOUBLE, DOUBLE ): 	return multiplicacao<Double,Double>( a.valor.get(), b.valor.get() ); 

    case tipo_args( INT, DOUBLE ): 	return multiplicacao<Int,Double>( a.valor.get(), b.valor.get() ); 
    case tipo_args( DOUBLE, INT ): 	return multiplicacao<Double,Int>( a.valor.get(), b.valor.get() ); 
    
    default:
      return Var();
   }
}

Var Var::sel_divisao( const Var& a, const Var& b ) {
    switch( tipo_args( a.valor->type, b.valor->type ) ) {
    case tipo_args( INT, INT ): 	return divisao<Int,Int>( a.valor.get(), b.valor.get() );
    case tipo_args( DOUBLE, DOUBLE ): 	return divisao<Double,Double>( a.valor.get(), b.valor.get() ); 

    case tipo_args( INT, DOUBLE ): 	return divisao<Int,Double>( a.valor.get(), b.valor.get() ); 
    case tipo_args( DOUBLE, INT ): 	return divisao<Double,Int>( a.valor.get(), b.valor.get() ); 
    
    default:
      return Var();
   }
}

Var Var::sel_menor( const Var& a, const Var& b ) {
  switch( tipo_args( a.valor->type, b.valor->type ) ) {
    case tipo_args( BOOL, BOOL ): 	return menor<Bool,Bool>( a.valor.get(), b.valor.get() ); 
    case tipo_args( CHAR, CHAR ): 	return menor<Char,Char>( a.valor.get(), b.valor.get() ); 
    case tipo_args( INT, INT ): 	return menor<Int,Int>( a.valor.get(), b.valor.get() );
    case tipo_args( DOUBLE, DOUBLE ): 	return menor<Double,Double>( a.valor.get(), b.valor.get() ); 
    case tipo_args( STRING, STRING): 	return menor<String,String>( a.valor.get(), b.valor.get() ); 

    case tipo_args( INT, CHAR ): 	return menor<Int,Char>( a.valor.get(), b.valor.get() );
    case tipo_args( CHAR, INT ): 	return menor<Char,Int>( a.valor.get(), b.valor.get() );

    case tipo_args( INT, DOUBLE ): 	return menor<Int,Double>( a.valor.get(), b.valor.get() ); 
    case tipo_args( DOUBLE, INT ): 	return menor<Double,Int>( a.valor.get(), b.valor.get() ); 
    
    case tipo_args( STRING, CHAR ): 	return ((const String*) a.valor.get())->value() < string( ((const Char*) b.valor.get())->value(), 1 ); 
    case tipo_args( CHAR, STRING ): 	return string( ((const Char*) a.valor.get())->value(), 1 ) < ((const String*) b.valor.get())->value(); 
    
    default:
      return Var();
   }
}

Var Var::sel_and( const Var& a, const Var& b ) {
    switch( tipo_args( a.valor->type, b.valor->type ) ) {
      case tipo_args( BOOL, BOOL ): 	return ((const Bool*) a.valor.get())->value() && ((const Bool*) b.valor.get())->value(); 
    
    default:
      return Var();
   }
}

Var Var::sel_or( const Var& a, const Var& b ) {
    switch( tipo_args( a.valor->type, b.valor->type ) ) {
      case tipo_args( BOOL, BOOL ): 	return ((const Bool*) a.valor.get())->value() || ((const Bool*) b.valor.get())->value(); 
    
    default:
      return Var();
   }
}

Var Var::sel_not( const Var& a ) {
    switch( a.valor->type ) {
      case BOOL: 	return !((const Bool*) a.valor.get())->value(); 
    
    default:
      return Var();
   }
}

ostream& operator << ( ostream& o, const Var& v ) {
  v.print( o );
  return o;
}

Var operator + ( const Var& a, const Var& b ) { return Var::sel_adicao( a, b ); }
Var operator - ( const Var& a, const Var& b ) { return Var::sel_subtracao( a, b ); }
Var operator * ( const Var& a, const Var& b ) { return Var::sel_multiplicacao( a, b ); }
Var operator / ( const Var& a, const Var& b ) { return Var::sel_divisao( a, b ); }
Var operator < ( const Var& a, const Var& b ) { return Var::sel_menor( a, b ); }
Var operator || ( const Var& a, const Var& b ) { return Var::sel_or( a, b ); }
Var operator && ( const Var& a, const Var& b ) { return Var::sel_and( a, b ); }
Var operator ! ( const Var& a ) { return Var::sel_not( a ); }

Var operator > ( const Var& a, const Var& b ) { return b<a; }
Var operator != ( const Var& a, const Var& b ) { return (a<b) || (b<a); }
Var operator == ( const Var& a, const Var& b ) { return !(a!=b); }
Var operator <= ( const Var& a, const Var& b ) { return !(b<a); }
Var operator >= ( const Var& a, const Var& b ) { return !(a<b); }

Var::Object* newObject() {
  return new Var::Object();
}

Var::Array* newArray() {
	return new Var::Array();
}
void Var::Array::print(ostream& o) const { cout << "[ "; for(Var x : v) cout << x << " "; cout << "]"; }
int main () {
	Var a, b;
	a = newArray();
	a["sqr"] = []( int n ){ return n*n; }; 

	for( b = 0; (b < 10).asBool(); b = b + 1 ) {
		
	  a[b] = 3;// a["sqr"]( b );
	  cout << a[b] << ", ";
  }
}
