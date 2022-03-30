#include<bits/stdc++.h>
using namespace std;
const int N=2005;
int n,m,u[N][N],d[N][N],l[N][N],r[N][N];
char s[N][N];
int main()
{
    scanf("%d%d",&n,&m);
    for(int i=1;i<=n;i++)
        scanf("%s",s[i]+1);
    for(int i=1;i<=n;i++)
        for(int j=1;j<=m;j++)
    {
        if(s[i][j]=='.')
        {
            u[i][j]=u[i-1][j]+1;
            l[i][j]=l[i][j-1]+1;
        }
    }
    for(int i=n;i>=1;i--)
        for(int j=m;j>=1;j--)
            if(s[i][j]=='.')
        {
            d[i][j]=d[i+1][j]+1;
            r[i][j]=r[i][j+1]+1;
        }
    int ans=0;
    for(int i=1;i<=n;i++)
        for(int j=1;j<=m;j++)
    {
        if(s[i][j]=='.')
        {
            ans=max(ans,u[i][j]+d[i][j]+l[i][j]+r[i][j]-3);
        }
    }
    printf("%d\n",ans);
}
