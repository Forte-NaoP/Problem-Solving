use std::cell::Ref;
use std::iter::Rev;
use std::mem::swap;
use std::cmp::{max, min, Ordering, Reverse};
use std::collections::{BinaryHeap, HashMap, HashSet, VecDeque, BTreeSet};
use std::pin::Pin;
use std::{default, i32, usize, vec};
use std::{
    io::{Write, BufWriter, StdoutLock}, cell::RefCell
};
use std::rc::{Rc, Weak};
use std::ops::Bound::{Included, Excluded, Unbounded};

struct Tree {
    root: usize,
    node: Vec<Vec<usize>>,
}

impl Tree {
    fn new(root: usize, size: usize) -> Self {
        Self {
            root, node: vec![vec![]; size + 1]
        }
    }

    fn append(&mut self, u: usize, v: usize) {
        self.node[u].push(v);
    }

    fn euler_tour(&self) -> Vec<DFSNode> {
        let mut dfs_tree = vec![DFSNode {id: 0, _in: 0, _out: 0, _depth: 0}; self.node.len()];
        let mut dfs_id = 0;
        let mut stack = vec![(self.root, 0, 0, true)];
        let mut depth = 0;
        while let Some((cur, parent, child_idx, enter)) = stack.pop() {
            if enter {
                depth += 1;
                dfs_tree[cur].id = cur;
                dfs_tree[cur]._in = dfs_id;
                dfs_tree[cur]._depth = depth;
                dfs_id += 1;

                stack.push((cur, parent, child_idx, false));

                for &child in self.node[cur].iter() {
                    if child != parent {
                        stack.push((child, cur, 0, true));
                    }
                }
            } else {
                dfs_tree[cur]._out = dfs_id;
                depth -= 1;
            }
        }
        dfs_tree
    }
}

#[derive(Clone, Copy)]
struct DFSNode {
    id: usize,
    _in: usize,
    _out: usize,
    _depth: i32,
}

struct SegmentTree {
    base: usize,
    node: Vec<i64>,
}

impl SegmentTree {
    fn new(size: usize) -> Self {
        let mut base = 1;
        while base < size {
            base <<= 1;
        }

        Self { base, node: vec![0; base << 1] }
    }

    fn update(&mut self, mut idx: usize) {
        idx += self.base;
        self.node[idx] += 1;
        idx >>= 1;

        while idx > 0 {
            self.node[idx] += 1;
            idx >>= 1;
        }
    }

    fn query(&self, l: usize, r: usize, s: usize, e: usize, idx: usize) -> i64 {
        if r < s || e < l {
            return 0;
        }

        if l <= s && e <= r {
            return self.node[idx];
        }

        let mid = (s + e) / 2;
        return self.query(l, r, s, mid, idx << 1) + self.query(l, r, mid + 1, e, idx << 1 | 1);
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

    let (n, c) = next!(usize, usize);
    let mut tree = Tree::new(c, n);
    for _ in 1..n {
        let (u, v) = next!(usize, usize);
        tree.append(u, v);
        tree.append(v, u);
    }

    let dfs_tree = tree.euler_tour();
    // for node in dfs_tree.iter().skip(1) {
    //     println!("Node {}: in = {}, out = {}, depth = {}", node.id, node._in, node._out, node._depth);
    // }

    let mut segtree = SegmentTree::new(n);
    let q = next!(usize);
    for _ in 0..q {
        let (t, a) = next!(usize, usize);
        match t {
            1 => segtree.update(dfs_tree[a]._in),
            2 => println!("{}", segtree.query(dfs_tree[a]._in, dfs_tree[a]._out - 1, 0, segtree.base - 1, 1) * dfs_tree[a]._depth as i64),
            _ => unreachable!(),
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