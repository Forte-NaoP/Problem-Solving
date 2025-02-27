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
    let mut planet: Vec<(i32, i32, i32, usize)> = vec![];
    for i in 0..n {
        let (x, y, z) = next!(i32, i32, i32);
        planet.push((x, y, z, i));
    }

    let mut edges: Vec<(i32, usize, usize)> = vec![];
    planet.sort_by_key(|k| k.0);
    for i in 0..n-1 {
        edges.push(((planet[i].0 - planet[i + 1].0).abs(), planet[i].3, planet[i + 1].3));
    }

    planet.sort_by_key(|k| k.1);
    for i in 0..n-1 {
        edges.push(((planet[i].1 - planet[i + 1].1).abs(), planet[i].3, planet[i + 1].3));
    }

    planet.sort_by_key(|k| k.2);
    for i in 0..n-1 {
        edges.push(((planet[i].2 - planet[i + 1].2).abs(), planet[i].3, planet[i + 1].3));
    }

    edges.sort_by_key(|k| k.0);

    let mut parent: Vec<usize> = (0..n).collect();
    fn find(x: usize, parent: &mut Vec<usize>) -> usize{
        if x == parent[x] {
            return x;
        }
        parent[x] = find(parent[x], parent);
        return parent[x];
    }

    fn union(mut x: usize, mut y: usize, parent: &mut Vec<usize>) -> bool {
        x = find(x, parent);
        y = find(y, parent);

        if x == y {
            return false;
        }

        parent[x] = y;
        return true;
    }

    let mut ans = 0;
    let mut cnt = n;
    for &(d, x, y) in edges.iter() {
        if union(x, y, &mut parent) {
            ans += d;
            cnt -= 1;
        }
        if cnt == 1 {
            break;
        }
    }
    println!("{}", ans);
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