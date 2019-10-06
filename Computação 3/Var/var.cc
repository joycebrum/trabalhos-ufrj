#include <iostream>
#include <string>
#include <type_traits>
#include <vector>
#include <algorithm>
#include <memory>
#include <map>

using namespace std;

class Undefined;
class Object;
class Var {
	public:
	// Construtores
		Var();
		Var(int n);
		Var(double n);
		Var(string n);
		Var(const char *c);
		Var(const char c);
		Var(bool b);
		Var(vector<Var> v);
		template<typename Func>
		Var(Func f);
		Var(map<string, Var> mapa);
		// Operadores
		Var operator = ( Var v )  { valor = shared_ptr( v.valor ); return *this; };
		Var operator = ( int n );
		Var operator = ( double n );
		Var operator = ( string n );
		Var operator = (const char* c);	
		Var operator = (const char c);	
		Var operator = (bool c);	
		Var operator = (vector<Var> c);	
		Var operator = ( Object* o);
		template<typename Func> Var operator = ( Func f);
		Var operator = (map<string,Var> mapa);
		Var operator () (Var arg1) const;
		Var operator [] (string campo) const;
		Var& operator [] (string campo);
		Var operator + (Var var2) const;
		Var operator - (Var var2) const;
		Var operator * (Var var2) const;
		Var operator / (Var var2) const;
		// logica
		Var operator ! () const;
		Var operator || (Var var2) const;
		Var operator && (Var var2) const;
		Var operator < (Var var2) const;
		Var operator > (Var b ) { return b<*this; }
		Var operator != (Var b ) { return (*this<b) || (b<*this); }
		Var operator == (Var b ) { return !(*this!=b); }
		Var operator >= (Var b ) { return !(b<*this); }
		Var operator <= (Var b ) { return !(*this<b); }		
	// Metodos
		Undefined* getValor() { return &(*valor); };
		
		virtual void print (ostream& o);
	// Classes
	class Erro {
	public:
	  Erro( string msg ): msg(msg) {}
	  
	  string operator()() const {
		return msg;
	  }
	  
	private:
	  string msg;
	};
	private:
		shared_ptr<Undefined> valor;
};
ostream& operator << (ostream& o, Var var);
Var operator - (int arg1, Var arg2);
Var operator - (Var arg1, int arg2);
Var operator / (int arg1, Var arg2) ;
Var operator / (Var arg1, int arg2);
Var operator * (int arg1, Var arg2);
Var operator * (Var arg1, int arg2);
Var operator * (double arg1, Var arg2);
Var operator * (Var arg1, double arg2);

class Undefined {
	public:
		virtual void print (ostream& o) { o << "undefined"; }
		virtual Var& get_value (string campo)  { cout << "aqui"; throw Var::Erro("Erro fatal: Essa variável não é um objeto");  }
		
		// Soma
		virtual Var sel_soma( Undefined* arg2 ) const { return Var(); }
		virtual Var soma( int arg1 ) const { return Var(); }
		virtual Var soma( double arg1 ) const { return Var(); }
		virtual Var soma(const char arg1) const { return Var(); }
		virtual Var soma(string arg1) const { return Var(); }
		virtual Var soma(bool arg1) const { return Var(); }
		
		//Subtracao
		virtual Var sel_sub( Undefined* arg2 ) const { return Var(); }
		virtual Var sub( int arg1 ) const { return Var(); }
		virtual Var sub( double arg1 ) const { return Var(); }
		virtual Var sub(const char arg1) const { return Var(); }
		
		//Multiplicacao
		virtual Var sel_mul(Undefined* arg2 ) const { return Var(); }
		virtual Var mul( int arg1 ) const { return Var(); }
		virtual Var mul( double arg1 ) const { return Var(); }
		
		//Divisao
		virtual Var sel_div(Undefined* arg2 ) const { return Var(); }
		virtual Var div( int arg1 ) const { return Var(); }
		virtual Var div( double arg1 ) const { return Var(); }
		
		//Logica
		virtual Var sel_not() const  { return Var(); }
		virtual Var sel_or(Undefined* arg2) const { return Var(); }
		virtual Var sel_less(Undefined* arg2) const { return Var(); }
		virtual Var less(int arg1) const { return Var(); }
		virtual Var less(double arg1) const { return Var(); }
		virtual Var op_or(int arg1) const { return Var(); }
		virtual Var op_or(bool arg1) const { return Var(); }
		virtual Var op_or(double arg1) const { return Var(); }
		virtual Var sel_and (Undefined* arg2) const { return Var(); }
		virtual Var op_and(int arg1) const { return Var(); }
		virtual Var op_and(bool arg1) const { return Var(); }
		virtual Var op_and(double arg1) const { return Var(); }
		
