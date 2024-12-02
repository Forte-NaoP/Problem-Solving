use std::cmp::Reverse;
use std::collections::{BinaryHeap, HashMap};
use std::vec;

fn get_pi(s: &[u8]) -> Vec<usize> {
    let s_len = s.len();
    let mut pi = vec![0; s_len];
    let mut matched = 0;

    for begin in 1..s_len {
        while matched > 0 && s[begin] != s[matched] {
            matched = pi[matched - 1];
        }
        if s[begin] == s[matched] {
            matched += 1;
            pi[begin] = matched;
        }
    }
    pi
}

fn kmp(s: &[u8], p: &[u8]) -> Vec<usize> {
    let pi = get_pi(p);
    let p_len = p.len();
    let s_len = s.len();
    let mut matched = 0;
    let mut find = vec![];

    for begin in 0..s_len {
        while matched > 0 && (matched < p_len && s[begin] != p[matched]) {
            matched = pi[matched - 1];
        }
        if matched < p_len && s[begin] == p[matched] {
            matched += 1;
            if matched == p_len {
                find.push(begin - p_len + 1);
                matched = pi[matched - 1];
            } 
        }
    }
    find
}

fn main() {
    let stdin = std::io::read_to_string(std::io::stdin()).unwrap();
    let mut tokens = stdin.lines();
    let mut next = || tokens.next().unwrap();
    let s = next();
    let p = next();

    let find = kmp(s.as_bytes(), p.as_bytes());

    println!("{}\n{}", find.len(), find.iter().map(|x| (x + 1).to_string()).collect::<Vec<_>>().join(" "));
}   
