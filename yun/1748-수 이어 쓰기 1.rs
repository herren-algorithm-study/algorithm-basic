use std::io;

fn simple_log(mut x: u64) -> u32{
    let mut result: u32 = 0;
    while x > 0 {
        x /= 10;
        result += 1
    }
    result
}

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect(" ");
    let input_num: u64 = input.trim().parse().expect(" ");

    let mut i = 1;
    let mut result = 0;

    while i <= input_num {
        result += simple_log(i);
        i += 1;
    }
    println!("{}", result);
}