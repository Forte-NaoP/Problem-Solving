use std::io::{stdin, BufReader, BufRead};
use std::fmt::Write;
use std::fs::File;
use std::collections::HashSet;
use std::cmp::min;

fn encode(s: &str) -> i64 {
    let mut ret = 0;
    for c in s.chars() {
        ret <<= 5;
        ret |= c as i64 - 'A' as i64 + 1;
    }
    ret
}

fn decode(mut n: i64) -> String {
    let mut ret: Vec<char> = vec![];
    while n > 0 {
        ret.push(((n & 31) as u8 + 'A' as u8 - 1) as char);
        n >>= 5;
    }
    ret.reverse();
    ret.iter().collect()
}

struct Trie {
    next: [Option<Box<Trie>>; 26],
    end: bool,
}

impl Trie {
    fn new() -> Self {
        Trie {
            next: Default::default(),
            end: false,
        }
    }

    fn insert(&mut self, s: i64) {
        if s == 0 {
            self.end = true;
            return
        }
        let c = (s & 31) as usize - 1;
        if self.next[c].is_none() {
            self.next[c] = Some(Box::new(Trie::new()));
        }
        self.next[c].as_mut().unwrap().insert(s >> 5);
    }

    fn find(&self, s: i64) -> bool {
        if s == 0 {
            return self.end
        }
        let c = (s & 31) as usize - 1;
        if self.next[c].is_none() {
            return false
        }
        self.next[c].as_ref().unwrap().find(s >> 5)
    }
}

static DIFF: [(i32, i32); 8] = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)];
static SCORE: [i32; 9] = [0, 0, 0, 1, 1, 2, 3, 5, 11];

struct Params {
    pub word: i64,
    pub len: usize,
    pub score: i32
}

fn dfs(
    x: usize, y: usize, mut word: i64, depth: usize,
    param: &mut Params,
    board: &[[u8; 4]; 4],
    trie: &mut Trie, 
    found: &mut HashSet<i64>,
    visited: &mut [[bool; 4]; 4]
) {
    visited[x][y] = true;
    word = (word << 5) + (board[x][y] - 64) as i64;

    if depth != 0 && found.get(&word).is_none() {
        if trie.find(word) {
            found.insert(word);
            param.score += SCORE[depth];
            if param.len < depth {
                param.word = word;
                param.len = depth;
            } else if param.len == depth {
                param.word = min(param.word, word);
            }
        }
    }

    if depth == 8 {
        word >>= 5;
        visited[x][y] = false;
        return;
    }
    
    for (dx, dy) in DIFF.iter() {
        let (nx, ny) = (x as i32 + dx, y as i32 + dy);
        if (0 <= nx && nx < 4) && (0 <= ny && ny < 4) {
            let (nx, ny) = (nx as usize, ny as usize);
            if !visited[nx][ny] {
                dfs(nx, ny, word, depth + 1, param, board, trie, found, visited);
            }
        }
    }

    word >>= 5;
    visited[x][y] = false;

}

fn main() {
    let offline = false;
    let mut input = if offline {
        let file = File::open("input.txt").unwrap();
        let istream: Box<dyn BufRead> = Box::new(BufReader::new(file));
        istream
    } else {
        Box::new(BufReader::new(stdin()))
    }.lines();
    
    let mut trie = Trie::new();
    let w: usize = input.next().unwrap().unwrap().parse().unwrap();
    for _ in 0..w {
        let s = input.next().unwrap().unwrap();
        trie.insert(encode(&s));
    }
    input.next();
    let b: usize = input.next().unwrap().unwrap().parse().unwrap();
    for _ in 0..b {
        let mut board: [[u8; 4]; 4] = [[0; 4]; 4];
        let mut visited: [[bool; 4]; 4] = [[false; 4]; 4];
        let mut param = Params{word: 0, len: 0, score: 0};
        let mut found: HashSet<i64> = HashSet::new();

        for i in 0..4 {
            let line: Vec<u8> = input.next().unwrap().unwrap().bytes().collect();
            for (j, c) in line.iter().enumerate() {
                board[i][j] = *c;
            }
        }

        for i in 0..4 {
            for j in 0..4 {
                dfs(i, j, 0, 1, &mut param, &board, &mut trie, &mut found, &mut visited);
            }
        }
        println!("{} {} {}", param.score, decode(param.word), found.len());
        input.next();
    }
}

