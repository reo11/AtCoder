use proconio::input;

fn main() {
    input! {
        n: usize,
        m: usize,
        a: [i64; n],
        b: [usize; m]
    }
    let mut ans = 0;
    for i in 0..m {
        ans += a[b[i] - 1];
    }
    println!("{}", ans);
}
