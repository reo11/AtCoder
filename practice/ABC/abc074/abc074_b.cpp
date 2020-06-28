#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);

    long long int n, k, x;
    long long int ans = 0;
    cin >> n;
    cin >> k;
    for (int i = 0; i < n; i++){
        cin >> x;
        ans += 2 * min(x, abs(k - x));
    }
    cout << ans << endl;
}
