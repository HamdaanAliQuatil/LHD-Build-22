//program to reverse the string

#include <bits/stdc++.h>

using namespace std;


int main(){

    char a[1000]; //string init
    cout<<"Enter the sting to be reversed: ";
    cin.getline (a, 1000); //input string
    int n= strlen(a);     //counting number of characters

    for (int i = 0; i < n / 2; i++){    //loop to swap
        swap(a[i], a[n - i - 1]);
    }
    for (int i = 0; i < n; i++){    //display the reversed string
        cout<<a[i];
    }

}
