use std::collections::VecDeque;
use std::mem::swap;
use std::rc::Rc;
use std::{i32, usize, vec};
use std::{
    io::{Write, BufWriter, StdoutLock}, cell::RefCell
};

struct Tree {
    tree: Vec<Vec<usize>>,
    parent: Vec<Vec<usize>>,
    depth: Vec<usize>,
}

impl Tree {
    fn new(size: usize, tree: Vec<Vec<usize>>) -> Self {
        Self { 
            tree, 
            parent: vec![vec![0; 17]; size + 1], 
            depth: vec![0; size + 1],
        }
    }

    fn init_parent(&mut self, root: usize) {
        let mut q = VecDeque::new();
        self.depth[root] = 1;
        self.parent[root][0] = 0;
        q.push_back(root);

        while let Some(node) = q.pop_front() {
            for &child in self.tree[node].iter() {
                if child != self.parent[node][0] {
                    self.depth[child] = self.depth[node] + 1;
                    self.parent[child][0] = node;
                    q.push_back(child);
                }
            }
        }
    }

    fn fill_parent(&mut self) {
        let size = self.tree.len() - 1;
        for j in 1..17 {
            for i in 1..=size {
                self.parent[i][j] = self.parent[self.parent[i][j - 1]][j - 1];
            }
        }
    }

    fn query(&self, mut a: usize, mut b: usize) -> usize {
        if self.depth[a] < self.depth[b] {
            swap(&mut a, &mut b);
        }

        let diff = self.depth[a] - self.depth[b];

        for i in 0..17 {
            if diff & (1 << i) != 0 {
                a = self.parent[a][i];
            }
        }

        if a != b {
            for i in (0..17).rev() {
                if self.parent[a][i] != self.parent[b][i] {
                    a = self.parent[a][i];
                    b = self.parent[b][i];
                }
            }
            a = self.parent[a][0];
        }

        a
    }

    fn nth_parent(&self, mut node: usize, nth: usize) -> usize {
        for i in 0..17 {
            if nth & (1 << i) != 0 {
                node = self.parent[node][i];
            }
        }
        node
    }

    fn distance(&self, a: usize, b: usize) -> usize {
        let ab = self.query(a, b);
        self.depth[a] + self.depth[b] - 2 * self.depth[ab]
    }

    fn find_circumcenter(&self, a: usize, b: usize, c: usize) -> Option<usize> {
        let pairs = [(a, b, c), (b, c, a), (c, a, b)];

        for &(x, y, z) in &pairs {
            let d = self.distance(x, y);
            if d % 2 != 0 {
                continue;
            }

            let xy = if self.depth[x] > self.depth[y] { x } else { y };
            let m = self.nth_parent(xy, d / 2);
            if self.distance(m, z) == d / 2 {
                return Some(m);
            }
        }
        None
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

    let n = next!(usize);
    let mut tree = vec![vec![]; n + 1];
    for _ in 1..n {
        let (u, v) = next!(usize, usize);
        tree[u].push(v);
        tree[v].push(u);
    }

    let mut lca = Tree::new(n, tree);
    lca.init_parent(1);
    lca.fill_parent();

    let m = next!(usize);
    for _ in 0..m {
        let (a, b, c) = next!(usize, usize, usize);
        match lca.find_circumcenter(a, b, c) {
            Some(cc) => println!("{}", cc),
            None => println!("-1"),
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