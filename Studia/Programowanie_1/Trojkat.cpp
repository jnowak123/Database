#include <iostream>
#include <cmath>
using namespace std;

main(){
    float a, b, c;
    cout << "Podaj pierwsza liczbe. \n";
    cin >> a;
    cout << "Podaj druga liczbe. \n";
    cin >> b;
    cout << "Podaj trzecia liczbe. \n";
    cin >> c;
    cout << "Boki a = " << a << ", b = " << b << " i c = ";

    if((a*a + b*b == c*c) or (b*b + c*c == a*a) or (c*c + a*a == b*b))
        cout << "tworza trojkat prostokatny.";
    else
        cout << "nie tworza trojkata prostokatnego."; 
}