use std::collections::VecDeque;
use std::mem::swap;
use std::rc::Rc;
use std::{i32, usize, vec};
use std::{
    io::{Write, BufWriter, StdoutLock}, cell::RefCell
};

fn neg(x: usize, n: usize) -> usize {
    if x <= n { x + n } else { x - n }
}

struct SCC {
    size: usize,
    graph: Vec<Vec<usize>>,
    next_label: usize,
    label: Vec<usize>,
    finished: Vec<usize>,
    stack: Vec<usize>,
}

impl SCC {
    fn new(size: usize, graph: Vec<Vec<usize>>) -> Self {
        Self { size, graph, next_label: 0, label: vec![0; 2 * size + 1], finished: vec![0; 2 * size + 1], stack: vec![] }
    }

    fn tarzan(&mut self, u: usize) -> usize {
        self.next_label += 1;
        self.label[u] = self.next_label;
        let mut parent = self.next_label;
        self.stack.push(u);

        let len = self.graph[u].len();
        for i in 0..len {
            let v = self.graph[u][i];
            if self.label[v] == 0 {
                parent = parent.min(self.tarzan(v));
            } else if self.finished[v] == 0 {
                parent = parent.min(self.label[v]);
            }
        }

        if parent == self.label[u] {
            while let Some(p) = self.stack.pop() {
                self.finished[p] = u;
                if p == u {
                    break;
                }
            }
        }
        parent
    }

    fn run(&mut self) {
        for i in 1..self.label.len() {
            if self.label[i] == 0 {
                self.tarzan(i);
            }
        }
    }

    fn query(&self) -> i32 {
        for i in 1..(self.size * 2 + 1) {
            if self.finished[i] == self.finished[neg(i, self.size)] {
                return 0;
            }
        }
        1
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

    while let Some(n) = tokens.next() {
        let n = n.parse::<usize>().unwrap();
        let m = tokens.next().unwrap().parse::<usize>().unwrap(); 
        let mut graph = vec![vec![]; n * 2 + 1];
        for _ in 0..m {
            let mut u = tokens.next().unwrap().parse::<i32>().unwrap();
            let mut v = tokens.next().unwrap().parse::<i32>().unwrap();
            u = if u < 0 { n as i32 - u } else { u };
            v = if v < 0 { n as i32 - v } else { v };
            graph[neg(u as usize, n)].push(v as usize);
            graph[neg(v as usize, n)].push(u as usize);
        }

        let mut scc = SCC::new(n, graph);
        scc.run();

        println!("{}", scc.query());
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