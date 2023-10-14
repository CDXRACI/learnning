#include <iostream>
using namespace std;

// var global
int g_val = 10;
// const 
const int g_conVar = 30;

int main(){
// var local
int l_val = 20;
// false: because g_conVar was defined to be const
//g_conVar += l_val;
g_val += l_val;
cout << g_conVar <<  "\r\n"<<l_val << endl;
cout << g_val << endl;
}