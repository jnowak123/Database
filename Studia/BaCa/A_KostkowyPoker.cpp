//Jakub Nowak
#include <iostream>
using namespace std;

main(){

    float pA_w = 0, pA_l = 0, pA_d = 0, pB_w = 0, pB_l = 0, pB_d = 0, pC_w = 0, pC_l = 0, pC_d = 0, pD_w = 0, pD_l = 0, pD_d = 0, pE_w = 0, pE_l = 0, pE_d = 0; // player x wins/losses
    int n;
    cin >> n;
    
    while(n != 0){
        char p1, p2;
        int p1_score = 9, p2_score = 9, p_winner = 0, p1_rep = 0, p2_rep = 0;
        int p1_a, p1_b, p1_c, p1_d, p2_a, p2_b, p2_c, p2_d;
        cin >> p1 >> p1_a >> p1_b >> p1_c >> p1_d >> p2 >> p2_a >> p2_b >> p2_c >> p2_d;

        if (p1_a == p1_b && p1_b == p1_c && p1_c == p1_d){ //Wszystkie takie same p1
            p1_score = 1;
            p1_rep = p1_a;
        }
        else if (p1_a != p1_b && p1_a != p1_c && p1_a != p1_d && p1_b != p1_c && p1_b != p1_d && p1_c != p1_d){ //Wszystkie rozne p1
            p1_score = 2;
        }
        else if (p1_a == p1_b && p1_c == p1_d){ //Dwie pary p1
            p1_score = 3;
            if (p1_a > p1_c)
                p1_rep = p1_a;
            else
                p1_rep = p1_c;
        }
        else if (p1_a == p1_c && p1_b == p1_d){
            p1_score = 3;
            if (p1_a > p1_b)
                p1_rep = p1_a;
            else
                p1_rep = p1_b;
        }
        else if (p1_a == p1_d && p1_b == p1_c){
            p1_score = 3;
            if (p1_a > p1_b)
                p1_rep = p1_a;
            else
                p1_rep = p1_b;
        }
        else if (p1_a == p1_b && p1_b == p1_c || p1_a == p1_b && p1_b == p1_d || p1_a == p1_c && p1_c == p1_d){ //Trojki p1
            p1_score = 4;
            p1_rep = p1_a;
        }
        else if (p1_b == p1_c && p1_c == p1_d){
            p1_score = 4;
            p1_rep = p1_b;
        }
        else if (p1_a == p1_b || p1_a == p1_c || p1_a == p1_d){ //Pary p1
            p1_score = 5;
            p1_rep = p1_a;
        }
        else if (p1_b == p1_c || p1_b == p1_d){
            p1_score = 5;
            p1_rep = p1_b;
        }
        else if (p1_c == p1_d){
            p1_score = 5;
            p1_rep = p1_c;
        }

        if (p2_a == p2_b && p2_b == p2_c && p2_c == p2_d){ //Wszystkie takie same p2
            p2_score = 1;
            p2_rep = p2_a;
        }
        else if (p2_a != p2_b && p2_a != p2_c && p2_a != p2_d && p2_b != p2_c && p2_b != p2_d && p2_c != p2_d){ //Wszystkie rozne p2
            p2_score = 2;
        }
        else if (p2_a == p2_b && p2_c == p2_d){ //Dwie pary p2
            p2_score = 3;
            if (p2_a > p2_c)
                p2_rep = p2_a;
            else
                p2_rep = p2_c;
        }
        else if (p2_a == p2_c && p2_b == p2_d){
            p2_score = 3;
            if (p2_a > p2_b)
                p2_rep = p2_a;
            else
                p2_rep = p2_b;
        }
        else if (p2_a == p2_d && p2_b == p2_c){
            p2_score = 3;
            if (p2_a > p2_b)
                p2_rep = p2_a;
            else
                p2_rep = p2_b;
        }
        else if (p2_a == p2_b && p2_b == p2_c || p2_a == p2_b && p2_b == p2_d || p2_a == p2_c && p2_c == p2_d){ //Trojki p2
            p2_score = 4;
            p2_rep = p2_a;
        }
        else if (p2_b == p2_c && p2_c == p2_d){
            p2_score = 4;
            p2_rep = p2_b;
        }
        else if (p2_a == p2_b || p2_a == p2_c || p2_a == p2_d){ //Pary p2
            p2_score = 5;
            p2_rep = p2_a;
        }
        else if (p2_b == p2_c || p2_b == p2_d){
            p2_score = 5;
            p2_rep = p2_b;
        }
        else if (p2_c == p2_d){
            p2_score = 5;
            p2_rep = p2_c;
        }
        
        if (p1_score < p2_score) // Result calc
            p_winner = 1;
        else if (p2_score < p1_score)
            p_winner = 2;
        else if ((p1_score == 1 || p1_score == 3 || p1_score == 4 || p1_score == 5) && p1_rep != p2_rep){
            if (p1_rep > p2_rep)
                p_winner = 1;
            else if (p1_rep < p2_rep)
                p_winner = 2;
        }

        else{
            if (p1_a + p1_b + p1_c + p1_d > p2_a + p2_b + p2_c + p2_d)
                p_winner = 1;
            else if (p1_a + p1_b + p1_c + p1_d < p2_a + p2_b + p2_c + p2_d)
                p_winner = 2;
            else
                p_winner = 3; // Draw
        }

        if (p1 == 'a'){ //Sum p1
            if (p_winner == 1)
                pA_w = pA_w +1;
            else if (p_winner == 2)
                pA_l = pA_l +1;
            else
                pA_d = pA_d +1;
        }
        else if (p1 == 'b'){
            if (p_winner == 1)
                pB_w = pB_w +1;
            else if (p_winner == 2)
                pB_l = pB_l +1;
            else
                pB_d = pB_d +1;
        }
        else if (p1 == 'c'){
            if (p_winner == 1)
                pC_w = pC_w +1;
            else if (p_winner == 2)
                pC_l = pC_l +1;
            else
                pC_d = pC_d +1;
        }
        else if (p1 == 'd'){
            if (p_winner == 1)
                pD_w = pD_w +1;
            else if (p_winner == 2)
                pD_l = pD_l +1;
            else
                pD_d = pD_d +1;
        }
        else if (p1 == 'e'){
            if (p_winner == 1)
                pE_w = pE_w +1;
            else if (p_winner == 2)
                pE_l = pE_l +1;
            else
                pE_d = pE_d +1;
        }
        if (p2 == 'a'){ //Sum p2
            if (p_winner == 2)
                pA_w = pA_w +1;
            else if (p_winner == 1)
                pA_l = pA_l +1;
            else
                pA_d = pA_d +1;
        }
        else if (p2 == 'b'){
            if (p_winner == 2)
                pB_w = pB_w +1;
            else if (p_winner == 1)
                pB_l = pB_l +1;
            else
                pB_d = pB_d +1;
        }
        else if (p2 == 'c'){
            if (p_winner == 2)
                pC_w = pC_w +1;
            else if (p_winner == 1)
                pC_l = pC_l +1;
            else
                pC_d = pC_d +1;
        }
        else if (p2 == 'd'){
            if (p_winner == 2)
                pD_w = pD_w +1;
            else if (p_winner == 1)
                pD_l = pD_l +1;
            else
                pD_d = pD_d  +1;
        }
        else if (p2 == 'e'){
            if (p_winner == 2)
                pE_w = pE_w +1;
            else if (p_winner == 1)
                pE_l = pE_l +1;
            else
                pE_d = pE_d +1;
        }
        n = n -1;
    }

    if (pA_w != 0 || pA_l != 0 || pA_d != 0){
        cout << "gracz a" << endl;
        if (pA_w != 0)
            cout << "    wygrane: " << pA_w / (pA_w + pA_d + pA_l) *100 << "%" << endl;
        if (pA_d != 0)
            cout << "    remisy: " << pA_d / (pA_w + pA_d + pA_l) *100 << "%" << endl;
        if (pA_l != 0)
            cout << "    przegrane: " << pA_l / (pA_w + pA_d + pA_l) *100 << "%" << endl;
        cout << endl;
    }
    if (pB_w != 0 || pB_l != 0 || pB_d != 0){
        cout << "gracz b" << endl;
        if (pB_w != 0)
            cout << "    wygrane: " << pB_w / (pB_w + pB_d + pB_l) *100 << "%" << endl;
        if (pB_d != 0)
            cout << "    remisy: " << pB_d / (pB_w + pB_d + pB_l) *100 << "%" << endl;
        if (pB_l != 0)
            cout << "    przegrane: " << pB_l / (pB_w + pB_d + pB_l) *100 << "%" << endl;
        cout << endl;
    }
    if (pC_w != 0 || pC_l != 0 || pC_d != 0){
        cout << "gracz c" << endl;
        if (pC_w != 0)
            cout << "    wygrane: " << pC_w / (pC_w + pC_d + pC_l) *100 << "%" << endl;
        if (pC_d != 0)
            cout << "    remisy: " << pC_d / (pC_w + pC_d + pC_l) *100 << "%" << endl;
        if (pC_l != 0)
            cout << "    przegrane: " << pC_l / (pC_w + pC_d + pC_l) *100 << "%" << endl;
        cout << endl;
    }
    if (pD_w != 0 || pD_l != 0 || pD_d != 0){
        cout << "gracz d" << endl;
        if (pD_w != 0)
            cout << "    wygrane: " << pD_w / (pD_w + pD_d + pD_l) *100 << "%" << endl;
        if (pD_d != 0)
            cout << "    remisy: " << pD_d / (pD_w + pD_d + pD_l) *100 << "%" << endl;
        if (pD_l != 0)
            cout << "    przegrane: " << pD_l / (pD_w + pD_d + pD_l) *100 << "%" << endl;
        cout << endl;
    }
    if (pE_w != 0 || pE_l != 0 || pE_d != 0){
        cout << "gracz e" << endl;
        if (pE_w != 0)
            cout << "    wygrane: " << pE_w / (pE_w + pE_d + pE_l) *100 << "%" << endl;
        if (pE_d != 0)
            cout << "    remisy: " << pE_d / (pE_w + pE_d + pE_l) *100 << "%" << endl;
        if (pE_l != 0)
            cout << "    przegrane: " << pE_l / (pE_w + pE_d + pE_l) *100 << "%" << endl;
        cout << endl;
    }
    return 0;
}