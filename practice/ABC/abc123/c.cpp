#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;

int main(){
    ll n;
    ll m = pow(10, 16);
    ll tmp;
    cin >> n;
    for(int i=0; i < 5; i++){
        cin >> tmp;
        m = min(m, tmp);
    }
    ll ans = ceil(n / double(m)) + 4;
    cout << ans << endl;
}