use std::collections::VecDeque;
use std::mem::swap;
use std::rc::Rc;
use std::{i32, usize, vec};
use std::{
    io::{Write, BufWriter, StdoutLock}, cell::RefCell
};

struct Articulation {
    num: Vec<usize>,
    low: Vec<usize>,
    point: Vec<bool>,
    cnt: usize,
}

impl Articulation {
    fn new(n: usize) -> Self {
        Self { num: vec![0; n + 1], low: vec![0; n + 1], point: vec![false; n + 1], cnt: 0 }
    }

    fn get_points(&mut self, graph: &Vec<Vec<usize>>) -> Vec<usize> {
        for u in 1..self.num.len() {
            if self.num[u] == 0 {
                self.cnt = 0;
                self.dfs(u, 0, graph);
            }
        }
        self.point
            .iter()
            .enumerate()
            .filter(|&(_, &is_point)| is_point)
            .map(|(idx, _)| idx)
            .collect::<Vec<_>>()
    }

    fn dfs(&mut self, u: usize, p: usize, graph: &Vec<Vec<usize>>) {
        self.cnt += 1;
        self.num[u] = self.cnt;
        self.low[u] = self.cnt;
        let mut child_cnt = 0;

        for &v in &graph[u] {
            if self.num[v] == 0 {
                child_cnt += 1;
                self.dfs(v, u, graph);
                self.low[u] = self.low[u].min(self.low[v]);

                if p != 0 && self.low[v] >= self.num[u] {
                    self.point[u] = true;
                }
            } else if v != p {
                self.low[u] = self.low[u].min(self.num[v]);
            }
        }

        if p == 0 && child_cnt > 1 {
            self.point[u] = true;
        }
    }
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

    let (n, m) = next!(usize, usize);
    let mut graph = vec![vec![]; n + 1];

    for _ in 0..m {
        let (u, v) = next!(usize, usize);
        graph[u].push(v);
        graph[v].push(u);
    }

    let mut ap = Articulation::new(n);
    let points = ap.get_points(&graph);
    println!("{}", points.len());
    for &u in &points {
        print!("{} ", u);
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