use proconio::input;

fn main() {
    input! {
        n: usize,
        m: usize,
        s: [String; n],
        t: [String; m]
    }

    let mut ans = 0;

    for s_i in s {
        for t_i in t.iter() {
            if s_i.ends_with(t_i) {
                ans += 1;
                break;
            }
        }
    }

    println!("{}", ans);
}
