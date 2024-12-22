use std::{usize, vec};

fn get_pi(s: &[usize]) -> Vec<usize> {
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

fn kmp(s: &[usize], p: &[usize]) -> Vec<usize> {
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

fn input_vec<F>(n: usize, size: usize, mut next: F) -> Vec<usize>
where
    F: FnMut() -> usize
{
    let mut v = vec![];
    v.reserve_exact(size);
    for _ in 0..n {
        v.push(next());
    }
    v
}

fn main() {
    let stdin = std::io::read_to_string(std::io::stdin()).unwrap();
    let mut tokens = stdin.split_whitespace();
    let mut next = || tokens.next().unwrap().parse::<usize>().unwrap();
    let mut output = String::new();
    
    let n = next();
    let mut c1 = input_vec(n, n * 2, &mut next);
    c1.sort();
    let mut c2 = input_vec(n, n, &mut next);
    c2.sort();

    let tmp = c1[0] + 360_000;
    for i in 1..n {
        c1[i - 1] = c1[i] - c1[i - 1];
    }
    c1[n - 1] = tmp - c1[n - 1];
    
    let tmp = c2[0] + 360_000;
    for i in 1..n {
        c2[i - 1] = c2[i] - c2[i - 1];
    }
    c2[n - 1] = tmp - c2[n - 1];
    
    for i in 0..n {
        c1.push(c1[i]);
    }

    let find = kmp(&c1, &c2);
    match find.is_empty() {
        false => println!("possible"),
        true => println!("impossible")
    }
}   
