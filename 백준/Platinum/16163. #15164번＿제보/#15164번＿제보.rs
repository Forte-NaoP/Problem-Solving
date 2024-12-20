use std::cmp::min;
use std::{usize, vec};
use std::fmt::Write;

fn manacher(s: Vec<u8>) -> u64 {
    let e = s.len() * 2 + 1;
    let mut extended = vec![0; e];
    for i in 0..s.len() {
        extended[i * 2 + 1] = s[i];
    }
    let mut r = 0;
    let mut p = 0;
    let mut dp = vec![0; e];
    let mut ans = 0;
    for i in 0..e {
        if i <= r {
            dp[i] = min(dp[p * 2 - i], r - i);
        }
        while i >= dp[i] + 1 && i + dp[i] + 1 < e && extended[i - dp[i] - 1] == extended[i + dp[i] + 1] {
            dp[i] += 1;
        }
        if r < i + dp[i] {
            r = i + dp[i];
            p = i;
        }
        ans += (dp[i] + 1) as u64 / 2;
    }
    ans
}

fn main() {
    let stdin = std::io::read_to_string(std::io::stdin()).unwrap();
    let mut tokens = stdin.split_whitespace();
    // let mut next = || tokens.next().unwrap().parse::<usize>().unwrap();
    let mut output = String::new();
    println!("{}", manacher(tokens.next().unwrap().bytes().collect()));
}   
