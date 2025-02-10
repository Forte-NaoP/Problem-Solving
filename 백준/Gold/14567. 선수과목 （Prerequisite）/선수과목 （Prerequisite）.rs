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

    let (n, m) = next!(usize, usize);
    let mut indegree = [0; 1001];
    let mut available = [0; 1001];
    let mut sem = 1;
    let mut graph = vec![vec![]; n + 1];
    for i in 0..m {
        let (u, v) = next!(usize, usize);
        graph[u].push(v);
        indegree[v] += 1;
    }
    
    let mut q = VecDeque::new();
    for i in 1..=n {
        if indegree[i] == 0 {
            q.push_back(i);
            available[i] = 1;
        }
    }

    while !q.is_empty() {
        let cur = q.pop_front().unwrap();

        for &nxt in graph[cur].iter() {
            indegree[nxt] -= 1;
            if indegree[nxt] == 0 {
                q.push_back(nxt);
                available[nxt] = available[cur] + 1;
            }
        }
    }

    for i in 1..=n {
        print!("{} ", available[i]);
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