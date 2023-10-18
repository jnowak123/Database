//Jakub Nowak
#include <iostream>
using namespace std;

int main()
{
    int div;
    cin >> div;
    int x;
    cin >> x;
    
    int nums[x];
    int num;
    for(int i = 0; i < x; i++){
        cin >> num;
        nums[i] = num;
    }
    
    for(int i = 0; i < x; i++){
        if (div % nums[i] == 0)
            cout << "TAK\n";
        else
            cout << "NIE\n";
          
    }
}