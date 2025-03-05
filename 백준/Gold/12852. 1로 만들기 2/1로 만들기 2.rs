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
    let mut visit = vec![0; 1_000_001];
    
    let mut q = VecDeque::new();
    q.push_back(1);

    while !q.is_empty() {
        let cur = q.pop_front().unwrap();

        if cur == n {
            break;
        }

        if cur + 1 <= n && visit[cur + 1] == 0 {
            visit[cur + 1] = cur;
            q.push_back(cur + 1);
        }
        if cur * 2 <= n && visit[cur * 2] == 0 {
            visit[cur * 2] = cur;
            q.push_back(cur * 2);
        }
        if cur * 3 <= n && visit[cur * 3] == 0 {
            visit[cur * 3] = cur;
            q.push_back(cur * 3);
        }
    }

    let mut cur = n;
    let mut ans = vec![];
    while cur != 0 {
        ans.push(cur);
        cur = visit[cur];
    }
    println!("{}", ans.len() - 1);
    for i in ans.iter() {
        print!("{} ", i);
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