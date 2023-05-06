use proconio::input;

fn main() {
    input! {
        t: f64,
        l: f64,
        x: f64,
        y: f64,
        q: usize,
        ask: [f64; q],
    }
    let l = l * 0.5;
    for e in ask {
        let rad = e / t * 2.0 * std::f64::consts::PI;
        let p = -l * rad.sin();
        let q = l - l * rad.cos();
        let w = (x.powi(2) + (y - p).powi(2)).sqrt();
        let ans = q.atan2(w) / 2.0 / std::f64::consts::PI * 360.0;
        println!("{:.8}", ans);
    }
}
