use std::io::{stdin, stdout, Read, Write, BufReader, BufWriter};
use std::cmp::*;

fn main() {
    let mut reader = BufReader::new(stdin());
    
    let mut input = String::new();
    reader.read_to_string(&mut input).unwrap();
    let mut input = input.split_ascii_whitespace().flat_map(str::parse::<usize>);

    let (n, k) = (input.next().unwrap(), input.next().unwrap());
    let (mut w, mut v) = (vec![0; 101], vec![0; 101]);
    let mut dp = vec![vec![0; 100_001]; 101];

    for i in 1..=n {
        w[i] = input.next().unwrap();
        v[i] = input.next().unwrap();
    }

    for i in 1..=n {
        for j in 1..=k {
            if j < w[i] {
                dp[i][j] = dp[i - 1][j];
            } else {
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w[i]] + v[i]);
            }
        }
    }

    println!("{}", dp[n][k]);
}
