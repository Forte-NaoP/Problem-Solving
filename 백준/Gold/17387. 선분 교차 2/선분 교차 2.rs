use std::io::{stdin, Read};
use std::cmp::{min, max};

pub fn ccw(a: &Vec<i64>, b: &Vec<i64>, c: &Vec<i64>) -> i64 {
    let _ccw = a[0]*b[1]+b[0]*c[1]+c[0]*a[1] - (b[0]*a[1]+c[0]*b[1]+a[0]*c[1]);
    if _ccw > 0 {
        1
    } else if _ccw == 0 {
        0
    } else {
        -1
    }
}

fn main() {
    let mut points: Vec<Vec<i64>> = vec![];

    for line in stdin().lines() {
        if let Ok(line) = line {
            let ab = line.split_ascii_whitespace()
                    .filter_map(|s| s.parse().ok())
                    .collect::<Vec<i64>>();
            points.push(ab[0..2].to_vec());
            points.push(ab[2..].to_vec());
        }
    }

    let abc = ccw(&points[0], &points[1], &points[2]);
    let abd = ccw(&points[0], &points[1], &points[3]);
    let cda = ccw(&points[2], &points[3], &points[0]);
    let cdb = ccw(&points[2], &points[3], &points[1]);

    if abc*abd == 0 && cda*cdb == 0 {
        if min(points[0][0], points[1][0]) <= max(points[2][0], points[3][0]) &&
            min(points[2][0], points[3][0]) <= max(points[0][0], points[1][0]) &&
            min(points[0][1], points[1][1]) <= max(points[2][1], points[3][1]) &&
            min(points[2][1], points[3][1]) <= max(points[0][1], points[1][1]) {
                println!("1");
            } else {
                println!("0");
            }
    } else {
        if abc*abd <= 0 && cda*cdb <= 0 {
            println!("1");
        } else {
            println!("0");
        }
    }

}