use std::mem::swap;
use std::cmp::{Ordering, max};
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
    
    fn preorder(inorder: &[usize], postorder: &[usize]) {
        if postorder.is_empty() {
            return;
        }
        let &sub_root = postorder.last().unwrap();
        print!("{} ", sub_root);
        if postorder.len() == 1 {
            return;
        }
        let sub_root_idx = inorder
            .iter()
            .position(|&x| x == sub_root)
            .unwrap();

        let left_size = sub_root_idx;
        let right_size = inorder.len() - sub_root_idx - 1;
        if left_size > 0 {
            preorder(&inorder[..sub_root_idx], &postorder[..left_size]);
        }
        if right_size > 0 {
            preorder(&inorder[sub_root_idx + 1..], &postorder[left_size..left_size + right_size]);
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

    preorder(&inorder[..], &postorder[..]);
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