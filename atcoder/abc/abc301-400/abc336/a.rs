use proconio::input;

fn main() {
    input! {
        n: usize,
    }

    let mut ans = String::new();

    ans.push_str("L");
    for i in 0..n {
        ans.push_str("o");
    }
    ans.push_str("ng");

    println!("{}", ans);
}
