use proconio::input;

fn main() {
    input! {
        d: usize,
        c: [i64; 26],
        s: [[i64; 26]; d],
        mut t: [i64; d],
        m: usize,
        dq: [(usize, usize); m],
    }
    let mut ans = vec![0; m];
    for ans_i in 0..m {
        let mut last = vec![0; 26];
        let mut cost = 0;
        t[dq[ans_i].0 - 1] = dq[ans_i].1 as i64;
        for i in 0..d {
            cost += s[i][t[i] as usize - 1];
            last[t[i] as usize - 1] = i + 1;

            for j in 0..26 {
                cost -= c[j] * ((i + 1) - last[j]) as i64;
            }
        }
        ans[ans_i] = cost;
    }

    for i in 0..m {
        println!("{}", ans[i]);
    }
}
