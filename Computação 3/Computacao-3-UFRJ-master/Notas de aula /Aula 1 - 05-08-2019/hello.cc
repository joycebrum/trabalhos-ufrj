#include <iostream>

// só vale para programa pequeno e dispensa o uso de std::
// pode usar quantos quiser
using namespace std;

int main (int argc, char* argv[]) {
	//std::cout << "Hello World!";
	cout << "Hello World!\n";
	cout << "Hello World!" << "\n";
	
	cout << "Hello World!"
		 << endl;
}

/* 
 * Existem 3 streams principais: cin, cout, cerr
 * cout - console out 
 * cin - console in
 * cerr - console error
 * 
 * O operador << é o shift quando está com números inteiros, quando se trata de stream
 * ele simbolisa a entrada/saída do stream
 * 
 * endl - além de pular linha, limpa o buffer
 * acaba sendo um pouco mais demorado que o "\n", mas é mais seguro
 * 
 * return 0 é default no main, se não tiver return, ele retorna 0
*/
