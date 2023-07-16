use proconio::input;

fn main() {
    input! {
        n: usize
    }
    let mut a = vec![0; n];
    let mut b = vec![0; n];
    for i in 0..n {
        input! {
            a_i: i64,
            b_i: i64
        }
        a[i] = a_i;
        b[i] = b_i;
    }

    fn sum(start: i64, last: i64, length: i64) -> i64 {
        (start + last) * length / 2
    }

    let mut ans = 0;
    for i in 0..n {
        ans += sum(a[i], b[i], b[i] - a[i] + 1);
    }

    println!("{}", ans);
}
