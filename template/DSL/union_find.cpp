#include <bits/stdc++.h>
using namespace std;
#define endl "\n"
using ll = long long;

struct UnionFind {
    vector<ll> data;

    UnionFind(ll sz){
        data.assign(sz, -1);
    }
    bool unite(ll x, ll y){
        x = find(x), y = find(y);
        if(x == y) return (false);
        if(data[x] > data[y]) swap(x, y);
        data[x] += data[y];
        data[y] = x;
        return (true);
    }
    ll find(ll k){
        if(data[k] < 0) return (k);
        return (data[k] = find(data[k]));
    }
    ll size(ll k) {
        return (-data[find(k)]);
    }
};