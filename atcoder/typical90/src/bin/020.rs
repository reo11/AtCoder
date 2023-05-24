use proconio::input;
use std::collections::HashMap;

pub mod strongly_connected_components {
    use std::collections::VecDeque;

    pub fn decompose(graph: &[Vec<usize>]) -> Vec<usize> {
        let mut vs = Vec::new();
        let num_v = graph.len();
        let mut cmp = vec![0; num_v];

        let mut reverse_graph = vec![vec![]; num_v];

        for (i, edges) in graph.iter().enumerate() {
            for &v in edges.iter() {
                reverse_graph[v].push(i);
            }
        }
        let mut used = vec![false; num_v];

        let mut stack = VecDeque::new();
        let mut added = vec![false; num_v];
        for i in 0..num_v {
            if used[i] {
                continue;
            }
            stack.push_front(i);
            while let Some(v) = stack.pop_front() {
                stack.push_front(v);
                used[v] = true;
                let mut pushed = false;
                for &u in graph[v].iter().rev() {
                    if !used[u] {
                        stack.push_front(u);
                        pushed = true;
                    }
                }
                if !pushed {
                    stack.pop_front();
                    if !added[v] {
                        vs.push(v);
                        added[v] = true;
                    }
                }
            }
        }

        used = vec![false; num_v];
        let mut k = 0;
        vs.reverse();
        for &i in vs.iter() {
            if used[i] {
                continue;
            }
            stack.push_front(i);
            used[i] = true;
            cmp[i] = k;
            while let Some(v) = stack.pop_front() {
                stack.push_front(v);
                let mut pushed = false;
                for &u in reverse_graph[v].iter() {
                    if used[u] {
                        continue;
                    }
                    used[u] = true;
                    cmp[u] = k;
                    stack.push_front(u);
                    pushed = true;
                }
                if !pushed {
                    stack.pop_front();
                }
            }
            k += 1;
        }

        cmp
    }
}

fn main() {
    input! {
        n: usize,
        m: usize,
        ab: [(usize, usize); m],
    }
    let mut graph = vec![vec![]; n];

    for (a, b) in ab {
        graph[a - 1].push(b - 1);
    }

    let cmp = strongly_connected_components::decompose(&graph);
    let mut counter = HashMap::new();
    cmp.iter().for_each(|x| {
        let count = counter.entry(x).or_insert(0);
        *count += 1;
    });

    let mut ans = 0;
    for (_k, v) in counter.iter() {
        ans += v * (v - 1) / 2;
    }

    println!("{}", ans);
}
