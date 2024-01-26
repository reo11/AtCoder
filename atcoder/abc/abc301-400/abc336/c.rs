use proconio::input;

fn decimal_to_quinary(mut decimal: u64) -> String {
    if decimal == 0 {
        return String::from("0");
    }

    let mut result = String::new();

    while decimal > 0 {
        let remainder = decimal % 5;
        result = remainder.to_string() + &result; // 数字を文字列に変換して前に追加
        decimal /= 5;
    }

    result
}

fn main() {
    input! {
        n: u64,
    }
    let mut x = decimal_to_quinary(n - 1);

    x = x.replace("4", "8");
    x = x.replace("3", "6");
    x = x.replace("2", "4");
    x = x.replace("1", "2");

    println!("{}", x);
}
