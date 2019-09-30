Var a, b = 10;
cout << a << " " << b << endl;
a = 3.14;
b = "uma string";
cout << a << " " << b << endl;

/*
 * undefined 10
 * 3.14 uma string
 */

Var a;
a = 3;
cout << a["mes"] << endl;

//Erro fatal: Essa variável não é um objeto

Var a;
a = newObject();
cout << a(5) << endl;

//Erro fatal: Essa variável não pode ser usada como função

Var a[5] = { true, 'X', 2, 2.1, "abracadabra" };
Var b = 200, c = 300.1, d = "palavra ";
for( auto& x: a ) {
  cout << x+b << "," << x+c << "," << x+d << "," << 3 / x << "," << 1.1 * x << ","
       << (x && true) << "," << (x && false) <<  "," << (b >= x) << "," << (x < d) << endl;
}
/*
 * undefined,undefined,undefined,undefined,undefined,true,false,undefined,undefined
 * 288,undefined,Xpalavra ,undefined,undefined,undefined,undefined,false,true
 * 202,302.1,undefined,1,2.2,undefined,undefined,false,undefined
 * 202.1,302.2,undefined,1.42857,2.31,undefined,undefined,false,undefined
 * undefined,undefined,abracadabrapalavra ,undefined,undefined,undefined,undefined,undefined,true 
 * */
 
Var a, b;
a = newObject();
b = "José Maria";
a["nome"] = b;
a["nascimento"] = 1998;
b = "Maria José";
try {
  print( a );
} catch( Var::Erro e ) {
  cout << "Erro fatal: " << e() << endl;
}
cout << a << " " << a["nome"] << " " << a["nascimento"] << endl;
/*
 * { nome: José Maria, idade: Erro fatal: Essa variável não pode ser usada como função
 * object José Maria 1998
 * */
 
Var a, b;
a = 10.1;
b = []( auto x ){ return x + x; };
cout << b( a ) << " ";
cout << b( "oba" ) << " ";
cout << b( 'X' ) << " ";
cout << b( true );
//'"20.2 obaoba XX undefined"

Var a = newObject();
Var b = "José", c = "Maria";
a["nome"] = b + ' ' + c;
a["idade"] = []( auto v ) { return 2019 - v["nascimento"]; };
a["nascimento"] = 1990;
a["print"] = &print;
b = a;
imprime( a );
a["nascimento"] = 2001;
imprime( a );
imprime( b );
/*
 * { nome: José Maria, idade: 29, nascimento: 1990, print: function, atr: undefined }
 * { nome: José Maria, idade: 18, nascimento: 2001, print: function, atr: undefined }
 * { nome: José Maria, idade: 18, nascimento: 2001, print: function, atr: undefined }
 * */

Var a, b;
a = newObject();
a["init"] = []( auto x ) { x["nome"] = "Manoel";
                           x["idade"] = []( auto v ) { return 2019 - v["nascimento"]; };
                           x["nascimento"] = 1987;
                           x["print"] = &print;
                           return x; };
b = [a]( auto x ){ return x( a ); };
a["funcao"] = b;
b = &print;
a["funcao"]( a["init"] );
a["atr"] = a["init"]( newObject() );
a["funcao"]( b );
imprime( a["atr"] );

/*
 * { nome: Manoel, idade: 32, nascimento: 1987, print: function, atr: object }
 * { nome: Manoel, idade: 32, nascimento: 1987, print: function, atr: undefined }
 * */


