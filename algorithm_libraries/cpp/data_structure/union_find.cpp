#include <bits/stdc++.h>
using namespace std;

struct UnionFind {
    vector<long long> data;

    UnionFind(long long sz){
        data.assign(sz, -1);
    }
    long long find(long long k){
        if(data[k] < 0) return (k);
        return (data[k] = find(data[k]));
    }
    bool unite(long long x, long long y){
        x = find(x), y = find(y);
        if(x == y) return (false);
        if(data[x] > data[y]) swap(x, y);
        data[x] += data[y];
        data[y] = x;
        return (true);
    }
    long long size(long long k) {
        return (-data[find(k)]);
    }
    bool same(long long x, long long y){
        return (find(x) == find(y));
    }
    long long group_count() {
        long long res = 0;
        long long size = data.size();
        for(long long i = 0; i < size; i++) {
            if(data[i] < 0) res++;
        }
        return (res);
    }
};

int main() {
    long long N, Q;
    cin >> N >> Q;
    UnionFind uf(N + 1);
    for(long long i = 0; i < Q; i++) {
        long long T, U, V;
        cin >> T >> U >> V;
        if(T == 0) {
            uf.unite(U, V);
        } else {
            if(uf.same(U, V)) cout << 1 << endl;
            else cout << 0 << endl;
        }
    }
    return (0);
}