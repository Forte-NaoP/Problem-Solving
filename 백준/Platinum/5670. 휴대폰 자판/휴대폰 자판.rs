use std::rc::Rc;
use std::{i32, usize, vec};
use std::{
    io::{Write, BufWriter, StdoutLock}, cell::RefCell
};

struct TrieNode {
    children: [Option<Box<TrieNode>>; 26],
    is_end: bool,
}

impl TrieNode {
    fn new() -> Self {
        Self {
            children: Default::default(),
            is_end: false,
        }
    }
}

pub struct Trie {
    root: TrieNode,
}

impl Trie {
    pub fn new() -> Self {
        Self { root: TrieNode::new() }
    }

    pub fn insert(&mut self, word: &str) {
        let mut node = &mut self.root;
        for b in word.bytes() {
            let idx = (b - b'a') as usize;
            node = node.children[idx]
                .get_or_insert_with(|| Box::new(TrieNode::new()));
        }
        node.is_end = true;
    }

    pub fn search(&self, word: &str) -> Option<i32> {
        let mut node = &self.root;
        let mut cnt = 0;
        for (i, b) in word.bytes().enumerate() {
            let idx = (b - b'a') as usize;
            let child_count = node.children.iter().filter(|c| c.is_some()).count();
            if i == 0 || child_count > 1 || node.is_end {
                cnt += 1;
            }

            match &node.children[idx] {
                Some(next) => node = next,
                None => return None,
            }
        }
        Some(cnt)
    }
}

fn solve(stdin: &str) {
    let mut tokens = stdin.split_ascii_whitespace();
    
    while let Some(n_str) = tokens.next() {
        let n: usize = match n_str.parse() {
            Ok(v) => v,
            Err(_) => break,
        };

        let mut trie = Trie::new();
        let mut words = Vec::with_capacity(n);
        for _ in 0..n {
            if let Some(w) = tokens.next() {
                words.push(w);
                trie.insert(w);
            }
        }
    
        let mut cnt = 0;
        for &word in &words {
            if let Some(c) = trie.search(word) {
                cnt += c;
            }
        }
        println!("{:.2}", (cnt as f32) / (n as f32));
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