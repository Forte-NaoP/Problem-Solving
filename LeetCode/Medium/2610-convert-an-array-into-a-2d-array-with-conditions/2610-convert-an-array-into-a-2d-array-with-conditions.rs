impl Solution {
    pub fn find_matrix(nums: Vec<i32>) -> Vec<Vec<i32>> {
        let mut cnt_num = vec![0; 201];
        for num in nums {
            cnt_num[num as usize] += 1;
        }

        let max_group = cnt_num.iter().max().unwrap();
        let mut ans = vec![vec![]; *max_group as usize];
        for i in 0..201 {
            for j in 0..cnt_num[i] {
                ans[j as usize].push(i as i32);
            }
        }
        return ans;
    }
}
