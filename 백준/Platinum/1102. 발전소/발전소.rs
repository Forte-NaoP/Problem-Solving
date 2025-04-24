use std::collections::VecDeque;
use std::mem::swap;
use std::rc::Rc;
use std::{i32, usize, vec};
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
    let mut dp = vec![i32::MAX; 1 << n];
    let mut cost = vec![vec![0; n]; n];
    for i in 0..n {
        for j in 0..n {
            cost[i][j] = next!(i32);
        }
    }

    let mut state: usize = 0;
    let state_str = next!();
    let p = next!(u32);

    for (i, &c) in state_str.as_bytes().iter().enumerate() {
        if c == b'Y' {
            state |= 1 << i;
        }
    }

    if state.count_ones() >= p {
        println!("0");
        return;
    }

    let mut ans = i32::MAX;
    let mut q = VecDeque::new();
    
    q.push_back(state);
    dp[state] = 0;

    while let Some(cur) = q.pop_front() {
        if cur.count_ones() >= p {
            ans = ans.min(dp[cur]);
        } else {
            for i in 0..n {
                if cur & (1 << i) == 0 {
                    let nxt = cur | (1 << i);
                    for j in 0..n {
                        if cur & (1 << j) != 0 {
                            if dp[nxt] > dp[cur] + cost[j][i] {
                                dp[nxt] = dp[cur] + cost[j][i];
                                q.push_back(nxt);
                            }
                        }
                    }
                }
            }
        }
    }

    if ans == i32::MAX {
        println!("-1");
    } else {
        println!("{}", ans);
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