use proconio::input;

fn main() {
    input! {
        d: usize,
        c: [i64; 26],
        s: [[i64; 26]; d],
        t: [i64; d],
    }

    let mut last = vec![0; 26];
    let mut ans = 0;
    for i in 0..d {
        ans += s[i][t[i] as usize - 1];
        last[t[i] as usize - 1] = i + 1;
        for j in 0..26 {
            ans -= c[j] * ((i + 1) - last[j]) as i64;
        }
        println!("{}", ans);
    }
}
