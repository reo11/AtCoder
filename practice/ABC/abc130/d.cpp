#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);

    ll n, k;
    cin >> n >> k;
    ll a[n] = {};
    for(int i = 0; i < n; i++){
        cin >> a[i];
    }

    ll l = 0, r = 0;
    ll sum = 0;
    ll ans = 0;
    while(l < n){
        if(sum < k){
            sum += a[r];
            r += 1;
        }else{
            ans += n - r + 1;
            sum -= a[l];
            l += 1;
        }
    }

    cout << ans << endl;
}
