#include<iostream>
using namespace std;
int main(){
    int l_var   = 21;
    int l_var1  = 12;
    float f_var = 6.87;
    char l_var3 = 65;

    l_var += 3; //23
    cout << "KQ1 = " << l_var << endl;
    l_var1 -= l_var;
    cout << "KQ2 = " <<  l_var1 << endl;
    f_var = (float)l_var1/5;
    cout << "KQ3 = " << f_var << endl;
    return 0;
} 