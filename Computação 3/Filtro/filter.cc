#include <vector>
#include <iostream>
#include <map>
#include <functional>


using namespace std;


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
	else if constexpr (is_same< unsigned long, typename result_of < Funcao( decltype(*v.begin() ) ) >::type >::value) {
		vector<decltype( (firstElement(v).*function) () )> res;

		for (auto x : v) {
			res.push_back( (x.*function)() );
		}
		return res;
	}
	else{ 
		vector<decltype(function(*v.begin()))> res;

		for (auto x : v) {
			res.push_back(function(x));
		}

		return res;
	}
}

template<typename Funcao, typename type, int n>
auto operator | (type(& v)[n], Funcao function) {
	if constexpr ( is_same< void, typename result_of < Funcao( type ) >::type >::value ) {
		stream(v, function);
		return;
	}
	else if constexpr ( is_same< bool, typename result_of < Funcao( type ) >::type >::value ) { 
		vector< type > vetor = {};
		for(type x : v) {
			if(function(x)) {
				vetor.push_back(x);
			}
		}
		return vetor;
	}
	else { 
		vector<decltype(function(v[0]))> res;

		for (auto x : v) {
			res.push_back(function(x));
		}

		return res;
	}
}

int main() {}
