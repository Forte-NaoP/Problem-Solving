use std::mem::swap;
use std::cmp::{Ordering, max};
use std::collections::HashMap;
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
    let mut fluid: Vec<i32> = vec![];
    for _ in 0..n {
        fluid.push(next!(i32));
    }

    let mut left = 0;
    let mut right = n - 1;
    
    let mut lf = fluid[left];
    let mut rf = fluid[right];
    let mut lr = (lf + rf).abs();

    while left < right {
        let sum = fluid[left] + fluid[right];
        if lr > sum.abs() {
            lf = fluid[left];
            rf = fluid[right];
            lr = sum.abs();

            if lr == 0 {
                break;
            }
        }

        if sum < 0 {
            left += 1;
        } else {
            right -= 1;
        } 
    }

    println!("{} {}", lf, rf);
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