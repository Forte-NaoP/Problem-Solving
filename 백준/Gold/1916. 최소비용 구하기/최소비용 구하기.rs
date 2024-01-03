use std::io::{stdin, stdout, Read, Write, BufWriter};
use std::collections::{binary_heap, BinaryHeap};
use std::cmp::Ordering;

#[derive(Clone, Copy, PartialEq, Eq)]
struct Edge {
    cost: usize,
    node: usize,
}

impl Ord for Edge {
    fn cmp(&self, other: &Self) -> Ordering {
        other.cost.cmp(&self.cost)
            .then_with(|| self.node.cmp(&other.node))
    }
}

impl PartialOrd for Edge {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        Some(self.cmp(other))
    }
}

fn main(){
    let mut input = String::new();
    stdin().read_to_string(&mut input).unwrap();
    let mut input = input.split_ascii_whitespace().flat_map(str::parse::<usize>);

    let (n, m) = (input.next().unwrap(), input.next().unwrap());
    let mut dist = vec![2147483647; n+1];
    let mut bus: Vec<Vec<Edge>> = vec![vec![]; n+1];

    for _ in 0..m {
        let (s, t, d) = (input.next().unwrap(), input.next().unwrap(), input.next().unwrap());
        bus[s].push(Edge { cost: d, node: t })
    }

    let (s, t) = (input.next().unwrap(), input.next().unwrap());
    let mut pq = BinaryHeap::new();
    pq.push(Edge { cost: 0, node: s});
    dist[s] = 0;

    while !pq.is_empty() {
        let cur = pq.pop().unwrap();
        if cur.cost > dist[cur.node] {
            continue;
        }

        for nxt in bus[cur.node].iter() {
            if dist[nxt.node] > nxt.cost+cur.cost {
                pq.push(Edge { cost: nxt.cost+cur.cost, node: nxt.node });
                dist[nxt.node] = nxt.cost+cur.cost;
            }
        }
    }

    let stdout = stdout();
    let mut writer = BufWriter::new(stdout);

    writeln!(writer, "{}", dist[t]).unwrap();

} 