impl Solution {
    pub fn max_operations(nums: Vec<i32>, k: i32) -> i32 {

        let mut nums = nums;
        nums.sort();
        let mut used = vec![false; nums.len()];

        let mut ans = 0;

        for i in 0..nums.len() {
            if used[i] { continue; }

            let diff = k-nums[i];
            let mut l_bound = lower_bound(&nums[i+1..], diff);
            let mut h_bound = upper_bound(&nums[i+1..], diff);

            if h_bound - l_bound == 0 {
                used[i] = true;
                continue;
            }

            while l_bound < h_bound && used[h_bound+i-1] {
                h_bound -= 1;
            }

            if l_bound < h_bound {
                used[h_bound+i-1] = true;
                ans += 1;
            }

            used[i] = true;

        }

        ans

    }


}

fn lower_bound(nums: &[i32], k: i32) -> usize {
    let mut lo = -1;
    let mut hi = nums.len() as i32;

    while (lo + 1) < hi {
        let mid = (lo + hi) / 2;

        if nums[mid as usize] < k {
            lo = mid;
        } else {
            hi = mid;
        }
    }
    hi as usize
}

fn upper_bound(nums: &[i32], k: i32) -> usize {
    let mut lo = -1;
    let mut hi = nums.len() as i32;

    while (lo + 1) < hi {
        let mid = (lo + hi) / 2;

        if nums[mid as usize] <= k {
            lo = mid;
        } else {
            hi = mid;
        }
    }
    hi as usize
}