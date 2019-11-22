#include <functional>
#include <type_traits>

template <typename F>
class Bind {
private:
	F f; 
public:
	Bind( F f ): f(f) {}

	template <typename ...Args>
	auto operator()( Args... args ) {
		if constexpr( std::is_invocable_v< F, Args... > )
			return std::invoke( f, args... );
		else
			return [=, *this]( auto... n ){ return Bind{f}( args..., n... ); };
	}
 
};

template <typename F, typename ...Args>
auto bind( F f, Args... args ) {
	return Bind{ f }( args... );
}

int main() {
	
	
}
