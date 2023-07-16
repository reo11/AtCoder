use proconio::input;
use std::collections::VecDeque;


fn main() {
    input! {
        t: i64
    }

    for _ in 0..t {
        input! {
            n: i64,
            m: i64,
            c: [i64; n],
            uv: [[i64; 2]; m]
        }

        // 幅優先探索
        let mut q: VecDeque<(i64, i64)> = VecDeque::new();
        // [現在地, コスト]
        q.push_back((1, 0));

        while let Some((current_edge, cost)) = q.pop_front() {
            
        }
    }


    println!("{}", ans);
}
