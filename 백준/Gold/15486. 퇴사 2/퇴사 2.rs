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
    let mut t = vec![0; n];
    let mut p = vec![0; n];
    let mut dp = vec![0; n];
    for i in 0..n {
        t[i] = next!(usize);
        p[i] = next!(usize);
    }

    fn recur(day: usize, n: usize, t: &Vec<usize>, p: &Vec<usize>, dp: &mut Vec<usize>) -> usize {
        if day == n {
            return 0;
        }

        if dp[day] != 0 {
            return dp[day];
        }

        if day + t[day] <= n {
            dp[day] = max(dp[day], recur(day + t[day], n, t, p, dp) + p[day]);
        }

        if day + 1 <= n {
            dp[day] = max(dp[day], recur(day + 1, n, t, p, dp));
        }
        dp[day]
    }

    recur(0, n, &t, &p, &mut dp);
    println!("{}", dp.iter().max().unwrap());
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