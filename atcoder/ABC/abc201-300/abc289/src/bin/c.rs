use proconio::input;

fn main() {
    input! {
        n: i64,
        m: i64
    }
    let mut set_vec = Vec::new();

    for i in 0..m {
        input! {
            c: i64,
            a: [i64; c]
        }

        set_vec.push(a);
    }

    let mut ans: i64 = 0;
    // bit全探索
    for num in 1..(2 << (m - 1)) {
        let mut flag = true;
        for target_num in 1..=n {
            // target_numがいずれかの集合に存在するか
            let mut exist_flag = false;
            for i in 0..m {
                if (num >> i) & 1 == 1 {
                    exist_flag = exist_flag || set_vec[i as usize].contains(&target_num);
                }
            }
            if !exist_flag {
                // 存在しない場合、フラグを折る
                flag = false;
            }
        }
        if flag {
            ans += 1;
        }
    }

    println!("{}", ans);
}
