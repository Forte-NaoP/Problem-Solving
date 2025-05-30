use std::collections::VecDeque;
use std::{i32, usize, vec};
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
        self.g[v].push(Edge { to: u, capacity: 0, flow: 0, rev: v_rev});
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

    let (n, m) = next!(usize, usize);
    let mut flow_graph = FlowGraph::new(n * m * 2);
    let graph: Vec<_> = (0..n).map(|_| next!().as_bytes()).collect();
    let mut src = 0;
    let mut dst = 0;

    for i in 0..n {
        for j in 0..m {
            let cur = i * m + j;
            match graph[i][j] {
                b'K' => src = cur,
                b'H' => dst = cur,
                _ => (),
            }
        }
    }

    for i in 0..n {
        for j in 0..m {
            if graph[i][j] == b'#' {
                continue;
            }

            let cur_in = i * m + j;
            let cur_out = cur_in + n * m;
            flow_graph.connect(cur_in, cur_out, 1);
            
            if j > 0 {
                let nxt_in = cur_in - 1;
                let nxt_out = nxt_in + n * m;
                let cap = if graph[i][j - 1] == b'#' {
                    0
                } else if (cur_in == src && nxt_in == dst) || (cur_in == dst && nxt_in == src) {
                    1_000_000_007
                } else {
                    1
                };
                flow_graph.connect(cur_out, nxt_in, cap);
                flow_graph.connect(nxt_out, cur_in, cap);
            }

            if j < m - 1 {
                let nxt_in = cur_in + 1;
                let nxt_out = nxt_in + n * m;
                let cap = if graph[i][j + 1] == b'#' {
                    0
                } else if (cur_in == src && nxt_in == dst) || (cur_in == dst && nxt_in == src) {
                    1_000_000_007
                } else {
                    1
                };
                flow_graph.connect(cur_out, nxt_in, cap);
                flow_graph.connect(nxt_out, cur_in, cap);
            }

            if i > 0 {
                let nxt_in = cur_in - m;
                let nxt_out = nxt_in + n * m;
                let cap = if graph[i - 1][j] == b'#' {
                    0
                } else if (cur_in == src && nxt_in == dst) || (cur_in == dst && nxt_in == src) {
                    1_000_000_007
                } else {
                    1
                };
                flow_graph.connect(cur_out, nxt_in, cap);
                flow_graph.connect(nxt_out, cur_in, cap);
            }

            if i < n - 1 {
                let nxt_in = cur_in + m;
                let nxt_out = nxt_in + n * m;
                let cap = if graph[i + 1][j] == b'#' {
                    0
                } else if (cur_in == src && nxt_in == dst) || (cur_in == dst && nxt_in == src) {
                    1_000_000_007
                } else {
                    1
                };
                flow_graph.connect(cur_out, nxt_in, cap);
                flow_graph.connect(nxt_out, cur_in, cap);
            }
        }
    }
    let ans = match flow_graph.max_flow(src + n * m, dst) {
        1_000_000_007.. => -1,
        val => val,
    };
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