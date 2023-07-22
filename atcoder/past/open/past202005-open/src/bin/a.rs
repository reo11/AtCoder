use proconio::input;

fn main() {
    input! {
        s: String,
        t: String,
    }

    if s == t {
        println!("same")
    } else if s.to_lowercase() == t.to_lowercase() {
        println!("case-insensitive")
    } else {
        println!("different")
    }
}
