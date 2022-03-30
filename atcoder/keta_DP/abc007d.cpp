#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;

ll solve(ll num){
    string num_str = to_string(num);
    ll dp[num_str.size()+1][2][2] = {};
    dp[0][0][0] = 1;
    for(int i=0; i < num_str.size(); i++){
        ll D = num_str[i] - '0';
        for(int j=0; j < 2; j++){
            for (int k = 0; k < 2; k++){
                for (int d = 0; d <= (j ? 9 : D); d++){
                    dp[i+1][j || (d < D)][k || d == 4 || d == 9] += dp[i][j][k];
                }
            }
        }
    }
    return dp[num_str.size()][0][1]+dp[num_str.size()][1][1];
}


int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    ll a, b;
    cin >> a >> b;
    ll ans;
    ans = solve(b) - solve(a-1);
    cout << ans << endl;
}