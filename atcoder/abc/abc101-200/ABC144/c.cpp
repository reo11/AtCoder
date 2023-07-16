#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);

    ll n;
    cin >> n;

    ll ans = pow(10, 12) + 1;
    for(ll i = 1; i <= ll(sqrt(n)); i++){
        if(n % i == 0){
            ans = min(ans, i + (n / i) - 2);
        }
    }
    cout << ans << endl;
}