		// Operadores
		virtual Var operator () (Var arg1) const  { throw Var::Erro("Essa variável não pode ser usada como função"); }
		Var operator + (Undefined* arg2) { return this->sel_soma(arg2); }
		Var operator - (Undefined* arg2) { return this->sel_sub(arg2); }
		Var operator * (Undefined* arg2) { return this->sel_mul(arg2); }
		Var operator / (Undefined* arg2) { return this->sel_div(arg2); }
		Var operator ! () { return this->sel_not(); }
		Var operator || (Undefined* arg2) { return this->sel_or(arg2); }
		Var operator && (Undefined* arg2) { return this->sel_and(arg2); }
		Var operator < (Undefined* arg2) { return this->sel_less(arg2); }
		
};

class Int: public Undefined {
	public:
		Int( int n ):n(n) {}
		virtual void print (ostream& o) {	o << n; }
		//soma
		virtual Var sel_soma( Undefined* arg2 ) const { return arg2->soma( n ); }
		virtual Var soma( int arg1 ) const { return Var(arg1 + n); }
		virtual Var soma( double arg1 ) const { return Var(arg1 + n); }
		virtual Var soma( const char arg1 ) const { return Var(arg1 + n); }
		virtual Var soma( bool arg1 ) const { return Var(arg1 + n); }
		//sub
		virtual Var sel_sub(Undefined* arg2) const { return arg2->sub(n); }
		virtual Var sub( int arg1 ) const { return Var(arg1 - n); }
		virtual Var sub( double arg1 ) const { return Var(arg1 - n); }
		virtual Var sub(const char arg1) const { return Var(arg1 - n); }
		//mul
		virtual Var sel_mul(Undefined* arg2 ) const { return arg2->mul(n); }
		virtual Var mul( int arg1 ) const { return Var(arg1 * n); }
		virtual Var mul( double arg1 ) const { return Var(arg1 * n); }
		//div
		virtual Var sel_div(Undefined* arg2 ) const { return arg2->div(n); }
		virtual Var div( int arg1 ) const { return Var(arg1 / n); }
		virtual Var div( double arg1 ) const { return Var(arg1 / n); }
		//logica
		virtual Var sel_not() const  { return Var(!n); }
		virtual Var sel_or(Undefined* arg2) const { return arg2->op_or(n); }
		virtual Var op_or(int arg1) const { return Var(n || arg1); }
		virtual Var sel_less(Undefined* arg2) const { return arg2->less(n); }
		virtual Var less(int arg1) const { return Var(arg1 < n); }
		virtual Var less(double arg1) const { return Var(arg1 < n); }
		
		virtual Var sel_and (Undefined* arg2) const { return arg2->op_and(n); }
		virtual Var op_and(int arg1) const { return Var(arg1 && n); }
		virtual Var op_and(bool arg1) const { return Var(arg1 && n); }
		virtual Var op_and(double arg1) const { return Var(arg1 && n); }
		
		
	private:
		int n;
};

class Double: public Undefined {
	public:
		Double( double n ):n(n) {}
		virtual void print (ostream& o) { o << n; }
		virtual Var sel_soma(Undefined* arg2 ) const { return arg2->soma(n); }
		virtual Var soma( int arg1 ) const { return Var(arg1 + n); }
		virtual Var soma( double arg1 ) const { return Var(arg1 + n); }
		virtual Var soma( bool arg1 ) const { return Var(arg1 + n); }
		//sub
		virtual Var sel_sub(Undefined* arg2) const { return arg2->sub(n); }
		virtual Var sub( int arg1 ) const { return Var(arg1 - n); }
		virtual Var sub( double arg1 ) const { return Var(arg1 - n);  }
		virtual Var sub(const char arg1) const { return Var(arg1 - n);  }
		//mul
		virtual Var sel_mul(Undefined* arg2 ) const { return arg2->mul(n); }
		virtual Var mul( int arg1 ) const { return Var(arg1 * n); }
		virtual Var mul( double arg1 ) const { return Var(arg1 * n); }
		//div
		virtual Var sel_div(Undefined* arg2 ) const { return arg2->div(n); }
		virtual Var div( int arg1 ) const { return Var(arg1 / n); }
		virtual Var div( double arg1 ) const { return Var(arg1 / n); }
		//logico
		virtual Var sel_not() const  { return Var(!n); }
		virtual Var sel_or(Undefined* arg2) const { return arg2->op_or(n); }
		virtual Var op_or(int arg1) const { return Var(n || arg1); }
		virtual Var sel_less(Undefined* arg2) const { return arg2->less(n); }
		virtual Var less(int arg1) const { return Var(arg1 < n); }
		virtual Var less(double arg1) const { return Var(arg1 < n); }
		//and
		
