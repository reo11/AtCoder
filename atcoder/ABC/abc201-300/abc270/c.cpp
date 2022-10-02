#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;
#define out cout
#define in cin

#define REP(i, n) for (ll i = 0, i##_len = (n); i < i##_len; ++i)

int main(){
    ll n, x, y;
    in >> n >> x >> y;
    map<ll, vector<ll>> edges = {};
    ll u, v;
    REP(i, n - 1){
        in >> u >> v;
        edges[u].push_back(v);
        edges[v].push_back(u);
    }

    deque<ll> dq = {};
    dq.push_back(x);
    bool visited[200001] = {false};

    while(1){
        ll count = 0;
        ll current_edge = dq[dq.size() - 1];
        visited[current_edge] = true;
        vector<ll> next_edges = edges[current_edge];

        REP(i, next_edges.size()){
            ll next_edge = next_edges[i];
            if(visited[next_edge]){
                continue;
            } else {
                dq.push_back(next_edge);
                count += 1;
                break;
            }
        }

        if(dq[dq.size() - 1] == y) break;
        if(count == 0){
            dq.pop_back();
        }
    }

    REP(i, dq.size()){
        out << dq[i];
        if(i == ll(dq.size() - 1)){
            out << endl;
        } else {
            out << " ";
        }
    }

    return 0;
}