use std::collections::HashMap;
use std::io::{stdin, BufReader, BufRead};
use std::fs::File;
use std::str::FromStr;
use std::vec;

struct SegTree {
    t: Vec<i64>,
}

impl SegTree {
    fn new(mut n: usize) -> Self {
        let mut b = 1;
        while n > 0 {
            b <<= 1;
            n >>= 1;
        }
        SegTree { t: vec![0; b << 1] }
    }

    fn update(&mut self, idx: usize, s: usize, e: usize, node: usize) {
        if (idx < s) || (e < idx) {
            return;
        }
        if s == e {
            self.t[node] = 1;
            return
        }
        let mid = (s + e) / 2;
        self.update(idx, s, mid, node * 2);
        self.update(idx, mid + 1, e, node * 2 + 1);
        self.t[node] = self.t[node * 2] + self.t[node * 2 + 1];
    }

    fn query(&self, l: usize, r: usize, s: usize, e: usize, node: usize) -> i64 {
        if (r < s) || (e < l) {
            return 0;
        }
        if (l <= s) && (e <= r) {
            return self.t[node];
        }
        let mid = (s + e) / 2;
        return self.query(l, r, s, mid, node * 2) + self.query(l, r, mid + 1, e, node * 2 + 1);
    }
}

fn make_tuple<T>(input: String) -> (T, T)
where
    T: FromStr,
    T::Err: std::fmt::Debug, 
{
    let mut parts = input.split_whitespace();
    let a = parts.next().unwrap().parse().unwrap();
    let b = parts.next().unwrap().parse().unwrap();
    (a, b)
}

fn main() {
    let offline = false;
    let mut input = if offline {
        let file = File::open("input.txt").unwrap();
        let istream: Box<dyn BufRead> = Box::new(BufReader::new(file));
        istream
    } else {
        Box::new(BufReader::new(stdin()))
    }.lines();

    let n: usize = input.next().unwrap().unwrap().parse().unwrap();
    let a: Vec<usize> = input.next().unwrap().unwrap()
        .split_whitespace()
        .map(|x| x.parse().unwrap())
        .collect();
    let b: HashMap<usize, usize> = input.next().unwrap().unwrap()
        .split_whitespace()
        .enumerate()
        .map(|(idx, val)| (val.parse::<usize>().unwrap(), idx))
        .collect();
    let mut segtree = SegTree::new(n);
    let mut ans = 0;
    for m in a.iter() {
        ans += segtree.query(b[m], n - 1, 0, n - 1, 1);
        segtree.update(b[m], 0, n - 1, 1);
    }
    println!("{}", ans);
}   

