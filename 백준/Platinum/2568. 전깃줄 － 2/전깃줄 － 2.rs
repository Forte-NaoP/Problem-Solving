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
    let mut seq: Vec<(usize, usize)> = vec![];
    for _ in 0..n {
        let (x, y) = next!(usize, usize);
        seq.push((x, y));
    }

    seq.sort_by_key(|k| k.1);
    
    let mut lis: Vec<usize> = vec![];
    let mut lis_idx: Vec<usize> = vec![n; n];
    let mut ans: Vec<usize> = vec![];
    for (i, &(num, _)) in seq.iter().enumerate() {
        let idx = lis.partition_point(|&x| x < num);
        if idx == lis.len() {
            lis.push(num);
        } else {
            lis[idx] = num;
        }
        lis_idx[i] = idx;
    }

    let mut lis_end: i32 = lis.len() as i32 - 1;
    
    for i in (0..n).rev() {
        if lis_idx[i] as i32 == lis_end {
            lis_end -= 1;
        } else {
            ans.push(seq[i].0);
        }
    }
    ans.sort();
    println!("{}", ans.len());
    for &val in ans.iter() {
        println!("{}", val);
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