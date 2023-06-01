use proconio::input;
use std::cmp;
use rand::Rng;

fn main() {
    let start =  std::time::Instant::now();
    let timeout = std::time::Duration::from_millis(1000);
    input! {
        d: usize,
        c: [i64; 26],
        s: [[i64; 26]; d],
    }

    let mut rng = rand::thread_rng();
    let mut ans = vec![1; d];
    let mut last = vec![0; 26];
    for i in 0..d {
        let mut v = vec![[0, 0]; 26];
        for j in 0..26 {
            v[j][0] = -c[j] * ((i + 1) - last[j]) as i64;
            v[j][1] = j as i64;
        }
        v.sort();
        let index = v[0][1];
        ans[i] = index + 1;
        last[index as usize] = i + 1;
    }

    let timeout = std::time::Duration::from_millis(1000);
    while std::time::Instant::now().duration_since(start) < timeout {
        let query_d = rng.gen_range(0, d);
        let query_q = rng.gen_range(1, 27);
        ans = update(&d, &c, &s, &ans, &query_d, &query_q);
    }

    for i in 0..d {
        println!("{}", ans[i]);
    }
}

fn update(d: &usize, c: &Vec<i64>, s: &Vec<Vec<i64>>, t: &Vec<i64>, query_d: &usize, query_q: &i64) -> Vec<i64> {
    let t_val = t[query_d];
    if calc_score(&d, &c, &s, &t, &query_d, &query_q) > calc_score(&d, &c, &s, &t, &query_d, &t_val) {
        t[query_d] = query_q;
    }
    return t;
}

fn calc_score(d: &usize, c: &Vec<i64>, s: &Vec<Vec<i64>>, t: &Vec<i64>, query_d: &usize, query_q: &i64) -> i64 {
    let mut last = vec![0; 26];
    let mut ans = 0;
    for i in 0..d {
        if i == query_d {
            ans += s[i][query_q as usize - 1];
            last[query_q as usize - 1] = i + 1;
        } else {
            ans += s[i][t[i] as usize - 1];
            last[t[i] as usize - 1] = i + 1;
        }
        for j in 0..26 {
            ans -= c[j] * ((i + 1) - last[j]) as i64;
        }
    }
    return cmp::max(0, 1000000 + ans);
}