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

int main(){
    string s;
    cin >> s;
    ll y, m, d;
    y = stoi(s.substr(0, 4));
    m = stoi(s.substr(5, 6));
    d = stoi(s.substr(8, 9));
    ll days[13] = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    while(true){
        if(y % (m * d) == 0) break;
        ll days_max = days[m], tmp = 0;
        if(m == 2){
            if(y % 4 == 0) tmp = 1;
            if(y % 100 == 0) tmp = 0;
            if(y % 400 == 0) tmp = 1;
            days_max += tmp;
        }
        if(d >= days_max){
            d = 1;
            if(m == 12){
                m = 1;
                y++;
            }else{
                m++;
            }
        }else{
            d++;
        }
    }
    cout << std::setw(2) << std::setfill('0') << y << "/" << std::setw(2) << std::setfill('0') << m << "/" <<std::setw(2) << std::setfill('0') << d << endl;
}