use std::io::{self, Error, ErrorKind, Read, Write};
use std::fs::File;
use std::mem::swap;
use std::str::FromStr;
use std::vec;

struct LCA {
    parent: Vec<Vec<usize>>,
    depth: Vec<usize>,
    max_depth: usize
}

impl LCA {
    fn new(n: usize) -> Self {
        let max_depth = (n as f64).log2() as usize + 1;
        let parent = vec![vec![0; n + 1]; max_depth];
        let depth = vec![0; n + 1];
        LCA{
            parent,
            depth,
            max_depth
        }
    }

    fn init(&mut self, tree: &Vec<Vec<usize>>, cur: usize, p: usize) {
        self.depth[cur] = self.depth[p] + 1;
        self.parent[0][cur] = p;

        for i in 1..self.max_depth {
            self.parent[i][cur] = self.parent[i - 1][self.parent[i - 1][cur]];
        }

        for &nxt in tree[cur].iter() {
            if nxt != p {
                self.init(tree, nxt, cur);
            }
        }
    }

    fn query(&self, mut a: usize, mut b: usize) -> usize {
        if self.depth[a] > self.depth[b] {
            swap(&mut a, &mut b);
        }

        let diff = self.depth[b] - self.depth[a];
        for i in 0..self.max_depth {
            if (diff >> i) & 1 == 1 {
                b = self.parent[i][b];
            }
        }
        
        if a == b {
            return a;
        }

        for i in (0..self.max_depth).rev() {
            if self.parent[i][a] != self.parent[i][b] {
                a = self.parent[i][a];
                b = self.parent[i][b];
            }
        } 
        return self.parent[0][a];
    }
}

fn main() -> Result<(), io::Error> {
    let mut buf = String::new();

    // let mut file = File::open("input.txt").unwrap();
    // file.read_to_string(&mut buf).unwrap();
    
    io::stdin().read_to_string(&mut buf).unwrap();
    let mut scanner: Scanner<_> = Scanner::new(buf.split_whitespace());
    let mut output: io::BufWriter<io::StdoutLock<'_>> = io::BufWriter::new(io::stdout().lock());

    let n: usize = scanner.next()?;
    let mut tree: Vec<Vec<usize>> = vec![vec![]; n + 1];
    for _ in 1..n {
        let a: usize = scanner.next()?;
        let b: usize = scanner.next()?;
        tree[a].push(b);
        tree[b].push(a);
    }

    let mut lca = LCA::new(n);
    lca.init(&tree, 1, 0);
    let m: usize = scanner.next()?;
    for _ in 0..m {
        let a: usize = scanner.next()?;
        let b: usize = scanner.next()?;
        writeln!(output, "{}", lca.query(a, b))?;
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