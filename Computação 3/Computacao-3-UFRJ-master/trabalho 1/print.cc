#include <initializer_list>
#include <string>
#include <sstream>
#include <iostream>
#include <vector>

using namespace std;

template<typename T>
string to_string(vector<T> vec);

template <typename T>
string toString(T t);

template<>
string toString(const char* c);

template<>
string toString(string s);

template<>
string toString(double d);


//template <typename A, typename B>
class Pair {
	public:
		template <typename A, typename B>
		Pair( A a, B b ) {
			first = toString(a);
			second = toString(b);
		}
		
		void imprime() {
			cout << first << " = " << second << endl;
		}
	
	private:
		//A first;
		//B second;
		string first;
		string second;
};

void print( initializer_list<Pair> lista ) {
	for (Pair par : lista) {
		par.imprime();
	}
}

int main() {
 
    //Pair<string, int> p( "1", 2 );
    Pair p("1", 2);
  
    print( { { "jan", 1 }, { string( "pi" ), 3.14 } } );
    
    cout << " ////////////////////////////////////////// " << endl;
    
    print( { { "jan", 1 }, { string( "pi" ), 3.14 } } );


  return 0;  
}

template<typename T>
string to_string(vector<T> vec) {
	string saida = "[";
	for (T valor : vec) {
		saida = saida + " " + toString(valor);
	}
	saida += " ]";
	return saida;
}

template <typename T>
string toString(T t) {
	return to_string(t);
}

template<>
string toString(const char* c) {
	string valor(c);
	return valor;
}
template<>
string toString(string s) {
	return s;
}
template<>
string toString(double d) {
	ostringstream strs;
	strs << d;
	return strs.str();
}



