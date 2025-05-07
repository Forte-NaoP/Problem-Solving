use std::collections::VecDeque;
use std::mem::swap;
use std::rc::Rc;
use std::{i32, usize, vec};
use std::{
    io::{Write, BufWriter, StdoutLock}, cell::RefCell
};

struct TrieNode {
    children: [Option<usize>; 2],
    count: u32,
}

impl TrieNode {
    fn new() -> Self {
        Self {
            children: [None; 2],
            count: 0,
        }
    }
}

pub struct Trie {
    nodes: Vec<TrieNode>,
    len: usize,
}

impl Trie {
    pub fn new() -> Self {
        let mut nodes = Vec::with_capacity(1 << 20);
        nodes.push(TrieNode::new());
        Self { nodes, len: 30 }
    }

    fn new_node(&mut self) -> usize {
        let idx = self.nodes.len();
        self.nodes.push(TrieNode::new());
        idx
    }

    fn get_or_insert_with(&mut self, cur: usize, idx: usize) -> usize {
        if let Some(child) = self.nodes[cur].children[idx] {
            child
        } else {
            let child = self.new_node();
            self.nodes[cur].children[idx] = Some(child);
            child
        }
    }

    pub fn insert(&mut self, word: &str) {
        let mut cur = 0;
        self.nodes[cur].count += 1;

        for _ in 0..(self.len - word.len()) {
            cur = self.get_or_insert_with(cur, 0);
            self.nodes[cur].count += 1;
        }

        for b in word.bytes() {
            let idx = (b - b'0') as usize;
            cur = self.get_or_insert_with(cur, idx);
            self.nodes[cur].count += 1;
        }
    }

    pub fn remove(&mut self, word: &str) {
        let mut cur = 0;
        self.nodes[cur].count -= 1;

        for _ in 0..(self.len - word.len()) {
            let child = self.nodes[cur].children[0].unwrap();
            if self.nodes[child].count == 1 {
                self.nodes[cur].children[0] = None;
                return;
            }
            cur = child;
            self.nodes[cur].count -= 1;
        }

        for b in word.bytes() {
            let idx = (b - b'0') as usize;
            let child = self.nodes[cur].children[idx].unwrap();
            if self.nodes[child].count == 1 {
                self.nodes[cur].children[idx] = None;
                return;
            }
            cur = child;
            self.nodes[cur].count -= 1;
        }
    }

    pub fn search(&self, word: &str) -> i32 {
        let mut cur = 0;
        let mut ret = 0;

        for _ in 0..(self.len - word.len()) {
            ret <<= 1;

            if let Some(child) = self.nodes[cur].children[1] {
                if self.nodes[child].count > 0 {
                    ret |= 1;
                    cur = child;
                    continue;
                }
            }
            cur = self.nodes[cur].children[0].unwrap();
        }

        for b in word.bytes() {
            let idx = (b - b'0') as usize;
            ret <<= 1;

            if let Some(child) = self.nodes[cur].children[idx ^ 1] {
                if self.nodes[child].count > 0 {
                    ret |= 1;
                    cur = child;
                    continue;
                }
            }
            cur = self.nodes[cur].children[idx].unwrap();
        }

        ret
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

    let mut trie = Trie::new();
    let n = next!(usize);
    let first = format!("{:b}", 0);
    trie.insert(&first);
    for _ in 0..n {
        let (q, x) =  next!(usize, i32);
        let bin = format!("{x:b}");
        match q {
            1 => trie.insert(&bin),
            2 => trie.remove(&bin),
            3 => println!("{}", trie.search(&bin)),
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