use proconio::input;

fn main() {
    input! {
        n: u32
    }

    if n % 2 == 0 {
        println!("White");
    } else {
        println!("Black");
    }
}