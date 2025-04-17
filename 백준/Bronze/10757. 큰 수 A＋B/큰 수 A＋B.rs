use std::cell::Ref;
use std::iter::Rev;
use std::mem::swap;
use std::cmp::{max, min, Ordering, Reverse};
use std::collections::{BinaryHeap, HashMap, HashSet, VecDeque, BTreeSet};
use std::pin::Pin;
use std::{default, i32, usize, vec};
use std::{
    io::{Write, BufWriter, StdoutLock}, cell::RefCell
};
use std::rc::{Rc, Weak};
use std::ops::Bound::{Included, Excluded, Unbounded};

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

    let mut _a = next!().as_bytes().into_iter().rev();
    let mut _b = next!().as_bytes().into_iter().rev();
    let z = '0' as u8;
    let mut ret = vec![];

    let mut c = 0;
    loop {
        let a = _a.next();
        let b = _b.next();

        if a.is_none() && b.is_none() {
            break;
        }

        let mut d = 0;
        d += match a {
            Some(&v) => v - z,
            None => 0,
        };

        d += match b {
            Some(&v) => v - z,
            None => 0,
        };

        d += c;

        ret.push((d % 10 + z) as char);
        c = d / 10;
    }

    if c != 0 {
        ret.push((c + z) as char);
    }

    println!("{}", ret.iter().rev().collect::<String>());
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