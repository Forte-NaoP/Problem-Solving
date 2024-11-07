use std::env::consts::FAMILY;
use std::io::{self, Error, ErrorKind, Read, Write};
use std::fs::File;
use std::mem::swap;
use std::str::FromStr;
use std::vec;
use std::fmt;

#[derive(Clone, Copy, Debug)]
struct Node {
    next: [Option<usize>; 10],
    end: bool
}

impl Node {
    fn new() -> Self {
        Node { next: [None; 10], end: false}
    }
}

#[derive(Debug)]
struct Trie {
    node: Vec<Node>,
}

impl Trie {
    fn new() -> Self {
        Trie {node: vec![Node::new()]}
    }

    fn insert(&mut self, num: &str) -> bool {
        let mut cur = 0;
        for digit in num.chars().map(|x| x as usize - '0' as usize) {
            if self.node[cur].next[digit].is_none() {
                self.node[cur].next[digit] = Some(self.node.len());
                self.node.push(Node::new());
            }
            cur = self.node[cur].next[digit].unwrap();
            if self.node[cur].end {
                return false;
            }
        }
        self.node[cur].end = true;
        true
    }

    fn find(&self, num: &str) -> bool {
        let mut cur = 0;
        for digit in num.chars().map(|x| x as usize - '0' as usize) {
            if self.node[cur].next[digit].is_none() {
                return false;    
            }
            cur = self.node[cur].next[digit].unwrap();
        }
        self.node[cur].end
    }

}

fn main() -> Result<(), io::Error> {
    let mut buf = String::new();

    // let mut file = File::open("input.txt").unwrap();
    // file.read_to_string(&mut buf).unwrap();
    
    io::stdin().read_to_string(&mut buf).unwrap();
    let mut scanner: Scanner<_> = Scanner::new(buf.split_whitespace());
    let mut output: io::BufWriter<io::StdoutLock<'_>> = io::BufWriter::new(io::stdout().lock());

    let t: usize = scanner.next().unwrap();
    for _ in 0..t {
        let n = scanner.next().unwrap();
        let mut trie = Trie::new();
        let mut nums = vec![];
        for _ in 0..n {
            let pn = scanner.next_str().unwrap();
            nums.push(pn);
        }
        nums.sort();
        let mut ans = true;
        for num in nums.iter() {
            if !trie.insert(num) {
                ans = false;
                break
            }
        }
        match ans {
            true => output.write(b"YES\n")?,
            false => output.write(b"NO\n")?
        };
    }

    Ok(())
}   

struct Scanner<'a, I: Iterator<Item = &'a str>> {
    iter: I
}

impl<'a, I: Iterator<Item = &'a str>> Scanner<'a, I> {
    fn new(from: I) -> Self {
        Self { iter: from }
    }
    fn next_str(&mut self) -> Result<&'a str, Error> {
        self.iter.next().ok_or(Error::new(ErrorKind::NotFound, ""))
    }
    fn next<T: std::str::FromStr>(&mut self) -> Result<T, Error> {
        let str = self.next_str()?;
        match str.parse() {
            Ok(res) => Ok(res),
            Err(_) => Err(Error::new(ErrorKind::InvalidInput, ""))
        }
    }
}