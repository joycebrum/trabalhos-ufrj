#include <iostream>
#include <vector>
#include <type_traits>
#include <functional>
#include <string>
#include <stdio.h>
using namespace std; 

auto x = []( auto v ){ return v; };
constexpr auto cte( auto valor ) { return [valor]( auto x ) { return valor; } ; }

template<typename Op>
constexpr auto getValue(Op v) {
	if constexpr (is_arithmetic<Op>::value || is_same<Op, string>:: value) {
		return cte(v);
	}
	else {
		return v;
	}
}

template <typename Op1, typename Op2>
auto operator + ( Op1 v1, Op2 v2 ) {
	auto a = getValue(v1);
	auto b = getValue(v2);
	return [a,b]( auto v ){ return a(v) + b(v); }; 
}
template <typename Op1, typename Op2>
auto operator - ( Op1 v1, Op2 v2 ) {
	auto a = getValue(v1);
	auto b = getValue(v2);
	return [a,b]( auto v ){ return a(v) - b(v); }; 
}
template <typename Op1, typename Op2>
auto operator * ( Op1 v1, Op2 v2 ) {
	auto a = getValue(v1);
	auto b = getValue(v2);
	return [a,b]( auto v ){ return a(v) * b(v); }; 
}
template <typename Op1, typename Op2>
auto operator / ( Op1 v1, Op2 v2 ) {
	auto a = getValue(v1);
	auto b = getValue(v2);
	return [a,b]( auto v ){ return a(v) / b(v); }; 
}
template <typename Op1, typename Op2>
auto operator % ( Op1 v1, Op2 v2 ) {
	auto a = getValue(v1);
	auto b = getValue(v2);
	return [a,b]( auto v ){ return a(v) % b(v); };
} 
template <typename Op1, typename Op2>
auto operator == ( Op1 v1, Op2 v2 ) {
	auto a = getValue(v1);
	auto b = getValue(v2);
	return [a,b]( auto v ){ return a(v) == b(v); };
} 
template <class Op1, typename Op2>
auto operator << ( Op1 v1, Op2 v2 ) {
	auto a = getValue(v1);
	auto b = getValue(v2);
	return [a,b]( auto v ){ a(v); cout << b(v); };
} 
template <class Op2>
auto operator << ( ostream& o, Op2 v2 ) {
	auto b = getValue(v2);
	return [b]( auto v ){ cout << b(v); };
}

ostream& operator << ( ostream& o, char c) {
	printf("%c", c);
	return o;
}
ostream& operator << ( ostream& o, string s) {
	const char *c = s.c_str();
	printf("%s", c);
	return o;
}
template <typename V, typename F>
auto operator | ( const V& v, F func ) {
    if constexpr( is_same_v< bool, invoke_result_t< F, decltype( *begin( v ) ) > > ) {
        vector< decay_t< decltype( *begin( v ) ) > > res;
 
	for( auto x: v )
            if( invoke( func, x ) )
                res.push_back( x );

        return res;
    }
    else if constexpr( is_same_v< void, invoke_result_t< F, decltype( *begin( v ) ) > > ) {
        for( auto x: v )
            func( x );
    }
    else {
        vector< decay_t< invoke_result_t< F, decltype( *begin( v ) ) > > > res;
        
        for( auto x: v )
            res.push_back( invoke( func, x ) );
            
        return res;
    }  
}

int main() {
	  
	string v1[] = { "a", "b2", "cc3", "saci" };
	v1 | []( string n ) { return n.length() % 2 == 0; } | (x+x) | cout << x << ' ';

}
