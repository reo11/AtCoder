#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;
#define REP(i, n) for (ll i = 0, i##_len = (n); i < i##_len; ++i)
#define REP_AB(i, a, b) for (ll i = ll(a); i < ll(b); ++i)
#define INF 100000000
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);

    ll h, n;
    cin >> h >> n;
    ll ab[n][2];
    REP(i, n){
        cin >> ab[i][0] >> ab[i][1];
    }

    ll max_ = 100000;
    ll dp[100000];
    REP(i, 100000){
        dp[i] = INF;
    }
    dp[0] = 0;
    REP(i, n){
        REP(j, max_){
            if(j - ab[i][0] >= 0){
                dp[j] = min(dp[j - ab[i][0]] + ab[i][1], dp[j]);
            }
        }
    }
    ll ans = INF;
    REP_AB(i, h, 100000){
        if(ans > dp[i]){
            ans = dp[i];
        }
    }
    cout << ans << endl;
}
