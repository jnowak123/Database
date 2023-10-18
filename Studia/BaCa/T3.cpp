//Jakub Nowak
#include <iostream>
using namespace std;

int main()
{
    int n;
    int n_count = 0;
    cin >> n;

    while (n_count != n)
    {   
        float num;
        float min;
        float max;
        float sum;
        cin >> num;
        min = max = sum = num;
        int i_count = 1;
        while (i_count != 5)
        {
            cin >> num;
            if(num < min)
                min = num;
            if(num > max)
                max = num;
            sum += num;
            i_count ++;
        }
        n_count ++;
        cout << min << " " << max << " " << sum/5 << "\n";
    }
    
    
}