use proconio::input;

fn main() {
    input! {
        s: String
    }
    let mut ans = String::from("");

    for i in 0..s.len() {
        if let Some(char_at_i) = s.chars().nth(i) {
            if char_at_i == '0' {
                ans.push('1');
            } else {
                ans.push('0');
            }
        } else {
            continue;
        }
    }


    println!("{}", ans);
}
