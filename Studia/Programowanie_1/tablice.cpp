#include <iostream>
using namespace std;

main(){
    int tabl[10];
    for(int i=0; i != 10; i++){
        tabl[i] = i;
        cout << tabl[i] << endl;
    }
    for(int i=9; i != -1; i--){
        tabl[i] = i;
        cout << tabl[i] << endl;
    }
}