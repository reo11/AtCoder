use proconio::input;
use num::integer::gcd;

fn solve1(n: &i64, d: &i64, k: &i64) {
    let a = n / gcd(*n, *d);
    let x: i64 = ((k - 1) / a) + (((k - 1) * d) % n);
    println!("{}", x);
}

fn main() {
    input! {
        t: i64
    }

    for _i in 0..t {
        input! {
            n: i64,
            d: i64,
            k: i64
        }

        // 愚直解
        solve1(&n, &d, &k);
    }
}
