#include <vector>
#include <iostream>
#include <map>
#include <functional>

using namespace std;

// --------------------------------------------------- Referentes ao trabalho de STREAM -------------------------------------------------------------
template<typename Funcao, typename Vetor>
constexpr operator | (Vetor&v, Funcao function) {
	/*for(auto x : v) {
		function(x);
	}*/
	auto resultado = 
    is_same< int, decltype(function(*v.begin())) >::value;
  
	if (resultado == "true") {
		return v;
	}
	// usar ifconstexpr 
	// usar o invoke result para decidir se retorna o vetor ou se retorna void
}
void print( int x ) { cout << x << " "; }



// --------------------------------------------------- Referentes ao trabalho de FILTER -------------------------------------------------------------


template <typename T>
ostream& operator << ( ostream& o, const vector<T>& v );

/*
template <class Function, typename tipo>
vector<typename result_of < Function( tipo ) >::type > apply( const initializer_list<tipo>& v, Function f);

template <class Function, typename tipo, int n>
vector<typename result_of < Function( tipo ) >::type > apply(tipo(& v)[n], Function f);*/





int main () {
	/*int tab[10] =  { 1, 2, 3, 2, 3, 4, 6, 0, 1, 8 };
	vector<int> v{ 2 , 6, 8 };
	tab | []( int x ) { cout << x*x << endl; };
	tab | [ &v ]( int x ) { v.push_back( x ); };
	v | []( int x ) { cout << x*x << endl; };
	v | &print;*/
	
	vector<int> v2{ 1, 3, 5 };
	
	cout << (v2 | []( int x ) { return  x == 3;});
}

// --------------------------------------------------- Referentes ao trabalho de FILTER -------------------------------------------------------------
template <typename T>
ostream& operator << ( ostream& o, const vector<T>& v ) {
    o << "[ ";
    for( auto x : v )
        o << x << " ";
        
    return o << "]";
}
