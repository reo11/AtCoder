use proconio::input;
use std::collections::HashSet;

fn main() {
    input! {
        n: i64,
        m: i64,
        a: [i64; m],
    }

    let mut ans = Vec::new();
    let mut v = Vec::new();
    let mut set = HashSet::new();

    for i in 0..m {
        set.insert(a[i as usize]);
    }

    let mut j = Some(0);
    for i in 1..=n {
        if set.contains(&i) {
            v.push(i);
        } else {
            ans.push(i);
            while let Some(value) = v.pop() {
                ans.push(value);
            }
        }
    }

    let output = ans
        .iter()
        .map(|number| number.to_string())
        .collect::<Vec<String>>()
        .join(" ");
    println!("{}", output);
}
