#include <iostream>
#include <string>
#include <vector>
#include <math.h>
using namespace std;

int main(){
    int num;
    cin >> num;
    
    string mylst[num];
    for(int i = 0; i<num; i++)
        cin >> mylst[i];

    vector<long long> stack;
    for(int i = 0; i<num; i++){
        if(mylst[i] == "+"){
            long long sum = 0;
            sum += stack.back();
            stack.pop_back();
            sum += stack.back();
            stack.pop_back();
            stack.push_back(sum);
        }
        else if(mylst[i] == "-"){
            long long temp = stack.back();
            stack.pop_back();
            long long sum = stack.back() - temp;
            stack.pop_back();
            stack.push_back(sum);
        }
        else if(mylst[i] == "*"){
            long long temp = stack.back();
            stack.pop_back();
            long long sum = stack.back()*temp;
            stack.pop_back();
            stack.push_back(sum);
        }
        else if(mylst[i] == "/"){
            double temp = (double) stack.back();
            stack.pop_back();
            double div = stack.back()/temp;
            long long sum = floor(div);
            stack.pop_back();
            stack.push_back(sum);
        }
        else
            stack.push_back(stoi(mylst[i]));
    }

    cout << stack[0];
}
