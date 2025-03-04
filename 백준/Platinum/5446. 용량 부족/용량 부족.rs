use std::mem::swap;
use std::cmp::{max, min, Ordering};
use std::collections::{HashMap, VecDeque};
use std::pin::Pin;
use std::{default, i32, usize, vec};
use std::{
    io::{Write, BufWriter, StdoutLock}, cell::RefCell
};

struct TrieNode {
    next: [Option<Box<TrieNode>>; 128],
    end: bool,
    forbidden: bool,
    fend: bool,
}

impl TrieNode {
    fn new() -> Self {
        TrieNode {
            next: std::array::from_fn(|_| None),
            end: false,
            forbidden: false,
            fend: true
        }
    }
}

struct Trie {
    root: Box<TrieNode>,
}

impl Trie {
    fn new() -> Trie {
        Trie {
            root: Box::new(TrieNode::new())
        }
    }

    fn insert(&mut self, s: &str, forbidden: bool) {
        let mut node = &mut *self.root;
        node.forbidden = forbidden;

        for c in s.chars() {
            let idx = c as usize;
            node = node.next[idx].get_or_insert_with(|| Box::new(TrieNode::new())).as_mut();
            node.forbidden = forbidden;
        }
        node.end = true;
        node.fend = forbidden;
    }

    fn search(&self) -> usize {
        fn dfs(node: &TrieNode /*, prefix: String*/) -> usize {
            if !node.forbidden {
                // println!("{}", prefix);
                return 1;
            }
            let mut sum = 0;

            if node.end && !node.fend {
                // println!("{}", prefix);
                sum += 1;
            }

            for i in 0..node.next.len() {
                if let Some(ref child) = node.next[i] {
                    // let new_prefix = format!("{}{}", prefix, i as u8 as char);
                    sum += dfs(child/*, new_prefix*/);
                }
            }
            sum
        }
        dfs(&self.root, /*String::new()*/)
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

    let T = next!(usize);
    for _ in 0..T {
        let mut trie = Trie::new();
        let n1 = next!(usize);
        for _ in 0..n1 {
            let s = next!();
            trie.insert(s, false);
        }
        let n2 = next!(usize);
        for _ in 0..n2 {
            let s = next!();
            trie.insert(s, true);
        }

        println!("{}", trie.search());
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