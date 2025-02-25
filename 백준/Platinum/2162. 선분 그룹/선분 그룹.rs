use std::mem::swap;
use std::cmp::{Ordering, max};
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
    let mut lines = vec![];
    let mut group = (0..n).collect::<Vec<usize>>();
    let mut group_num = n;
    let mut size = vec![1; n];
    for _ in 0..n {
        let (x1, y1, x2, y2) = next!(i32, i32, i32, i32);
        let mut p1 = Point{x: x1, y: y1};
        let mut p2 = Point{x: x2, y: y2};
        if p1 > p2 {
            swap(&mut p1, &mut p2);
        }
        lines.push(Line{p1, p2});
    }
    // https://killerwhale0917.tistory.com/6

    for i in 0..n {
        for j in i+1..n {
            if intersect(&lines[i], &lines[j]) {
                union(i, j, &mut group_num, &mut group, &mut size);
            }
        }
    }

    println!("{}\n{}",group_num, size.iter().max().unwrap());
    

}

struct Point {
    x: i32, y: i32
}

impl PartialEq for Point {
    fn eq(&self, other: &Self) -> bool {
        self.x == other.x && self.y == other.y
    }
}

impl Eq for Point {}

impl PartialOrd for Point {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        Some(self.x.cmp(&other.x).then(self.y.cmp(&other.y)))
    }
}

impl Ord for Point {
    fn cmp(&self, other: &Self) -> Ordering {
        self.x.cmp(&other.x).then(self.y.cmp(&other.y))
    }
}

fn ccw(a: &Point, b: &Point, c: &Point) -> i32 {
    match (b.x - a.x) * (c.y - a.y) - (c.x - a.x) * (b.y - a.y) {
        1.. => 1,
        0 => 0,
        ..=-1 => -1
    }
}

struct Line {
    p1: Point, p2: Point
}

fn intersect(l1: &Line, l2: &Line) -> bool {
    let l1_p34 = ccw(&l1.p1, &l1.p2, &l2.p1) * ccw(&l1.p1, &l1.p2, &l2.p2);
    let l2_p12 = ccw(&l2.p1, &l2.p2, &l1.p1) * ccw(&l2.p1, &l2.p2, &l1.p2);

    if l1_p34 == 0 && l2_p12 == 0 {
        return l2.p1 <= l1.p2 && l1.p1 <= l2.p2;
    }
    return l1_p34 <= 0 && l2_p12 <= 0;
}

fn find(x: usize, parent: &mut Vec<usize>) -> usize {
    if x == parent[x] {
        return x;
    }
    parent[x] = find(parent[x], parent);
    return parent[x];
}

fn union(mut x: usize, mut y: usize, group_num: &mut usize, parent: &mut Vec<usize>, size: &mut Vec<usize>) {
    x = find(x, parent);
    y = find(y, parent);

    if x == y {
        return;
    }

    if size[x] > size[y] {
        swap(&mut x, &mut y);
    }

    parent[x] = y;
    size[y] += size[x];
    *group_num -= 1;
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