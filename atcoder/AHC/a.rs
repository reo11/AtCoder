use proconio::input;

fn main() {
    input! {
        d: usize,
        c: [i64; 26],
        s: [[i64; 26]; d],
    }

    for i in 0..d {
        let max_index = s[i].iter().position(|&x| x == *s[i].iter().max().unwrap()).unwrap();
        println!("{}", max_index + 1);
    }
}
