#include <iostream>
#include <string>
#include <type_traits>
#include <vector>
#include <algorithm>
#include <memory>
#include <map>

using namespace std;

class Var;
ostream& operator << (ostream& o, Var var);

class Erro {
public:
  Erro( string msg ): msg(msg) {}
  
  string operator()() const {
    return msg;
  }
  
private:
  string msg;
};

class Undefined {
	public:
		virtual void print (ostream& o) {}
};

class Int: public Undefined {
	public:
		Int( int n ):n(n) {}
		virtual void print (ostream& o) {
			o << n; 
		}
	private:
		int n;
};

class Double: public Undefined {
	public:
		Double( double n ):n(n) {}
		virtual void print (ostream& o) {
			o << n; 
		}
	private:
		double n;
};

class String: public Undefined {
	public:
		String (string s): s(s) {}
		virtual void print (ostream& o) {
			o << s;
		}
	private: 
		string s;
};

class Object: public Undefined {
	public:
		Object () {}
		virtual void print (ostream& o) {
			//o << n;
		}
	private: 
	// usar std::variant
		map<string, int> n;
};

class Var {
	public:
		Var(): valor( new Undefined() ) {}
		Var(int n): valor( new Int(n) ) {}
		Var(double n): valor( new Double(n) ) {}
		Var(string n): valor( new String(n) ) {}

		Var operator = ( int n ) {
			valor = shared_ptr<Undefined>( new Int( n ) );
			return *this;
		}
		Var operator = ( double n ) {
			valor = shared_ptr<Undefined>( new Double( n ) );
			return *this;
		}
		Var operator = ( string n ) {
			valor = shared_ptr<Undefined>( new String( n ) );
			return *this;
		}
		
		Var operator = ( Object* o) {
			valor = shared_ptr<Undefined>( o );
			return *this;
		}
		
		virtual void print (ostream& o) {
			(*valor).print(o);
		}
	private:
		shared_ptr<Undefined> valor;
};

ostream& operator << (ostream& o, Var var) {
	var.print(o);
	return o;
}
/*
class Var;
class Undefined;

class Int: public Undefined {
public:
  Int( int n ):n(n) {}
  // Nessa chamada de sel_soma já sabemos que n é int
  virtual Var sel_soma( Undefined* arg1 ) const { arg1->soma( n ); }
  virtual Var soma( int arg2 ) const { return n + arg2; }
  virtual Var soma( double arg2 ) const { return n + arg2; }
  int value() const { return n; }
private:
  int n;
};

class String: public Undefined {
public:
  String( string st ): st(st) {}
  
	virtual Var sel_soma( Undefined* arg1 ) const { arg1->soma( st ); }
  virtual Var soma( string arg2 ) const { return st + arg2; }
  virtual Var soma( char arg2 ) const { return st + arg2; }
  string value() const { return st; }
private:
  string st;
};
* */
int main() {
  Var a, b;
  Var c = 5;
  
  cout << a << endl; // saída: "undefined"
  a = 1;
  cout << a << endl; // saída: 1
  a = "hello";
  cout << a << endl; // saída: hello
  
  a = new Object();
  //a["atr"] = 9;
  //a["metodo"] = []( auto x ){ return x*x; };
  b = 4;
  //cout << a["metodo"]( b ) << endl; // Saída: 16;
}


/*
class Var {
public:
  Var(): valor( new Undefined() ) {}

  Var operator = ( int n ) {
    valor = shared_ptr<Undefined>( new Int( n ) );
  }
  Var operator = ( double n ) {
    valor = shared_ptr<Undefined>( new Double( n ) );
  }
private:
  shared_ptr<Undefined> valor;
};
class Undefined {
public:
	Undefined() {}
  virtual Var sel_soma( Undefined* arg1 ) const { return Var(); }
  virtual Var soma( int arg2 ) const { return Var(); }
  virtual Var soma( double arg2 ) const { return Var(); }
  virtual Var soma( char arg2 ) const { return Var(); }
  virtual Var soma( bool arg2 ) const { return Var(); }
  virtual Var soma( string arg2 ) const { return Var(); }  
};
*/

// Os operadores abaixo podem ser implementados utilizando os operadores !, || e <
/*
Var operator > ( const Var& a, const Var& b ) { return b<a; }
Var operator != ( const Var& a, const Var& b ) { return (a<b) || (b<a); }
Var operator == ( const Var& a, const Var& b ) { return !(a!=b); }
Var operator >= ( const Var& a, const Var& b ) { return !(b<a); }
Var operator <= ( const Var& a, const Var& b ) { return !(a<b); }
*/


// VMWearPlayer
