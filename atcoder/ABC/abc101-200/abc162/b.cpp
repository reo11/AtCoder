#include <bits/stdc++.h>
using namespace std;

void solve(){
    int64_t n, ans = 0;
    cin >> n;
    for(int64_t i = 1; i <= n; i++){
        if(i % 3 != 0 && i % 5 != 0){
            ans += i;
        }
    }
    cout << ans << endl;
}

int main(){
    solve();
}
