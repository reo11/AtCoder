use proconio::input;

fn main() {
    input! {
        n: i64,
    }

    for i in 0..n {
        input! {
            a: i64,
            b: i64
        }

        println!("{}", a + b);
    }
}
