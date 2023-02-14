#include <iostream>
/**
 * Para executar: g++ -Wall -std=c++17 -o pilha pilha.cc
 * 
 * CONSTANTES
 * Para declarar constantes, apesar de ser compatível com C,
 * a maneira correta de fazêlo em C++ é com const
 * const int MAX_PÍLHA = 100;
 */
/* 
 * ou, mania de quem ainda está habituado em C
 * enum Constantes = { MAX_PILHAS: 100 }
*/

class PilhaInt {

	public:
		PilhaInt() {
			for( int i = 0; i < MAX_PILHA; i++ )
				tab[i] = 0;
			atual = 0;
		}
		
		int desempilha() {
			if (atual > 0) {
				return tab[--atual];
			}
			return -1;
		}
		
	private:
		static const int MAX_PILHA = 128;
		int tab[MAX_PILHA];
		int atual;
};

inline void PilhaInt::empilha (int valor) {
	if (atual >= 0 && atual < MAX_PILHA) {
		tab[atual++] = valor;
	}
}
/**
 * Inline faz com que não faça chamada de funções, e sim adicione o codigo assembly no lugar que for chamar
*/

/*
 * As visibilidades são definidas em seções: seções de público, privado, protected
 * Métodos declarados dentro da classe o compilador tenta substituir a chamada de função pela inserção do código assembly diretamente 
 * 
 * Para definir constantes
 */

// g++ -Wall -std=c++17 -o pilha pilha.cc

int main () {
	PilhaInt p, *q = new PilhaInt;
	// PilhaInt *tab = new PilhaInt[10]; // obrigatorio com *
	int x;
	int y;

	p.empilha( 3 );
	q->empilha( 5 );
	q->empilha ( 7 );
	p.empilha( 11 );
	// p.atual = 2; => erro de compilação: 
	// int PilhaInt::atual’ is private within this context
	x = p.desempilha();
	y = q->desempilha();
	
	std::cout << x + y << std::endl;
}

/**
 *  Para o C++ ponteiro e array são essencialmente diferentes	
 *	PilhaInt *q = new PilhaInt();
 *  delete q;
 *  PilhaInt *tab = new PilhaInt[10];
 *  delete [] tab;
 * 
 *  Isso pode dar muitos erros, por isso evite
 *  Em vez disso use vector
 * 
 *  DESTRUTORES
 * 	Os destrutores são chamados na ordem inversa de criação, a não ser que
 *  sejam explicitamente chamados.
 */
 