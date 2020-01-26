#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;
#define REP(i, n) for (ll i = 0, i##_len = (n); i < i##_len; ++i)
#define REP_AB(i, a, b) for (ll i = ll(a); i < ll(b); ++i)
#define ALL(v) v.begin(), v.end()
#define SORT(v) sort(ALL(v))

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);

    ll n, d, a;
    cin >> n >> d >> a;
    vector<vector<ll>> xh(n, vector<ll>(2));
    REP(i, n)
    {
        cin >> xh[i][0] >> xh[i][1];
    }
    SORT(xh);
    ll ans = 0;
    ll a_num, base_x;
    REP(i, n){
        if(xh[i][1] > 0){
            a_num = ceil(xh[i][1] / a);
            xh[i][1] -= a_num * a;
            ans += a_num;
            base_x = xh[i][0];
            REP_AB(j, i, n){
                if(xh[j][0] <= base_x + (2 * d)){
                    xh[j][1] -= a_num * a;
                }else{
                    break;
                }
            }
        }
    }
    cout << ans << endl;
}
