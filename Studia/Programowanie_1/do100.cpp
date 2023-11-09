// &a i sizeof(a) mają taką samą wartość pierwszeństwa (3)

#include <iostream>
using namespace std;

int main(){
    for (int i = 1; i <= 100; i++){
        cout << i << " ";
        if (i % 10 == 0) cout << endl << "zakonczona dziesiatka" << endl;
    }
}