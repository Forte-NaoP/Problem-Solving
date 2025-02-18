use std::cmp::{max, min, Reverse};
use std::collections::{vec_deque, BinaryHeap, HashMap, VecDeque};
use std::mem::swap;
use std::ops::Index;
use std::{default, i32, usize, vec};
use std::{
    io::{Write, BufWriter, StdoutLock}, cell::RefCell
};

const MAX_DEPTH: usize = 17;

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
    let mut tree = vec![vec![]; n + 1];
    
    for _ in 0..n-1 {
        let (a, b) = next!(usize, usize);
        tree[a].push(b);
        tree[b].push(a);
    }

    let mut depth = vec![0; n + 1];
    let mut parent = vec![vec![0; MAX_DEPTH]; n + 1];

    let mut q: VecDeque<usize> = VecDeque::new();
    q.push_back(1);
    depth[1] = 1;
    parent[1][0] = 0;

    while !q.is_empty() {
        let cur = q.pop_front().unwrap();

        for &nxt in tree[cur].iter() {
            if nxt == parent[cur][0] {
                continue;
            }
            depth[nxt] = depth[cur] + 1;
            parent[nxt][0] = cur;
            q.push_back(nxt);
        }
    }

    for d in 1..MAX_DEPTH {
        for node in 1..=n {
            parent[node][d] = parent[parent[node][d - 1]][d - 1];
        }
    }

    fn query(mut a: usize, mut b: usize, depth: &Vec<i32>, parent: &Vec<Vec<usize>>) -> usize {
        if depth[a] < depth[b] {
            swap(&mut a, &mut b);
        }

        let diff = depth[a] - depth[b];

        for i in 0..MAX_DEPTH {
            if (diff & (1 << i)) != 0 {
                a = parent[a][i];
            }
        }

        if a != b {
            for i in (0..MAX_DEPTH).rev() {
                if parent[a][i] != parent[b][i] {
                    a = parent[a][i];
                    b = parent[b][i];
                }
            }
            a = parent[a][0];
        }
        a
    }

    let m = next!(usize);
    for _ in 0..m {
        let (a, b) = next!(usize, usize);
        println!("{}", query(a, b, &depth, &parent));
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