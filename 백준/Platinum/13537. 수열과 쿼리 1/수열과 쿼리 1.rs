use std::iter::Rev;
use std::mem::swap;
use std::cmp::{max, min, Ordering, Reverse};
use std::collections::{BinaryHeap, HashMap, HashSet, VecDeque};
use std::pin::Pin;
use std::{default, i32, usize, vec};
use std::{
    io::{Write, BufWriter, StdoutLock}, cell::RefCell
};

fn merge(left: &[i32], right: &[i32]) -> Vec<i32> {
    let mut result = Vec::with_capacity(left.len() + right.len());
    let (mut i, mut j) = (0, 0);

    while i < left.len() && j < right.len() {
        if left[i] <= right[j] {
            result.push(left[i]);
            i += 1;
        } else {
            result.push(right[j]);
            j += 1;
        }
    }

    result.extend_from_slice(&left[i..]);
    result.extend_from_slice(&right[j..]);

    result
}

fn upper_bound(arr: &[i32], value: i32) -> usize {
    let mut left = 0;
    let mut right = arr.len();

    while left < right {
        let mid = (left + right) / 2;
        if arr[mid] <= value {
            left = mid + 1;
        } else {
            right = mid;
        }
    }

    left
}

struct MST {
    t: Vec<Vec<i32>>,
    base: usize
}

impl MST {
    fn new(arr: &Vec<i32>) -> Self {
        let mut base = 1;
        let n = arr.len();
        while base < n {
            base <<= 1;
        }
        let mut t = vec![vec![]; base << 1];
        for idx in 0..n {
            t[idx | base].push(arr[idx]); 
        }

        for idx in (1..base).rev() {
            t[idx] = merge(&t[idx << 1], &t[idx << 1 | 1]);
        }

        Self { t, base }
    }

    fn query(&self, mut l: usize, mut r: usize, k: i32) -> usize {
        l |= self.base;
        r |= self.base;
        let mut ret = 0;
        while l <= r {
            if l & 1  == 1 {
                ret += self.t[l].len() - upper_bound(&self.t[l], k);
                l += 1;
            }
            if r & 1 == 0 {
                ret += self.t[r].len() - upper_bound(&self.t[r], k);
                r -= 1;
            }
            l >>= 1;
            r >>= 1;
        }
        ret
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
    let mut arr = vec![];
    arr.reserve(n);
    for _ in 0..n {
        arr.push(next!(i32));
    }

    let tree = MST::new(&arr);
    let m = next!(usize);
    for _ in 0..m {
        let (i, j, k) = next!(usize, usize, i32);
        println!("{}", tree.query(i - 1, j - 1, k));
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
        });
    };
}

#[macro_export]
macro_rules! print {
    ($($t:tt)*) => {
        STDOUT.with(|refcell| {
            use std::io::*;
            write!(refcell.borrow_mut(), $($t)*).unwrap();
        });
    };
}