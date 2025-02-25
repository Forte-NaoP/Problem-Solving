use std::cmp::{max, min, Reverse};
use std::collections::{vec_deque, BinaryHeap, HashMap, VecDeque};
use std::mem::swap;
use std::ops::Index;
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
    let mut points = vec![];
    for _ in 0..n {
        let (x, y) = next!(i64, i64);
        points.push(Point{x, y});
    }
    points.push(points[0]);

    let mut ccw_sum: f64 = 0.0;
    for i in 1..n {
        ccw_sum += ccw(&points[0], &points[i - 1], &points[i]);
    }

    println!("{:.1}", ccw_sum.abs());
}

#[derive(Clone, Copy)]
struct Point {
    x: i64, y: i64
}

fn ccw(a: &Point, b: &Point, c: &Point) -> f64 {
    ((b.x - a.x) * (c.y - a.y) - (c.x - a.x) * (b.y - a.y)) as f64 / 2.0
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