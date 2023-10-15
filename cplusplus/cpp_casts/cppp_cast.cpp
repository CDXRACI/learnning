#include "cpp_cast.h"
#include <iostream>
using namespace std;

int main(){    
    no_cast(355, 0 );
    int d = 3;
    float p = 2.1;
    p = (float)d/p;
    float x = 0;
    x = (float)d/2;
    cout << x << endl;
    cout << p << endl;
    return 0;
}

void no_cast(int p, char c){
    if ( (c >= 0 && p >= 0 ) != true ){
        cout << " error"<< endl; }
    c = p;
    cout << (int )c << endl;
}
void has_castx( int p, float t){
    // if ( (p >= 0 ) != true ){
    //     cout << "error "<< endl; }
    // t = p/2;
    // cout << t << endl;
}