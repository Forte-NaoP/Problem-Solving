impl Solution {
    pub fn permute(mut nums: Vec<i32>) -> Vec<Vec<i32>> {
        nums.sort();
        let mut ans = vec![];
        ans.push(nums.to_owned());
        while Solution::_next_permutation(&mut nums) {
            ans.push(nums.to_owned());
        }
        ans
    }

    fn _next_permutation(nums: &mut Vec<i32>) -> bool {
        if nums.len() < 2 {
            return false;
        }

        let mut i = nums.len() - 1;
        while i > 0 && nums[i-1] >= nums[i] {
            i -= 1;
        }

        if i == 0 {
            return false;
        }

        let mut j = nums.len() - 1;
        while nums[i-1] >= nums[j] {
            j -= 1;
        }

        nums.swap(i-1, j);
        nums[i..].reverse();

        true
    }
}