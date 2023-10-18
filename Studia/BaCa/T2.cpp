// Jakub Nowak
#include <iostream>
using namespace std;

int main()
{
    int n;
    cin >> n;

    string students_id[n];
    int students_res[n][2];
    for (int i = 0; i < n; i++)
        cin >> students_id[i] >> students_res[i][0] >> students_res[i][1];

    for (int i = 0; i < n; i++)
    {
        int res = students_res[i][0] + students_res[i][1];
        cout << students_id[i] << " " << res << "% ";
        if (res < 50)
            cout << "niedostateczny (2.0)";
        else if (res >= 50 and res < 60)
            cout << "dostateczny (3.0)";
        else if (res >= 60 and res < 70)
            cout << "dostateczny plus (3.5)";
        else if (res >= 70 and res < 80)
            cout << "dobry (4.0)";
        else if (res >= 80 and res < 90)
            cout << "dobry plus (4.5)";
        else
            cout << "bardzo dobry (5.0)";
        cout << "\n";
    }
    
}