use proconio::input;

pub struct UnionFind {
    parent: Vec<usize>,
    sizes: Vec<usize>,
    size: usize,
}

impl UnionFind {
    pub fn new(n: usize) -> UnionFind {
        UnionFind {
            parent: (0..n).map(|i| i).collect::<Vec<usize>>(),
            sizes: vec![1; n],
            size: n,
        }
    }

    pub fn find(&mut self, x: usize) -> usize {
        if x == self.parent[x] {
            x
        } else {
            let px = self.parent[x];
            self.parent[x] = self.find(px);
            self.parent[x]
        }
    }

    pub fn unite(&mut self, x: usize, y: usize) -> bool {
        let parent_x = self.find(x);
        let parent_y = self.find(y);
        if parent_x == parent_y {
            return false;
        }

        let (large, small) = if self.sizes[parent_x] < self.sizes[parent_y] {
            (parent_y, parent_x)
        } else {
            (parent_x, parent_y)
        };

        self.parent[small] = large;
        self.sizes[large] += self.sizes[small];
        self.sizes[small] = 0;
        self.size -= 1;
        true
    }
}

fn main() {
    input! {
        n: usize,
        m: usize
    }
    let mut uf = UnionFind::new(n + 1);
    let mut ans = 0;
    for _ in 0..m {
        input! {
            a: usize,
            b: usize
        }
        if uf.find(a) != uf.find(b) {
            uf.unite(a, b);
        } else {
            ans += 1;
        }
    }


    println!("{}", ans);
}