		virtual Var sel_and (Undefined* arg2) const { return arg2->op_and(n); }
		virtual Var op_and(int arg1) const { return Var(arg1 && n); }
		virtual Var op_and(bool arg1) const { return Var(arg1 && n); }
		virtual Var op_and(double arg1) const { return Var(arg1 && n); }
		
	private:
		double n;
};

class String: public Undefined {
	public:
		String (string s): n(s) {}
		String (const char* c): n(c) {}
		virtual void print (ostream& o) { o << n; }
		virtual Var sel_soma(Undefined* arg2) const { return arg2->soma(n); }
		virtual Var soma (const char arg1) const { return Var(arg1 + n); } 
		virtual Var soma (string arg1) const { return Var(arg1 + n); } 
	private: 
		string n;
};

class Object: public Undefined {
	public:
		Object (map<string,Var> mapa): n(mapa) {}
		virtual void print (ostream& o) { o << "object"; }
		Var& get_value(string campo) override { return n[campo]; }
	private: 
	// usar std::variant
		map<string, Var> n;
};
class Bool: public Undefined {
	public:
		Bool(bool b): n(b) {}
		virtual void print(ostream& o) {o << n;}
		virtual Var soma( int arg1 ) const { return Var(arg1 + n); }
		virtual Var soma( double arg1 ) const { return Var(arg1 + n); }
		//log
		virtual Var sel_not() const  { return Var(!n); }
		virtual Var sel_or(Undefined* arg2) const { return arg2->op_or(n); }
		virtual Var op_or(int arg1) const { return Var(n || arg1); }
		virtual Var op_or(double arg1) const { return Var(n || arg1); }
		virtual Var op_or(bool arg1) const { return Var(n || arg1); }
		
		virtual Var sel_and (Undefined* arg2) const { return arg2->op_and(n); }
		virtual Var op_and(int arg1) const { return Var(arg1 && n); }
		virtual Var op_and(bool arg1) const { return Var(arg1 && n); }
		virtual Var op_and(double arg1) const { return Var(arg1 && n); }
	private:
		bool n;
};


class Char: public Undefined {
	public:
		Char(const char c): n(c) {}
		virtual void print(ostream& o) {o << n;}
		virtual Var sel_soma(Undefined* arg2) const { return arg2->soma(n); }
		virtual Var soma (const char arg1) const { return Var(arg1 + n); } 
		virtual Var soma (string arg1) const { return Var(arg1 + n); } 
	private:
		char n;
};
class Array: public Undefined {
	public:
		Array(vector<Var> v): n(v) {}
		virtual void print(ostream& o) {
			for ( auto x : n ) {
				o << x + ", ";
			}
		}
	private:
		vector<Var> n;
};

Var newObject() {
	map<string, Var> mapa;
	Var obj = mapa;
	return obj;
}
class AbstractFunction {
	public:
		virtual ~AbstractFunction(){}
		virtual Var operator () (Var arg1) const { return Var(); }
};
template<typename Func>
class ImplFunction: public AbstractFunction {
	public:
		ImplFunction(const Func& f): f(f) {}
		virtual Var operator () (Var arg1) const { return f(arg1); }
	private:
		Func f;
};

class Function: public Undefined {
	public:
		template<typename Func>
		Function(Func f): af(new ImplFunction{f} ) {}
		Var operator () (Var arg1) const { return (*af)(arg1); }
		virtual void print(ostream& o) { o << "function"; }
	private:
		shared_ptr<AbstractFunction> af;
};

Var print( const Var& o ) {
  cout << "{ nome: " << o["nome"]
       << ", idade: " << o["idade"]( o )
       << ", nascimento: " << o["nascimento"]
       << ", print: " << o["print"] 
       << ", atr: " << o["atr"] 
       << " }" << endl;
       
  return Var();     
}

