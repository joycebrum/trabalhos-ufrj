#include <vector>
#include <iostream>
#include <map>
#include <functional>

using namespace std;


template<typename Vetor>
auto firstElement(Vetor v) {
	return 4;
}

template <bool N, typename T> 
struct IfTrue {
  typedef T tipo;
};

template <typename T> 
struct IfTrue<false, T> {
	typedef void tipo;
};

template<typename Funcao, typename Vetor>
void stream (Vetor& v, Funcao function) {
	for(auto x : v) {
		function(x);
	}
}

template<typename Funcao, typename Vetor>
auto operator | (Vetor&v, Funcao function) {
	constexpr auto resultado = 
    is_same< bool, decltype(function(*v.begin())) >::value;
  
	if constexpr (true) {
		vector<decltype(firstElement(v))> vetor = {};
		for(auto x : v) {
			if(function(x)) {
				vetor.push_back(x);
			}
		}
		return vetor;
	}
	else {
		return stream(v, function);
	}
}

/*
template<typename Funcao, typename type, int n>
auto operator | (type(& v)[n], Funcao function) {
	constexpr auto resultado = 
    is_same< bool, decltype(function(v[0])) >::value;
  
	cout << "Resultado: " << (resultado ? "True" : "False") << endl;
  
	if constexpr (resultado) {
		return filter(v, function);
		vector<decltype(function(v[0]))> vetor = {};
		for(auto x : v) {
			if(function(x)) {
				vetor.push_back(x);
			}
		}
		return vetor;
	}
	else {
		stream(v, function);
	}
}*/

void print( int x ) { cout << x << " "; }

template <typename T>
ostream& operator << ( ostream& o, const vector<T>& v );





int main () {
	int tab[10] =  { 1, 2, 3, 2, 3, 4, 6, 0, 1, 8 };
	vector<int> v{ 2 , 6, 8 };
	//tab | []( int x ) { cout << x*x << endl; };
	/*tab | [ &v ]( int x ) { v.push_back( x ); };
	v | []( int x ) { cout << x*x << endl; };
	v | &print;*/
	
	//vector<int> v2{ 1, 3, 5 };
	
	//cout << (v2 | []( int x ) { return  x == 3;});
}

// --------------------------------------------------- Referentes ao trabalho de FILTER -------------------------------------------------------------
template <typename T>
ostream& operator << ( ostream& o, const vector<T>& v ) {
    o << "[ ";
    for( auto x : v )
        o << x << " ";
        
    return o << "]";
}
