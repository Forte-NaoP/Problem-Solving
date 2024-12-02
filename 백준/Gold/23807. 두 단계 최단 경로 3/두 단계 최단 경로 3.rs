use std::cmp::Reverse;
use std::collections::{BinaryHeap, HashMap};
use std::vec;

fn dijkstra(g: &Vec<Vec<(usize, i64)>>, n: usize, st: usize) -> Vec<i64> {
    let mut dist = vec![i64::MAX; n + 1];
    let mut pq = BinaryHeap::new();
    dist[st] = 0;
    pq.push(Reverse((0, st)));

    while let Some(Reverse((cur_d, cur))) = pq.pop() {
        if cur_d > dist[cur] {
            continue;
        }
        for &(nxt, mut nxt_d) in g[cur].iter() {
            nxt_d += cur_d;
            if dist[nxt] > nxt_d {
                dist[nxt] = nxt_d;
                pq.push(Reverse((nxt_d, nxt)));
            }
        }
    }
    dist
}

struct ProblemParam {
    dist: HashMap<usize, Vec<i64>>,
    st: usize,
    ed: usize,
}

fn permutation(
    mid: &[usize],
    r: usize, 
    p: &ProblemParam
) {
    let mut pick = [0; 3];
    let mut used = [false; 100];

    fn backtrack(
        mid: &[usize],
        r: usize,
        idx: usize,
        pick: &mut [usize],
        used: &mut [bool],
        p: &ProblemParam,
    ) -> i64 {
        if idx == r {
            let d1 = p.dist[&p.st][pick[0]];
            let d2 = p.dist[&pick[0]][pick[1]];
            let d3 = p.dist[&pick[1]][pick[2]];
            let d4 = p.dist[&pick[2]][p.ed];

            if d1 == i64::MAX || d2 == i64::MAX || d3 == i64::MAX || d4 == i64::MAX {
                return i64::MAX;
            }

            return d1 + d2 + d3 + d4;
        }
        let mut res = i64::MAX;
        for i in 0..mid.len() {
            if used[i] {
                continue;
            }
            used[i] = true;
            pick[idx] = mid[i];
            res = std::cmp::min(res, backtrack(mid, r, idx + 1, pick, used, p));
            used[i] = false;
        }
        res
    }

    let res = backtrack(mid, r, 0, &mut pick, &mut used, p);
    if res == i64::MAX {
        println!("{}", -1);
    } else {
        println!("{}", res);
    }
}

fn main() {
    let stdin = std::io::read_to_string(std::io::stdin()).unwrap();
    let mut tokens = stdin.split_whitespace();
    let mut next = || tokens.next().unwrap();
    let mut output = String::new();
    
    let n: usize = next().parse().unwrap();
    let m: usize = next().parse().unwrap();

    let mut g: Vec<Vec<(usize, i64)>> = vec![vec![]; n + 1];
    for _ in 0..m {
        let a: usize = next().parse().unwrap();
        let b: usize = next().parse().unwrap();
        let c: i64 = next().parse().unwrap();
        g[a].push((b, c));
        g[b].push((a, c));
    }

    let st: usize = next().parse().unwrap();
    let ed: usize = next().parse().unwrap();
    let p: usize = next().parse().unwrap();
    let mut mid: Vec<usize> = vec![0; p];
    for i in 0..p {
        mid[i] = next().parse().unwrap();
    }

    let mut dist: HashMap<usize, Vec<i64>> = HashMap::new();
    for &p in mid.iter().chain(std::iter::once(&st)) {
        let result = dijkstra(&g, n, p);
        dist.insert(p, result);
    }

    let param = ProblemParam{dist, st, ed};
    permutation(&mid, 3, &param);
}   
