use std::{i32, usize, vec};
use std::{
    io::{Write, BufWriter, StdoutLock}, cell::RefCell
};

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
        let mut dfs_tree = vec![DFSNode {id: 0, _in: 0, _out: 0}; self.node.len()];
        let mut dfs_id = 0;
        let mut stack = vec![(self.root, 0, 0, true)];
        while let Some((cur, parent, child_idx, enter)) = stack.pop() {
            if enter {
                dfs_tree[cur].id = cur;
                dfs_tree[cur]._in = dfs_id;
                dfs_id += 1;

                stack.push((cur, parent, child_idx, false));

                for &child in self.node[cur].iter() {
                    if child != parent {
                        stack.push((child, cur, 0, true));
                    }
                }
            } else {
                dfs_tree[cur]._out = dfs_id;
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
}

pub trait RangeOp: Default + Clone {
    type D: Default + Clone + PartialEq;
    type U: Default + Clone + PartialEq;

    fn combine(a: &Self::D, b: &Self::D) -> Self::D;
    fn apply(node: &Self::D, upd: &Self::U, len: usize) -> Self::D;
    fn compose(old: &Self::U, new: &Self::U) -> Self::U;
}

pub struct SegmentTreeLazy<Op>
where
    Op:RangeOp,
{
    base: usize,
    node: Vec<Op::D>,
    lazy: Vec<Op::U>,
}

impl<Op> SegmentTreeLazy<Op>
where
    Op: RangeOp,
{
    pub fn new(size: usize) -> Self {
        let mut base = 1;
        while base < size {
            base <<= 1;
        }
        let capacity = base << 1;
        SegmentTreeLazy { 
            base,
            node: vec![Op::D::default(); capacity], 
            lazy: vec![Op::U::default(); capacity],
        }
    }

    fn propagate(&mut self, s: usize, e: usize, idx: usize) {
        let upd = std::mem::take(&mut self.lazy[idx]);
        if upd != Op::U::default() {
            self.node[idx] = Op::apply(&self.node[idx], &upd, e - s + 1);

            if s != e {
                let left = idx << 1;
                let right = idx << 1 | 1;

                self.lazy[left] = Op::compose(&self.lazy[left], &upd);
                self.lazy[right] = Op::compose(&self.lazy[right], &upd);
            }
        }
    }

    pub fn update_range(&mut self, l: usize, r: usize, upd: Op::U) {
        self._update(l, r, upd, 0, self.base - 1, 1);
    }

    fn _update(&mut self, l: usize, r: usize, upd: Op::U, s: usize, e: usize, idx: usize) {
        self.propagate(s, e, idx);
        if r < s || e < l {
            return;
        }
        if l <= s && e <= r {
            self.lazy[idx] = Op::compose(&self.lazy[idx], &upd);
            self.propagate(s, e, idx);
            return;
        }
        let mid = (s + e) >> 1;
        self._update(l, r, upd.clone(), s, mid, idx << 1);
        self._update(l, r, upd, mid + 1, e, idx << 1 | 1);
        self.node[idx] = Op::combine(
            &self.node[idx << 1],
            &self.node[idx << 1 | 1],
        );
    }

    pub fn query_range(&mut self, l: usize, r: usize) -> Op::D {
        self._query(l, r, 0, self.base - 1, 1)
    }

    fn _query(&mut self, l: usize, r: usize, s: usize, e: usize, idx: usize) -> Op::D {
        self.propagate(s, e, idx);
        if r < s || e < l {
            return Op::D::default();
        }
        if l <= s && e <= r {
            return self.node[idx].clone();
        }
        let mid = (s + e) >> 1;
        let left  = self._query(l, r, s, mid, idx << 1);
        let right = self._query(l, r, mid + 1, e, idx << 1 | 1);
        Op::combine(&left, &right)
    }
}

#[derive(Default, Clone, PartialEq)]
struct SumAdd;

impl RangeOp for SumAdd {
    type D = i64;
    type U = i64;

    fn combine(a: &Self::D, b: &Self::D) -> Self::D {
        *a + *b
    }

    fn apply(node: &Self::D, upd: &Self::U, len: usize) -> Self::D {
        *node + (*upd) * (len as i64)
    }

    fn compose(old: &Self::U, new: &Self::U) -> Self::U {
        *old + *new
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
    let mut tree = Tree::new(1, n);
    next!(i32);
    for u in 2..=n {
        let v = next!(usize);
        tree.append(u, v);
        tree.append(v, u);
    }

    let dfs_tree = tree.euler_tour();
    let mut segtree: SegmentTreeLazy<SumAdd> = SegmentTreeLazy::new(n);
    for _ in 0..m {
        let c = next!(usize);
        match c {
            1 => {
                let (a, b) = next!(usize, i64);
                segtree.update_range(dfs_tree[a]._in, dfs_tree[a]._out - 1, b);
            },
            2 => {
                let a = next!(usize);
                println!("{}", segtree.query_range(dfs_tree[a]._in, dfs_tree[a]._in));
            },
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