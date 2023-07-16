#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;


double dis(ll xy1[], ll xy2[]){
    return sqrt(pow((xy2[0] - xy1[0]), 2) + pow((xy2[1] - xy1[1]), 2));
}

ll f(ll n){
    if(n == 1){
        return 1;
    }else{
        return n * f(n-1);
    }
}


int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);

    ll n;
    cin >> n;

    ll xy[n][2];
    for(ll i=0; i < n; i++){
        cin >> xy[i][0] >> xy[i][1];
    }
    double ans = 0.0;
    for(ll i=0; i < n; i++){
        for(ll j=0; j < n; j++){
            ans += dis(xy[i], xy[j]) / n;
        }
    }
    cout << fixed << setprecision(10) << ans << endl;
}
