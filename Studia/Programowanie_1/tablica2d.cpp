#include <iostream>
using namespace std;

main(){
    int diagonalna[10][10];
    for(int i = 0; i != 10; i++){
        for(int j = 0; j != 10; j++){
            if(i == j)
                diagonalna[i][j] = 1;
            else
                diagonalna[i][j] = 0;
            cout << diagonalna[i][j];
        }
        cout << endl;
    }
    int sum = 0;
    for (int i = 0; i != 10; i++)
        sum += diagonalna[i][i];
    cout << sum;
}