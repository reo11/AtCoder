use proconio::input;

fn main() {
    input! {
        n: usize,
        k: i64,
        mut s: [String; n]
    }
    let mut ans: Vec<String> = Vec::new();
    for i in 0..k {
        ans.push(s[i as usize].clone());
    }

    ans.sort();

    for i in 0..k {
        println!("{}", ans[i as usize]);
    }
}
