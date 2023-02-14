#ifndef variables
#define variables


// tipos de IO
#define DISCO 0
#define FITA_MAGNETICA 1
#define IMPRESSORA 2

#define MAX_PROCESSOS 50
#define TEMPO_RR 4
#define TEMPO_MAXIMO 20
#define TEMPO_MINIMO 1
#define TEMPO_MAX_CHEGADA 60
#define PID_INICIAL 10

// Gerenciados de Memoria
#define MEM_PRINCIPAL 64
#define INTERV_TEMP_PROC 3
#define INTERV_PAGS 3
#define WSL 4
#define MAX_VIRT_PAGE 64 // tamanho da tabela de paginas

/*-Variáveis Globais---------------------------------------------------*/

/*Tupla que indica o tipo de IO e a duração*/
typedef struct _IO {
	int tipoIO;
	char nomeTipo[20];
	int tempo;
	bool vaiPraAlta;
} IO;

//tipos de IO e seus respectivos tempos
IO tiposIO[3] = {{DISCO, "Disco", 3, 0}, {FITA_MAGNETICA, "Fita Magnética", 6, 1}, {IMPRESSORA, "Impressora", 10, 1}};

//não pode ser "new" ou "exit" pq sao simbolos da linguagem
enum statusTypes {novo, ready, ready_suspend, running, blocked, blocked_suspend, terminado};


int memoria[MEM_PRINCIPAL]; //em frames

// ---------------------------- variaveis do LRU -----------------
typedef struct _No {
	struct _No *proximo;
	struct _No *anterior;
	int valor;
}No;

typedef struct _GerenciadorPaginas {
	No *head;
	No *tail;
    int numberOfElements;
}GerenciadorPaginas;

// ---------------------------- variaveis do Processo -----------------

/*Tuplas da forma (IO, tempo), onde tempo*/
typedef struct _TempoChamadaIO {
	IO tipoIO;
	int tempoBloqueio;
} TempoChamadaIO;

/*Struct da Tabela de Páginas*/
typedef struct _Tabela_Paginas{
    int num_frame; // -1 se não tiver carregada
} Tabela_Paginas;

typedef struct _PaginasReferenciadas {
	int* vetor;
	int ultimaPaginaReferenciada;
	int quantidade;
} PaginasReferenciadas;

typedef struct _Processo {
	int PID;
	int PPID;
	int priority;
	enum statusTypes status;//Indica o status atual do processo
	int tempoEntrada;//Tempo em que o processo é criado
	int tempoServico;//Tempo previsto de processamento do processo
	int tempoExecutado;//Sempre no intervalo [tempoEntrada,tempoServico]
	int tempoTermino;//Tempo em que o processo termina de executar
	int tempoEspera;//Tempo que processo está ocioso na fila de baixa prioridade (ready)
	int tempoBloqueado; //Tempo que o processo está executando I/O
	int quantidadeChamadas; //Quantidade de IO que o processo irá executar
	TempoChamadaIO *chamada; //Vetor com os tempos de chamada de cada IO
	// parte referente a gerenciamento de memoria
	int numPaginas;
	Tabela_Paginas tabelaPaginas[MAX_VIRT_PAGE];
	PaginasReferenciadas paginasReferenciadas;
	GerenciadorPaginas *gerenciadorPaginas;
} Processo;


// ---------------------------- variaveis do FIFO ----------------
typedef struct _FIFO {
	Processo *queue[MAX_PROCESSOS];
    int numberOfElements;
    int head;
    int tail;
}FIFO;


// ----------------------------- Variaveis das filas

FIFO altaPrioridade;
FIFO baixaPrioridade;
FIFO filaDisco;
FIFO filaFita;
FIFO filaImpressora;


#endif

