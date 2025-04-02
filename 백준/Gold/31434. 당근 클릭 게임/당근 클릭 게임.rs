use std::iter::Rev;
use std::mem::swap;
use std::cmp::{max, min, Ordering, Reverse};
use std::collections::{BinaryHeap, HashMap, HashSet, VecDeque};
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
    
    let mut a = [0; 100];
    let mut b = [0; 100];
    let (n, k) = next!(usize, usize);
    for i in 0..n {
        a[i] = next!(i32);
        b[i] = next!(i32);
    }
    
    let mut dp = [[-1; 5001]; 101];
    dp[0][1] = 0;
    for i in 0..k {
        for j in 0..5001 {
            if dp[i][j] == -1 {
                continue;
            }
            dp[i + 1][j] = dp[i + 1][j].max(dp[i][j] + j as i32);
            for l in 0..n {
                dp[i + 1][j + b[l] as usize] = dp[i + 1][j + b[l] as usize].max(dp[i][j] - a[l]);
            }
        }
    }

    println!("{}", dp[k].iter().max().unwrap());
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