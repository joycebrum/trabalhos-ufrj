#include <initializer_list>
#include <iostream>
#include <memory>

using namespace std;

class AbstractPair {
public:
  virtual ~AbstractPair() {}

  virtual void imprime( ostream& o ) const = 0; 
};

template <typename A, typename B>
class ImplPair: public AbstractPair {
public:
  ImplPair( const A& a, const B& b ): a(a), b(b) {}

  virtual void imprime( ostream& o ) const {
    o << a << " = " << b;
  }
  
private:
  A a;
  B b;
};

class Pair {
public:
  template <typename A, typename B>
  Pair( A a, B b ): ap( new ImplPair( a, b ) ) {}
  
  void imprime( ostream& o ) const {
    ap->imprime( o );
  }
  
private:
  shared_ptr<AbstractPair> ap;
};

ostream& operator << ( ostream& o, const Pair& p ) {
  p.imprime( o );
  return o;
}

void print( initializer_list<Pair> lista ) { 
  for( auto p : lista )
    cout << p << endl;
}

int main () {

}
