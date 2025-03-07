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

    let n = next!(usize);
    
    let mut graph = vec![vec![0; n]; n];
    let mut dist = vec![vec![i32::MAX; n]; n];

    for i in 0..n {
        for j in 0..n {
            graph[i][j] = next!(i32);
        }
    }

    dist[0][0] = 0;
    let mut pq = BinaryHeap::new();
    pq.push((0, 0, 0));

    while !pq.is_empty() {
        let (cost, cx, cy) = pq.pop().unwrap();

        if dist[cx][cy] < -cost {
            continue;
        }

        if cx == n - 1 && cy == n - 1 {
            println!("{}", -cost);
            break;
        }

        if cx < n - 1 {
            let nxt_cost = -cost + max(graph[cx + 1][cy] - graph[cx][cy] + 1, 0);
            if dist[cx + 1][cy] > nxt_cost {
                dist[cx + 1][cy] = nxt_cost;
                pq.push((-nxt_cost, cx + 1, cy));
            }
        }

        if cy < n - 1 {
            let nxt_cost = -cost + max(graph[cx][cy + 1] - graph[cx][cy] + 1, 0);
            if dist[cx][cy + 1] > nxt_cost {
                dist[cx][cy + 1] = nxt_cost;
                pq.push((-nxt_cost, cx, cy + 1));
            }
        }
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