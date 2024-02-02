use proconio::input;

fn main() {
    input! {
        n: i32,
        m: i32,
        x: i32,
        t: i32,
        d: i32,
    }

    let mut ans = t - (x * d);

    for i in 1..=n {
        if i > m {
            break;
        }
        ans += d;
        if i == x {
            break;
        }
    }
    println!("{}", ans);
}