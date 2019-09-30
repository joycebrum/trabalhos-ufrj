#include <vector>
#include <iostream>
#include <map>
#include <functional>

using namespace std;
template <typename T>
ostream& operator << ( ostream& o, const vector<T>& v ) {
    o << "[ ";
    for( auto x : v )
        o << x << " ";
        
    return o << "]";
}
template<typename T, typename F> auto apply(const T& coll, F f) -> std::vector<decltype(f(*std::begin(coll)))>;
template<typename T, typename F> auto apply( std::initializer_list<T> coll, F f) -> std::vector<decltype(f(*coll.begin()))>;

template<typename Vetor> auto firstElement(Vetor v) {
	return *v.begin();
}

template<typename Funcao, typename Vetor>
void stream (Vetor& v, Funcao function) {
	for(auto x : v) {
		function(x);
	}
}

template<typename Funcao, typename Vetor>
auto operator | (Vetor v, Funcao function) {
		
	if constexpr ( is_same< void, typename result_of < Funcao( decltype(*v.begin() ) ) >::type >::value ) {
		stream(v, function);
		return;
	}
	else if constexpr ( is_same< bool, typename result_of < Funcao( decltype(*v.begin() ) ) >::type >::value ) { 
		vector<decltype(firstElement(v))> vetor = {};
		for(auto x : v) {
			if(function(x)) {
				vetor.push_back(x);
			}
		}
		return vetor;
	}
	else { 
		return apply(v, function);
	}
}

/*
template<typename Funcao, typename type, int n>
auto operator | (type(& v)[n], Funcao function) {
	constexpr auto resultado = 
    is_same< bool, typename result_of < Funcao( type ) >::type >::value;
	if constexpr (resultado) {
		vector<type> vetor = {};
		for(type x : v) {
			if(function(x)) {
				vetor.push_back(x);
			}
		}
		return vetor;
	}
	else {
		stream(v, function);
	}
}
*/


int main () {
	map<string,string> v = { { "a", "1" }, { "b", "2" }, { "c", "3" }, { "d", "4" }, { "e", "5" } };
	v | []( auto x ){ return pair{ x.first, stod( x.second ) }; } /*| []( auto p ) { cout << p.second + 1.1 << " "; }*/;

}

template<typename T, typename F>
auto apply(const T& coll, F f) -> std::vector<decltype(f(*std::begin(coll)))>
{
  std::vector<decltype(f(*std::begin(coll)))> res;

  for (auto x : coll) {
    res.push_back(f(x));
  }

  return res;
}

template<typename T, typename F>
auto apply( std::initializer_list<T> coll, F f) -> std::vector<decltype(f(*coll.begin()))>
{
  std::vector<decltype(f(*coll.begin()))> res;

  for (auto x : coll) {
    res.push_back(f(x));
  }

  return res;
}



