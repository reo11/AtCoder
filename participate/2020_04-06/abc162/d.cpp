#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;

void solve(){
    int64_t n;
    string s;
    cin >> n >> s;
    int64_t r = 0, g = 0, b = 0;
    for(int64_t i = 0; i < n; i++){
        if(s[i] == 'R'){
            r++;
        }else if(s[i] == 'G'){
            g++;
        }else{
            b++;
        }
    }
    int64_t ans = r * g * b;
    int64_t l;
    for(int64_t i = 0; i < n; i++){
        for(int64_t j = i+1; j < n; j++){
            l = j + (j - i);
            if(l >= n){
                continue;
            }
            if(s[i] != s[j] && s[j] != s[l] && s[i] != s[l]){
                ans--;
            }
        }
    }
    cout << ans << endl;
}

int main(){
    solve();
}