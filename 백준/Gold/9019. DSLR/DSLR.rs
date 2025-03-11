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

    let op = ['L', 'R', 'D', 'S'];
    let mut graph = [[None, None]; 10000];
    let mut q = VecDeque::new();
    let T = next!(usize);
    for _ in 0..T {
        for i in 0..10000 {
            graph[i][0] = None;
            graph[i][1] = None;
        }
        q.clear();

        let (st, ed) = next!(usize, usize);
        q.push_back(st);
        
        while !q.is_empty() {
            let cur = q.pop_front().unwrap();
            if cur == ed {
                break;
            }

            let d = (cur * 2) % 10000;
            let s = if cur == 0 { 9999 } else { cur - 1 };
            let l = (cur * 10 + cur / 1000) % 10000;
            let r = (cur % 10) * 1000 + cur / 10;

            if graph[d][0].is_none() && d != st {
                graph[d][0] = Some(cur);
                graph[d][1] = Some(2);
                q.push_back(d);
            }

            if graph[s][0].is_none() && s != st {
                graph[s][0] = Some(cur);
                graph[s][1] = Some(3);
                q.push_back(s);
            }

            if graph[l][0].is_none() && l != st {
                graph[l][0] = Some(cur);
                graph[l][1] = Some(0);
                q.push_back(l);
            }

            if graph[r][0].is_none() && r != st {
                graph[r][0] = Some(cur);
                graph[r][1] = Some(1);
                q.push_back(r);
            }
        }

        let mut ans = vec![];
        let mut cur = ed;
        while let Some(now) = graph[cur][0] {
            ans.push(op[graph[cur][1].unwrap()]);
            cur = now;
        }
        println!("{}", String::from_iter(ans.iter().rev()));
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