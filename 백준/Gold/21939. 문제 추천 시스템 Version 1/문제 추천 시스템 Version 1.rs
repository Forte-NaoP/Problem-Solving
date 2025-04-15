use std::cell::Ref;
use std::iter::Rev;
use std::mem::swap;
use std::cmp::{max, min, Ordering, Reverse};
use std::collections::{BinaryHeap, HashMap, HashSet, VecDeque, BTreeSet};
use std::pin::Pin;
use std::{default, i32, usize, vec};
use std::{
    io::{Write, BufWriter, StdoutLock}, cell::RefCell
};
use std::rc::{Rc, Weak};
use std::ops::Bound::{Included, Excluded, Unbounded};

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

    #[derive(PartialEq, Eq, Clone, Copy, Default)]
    struct Problem {
        id: i32,
        lv: usize,
        tag: usize,
    }

    impl Ord for Problem {
        fn cmp(&self, other: &Self) -> Ordering {
            self.lv.cmp(&other.lv)
                .then_with(|| self.id.cmp(&other.id))
        }
    }
    
    impl PartialOrd for Problem {
        fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
            Some(self.cmp(other))
        }
    }

    let mut division = vec![BTreeSet::<Problem>::new(); 101];
    let mut problems = vec![Problem::default(); 100001];

    let n = next!(usize);
    for _ in 0..n {
        let (id, lv) = next!(usize, usize);
        let p = Problem { id: id as i32, lv, tag: 0 };
        division[0].insert(p);
        problems[id] = p;
    }

    let m = next!(usize);
    for _ in 0..m {
        let cmd = next!();
        match cmd {
            "recommend" => {
                // let tag = next!(usize);
                let op = next!(i32);
                
                if op == 1 {
                    println!("{}", division[0].last().unwrap().id);
                } else {
                    println!("{}", division[0].first().unwrap().id);
                }
            },
            "recommend2" => {
                let op = next!(i32);
                let mut ans: Option<Problem> = None;
                match op {
                    1 => {
                        for div in division.iter() {
                            if let Some(&p) = div.last() {
                                ans = Some(match ans {
                                    Some(cur) => cur.max(p),
                                    None => p,
                                });
                            }
                        }
                    },
                    -1 => {
                        for div in division.iter() {
                            if let Some(&p) = div.first() {
                                ans = Some(match ans {
                                    Some(cur) => cur.min(p),
                                    None => p,
                                });
                            }
                        }
                    },
                    _ => unreachable!(),
                }
                println!("{}", ans.map(|p| p.id).unwrap_or(-1));
            },
            "recommend3" => {
                let op = next!(i32);
                let lv = next!(usize);
                let mut ans: Option<Problem> = None;

                match op {
                    1 => {
                        let key = Problem { id: i32::MIN, lv, tag: 0 };

                        for div in division.iter() {
                            if let Some(&p) = div.range((Included(&key), Unbounded)).next() {
                                ans = Some(match ans {
                                    Some(cur) => cur.min(p),
                                    None => p,
                                });
                            }
                        }
                    },
                    -1 => {
                        let key = Problem { id: i32::MIN, lv, tag: 0 };

                        for div in division.iter() {
                            if let Some(&p) = div.range((Unbounded, Excluded(&key))).next_back() {
                                ans = Some(match ans {
                                    Some(cur) => cur.max(p),
                                    None => p,
                                });
                            }
                        }
                    }
                    _ => unreachable!(),
                }
                println!("{}", ans.map(|p| p.id).unwrap_or(-1));
            },
            "add" => {
                let (id, lv) = next!(usize, usize);
                division[0].insert(Problem { id: id as i32, lv, tag: 0 });
                problems[id] = Problem { id: id as i32, lv, tag: 0 };
            },
            "solved" => {
                let id = next!(usize);
                // let tag = problems[id].tag;
                division[0].remove(&problems[id]);
            }
            _ => unreachable!(),
        }
    }

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
        })
    };
}

#[macro_export]
macro_rules! print {
    ($($t:tt)*) => {
        STDOUT.with(|refcell| {
            use std::io::*;
            write!(refcell.borrow_mut(), $($t)*).unwrap();
        })
    };
}