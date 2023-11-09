//Jakub Nowak
#include <iostream>
using namespace std;

int main(){
    int arr_n, n;
    cin >> arr_n;
    
    while (arr_n != 0){ // fr each array
        
        cin >> n;
        int arr[n];
        int i = 0;
        while (i != n){ // input fr array
            cin >> arr[i];
            i = i +1;
        }
        i = 0;
        while (i != n){
            cout << arr[i] << " "; // original array output
            i = i +1;
        }
        cout << endl;

        char command;
        cin >> command;
        while (command != 'F'){ // command logic

            int beg, len;
            cin >> beg >> len;
            beg = beg %n;
            if (beg < 0) beg = beg +n;
                int sh;
                if (len == 0){
                    if (command == 'M') cin >> sh;
                }

                else if (command == 'R'){ // Reverse
                    int end = (beg + len -1) %n;
                    int frag_n = n / len;
                    while (frag_n != 0){

                        int t_beg = beg, t_end = end, t_len = len/2;
                        while(t_len != 0){
                            int temp = arr[t_beg];
                            arr[t_beg] = arr[t_end];
                            arr[t_end] = temp;
                            t_beg = (t_beg +1) %n;
                            t_end = (t_end -1);
                            if (t_end < 0) t_end = t_end +n;
                            t_len = t_len -1;
                        }

                        beg = (beg + len) %n;
                        end = (end + len) %n;
                        frag_n = frag_n -1;
                    }
                }
                else if (command == 'M'){ // Move
                    int mov, frag_n = n /len, og_beg = beg;
                    cin >> mov;
                    int og_mov = mov;
                    mov = mov %len;
                    if (mov < 0) mov = mov + len;

                    while (frag_n != 0){
                        int t_mov = mov;
                        while (t_mov != 0){
                            int t_len = len, t_beg = beg, t2_beg, a = arr[beg], b;
                            while (t_len != 0){
                                t2_beg = (t_beg +1) %n;
                                if (t_len == 1) t2_beg = beg;
                                b = arr[t2_beg];
                                arr[t2_beg] = a;
                                a = b;
                                t_beg = t2_beg;
                                t_len = t_len -1;
                            }
                        
                        t_mov = t_mov -1;
                        }
                        beg = (beg + len) %n;
                        frag_n = frag_n -1;
                    }

                    len = og_beg - beg; // shift fr remainder
                    if (len < 0) len = len +n;
                    if (len != 0 && len != 1){
                        mov = og_mov %len;
                        if (mov < 0) mov = mov + len;
                        int t_mov = mov;
                        while (t_mov != 0){
                            int t_len = len, t_beg = beg, t2_beg, a = arr[beg], b;
                            while (t_len != 0){
                                t2_beg = (t_beg +1) %n;
                                if (t_len == 1) t2_beg = beg;
                                b = arr[t2_beg];
                                arr[t2_beg] = a;
                                a = b;
                                t_beg = t2_beg;
                                t_len = t_len -1;
                            }
                        t_mov = t_mov -1;
                        }
                    }
                }
                else if (command == 'C'){

                    int beg2 = (beg + len) %n;
                    int frag_n = n / (len*2);

                    while (frag_n != 0){
                        int t_len = len, t_beg = beg, t_beg2 = beg2;
                        while (t_len != 0){
                            int temp = arr[t_beg];
                            arr[t_beg] = arr[t_beg2];
                            arr[t_beg2] = temp;
                            t_beg = (t_beg +1) %n;
                            t_beg2 = (t_beg2 +1) %n;
                            t_len = t_len -1;
                        }
                        
                        beg = (beg + len*2) %n;
                        beg2 = (beg2 + len*2) %n;
                        frag_n = frag_n -1;
                    }
                    
                }
                else if (command == 'S'){ // sort

                    int type = 1;
                    if (len < 0){
                        len = -len;
                        type = -1;
                    }
                    if (len > n) len = n;

                    int frag_n = n / len, og_beg = beg;
                    while (frag_n != 0){

                        int sorted = 0;
                        while (sorted == 0){
                            sorted = 1;
                            int t_len = len -1, t_beg = beg;
                            if (type > 0){
                                while (t_len != 0){
                                    if (arr[t_beg] > arr[(t_beg +1) %n]){
                                        int temp = arr[t_beg];
                                        arr[t_beg] = arr[(t_beg +1) %n];
                                        arr[(t_beg +1) %n] = temp;
                                        sorted = 0;
                                    }
                                    t_len = t_len -1;
                                    t_beg = (t_beg +1) %n;
                                }
                            }
                            else {
                                while (t_len != 0){
                                    if (arr[t_beg] < arr[(t_beg +1) %n]){
                                        int temp = arr[t_beg];
                                        arr[t_beg] = arr[(t_beg +1) %n];
                                        arr[(t_beg +1) %n] = temp;
                                        sorted = 0;
                                    }
                                    t_len = t_len -1;
                                    t_beg = (t_beg +1) %n;
                                }
                            }
                        }
                        beg = (beg + len)%n;
                        frag_n = frag_n -1;
                    }
                    
                    int len2 = og_beg - beg;
                    if (len2 < 0) len2 = len2 +n;
                    if (len2 != 0){
                        int sorted = 0;
                        while (sorted == 0){
                            sorted = 1;
                            int t_len = len2 -1, t_beg = beg;
                            if (type > 0){
                                while (t_len != 0){
                                    if (arr[t_beg] > arr[(t_beg +1) %n]){
                                        int temp = arr[t_beg];
                                        arr[t_beg] = arr[(t_beg +1) %n];
                                        arr[(t_beg +1) %n] = temp;
                                        sorted = 0;
                                    }
                                    t_len = t_len -1;
                                    t_beg = (t_beg +1) %n;
                                }
                            }
                            else {
                                while (t_len != 0){
                                    if (arr[t_beg] < arr[(t_beg +1) %n]){
                                        int temp = arr[t_beg];
                                        arr[t_beg] = arr[(t_beg +1) %n];
                                        arr[(t_beg +1) %n] = temp;
                                        sorted = 0;
                                    }
                                    t_len = t_len -1;
                                    t_beg = (t_beg +1) %n;
                                }
                            }
                    }
                }
                
                
            }
            cin >> command;
        }

        i = 0;
        while (i != n){
            cout << arr[i] << " "; // finished arr output
            i = i +1;
        }
        cout << endl;
        
        arr_n = arr_n -1;
    }
    
    return 0;
}