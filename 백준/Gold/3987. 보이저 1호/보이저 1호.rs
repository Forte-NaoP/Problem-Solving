use std::cmp::{max, min, Reverse};
use std::collections::{vec_deque, BinaryHeap, HashMap, VecDeque};
use std::mem::swap;
use std::ops::Index;
use std::{default, i32, usize, vec};
use std::{
    io::{Write, BufWriter, StdoutLock}, cell::RefCell
};

struct Signal {
    x: i32, y: i32, d: usize, v: i32
}

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

    let mut space = vec![vec![' '; 500]; 500];
    let (n, m) = next!(i32, i32);

    for i in 0..n as usize {
        let row = next!();
        for (j, c) in row.chars().enumerate() {
            space[i][j] = c;
        }
    }

    let dir = ['U', 'R', 'D', 'L'];
    let (x, y) = next!(i32, i32);
    let dx = [-1, 0, 1, 0];
    let dy = [0, 1, 0, -1];

    let mut q: VecDeque<Signal> = VecDeque::new();

    let mut how_far = 0;
    let mut far_dir = 0;

    for i in 1..5 {
        q.clear();
        q.push_back(Signal{x: x - 1, y: y - 1, d: i - 1, v: 1});
        
        while !q.is_empty() {
            let cur = q.pop_front().unwrap();
            let (nx, ny) = (cur.x + dx[cur.d], cur.y + dy[cur.d]);
            let mut nxt_d = cur.d;

            if nx < 0 || nx >= n || ny < 0 || ny >= m {
                if cur.v > how_far {
                    how_far = cur.v;
                    far_dir = i - 1;
                }
                break;
            }

            if space[nx as usize][ny as usize] == 'C' {
                if cur.v > how_far {
                    how_far = cur.v;
                    far_dir = i - 1;
                }
                break;
            }

            if space[nx as usize][ny as usize] == '\\' {
                nxt_d = match cur.d {
                    0 => 3,
                    1 => 2,
                    2 => 1,
                    3 => 0,
                    _ => unreachable!(),
                };
            } else if space[nx as usize][ny as usize] == '/' {
                nxt_d = match cur.d {
                    0 => 1,
                    1 => 0,
                    2 => 3,
                    3 => 2,
                    _ => unreachable!(),
                };
            }

            if cur.v >= 1_000_000 {
                println!("{}\nVoyager", dir[i - 1]);
                return;
            }

            q.push_back(Signal{x: nx, y: ny, d: nxt_d, v: cur.v + 1});
        }
    }
    
    println!("{}\n{}", dir[far_dir], how_far);
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