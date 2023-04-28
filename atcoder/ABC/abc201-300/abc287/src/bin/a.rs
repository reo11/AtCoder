use proconio::input;

fn main() {
    input! {
        n: i64
    }

    let mut ans = 0;

    for _ in 0..n {
        input! {
            s: String
        }
        if s == "For" {
            ans += 1;
        }
    }

    if ans > n / 2 {
        println!("Yes");
    } else {
        println!("No");
    }
}
