#include <iostream>
using namespace std;

int main(){

    char alf = 65;

    for (int n = 4; n != 0; n--){
        cout << alf ++ << " " <<  alf ++ << endl;
    }

    int range;
    cin >> range;
    int line_n = 18/ range, remainder = 18% range;

    for (int n = line_n; n != 0; n--){
        int temp_range = range;
        for(temp_range; temp_range != 0; temp_range --){
            cout << alf ++ << " ";
        }
        cout << endl;
    }
    int temp_range = remainder;
        for(temp_range; temp_range != 0; temp_range --){
            cout << alf ++ << " ";
        }
}
