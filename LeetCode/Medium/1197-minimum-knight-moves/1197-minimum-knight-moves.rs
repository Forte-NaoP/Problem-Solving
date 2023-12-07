use std::collections::VecDeque;

impl Solution {
    pub fn min_knight_moves(x: i32, y: i32) -> i32 {
        let mut arr = vec![vec![999; 601]; 601];
        let mut visit = vec![vec![false; 601]; 601];
        let mut queue = VecDeque::new();
        let knight = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)];
        
        let (x, y) = (x+300,  y+300);
        
        queue.push_back((0, x, y));
        visit[x as usize][y as usize] = true;

        while !queue.is_empty() {
            let (d, r, c) = queue.pop_front().unwrap();
            if d < arr[r as usize][c as usize] {
                arr[r as usize][c as usize] = d;
            }
            for (mr, mc) in knight.iter() {
                let (nr, nc) = (r+mr, c+mc); 
                if Solution::range_check(r+mr, c+mc) && !visit[nr as usize][nc as usize] {
                    queue.push_back((d+1, nr, nc));
                    visit[nr as usize][nc as usize] = true;
                }
            }
        }
        arr[300][300]
    }
    
    pub fn range_check(x: i32, y: i32) -> bool {
        (0 <= x && x <= 600 && 0 <= y && y <= 600) && x.abs()+y.abs() <= 900
    }
    
}