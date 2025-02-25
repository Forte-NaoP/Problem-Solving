use std::mem::swap;
use std::cmp::{Ordering, max};
use std::collections::HashMap;
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
    
    fn preorder(in_pos: &HashMap<usize, usize>, 
        inorder: &[usize], 
        postorder: &[usize], 
        in_l: usize, 
        in_r: usize, 
        post_l: usize, 
        post_r: usize
    ) {
        if post_l > post_r {
            return;
        }
    
        let sub_root = postorder[post_r];
        print!("{} ", sub_root);
    
        let sub_root_idx = in_pos[&sub_root];
        let left_size = sub_root_idx - in_l;
        let right_size = in_r - sub_root_idx;
    
        if left_size > 0 {
            preorder(in_pos, inorder, postorder, in_l, sub_root_idx - 1, post_l, post_l + left_size - 1);
        }
    
        if right_size > 0 {
            preorder(in_pos, inorder, postorder, sub_root_idx + 1, in_r, post_l + left_size, post_r - 1);
        }
    }

    let n = next!(usize);
    let mut inorder = vec![];
    let mut postorder = vec![];
    for _ in 0..n {
        inorder.push(next!(usize));
    }
    for _ in 0..n {
        postorder.push(next!(usize));
    }

    let in_pos: HashMap<usize, usize> = inorder
        .iter()
        .enumerate()
        .map(|(idx, &val)| (val, idx))
        .collect();

    preorder(&in_pos, &inorder, &postorder, 0, n - 1, 0, n - 1);
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