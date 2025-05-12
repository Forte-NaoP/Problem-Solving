use std::collections::VecDeque;
use std::{i32, usize, vec};
use std::{
    io::{Write, BufWriter, StdoutLock}, cell::RefCell
};

struct MergeSortTree {
    tree: Vec<Vec<usize>>,
    size: usize,
}

impl MergeSortTree {
    fn new(arr: &Vec<usize>) -> Self {
        let size = arr.len().next_power_of_two();
        let mut tree = vec![vec![]; size << 1];
        
        for i in 1..=arr.len() {
            tree[size + i] = vec![arr[i - 1]];
        }

        for i in (1..size).rev() {
            tree[i] = merge(&tree[i << 1], &tree[i << 1 | 1]);
        }

        Self { tree, size }
    }

    fn query(&self, mut l: usize, mut r: usize, k: usize) -> usize {
        l += self.size;
        r += self.size + 1;

        let mut res = 0;

        while l < r {
            if l % 2 == 1 {
                res += upper_bound(&self.tree[l], k);
                l += 1;
            }
            if r % 2 == 1 {
                r -= 1;
                res += upper_bound(&self.tree[r], k);
            }
            l >>= 1;
            r >>= 1;
        }

        res
    }
}

fn merge(a: &[usize], b: &[usize]) -> Vec<usize> {
    let mut merged = Vec::with_capacity(a.len() + b.len());
    let (mut i, mut j) = (0, 0);
    while i < a.len() && j < b.len() {
        if a[i] <= b[j] {
            merged.push(a[i]);
            i += 1;
        } else {
            merged.push(b[j]);
            j += 1;
        }
    }
    merged.extend_from_slice(&a[i..]);
    merged.extend_from_slice(&b[j..]);
    merged
}

fn upper_bound(sorted: &[usize], k: usize) -> usize {
    match sorted.binary_search(&(k + 1)) {
        Ok(i) | Err(i) => sorted.len() - i,
    }
}

fn solve(stdin: &str) {
    let mut tokens = stdin.split_ascii_whitespace();
    
    macro_rules! next {
        () => {
            tokens.next().unwrap()
        };

        ($t:ty) => {
            tokens.next().unwrap().parse::<$t>().unwrap()
        };

        ($t:ty, $($ts:ty),+) => {
            (
                tokens.next().unwrap().parse::<$t>().unwrap(),
                $(tokens.next().unwrap().parse::<$ts>().unwrap()),+
            )
        };
    }

    let n = next!(usize);
    let arr: Vec<usize> = (0..n).map(|_| next!(usize)).collect();
    let mut mst = MergeSortTree::new(&arr);
    let m = next!(usize);
    let mut last = 0;
    for _ in 0..m {
        let (mut a, mut b, mut c) = next!(usize, usize, usize);
        a ^= last;
        b ^= last;
        c ^= last;
        last = mst.query(a, b, c);
        println!("{}", last);
    }


}

fn main() {
    let stdin = std::io::read_to_string(std::io::stdin()).unwrap();
    solve(&stdin);
    STDOUT.with(|refcell| {
        Write::flush(&mut *refcell.borrow_mut()).unwrap();
    });
}   


/* https://blog.kiwiyou.dev/posts/rust-fastio/ */
thread_local! {
    static STDOUT: RefCell<BufWriter<StdoutLock<'static>>> 
        = RefCell::new(
            BufWriter::with_capacity(
                1 << 17, 
                std::io::stdout().lock()
            )
        );
}

#[macro_export]
macro_rules! println {
    ($($t:tt)*) => {
        STDOUT.with(|refcell| {
            use std::io::*;
            writeln!(refcell.borrow_mut(), $($t)*).unwrap();
        })
    };
}

#[macro_export]
macro_rules! print {
    ($($t:tt)*) => {
        STDOUT.with(|refcell| {
            use std::io::*;
            write!(refcell.borrow_mut(), $($t)*).unwrap();
        })
    };
}