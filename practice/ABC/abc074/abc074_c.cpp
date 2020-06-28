// template
#include <bits/stdc++.h>
using namespace std;

// template end

double calc(int a, int b, int c, int d, int e, int f){
    double a_ = a + b;
    double b_ = c + d;
    if (a_ + b_ > f){
        return 0;
    }
    if (a_ == 0 or b_ == 0){
        return 0;
    }
    double dens = double((100.0 * b_) / (a_ + b_ + 0.0));
    if (dens > double((e * 100.0) / (e + 100.0))){
        dens = 0;
    }
    return dens;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);

    long long int a, b, c, d, e, f;
    cin >> a >> b >> c >> d >> e >> f;
    long long int sugar_w = a*100, sugar = 0;
    double dens, max_dens = 0;
    for (int i = 0; i <= ceil(f / a / 100); i++){
        for (int j = 0; j <= ceil(f / b / 100); j++){
            for (int k = 0; k <= ceil(f / c); k++){
                for (int l = 0; l <= ceil(f / d); l++){
                    dens = calc(100*i*a, 100*j*b, k*c, l*d, e, f);
                    if (dens > max_dens){
                        max_dens = dens;
                        sugar_w = 100*i*a + 100*j*b + k*c + l*d;
                        sugar = k*c + l*d;
                    }
                }
            }
        }
    }
    cout << sugar_w << " " << sugar << endl;
}
