use proconio::input;

fn main() {
    input! {
        n: usize,
        mut k: i64,
        mut a: [i64; n]
    }

    a.sort();

    let mut ans = 0;
    for i in 0..n {
        if a[i] == ans && k > 0 {
            ans += 1;
            k -= 1;
        }
    }

    println!("{}", ans);
}
