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

    let mut max_heap = BinaryHeap::new();
    let mut min_heap = BinaryHeap::new();
    let mut chk = HashMap::new();

    let t = next!(usize);
    for _ in 0..t {
        max_heap.clear();
        min_heap.clear();
        chk.clear();
        let n = next!(usize);
        for _ in 0..n {
            let q = next!(char);
            let x = next!(i32);

            if q == 'I' {
                max_heap.push(x);
                min_heap.push(Reverse(x));
                *chk.entry(x).or_insert(0) += 1;
            } else {
                if x == -1 {
                    while let Some(top) = min_heap.pop() {
                        if *chk.get(&top.0).unwrap() > 0 {
                            chk.entry(top.0).and_modify(|e| { *e -= 1; });
                            break;
                        }
                    }
                } else {
                    while let Some(top) = max_heap.pop() {
                        if *chk.get(&top).unwrap() > 0 {
                            chk.entry(top).and_modify(|e| { *e -= 1; });
                            break;
                        }
                    }
                }
            }
        }

        let mut min_val = None;
        let mut max_val = None;
        while let Some(&top) = min_heap.peek() {
            if *chk.get(&top.0).unwrap() > 0 {
                min_val = Some(top.0);
                break;
            }
            min_heap.pop();
        }

        while let Some(&top) = max_heap.peek() {
            if *chk.get(&top).unwrap() > 0 {
                max_val = Some(top);
                break;
            }
            max_heap.pop();
        }

        if min_val.is_none() || max_val.is_none() {
            println!("EMPTY");
        } else {
            println!("{} {}", max_val.unwrap(), min_val.unwrap());
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