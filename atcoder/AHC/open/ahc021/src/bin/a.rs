use proconio::input;

const N: usize = 30;
const M: usize = 465;
const T: [usize; N] = [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210, 231, 253, 276, 300, 325, 351, 378, 406, 435];

fn up(x: i64, y: i64) -> Vec<(i64, i64)> {
    if x == 0 {
        return [].to_vec();
    } else if y == 0 {
        return [(x - 1, y)].to_vec();
    } else if x == y {
        return [(x - 1, y - 1)].to_vec();
    } else {
        return [(x - 1, y - 1), (x - 1, y)].to_vec();
    }
}

fn main() {
    input!(mut b: [usize; M]);
    let id = |i: usize, j: usize| T[i] + j;
    let mut places = vec![(-1, -1); M];
    let mut process = vec![];
    for i in 0..N {
        for j in 0..=i {
            places[b[id(i, j)]] = (i as i64, j as i64);
        }
    }

    for target_num in 0..M {
        let (i, j) = places[target_num];
        let mut x = i as i64;
        let mut y = j as i64;
        while x > 0 {
            let mut best = (M, 0, 0);
            for &(dx, dy) in &up(x as i64, y as i64) {
                if b[id(dx as usize, dy as usize)] > b[id(x as usize, y as usize)] {
                    if best.0 == M || b[id(dx as usize, dy as usize)] > best.0 {
                        best = (b[id(dx as usize, dy as usize)], dx as usize, dy as usize);
                    }
                }
            }
            if best == (M, 0, 0) {
                break;
            }
            let (_num, dx, dy) = best;
            let swap_num = b[id(dx as usize, dy as usize)];
            places[target_num as usize] = (dx as i64, dy as i64);
            places[swap_num as usize] = (x as i64, y as i64);
            b.swap(id(x as usize, y as usize), id(dx as usize, dy as usize));
            process.push((x as usize, y as usize, dx as usize, dy as usize));
            x = dx as i64;
            y = dy as i64;
        }
    }

    process.truncate(10000);
    println!("{}", process.len());
    for &(i0, j0, i1, j1) in &process {
        println!("{} {} {} {}", i0, j0, i1, j1);
    }
}
