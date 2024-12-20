use std::cmp::{max, min, Reverse};
use std::collections::{BinaryHeap, HashMap};
use std::mem::swap;
use std::{default, i32, usize, vec};
use std::ops::{BitOr, BitXor, Deref, DerefMut};
use std::fmt::Write;


struct SegTree<T>
where T: std::cmp::Ord + Copy {
    t: Vec<T>,
    base: usize,
    default: T,
    cmp: fn(T, T) -> T
}

impl<T> SegTree<T>
where T: std::cmp::Ord + Copy {
    fn new(mut n: usize, default: T, cmp: fn(T, T) -> T) -> Self {
        let mut b = 1;
        while n > 0 {
            b <<= 1;
            n >>= 1;
        }
        SegTree { t: vec![default; b << 1], base: b, default, cmp }
    }

    fn update_bu(&mut self, mut idx: usize, val: T) {
        idx += self.base;
        self.t[idx] = val;
        idx >>= 1;
        while idx > 0 {
            self.t[idx] = (self.cmp)(self.t[idx << 1], self.t[idx << 1 | 1]);
            idx >>= 1;
        }
    }

    fn query_td(&self, l: usize, r: usize) -> T {
        self._query_td(l, r, 0, self.base - 1, 1)
    }

    fn _query_td(&self, l: usize, r: usize, s: usize, e: usize, idx: usize) -> T {
        if r < s || e < l {
            return self.default;
        }
        if l <= s && e <= r {
            return self.t[idx];
        }
        let mid = (s + e) / 2;
        (self.cmp)(
            self._query_td(l, r, s, mid, idx << 1), 
            self._query_td(l, r, mid + 1, e, idx << 1 | 1)
        )
    }
}

fn main() {
    let stdin = std::io::read_to_string(std::io::stdin()).unwrap();
    let mut tokens = stdin.split_whitespace();
    let mut next = || tokens.next().unwrap().parse::<usize>().unwrap();
    let mut output = String::new();

    let (n, m) = (next(), next());
    let mut mintree = SegTree::new(n, usize::MAX, min);
    let mut maxtree = SegTree::new(n, 0, max);
    for i in 0..n {
        let val = next();
        mintree.update_bu(i, val);
        maxtree.update_bu(i, val);
    }

    for _ in 0..m {
        let (a, b) = (next() - 1, next() - 1); 
        writeln!(output, "{} {}", mintree.query_td(a, b), maxtree.query_td(a, b)).unwrap();
    }
    print!("{}", output);
}   
