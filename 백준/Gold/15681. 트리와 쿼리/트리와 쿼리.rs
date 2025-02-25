use std::cmp::{max, min, Reverse};
use std::collections::{vec_deque, BinaryHeap, HashMap, VecDeque};
use std::mem::swap;
use std::ops::Index;
use std::{default, i32, usize, vec};
use std::{
    io::{Write, BufWriter, StdoutLock}, cell::RefCell
};

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

    let (n, r, q) = next!(usize, usize, usize);
    let mut tree: Vec<Vec<usize>> = vec![vec![]; n + 1];
    let mut sub_size = vec![0; n + 1];
    for _ in 0..n-1 {
        let (u, v) = next!(usize, usize);
        tree[u].push(v);
        tree[v].push(u);
    }

    fn dfs(cur: usize, p: usize, tree: &Vec<Vec<usize>>, sub_size: &mut Vec<i32>) {
        sub_size[cur] = 1;
        for &nxt in tree[cur].iter() {
            if nxt != p {
                dfs(nxt, cur, tree, sub_size);
                sub_size[cur] += sub_size[nxt];
            }
        }
    }

    dfs(r, 0, &tree, &mut sub_size);

    for _ in 0..q {
        let u = next!(usize);
        println!("{}", sub_size[u]);
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