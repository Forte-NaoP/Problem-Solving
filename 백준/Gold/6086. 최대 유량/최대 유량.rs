use std::iter::Rev;
use std::mem::swap;
use std::cmp::{max, min, Ordering, Reverse};
use std::collections::{BinaryHeap, HashMap, HashSet, VecDeque};
use std::pin::Pin;
use std::{default, i32, usize, vec};
use std::{
    io::{Write, BufWriter, StdoutLock}, cell::RefCell
};

#[derive(Default, Clone, Copy)]
struct Edge {
    to: usize,
    capacity: i32,
    flow: i32,
    rev: usize,
}

struct FlowGraph {
    g: Vec<Vec<Edge>>,
}

impl FlowGraph {
    fn new(n: usize) -> Self {
        Self {
            g: vec![Vec::new(); n + 1],
        }
    }

    fn connect(&mut self, u: usize, v: usize, capacity: i32) {
        let u_rev = self.g[v].len();
        let v_rev = self.g[u].len();

        self.g[u].push(Edge { to: v, capacity, flow: 0, rev: u_rev});
        self.g[v].push(Edge { to: u, capacity, flow: 0, rev: v_rev});
    }

    fn bfs(&self, src: usize, sink: usize, parent: &mut Vec<Option<(usize, usize)>>) -> i32 {
        parent.fill(None);
        let mut q = VecDeque::new();
        q.push_back(src);
        parent[src] = Some((src, 0));

        while let Some(u) = q.pop_front() {
            for (i, edge) in self.g[u].iter().enumerate() {
                if parent[edge.to].is_none() && edge.capacity > edge.flow {
                    parent[edge.to] = Some((u, i));
                    if edge.to == sink {
                        let mut flow = i32::MAX;
                        let mut cur = sink;
                        while cur != src {
                            let (prev, edge_idx) = parent[cur].unwrap();
                            flow = flow.min(self.g[prev][edge_idx].capacity - self.g[prev][edge_idx].flow);
                            cur = prev;
                        }
                        return flow;
                    }
                    q.push_back(edge.to);
                }
            }
        }
        0
    }

    fn max_flow(&mut self, src: usize, sink: usize) -> i32 {
        let mut flow = 0;
        let n = self.g.len();
        let mut parent = vec![None; n];

        loop {
            let aug_flow = self.bfs(src, sink, &mut parent);
            if aug_flow == 0 {
                break;
            }
            flow += aug_flow;

            let mut cur = sink;
            while cur != src {
                let (prev, edge_idx) = parent[cur].unwrap();
                self.g[prev][edge_idx].flow += aug_flow;
                let rev_idx = self.g[prev][edge_idx].rev;
                self.g[cur][rev_idx].flow -= aug_flow;
                cur = prev;
            }
        }
        flow
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

    let m = next!(usize);
    let mut fg = FlowGraph::new(53);
    for _ in 0..m {
        let (u, v, c) = next!(char, char, i32);
        let u = if u >= 'a' {
            u as usize - 'a' as usize + 26
        } else {
            u as usize - 'A' as usize
        };
        let v = if v >= 'a' {
            v as usize - 'a' as usize + 26
        } else {
            v as usize - 'A' as usize
        };

        fg.connect(u, v, c);
    }

    println!("{}", fg.max_flow(0, 25));

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