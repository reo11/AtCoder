// template
#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;
#define REP(i, n) for (ll i = 0, i##_len = (n); i < i##_len; ++i)

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);

    ll q, x;
    ll y, min_v, ans = 0;
    cin >> q >> x;
    ll a[x + 1] = {};

    REP(i, q)
    {
        cin >> y;
        a[y % x]++;
        while (a[ans % x])
        {
            a[ans % x]--;
            ans++;
        }
        cout << ans << endl;
    }
}
