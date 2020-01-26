#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;
#define MOD 1000000007
#define REP(i, n) for (ll i = 0, i##_len = (n); i < i##_len; i++)

ll solve(string num_str, ll mod)
{
    ll L = num_str.size();
    ll dp[L + 1][2][mod];
    fill((long long *)dp, (long long *)dp + sizeof(dp) / sizeof(long long), 0);

    dp[0][0][0] = 1;
    REP(i, L)
    {
        ll D = num_str[i] - '0';
        REP(j, 2)
        {
            REP(k, mod)
            {
                REP(d, (j ? 10 : D + 1))
                {
                    dp[i + 1][j || (d < D)][k] += dp[i][j][((mod * 10) + k - d) % mod];
                    dp[i + 1][j || (d < D)][k] %= MOD;
                }
            }
        }
    }
    return (MOD - 1 + dp[L][0][0] + dp[L][1][0]) % MOD;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);

    ll d;
    string n;
    cin >> n >> d;
    cout << solve(n, d) << endl;
}
