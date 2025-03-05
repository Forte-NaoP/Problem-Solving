use std::mem::swap;
use std::cmp::{max, min, Ordering};
use std::collections::{HashMap, VecDeque, BinaryHeap};
use std::pin::Pin;
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

    let (n, m, k) = next!(usize, usize, usize);
    let mut graph = vec![vec![]; n + 1];
    for _ in 0..m {
        let (u, v, c) = next!(usize, usize, i64);
        graph[u].push((v, c));
        graph[v].push((u, c));
    }

    let mut dist = vec![vec![i64::MAX; k + 1]; n + 1];
    let mut pq: BinaryHeap<(i64, usize, usize)> = BinaryHeap::new();
    
    dist[1][0] = 0;
    pq.push((0, 1, 0));

    while !pq.is_empty() {
        let cur = pq.pop().unwrap();

        if dist[cur.1][cur.2] < -cur.0 {
            continue;
        }

        for &nxt in graph[cur.1].iter() {
            let nxt_cost = nxt.1 - cur.0;
            if nxt_cost < dist[nxt.0][cur.2] {
                dist[nxt.0][cur.2] = nxt_cost;
                pq.push((-nxt_cost, nxt.0, cur.2));
            }

            if cur.2 + 1 <= k && -cur.0 < dist[nxt.0][cur.2 + 1] {
                dist[nxt.0][cur.2 + 1] = -cur.0;
                pq.push((cur.0, nxt.0, cur.2 + 1));
            }
        }
    }

    println!("{}", dist[n].iter().min().unwrap());
    
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