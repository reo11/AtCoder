use proconio::input;

fn main() {
    input! {
        h: usize,
        w: usize,
        c: [String; h],
    }

    for i in 0..h {
        println!("{}", c[i]);
    }
}