void imprime( Var v ) {
    v["print"]( v );
}

int main() try {     
Var a[5] = { true, 'X', 2, 2.1, "abracadabra" };
Var b = 200, c = 300.1, d = "palavra ";

cout << (a[0] && true) << endl;
for( auto& x: a ) {
  cout << x+b << "," << x+c << "," << x+d << "," << 3 / x << "," << 1.1 * x << ","
       << (x && true) << "," << (x && false) <<  "," << (b >= x) << "," << (x < d) << endl;
}

  return 0;
} catch( Var::Erro e ) {
  cout << "Erro fatal: " << e() << endl;
}

Var::Var(): valor( new Undefined() ) {};
Var::Var(int n): valor( new Int(n) ) {};
Var::Var(double n): valor( new Double(n) ) {};
Var::Var(string n): valor( new String(n) ) {};
Var::Var(const char* c): valor(new String(c)){};
Var::Var(const char c): valor(new Char(c) ) {};
Var::Var(bool b): valor( new Bool(b) ){};
Var::Var(vector<Var> v): valor ( new Array(v) ) {};
Var::Var(map<string, Var>mapa): valor(new Object(mapa)) {};
template<typename Func>
Var::Var( Func f): valor (new Function(f)) {};
//operadores;
Var Var::operator = ( int n ) { valor = shared_ptr<Undefined>( new Int( n ) ); 	return *this; };
Var Var::operator = ( double n ) { valor = shared_ptr<Undefined>( new Double( n ) ); return *this; };
Var Var::operator = ( string n ) { valor = shared_ptr<Undefined>( new String( n ) ); return *this; };
Var Var::operator = ( Object* o) { valor = shared_ptr<Undefined>( o ); return *this; };
Var Var::operator = ( const char *c ) { valor = shared_ptr<Undefined>( new String(c) ); return *this; };
Var Var::operator = ( const char c ) { valor = shared_ptr<Undefined>( new Char(c) ); return *this; };
Var Var::operator = ( bool c ) { valor = shared_ptr<Undefined>( new Bool(c) ); return *this; };
Var Var::operator = ( vector<Var> c ) { valor = shared_ptr<Undefined>( new Array(c) ); return *this; };
Var Var::operator = (map<string,Var> mapa) { valor = shared_ptr<Undefined>( new Object(mapa) ); return *this; };
Var& Var::operator [] (string campo) { return (*valor).get_value(campo); };
Var Var::operator [] (string campo) const { return (*valor).get_value(campo); };
template<typename Func>
Var Var::operator = ( Func f) { valor = shared_ptr<Undefined>(new Function(f)); return *this;};
Var Var::operator () (Var arg1) const { return (*valor)(arg1); };
Var Var::operator + (Var var2) const {return *valor + var2.getValor();};
Var Var::operator - (Var var2) const {return *valor - var2.getValor();};
Var Var::operator * (Var var2) const {return *valor * var2.getValor();};
Var Var::operator / (Var var2) const {return *valor / var2.getValor(); };
Var Var::operator ! () const { return !*valor; };
Var Var::operator || (Var var2) const { return *valor || var2.getValor();};
Var Var::operator && (Var var2) const { return *valor && var2.getValor(); };
Var Var::operator < (Var var2) const { return *valor < var2.getValor(); };
// funções
void Var::print (ostream& o) { (*valor).print(o); };

ostream& operator << (ostream& o, Var var) {
	var.print(o);
	return o;
}

Var operator - (int arg1, Var arg2) {
	Var argv = arg1;
	return argv - arg2;
}
Var operator - (Var arg1, int arg2) {
	Var argv= arg2;
	return arg1 - argv;
}
Var operator / (int arg1, Var arg2) {
	Var argv = arg1;
	return argv / arg2;
}
Var operator / (Var arg1, int arg2) {
	Var argv = arg2;
	return arg1 / argv;
}
Var operator && (bool arg1, Var arg2) { return Var(arg1) && arg2; }
Var operator && (Var arg1, bool arg2) { return arg1 && Var(arg2); }
Var operator * (int arg1, Var arg2) { return Var(arg1) * arg2; }
Var operator * (Var arg1, int arg2) { return arg1 * Var(arg2); }
Var operator * (double arg1, Var arg2) { return Var(arg1) * arg2; }
Var operator * (Var arg1, double arg2) { return arg1 * Var(arg2); }

// VMWearPlayer
