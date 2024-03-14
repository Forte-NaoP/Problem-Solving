use std::io::{stdin, Read, BufReader};
use std::fs::File;
use std::collections::{VecDeque};
use std::cmp::*;

#[derive(Clone, Copy, PartialEq, Eq)]
struct P {
    x: usize, y: usize, d: usize,
}

impl PartialOrd for P {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        if self.d != other.d {
            return self.d.partial_cmp(&other.d);
        }
        if self.x != other.x {
            return self.x.partial_cmp(&other.x);
        }
        self.y.partial_cmp(&other.y)
    }
}

impl Ord for P {
    fn cmp(&self, other: &Self) -> Ordering {
        self.partial_cmp(other).unwrap()
    }
}

struct Sea {
    n: isize,
    sea: [[usize; 20]; 20],
    visit: [[i32; 20]; 20],
}

const NEVER_REACH: usize = 999;

fn bfs(big: usize, mut cur: P, map: &mut Sea, lv: i32) -> Option<P> {
    let dv = [(0, -1), (0, 1), (1, 0), (-1, 0)];

    let mut food = P {x: 999, y: 999, d: NEVER_REACH};
    let mut q = VecDeque::new();

    cur.d = 0;
    map.visit[cur.x][cur.y] = lv;
    q.push_back(cur);
    
    while let Some(now) = q.pop_front() {
        if now.d >= food.d {
            break;
        }
        for &(dx, dy) in dv.iter() {
            let (nx, ny) = (now.x as isize + dx, now.y as isize + dy);
            if !(0..map.n).contains(&nx) || !(0..map.n).contains(&ny) {
                continue;
            }

            let nxt = P {x: nx as usize, y: ny as usize, d: now.d + 1};
            if map.sea[nxt.x][nxt.y] > big || map.visit[nxt.x][nxt.y] == lv {
                continue;
            }

            if map.sea[nxt.x][nxt.y] != 0 && map.sea[nxt.x][nxt.y] < big && nxt < food {
                food = nxt;
            }
            map.visit[nxt.x][nxt.y] = lv;
            q.push_back(nxt);
        }
    }

    if food.d == NEVER_REACH { None } else { Some(food) }
}

fn main() {
    let mut reader = BufReader::new(stdin());
    
    let mut input = String::new();
    reader.read_to_string(&mut input).unwrap();
    let mut input = input.split_ascii_whitespace().flat_map(str::parse::<usize>);

    let n = input.next().unwrap();
    let mut map = Sea{n: n as isize, sea: [[0; 20]; 20], visit: [[0; 20]; 20]};

    let mut ans = 0;
    let (mut size, mut ate) = (2, 0);
    let mut cur = P{x: 0, y: 0, d: 0};
    let mut lv = 1;

    for i in 0..n {
        for j in 0..n {
            let mut x = input.next().unwrap();
            if x == 9 {
                cur = P{x: i, y: j, d: 0};
                x = 0;
            }
            map.sea[i][j] = x;
        }
    }

    while let Some(food) = bfs(size, cur, &mut map, lv) {
        lv += 1;
        ate += 1;
        map.sea[food.x][food.y] = 0;
        if size == ate {
            size += 1;
            ate = 0;
        }
        ans += food.d;
        cur = food;
    }

    println!("{}", ans);
}
