#include <iostream>
#include <string.h>

using namespace std;
int g_val = 3;
char g_chr = 'a';
float g_fl = 9.21;
string g_str = "helloworld";
uint32_t g_u32 = 333;

int main(){
    cout << g_val << endl;
    cout << g_chr << endl;
    cout << g_fl  << endl;
    cout << g_str << endl;
    cout << g_u32 << endl;   
    return 0;
}