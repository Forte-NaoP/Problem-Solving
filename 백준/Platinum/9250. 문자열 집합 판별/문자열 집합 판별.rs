use std::cell::Ref;
use std::iter::Rev;
use std::mem::swap;
use std::cmp::{max, min, Ordering, Reverse};
use std::collections::{BinaryHeap, HashMap, HashSet, VecDeque};
use std::pin::Pin;
use std::{default, i32, usize, vec};
use std::{
    io::{Write, BufWriter, StdoutLock}, cell::RefCell
};
use std::rc::{Rc, Weak};

struct TrieNode {
    children: [Option<Rc<RefCell<TrieNode>>>; 26],
    fail_link: Option<Weak<RefCell<TrieNode>>>,
    is_end: bool,
}

impl TrieNode {
    fn new() -> Self {
        TrieNode {
            children: Default::default(),
            fail_link: None,
            is_end: false,
        }
    }
}

struct Trie {
    root: Rc<RefCell<TrieNode>>,
}

impl Trie {
    fn new() -> Self {
        Trie {
            root: Rc::new(RefCell::new(TrieNode::new())),
        }
    }

    fn insert(&mut self, word: &str) {
        let mut node = self.root.clone();
        for c in word.chars() {
            let idx = c as usize - 'a' as usize;
            node = {
                let mut node_mut = node.borrow_mut();
                node_mut
                    .children[idx]
                    .get_or_insert_with(|| Rc::new(RefCell::new(TrieNode::new())))
                    .clone()
            };
        }
        node.borrow_mut().is_end = true;
    }

    fn search(&self, word: &str) -> bool {
        let mut node = self.root.clone();
        for c in word.chars() {
            let idx = c as usize - 'a' as usize;
            while !Rc::ptr_eq(&node, &self.root) && node.borrow().children[idx].is_none() {
                node = {
                    let node_bwr = node.borrow();
                    node_bwr
                        .fail_link
                        .as_ref()
                        .unwrap()
                        .upgrade()
                        .unwrap()
                };
            }

            if node.borrow().children[idx].is_some() {
                node = {
                    let node_bwr = node.borrow();
                    node_bwr
                        .children[idx]
                        .as_ref()
                        .unwrap()
                        .clone()
                };
            }

            if node.borrow().is_end {
                return true;
            }
        }
        false
    }

    fn failure(&mut self) {
        let mut dq = VecDeque::new();
        dq.push_back(self.root.clone());

        while let Some(node) = dq.pop_front() {
            for idx in 0..26 {
                if let Some(child) = node.borrow().children[idx].clone() {
                    if Rc::ptr_eq(&node, &self.root) {
                        child.borrow_mut().fail_link = Some(Rc::downgrade(&self.root));
                    } else {
                        let mut parent = node.borrow().fail_link.as_ref().unwrap().upgrade().unwrap();
                        while !Rc::ptr_eq(&parent, &self.root) && parent.borrow().children[idx].is_none() {
                            parent = {
                                let parent_bwr = parent.borrow();
                                parent_bwr
                                    .fail_link
                                    .as_ref()
                                    .unwrap()
                                    .upgrade()
                                    .unwrap()
                            };
                        }
                        
                        if parent.borrow().children[idx].is_some() {
                            parent = {
                                let parent_bwr = parent.borrow();
                                parent_bwr
                                    .children[idx]
                                    .as_ref()
                                    .unwrap()
                                    .clone()
                            };
                        }

                        child.borrow_mut().fail_link = Some(Rc::downgrade(&parent));
                    }

                    if child.borrow().fail_link.as_ref().unwrap().upgrade().unwrap().borrow().is_end {
                        child.borrow_mut().is_end = true;
                    }

                    dq.push_back(child.clone());
                }
            }
        }
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
    for _ in 0..n {
        trie.insert(next!());
    }
    trie.failure();
    let m = next!(usize);
    for _ in 0..m {
        match trie.search(next!()) {
            true => println!("YES"),
            false => println!("NO"),
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