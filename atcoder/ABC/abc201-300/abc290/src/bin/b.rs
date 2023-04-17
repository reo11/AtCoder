use proconio::input;

fn main() {
    input! {
        n: usize,
        mut k: i64,
        s: String
    }

    let mut ans = String::from("");
    for i in 0..n {
        if let Some(char_at_i) = s.chars().nth(i) {
            if char_at_i == 'o' && k > 0 {
                ans.push('o');
                k -= 1;
            } else {
                ans.push('x');
            }
        } else {
            continue;
        }
    }
    println!("{}", ans);
}
