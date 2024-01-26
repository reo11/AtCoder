use proconio::input;

fn ctz(mut x: u32) -> u32 {
    let mut res = 0;
    while x & 1 == 0 {
        x >>= 1;
        res += 1;
    }
    res
}

fn main() {
    input! {
        n: u32,
    }

    println!("{}", ctz(n));
}
