#include "ifelse.h"
#include <iostream>
using namespace std;
int main(){
    int p = 1;
    ifelsecheck( 1 );
    return 0;
}

void ifelsecheck( int t ){
    if( t ){
        cout << "yes var is great than > " << endl;
    } else {
        cout << " no " << endl;
    }
}