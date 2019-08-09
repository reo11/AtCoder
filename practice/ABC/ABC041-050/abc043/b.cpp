// template
#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;
typedef pair<long long, long long> LP;
#define INF 999999999
#define MOD 1000000007
#define REP(i, n) for(int i = 0, i##_len = (n); i < i##_len; ++i)
#define REP_AB(i, a, b) for (int i = int(a); i <= int(b); ++i)
#define ALL(v) v.begin(), v.end()
#define SORT(v) sort(ALL(v))
#define UNIQUE(v) sort(ALL(v));v.erase(unique(ALL(v)), v.end());
#define SIZE(x) ((ll)(x).size())
int gcd(int a,int b){return b?gcd(b,a%b):a;}
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

    string s;
    in >> s;
    stack<char> output;
    REP(i, s.size()){
        if(s[i] == '0'){
            output.push('0');
        }else if(s[i] == '1'){
            output.push('1');
        }else{
            if(!output.empty()){
                output.pop();
            }
        }
    }
    int n = output.size();
    string ans[n];
    REP(i, n){
        ans[i] = output.top();
        output.pop();
    }
    REP(i, n){
        out << ans[n-i-1];
    }
    out << endl;
}
