// template
#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;
typedef pair<long long, long long> LP;
#define INF 999999999
#define MOD 1000000007
#define REP(i, n) for(ll i = 0, i##_len = (n); i < i##_len; ++i)
#define REP_AB(i, a, b) for (ll i = ll(a); i <= ll(b); ++i)
#define ALL(v) v.begin(), v.end()
#define SORT(v) sort(ALL(v))
#define UNIQUE(v) sort(ALL(v));v.erase(unique(ALL(v)), v.end());
#define SIZE(x) ((ll)(x).size())
#define REVERSE(v) reverse(ALL(v))
ll gcd(ll a,ll b){return b?gcd(b,a%b):a;}
ll lcm(ll a,ll b){return (a / gcd(a, b)) * b;}
int dx[4]={1,0,-1,0};
int dy[4]={0,1,0,-1};
#define out cout
#define in cin
template<class T>bool chmax(T &a, const T &b) { if (a<b) { a=b; return 1; } return 0; }
template<class T>bool chmin(T &a, const T &b) { if (b<a) { a=b; return 1; } return 0; }
// template end


int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    ll n;
    in >> n;
    if(n==1){
        ll a;
        in >> a;
        out << a << endl;
    }else{
        vector<ll> even(ceil(n/2.0));
        vector<ll> odd(int(n/2));
        REP(i, n){
            if(i % 2 == 0){
                in >> even[int(i/2)];
            }else{
                in >> odd[int(i/2)];
            }
        }
        if(n % 2 == 1){
            REVERSE(even);
            REP(i, even.size()){
                out << even[i] << " ";
            }
            REP(i, odd.size()){
                if(i < odd.size()-1){
                    out << odd[i] << " ";
                }else{
                    out << odd[i] << endl;
                }
            }
        }else{
            REVERSE(odd);
            REP(i, odd.size()){
                out << odd[i] << " ";
            }
            REP(i, even.size()){
                if(i < even.size()-1){
                    out << even[i] << " ";
                }else{
                    out << even[i] << endl;
                }
            }
        }
    }
}
