use std::collections::VecDeque;
use std::mem::swap;
use std::rc::Rc;
use std::{i32, usize, vec};
use std::{
    io::{Write, BufWriter, StdoutLock}, cell::RefCell
};

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

#[derive(Clone, PartialEq, Debug)]
pub struct Update {
    pub assign: Option<i64>,
    pub mul: i64,
    pub add: i64,
}

impl Update {
    pub fn set(x: i64) -> Self {
        Update { assign: Some(x), mul: 1, add: 0 }
    }

    pub fn mul(x: i64) -> Self {
        Update { assign: None, mul: x, add: 0 }
    }

    pub fn add(x: i64) -> Self {
        Update { assign: None, mul: 1, add: x }
    }
}

impl Default for Update {
    fn default() -> Self {
        Update { assign: None, mul: 1, add: 0 }
    }
}

#[derive(Clone, Default)]
struct Node;

impl RangeOp for Node {
    type D = i64;
    type U = Update;

    fn combine(a: &Self::D, b: &Self::D) -> Self::D {
        (*a + *b) % 1_000_000_007
    }

    fn apply(node: &Self::D, upd: &Self::U, len: usize) -> Self::D {
        if let Some(v) = upd.assign {
            (v * len as i64) % 1_000_000_007
        } else {
            (node * upd.mul + upd.add * len as i64) % 1_000_000_007
        }
    }

    fn compose(old: &Self::U, new: &Self::U) -> Self::U {
        if new.assign.is_some() {
            return new.clone();
        }

        let assign = old.assign.map(|v| (v * new.mul + new.add) % 1_000_000_007);
        let mul = (old.mul * new.mul) % 1_000_000_007;
        let add = (old.add * new.mul + new.add) % 1_000_000_007;
        Update {assign, mul, add}
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
    let mut tree = SegmentTreeLazy::<Node>::new(n);
    for i in 0..n {
        tree.update_range(i, i, Update::set(next!(i64)));
    }

    let m = next!(usize);
    for _ in 0..m {
        let (q, x, y) = next!(usize, usize, usize);
        match q {
            1 => {
                tree.update_range(x - 1, y - 1, Update::add(next!(i64)));
            },
            2 => {
                tree.update_range(x - 1, y - 1, Update::mul(next!(i64)));
            },
            3 => {
                tree.update_range(x - 1, y - 1, Update::set(next!(i64)));
            },
            4 => {
                println!("{}", tree.query_range(x - 1, y - 1));
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