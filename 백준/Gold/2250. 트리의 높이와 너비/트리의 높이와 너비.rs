use std::mem::swap;
use std::cmp::{max, min, Ordering};
use std::collections::{HashMap, VecDeque, BinaryHeap};
use std::pin::Pin;
use std::{default, i32, usize, vec};
use std::{
    io::{Write, BufWriter, StdoutLock}, cell::RefCell
};

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

    let n = next!(usize);
    let mut tree = [[0, 0]; 10001];
    let mut sub_size = [[0, 0]; 10001];
    let mut col = [0; 10001];
    let mut cnt = [0; 10001];

    for _ in 0..n {
        let (u, l, r) = next!(usize, i32, i32);
        if l != -1 {
            cnt[l as usize] += 1; 
            tree[u][0] = l as usize;
        }

        if r != -1 {
            cnt[r as usize] += 1; 
            tree[u][1] = r as usize;
        }
    }

    let mut root = 0;
    for i in 1..=n {
        if cnt[i] == 0 {
            root = i;
            break;
        }
    }

    // println!("{}", root);

    fn dfs(cur: usize, tree: &[[usize; 2]; 10001], sub_size: &mut [[i32; 2]; 10001]) -> i32 {
        if tree[cur][0] != 0 {
            sub_size[cur][0] = dfs(tree[cur][0], tree, sub_size);
        }

        if tree[cur][1] != 0 {
            sub_size[cur][1] = dfs(tree[cur][1], tree, sub_size);
        }

        sub_size[cur][0] + sub_size[cur][1] + 1
    }

    dfs(root, &tree, &mut sub_size);

    fn place(cur: usize, l: usize, r: usize, 
        tree: &[[usize; 2]; 10001], 
        sub_size: &[[i32; 2]; 10001], 
        col: &mut [usize; 10001]
    ) {
        let mid = l + sub_size[cur][0] as usize;
        col[cur] = mid;

        if tree[cur][0] != 0 {
            place(tree[cur][0], l, mid - 1, tree, sub_size, col);
        }

        if tree[cur][1] != 0 {
            place(tree[cur][1], mid + 1, r, tree, sub_size, col);
        }
    }

    place(root, 1, n, &tree, &sub_size, &mut col);

    // for i in 1..=n {
    //     println!("{}: {} {} {}", i, sub_size[i][0], sub_size[i][1], col[i]);
    // }

    let mut level = VecDeque::new();
    level.push_back(root);

    let (mut l, mut r) = (n, 1);
    let mut cur_level = 1;
    let mut ans = 0;
    let mut width = 0;
    while !level.is_empty() {
        let level_size = level.len();
        l = n;
        r = 1;
        for _ in 0..level_size {
            let cur = level.pop_front().unwrap();
            l = l.min(col[cur]);
            r = r.max(col[cur]);
            if tree[cur][0] != 0 {
                level.push_back(tree[cur][0]);
            }
            if tree[cur][1] != 0 {
                level.push_back(tree[cur][1]);
            }
        }
        if width < r - l + 1 {
            width = r - l + 1;
            ans = cur_level;
        }
        cur_level += 1;
    }

    println!("{} {}", ans, width);
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
        });
    };
}

#[macro_export]
macro_rules! print {
    ($($t:tt)*) => {
        STDOUT.with(|refcell| {
            use std::io::*;
            write!(refcell.borrow_mut(), $($t)*).unwrap();
        });
    };
}