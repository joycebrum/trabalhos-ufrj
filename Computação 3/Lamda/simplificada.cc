#include <iostream>
using namespace std; 

auto x = []( auto v ){ return v; };
auto cte( auto valor ) { return [valor]( auto x ) { return valor; } ; }

// --------------- operador Soma

template <typename Op1, typename Op2>
auto operator + ( Op1 a, Op2 b ) {
	return [a,b]( auto v ){ return a(v) + b(v); }; 
}
template <typename Op1>
auto operator + ( Op1 a, int valor ) {
	auto b = cte(valor);
	return [a,b]( auto v ){ return a(v) + b(v); }; 
}
template <typename Op2>
auto operator + ( int a, Op2 valor ) {
	auto b = cte(valor);
	return [a,b]( auto v ){ return a(v) + b(v); }; 
}
template <typename Op1>
auto operator + ( Op1 a, double valor ) {
	auto b = cte(valor);
	return [a,b]( auto v ){ return a(v) + b(v); }; 
}
template <typename Op2>
auto operator + ( double a, Op2 valor ) {
	auto b = cte(valor);
	return [a,b]( auto v ){ return a(v) + b(v); }; 
}

// ------------------ operador Subtração
template <typename Op1, typename Op2>
auto operator - ( Op1 a, Op2 b ) {
	return [a,b]( auto v ){ return a(v) - b(v); }; 
}
template <typename Op1>
auto operator - ( Op1 a, int valor ) {
	auto b = cte(valor);
	return [a,b]( auto v ){ return a(v) - b(v); }; 
}
template <typename Op2>
auto operator - ( int a, Op2 valor ) {
	auto b = cte(valor);
	return [a,b]( auto v ){ return a(v) - b(v); }; 
}
template <typename Op1>
auto operator - ( Op1 a, double valor ) {
	auto b = cte(valor);
	return [a,b]( auto v ){ return a(v) - b(v); }; 
}
template <typename Op2>
auto operator - ( double a, Op2 valor ) {
	auto b = cte(valor);
	return [a,b]( auto v ){ return a(v) - b(v); }; 
}

// ------------------ operador Multiplicação
template <typename Op1, typename Op2>
auto operator * ( Op1 a, Op2 b ) {
	return [a,b]( auto v ){ return a(v) * b(v); }; 
}
template <typename Op1>
auto operator * ( Op1 a, int valor ) {
	auto b = cte(valor);
	return [a,b]( auto v ){ return a(v) * b(v); }; 
}
template <typename Op2>
auto operator * ( int a, Op2 valor ) {
	auto b = cte(valor);
	return [a,b]( auto v ){ return a(v) * b(v); }; 
}
template <typename Op1>
auto operator * ( Op1 a, double valor ) {
	auto b = cte(valor);
	return [a,b]( auto v ){ return a(v) * b(v); }; 
}
template <typename Op2>
auto operator * ( double a, Op2 valor ) {
	auto b = cte(valor);
	return [a,b]( auto v ){ return a(v) * b(v); }; 
}

// ------------------ operador Divisão
template <typename Op1, typename Op2>
auto operator / ( Op1 a, Op2 b ) {
	return [a,b]( auto v ){ return a(v) / b(v); }; 
}
template <typename Op1>
auto operator / ( Op1 a, int valor ) {
	auto b = cte(valor);
	return [a,b]( auto v ){ return a(v) / b(v); }; 
}
template <typename Op2>
auto operator / ( int a, Op2 valor ) {
	auto b = cte(valor);
	return [a,b]( auto v ){ return a(v) / b(v); }; 
}
template <typename Op1>
auto operator / ( Op1 a, double valor ) {
	auto b = cte(valor);
	return [a,b]( auto v ){ return a(v) / b(v); }; 
}
template <typename Op2>
auto operator / ( double a, Op2 valor ) {
	auto b = cte(valor);
	return [a,b]( auto v ){ return a(v) / b(v); }; 
}

int main() {
	auto s = x + x + 7 - 1;
	cout << s(8) << endl;
}
