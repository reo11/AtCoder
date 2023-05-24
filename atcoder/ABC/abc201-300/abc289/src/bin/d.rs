use proconio::input;
use std::collections::HashSet;

fn main() {
    input! {
        n: i64,
        a: [i64; n],
        m: i64,
        b: [i64; m],
        x: i64
    }

    // xまで上る
    let mut is_possible: [bool; 100001] = [false; 100001];
    is_possible[0] = true;
    let mut b_set = HashSet::new();
    for i in 0..m {
        b_set.insert(b[i as usize]);
    }

    for i in 1..=x {
        // i段目に登れるか確認
        if b_set.contains(&i) {
            continue;
        }
        for j in 0..n {
            if i - a[j as usize] >= 0 {
                is_possible[i as usize] = is_possible[i as usize] || is_possible[(i - a[j as usize]) as usize];
            }
        }
    }

    if is_possible[x as usize] {
        println!("Yes");
    } else {
        println!("No")
    }
}
