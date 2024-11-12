use std::collections::BTreeMap;
use std::io::{self, Error, ErrorKind, Read, Write};
use std::fs::File;
use std::vec;
use std::fmt::Write as fmt_Write;

fn encode(s: &str) -> u128 {
    let mut val = 0;
    for c in s.chars() {
        val <<= 5;
        val += c as u128 - 'A' as u128 + 1;
    }
    for _ in 0..15-s.len() {
        val <<= 5;
    }
    val
}

fn decode(mut val: u128) -> String {
    let mut s = vec![];
    while val > 0 {
        let c = (val & 31) as u8;
        if c != 0 {
            s.push((c + 'A' as u8 - 1) as char);
        }
        val >>= 5;
    }
    s.iter().rev().collect()
}

#[derive(Clone, Debug)]
struct Node {
    next: BTreeMap<u128, usize>,
}

impl Node {
    fn new() -> Self {
        Node { next: BTreeMap::new()}
    }
}

#[derive(Debug)]
struct Trie {
    node: Vec<Node>,
}

impl Trie {
    fn new() -> Self {
        Trie {
            node: vec![Node::new()],
        }
    }

    fn insert(&mut self, dirs: &Vec<u128>) {
        let mut cur = 0;
        for dir in dirs.iter() {
            if self.node[cur].next.get(dir).is_none() {
                let idx = self.node.len();
                self.node.push(Node::new());
                self.node[cur].next.entry(*dir).or_insert(idx);
            }
            cur = *self.node[cur].next.get(dir).unwrap();
        }
    }

    fn travel(&self, buf: &mut String, cur: usize, depth: usize) {
        for (k, v) in self.node[cur].next.iter() {
            for _ in 0..depth {
                write!(buf, "--").unwrap();
            }
            writeln!(buf, "{}", decode(*k)).unwrap();
            self.travel(buf, *v, depth + 1);
        }
    }
}

fn main() -> Result<(), io::Error> {
    let mut buf = String::new();

    // let mut file = File::open("input.txt").unwrap();
    // file.read_to_string(&mut buf).unwrap();
    
    io::stdin().read_to_string(&mut buf).unwrap();
    let mut scanner: Scanner<_> = Scanner::new(buf.split_whitespace());
    let mut output: io::BufWriter<io::StdoutLock<'_>> = io::BufWriter::new(io::stdout().lock());

    let n: usize = scanner.next().unwrap();
    let mut dirs: Vec<Vec<u128>> = vec![];
    let mut trie = Trie::new();

    for _ in 0..n {
        let k = scanner.next().unwrap(); 
        let mut dir = vec![];
        for _ in 0..k {
            let s = scanner.next_str().unwrap();
            let e = encode(s);
            dir.push(e);
        }
        dirs.push(dir);
    }
    dirs.sort();
    for dir in dirs.iter() {
        trie.insert(dir);
    }
    let mut res = String::new();
    trie.travel(&mut res, 0, 0);
    write!(output, "{}", res).unwrap();
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