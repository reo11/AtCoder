#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;

#define MOD 1000000007
// 青のボールを並べて入る場所を列挙
// 赤のボールの数を考えずにが入る場所をcomb(n, b, mod)とかで求める
// 余った赤のボールの数の階乗とかをかける
// これをテーブルで持っておいてあとで引いてくる
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);

    ll n, k;
    cin >> n >> k;

    ll dp[n+1][n+1] = {};
    for(int i=1; i <= n; i++){
        for(int j=1; j <= i; j++){
            dp[i][j] = n - j + 1;
        }
    }
}