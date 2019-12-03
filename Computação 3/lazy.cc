#include <vector>
#include <iostream>
#include <functional>

using namespace std;

class Iterator {
	public:
	Iterator(int a): a(a), elemento(a) {}
	
	auto begin() {
		elemento = a;
		return *this;
	}
	
	auto end() {
		return *this;
	}
	
	int operator * () {
		return elemento;
	}
	
	auto operator ++ (int n) {
		elemento += 1;
		return *this;
	}
	
	private:
	int elemento;
	int a;
};

template <typename V, typename F>
auto operator | ( const V& v, F func ) {
    if constexpr( is_same_v< bool, invoke_result_t< F, decltype( *v.begin() ) > > ) {
        vector< decay_t< decltype( *v.begin() ) > > res;
 
	for( auto x: v )
            if( invoke( func, x ) )
                res.push_back( x );

        return res;
    }
    else if constexpr( is_same_v< void, invoke_result_t< F, decltype( *v.begin() ) > > ) {
        for( auto x: v )
            func( x );
    }
    else {
        vector< decay_t< invoke_result_t< F, decltype( *v.begin() ) > > > res;
        
        for( auto x: v )
            res.push_back( invoke( func, x ) );
            
        return res;
    }  
}

vector<int> Intervalo( int a, int b ) {
	vector<int> v;
	for(int i = a; i < b; i++) {
		v.push_back(i);
	} 
	return vector<int>(v);
}

Iterator Intervalo( int a ) {
	return Iterator(a);
}

int main() {
	Intervalo( 9, 12 )  | []( auto x ) { cout << x << " "; };
	cout << *Intervalo(1).begin() << " " << *(Intervalo(1)++);
}
