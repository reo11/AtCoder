#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using llpair = pair<ll, ll>;
#define INF 10000000000000
// 大きい配列はグローバルで書く
ll a[51][51];
ll dxy[4][2] = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

ll dijakstra(llpair start, ll h, ll w){
    ll d[h][w];
    for(ll i=0; i < h; i++){
        for(ll j=0; j < w; j++){
            d[i][j] = INF;
        }
    }
    d[start.second][start.first] = 0;
    priority_queue<pair<ll, llpair>> que;
    que.push(pair<ll, llpair>(0, start));
    while(!que.empty()){
        pair<ll, llpair> top = que.top();
        ll u_i = top.second.first, u_j = top.second.second;
        que.pop();
        // if(d[0][w-1] != INF && d[h-1][0] != INF && d[h-1][w-1] != INF){
        //     break;
        // }
        ll v_i, v_j;
        for(ll i=0; i < 4; i++){
            v_i = u_i + dxy[i][0];
            v_j = u_j + dxy[i][1];
            if(!((0 <= v_i && v_i <= w-1) && (0 <= v_j && v_j <= h-1))){
                continue;
            }
            ll alt = d[u_j][u_i] + a[v_j][v_i];
            if(d[v_j][v_i] > alt){
                d[v_j][v_i] = alt;
                que.push(pair<ll, llpair>(alt, llpair(v_i, v_j)));
            }
        }
    }
    return d[0][w-1] + d[h-1][0] + d[h-1][w-1] + a[start.second][start.first];
}

void solve(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    // input
    ll h, w;
    cin >> h >> w;
    for(ll i=0; i < h; i++){
        for(ll j=0; j < w; j++){
            cin >> a[i][j];
        }
    }

    ll ans = INF, cost;
    for(ll i=0; i < w; i++){
        for(ll j=0; j < h; j++){
            cost = dijakstra(llpair(i, j), h, w);
            ans = min(ans, cost);
            // cout << ans << endl;
        }
    }
    cout << ans << "\n";
}

int main(){
    solve();
}