#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;

int main(){
    string s, t, u;
    ll a, b;
    cin >> s >> t;
    cin >> a >> b;
    cin >> u;

    if(s == u){
        a--;
    }else
    {
        b--;
    }
    cout << a << " " << b << "\n";
}