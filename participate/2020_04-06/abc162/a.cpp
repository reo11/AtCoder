#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;

void solve(){
    string n;
    cin >> n;
    bool f = false;
    for(int i = 0; i < 3; i++){
        if(n[i] == '7'){
            f = true;
        }
    }
    if(f){
        cout << "Yes" << endl;
    }else{
        cout << "No" << endl;
    }
}

int main(){
    solve();
}