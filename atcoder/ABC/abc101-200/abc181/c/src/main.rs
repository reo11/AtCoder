use proconio::input;

fn main() {
    input! {
        n: usize
    }
    let mut x = vec![0; n];
    let mut y = vec![0; n];
    for i in 0..n {
        input! {
            x_i: i64,
            y_i: i64
        }
        x[i] = x_i;
        y[i] = y_i;
    }

    let mut ans = false;

    for i in 0..n {
        let xy1 = (x[i], y[i]);
        for j in 0..n {
            if i == j { continue; }
            let xy2 = ((x[j] - x[i]), (y[j] - y[i]));
            for k in 0..n {
                if i == k || j == k { continue; }
                let xy3 = ((x[k] - x[i]), (y[k] - y[i]));
                if xy2.0 * xy3.1 == xy2.1 * xy3.0 {
                    ans = true;
                }
            }
        }
    }

    if ans {
        println!("Yes");
    } else {
        println!("No");
    }
}
