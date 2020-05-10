#include <bits/stdc++.h>
using namespace std;
#define endl "\n"
using ll = long long;
using P = pair<ll, ll>;

const ll infll = (1LL << 62) - 1;
const int inf = (1 << 30) - 1;

struct IoSetup {
    IoSetup() {
        cin.tie(nullptr);
        ios::sync_with_stdio(false);
        cout << fixed << setprecision(10);
        cerr << fixed << setprecision(10);
    }
} iosetup;

template< typename T1, typename T2 >
inline bool chmax(T1 &a, T2 b) { return a < b && (a = b, true); }

template< typename T1, typename T2 >
inline bool chmin(T1 &a, T2 b) { return a > b && (a = b, true); }

void fail() {
    cout << -1 << endl;
    exit(0);
}

ll digit_sum(ll num){
    if(num < 10) return num;
    return digit_sum(num/10) + num % 10;
}

int main(){
    string s;
    cin >> s;
    ll n = s.size();
    ll dp[n+1][2][10];
    for(ll i=0; i < n+1; i++){
        for(ll j=0; j < 2; j++){
            for(ll k=0; k < 10; k++){
                dp[i][j][k] = -1000000;
            }
        }
    }
    dp[0][1][0] = 0;
    ll pre_d = 0, d = 0;
    for(ll i=1; i < n+1; i++){
        pre_d = d;
        d = s[i-1] - '0';
        for(ll j=0; j < 2; j++){
            if(j == 0){
                for(ll k=0; k < 10; k++){
                    for(ll m=0; m < 2; m++){
                        if(m==0){
                            for(ll l=0; l < 10; l++){
                                if(k >= d) break;
                                chmax(dp[i][j][k], dp[i-1][1][l] + k);
                            }
                        }else{
                            for(ll l=0; l < 10; l++){
                                chmax(dp[i][j][k], dp[i-1][0][l] + k);
                            }
                        }
                    }
                }
            }else{
                chmax(dp[i][1][d], dp[i-1][1][pre_d] + d);
            }
        }
    }
    ll ans = 0;
    for(ll i=0; i < 2; i++){
        for(ll j=0; j < 10; j++){
            chmax(ans, dp[n][i][j]);
            // cout << ans << endl;
        }
    }
    // for(ll k=0; k < n+1; k++){
    //     for(ll i=0; i < 2; i++){
    //         for(ll j=0; j < 10; j++){
    //             cout << dp[k][i][j] << " ";
    //         }
    //         cout << endl;
    //     }
    // }
    cout << ans << endl;
}