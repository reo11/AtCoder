use proconio::input;
use std::cmp::min;

fn main() {
    input! {
        n: usize,
        a: [i64; 2 * n],
    }

    let mut dp = vec![vec![10000000000; 2 * n]; 2 * n];

    for i in 1..(2 * n) {
        dp[i - 1][i] = (a[i - 1] - a[i]).abs();
    }

    for dist in 2..=n {
        for i in 0..(2 * n) {
            let j = i + (2 * dist) - 1;
            if j < 2 * n {
                dp[i][j] = min(
                    dp[i][j],
                    (a[i] - a[j]).abs() + dp[i + 1][j - 1]
                );
                for k in i + 1..j - 1 {
                    dp[i][j] = min(
                        dp[i][j],
                        dp[i][k] + dp[k + 1][j]
                    );
                }
            }
        }
    }
    // for i in 0..2 * n {
    //     for j in 0..2 * n {
    //         print!("{} ", dp[i][j]);
    //     }
    //     println!();
    // }

    // 区間DP?
    // dp[i][j] = 区間[i, j)の最小コスト
    // dp[i][j] = min((dp[i + 2][j] [i + 2] + (a[i] - a[i + 1]).abs(), (dp[i][j - 2] + (a[j - 1] - a[j]).abs())


    println!("{}", dp[0][2 * n - 1]);
}
