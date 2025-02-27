use std::mem::swap;
use std::cmp::{max, min, Ordering};
use std::collections::{HashMap, VecDeque};
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

    let (n, m) = next!(usize, usize);
    let mut capacity = [[0; 501]; 501];
    let mut flow = [[0; 501]; 501];
    let mut parent = [0; 501];
    let mut graph = vec![vec![]; 501];

    for _ in 0..m {
        let (u, v, c) = next!(usize, usize, i32);
        graph[u].push(v);
        graph[v].push(u);
        capacity[u][v] = c;
        capacity[v][u] = c;
    }

    let (st, ed) = next!(usize, usize);
    let mut ans = 0;
    
    let mut q = VecDeque::new();
    while true {
        parent.fill(0);
        q.clear();

        q.push_back(st);

        while !q.is_empty() && parent[ed] == 0 {
            let cur = q.pop_front().unwrap();

            for &nxt in graph[cur].iter() {
                if capacity[cur][nxt] > flow[cur][nxt] && parent[nxt] == 0 {
                    q.push_back(nxt);
                    parent[nxt] = cur;
                }
            }
        }

        if parent[ed] == 0 {
            break;
        }

        let mut amount = i32::MAX;
        let mut cur = ed;
        while cur != st {
            amount = min(amount, capacity[parent[cur]][cur] - flow[parent[cur]][cur]);
            cur = parent[cur];
        }

        cur = ed;
        while cur != st {
            flow[parent[cur]][cur] += amount;
            flow[cur][parent[cur]] -= amount;
            cur = parent[cur];
        }
        ans += amount;
    }

    println!("{}", ans);
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