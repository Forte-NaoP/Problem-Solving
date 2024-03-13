use std::io::{stdin, stdout, Read, Write, BufReader, BufWriter};
use std::fs::File;
use std::collections::{BinaryHeap, HashMap};
use std::cmp::*;

fn main() {
    let mut reader = BufReader::new(stdin());
    
    let mut input = String::new();
    reader.read_to_string(&mut input).unwrap();
    let mut input = input.split_ascii_whitespace().flat_map(str::parse::<usize>);

    let (v, e) = (input.next().unwrap(), input.next().unwrap());
    let k = input.next().unwrap();

    let mut graph = vec![HashMap::<usize, usize>::new(); 20001];
    for _ in 0..e {
        let (_u, _v, _w) = (input.next().unwrap(), input.next().unwrap(), input.next().unwrap());
        graph[_u].entry(_v).and_modify(|e| {
            *e = min(*e, _w);
        }). or_insert(_w);
    }
    let max_dist = 99999999_usize;
    let mut dist = vec![max_dist; 20001];
    let mut pq = BinaryHeap::<Reverse<(usize, usize)>>::new();

    dist[k] = 0;
    pq.push(Reverse((0, k)));

    while let Some(Reverse((cost, cur))) = pq.pop() {
        if cost > dist[cur] {
            continue;
        }

        if let Some(connected) = graph.get(cur) {
            for (&nxt_node, &nxt_dist) in connected {
                let nxt_cost = nxt_dist + cost;
                if dist[nxt_node] > nxt_cost {
                    dist[nxt_node] = nxt_cost;
                    pq.push(Reverse((nxt_cost, nxt_node)));
                }
            }
        }
    }

    for i in 1..=v {
        if dist[i] == max_dist {
            println!("INF");
        } else {
            println!("{}", dist[i]);
        }
    }
}
