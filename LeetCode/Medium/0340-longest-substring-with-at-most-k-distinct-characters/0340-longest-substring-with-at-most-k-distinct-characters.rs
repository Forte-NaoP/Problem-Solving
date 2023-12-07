impl Solution {
    pub fn length_of_longest_substring_k_distinct(s: String, k: i32) -> i32 {
        use std::collections::HashMap;
        
        let mut cnt = HashMap::new();
        let (mut max_len, mut new_char) = (0, 0);
        let mut chars = s.chars().collect::<Vec<char>>();

        for c in s.chars() {
            cnt.entry(c).or_insert(0);
        }
        
        let (mut i, mut j) = (0, 0);

        while i <= j && j < s.len() {

            if cnt[&chars[j]] == 0 {
                new_char += 1;
            }
            cnt.entry(chars[j]).and_modify(|counter| *counter += 1);

            j += 1;
            while new_char > k {
                cnt.entry(chars[i]).and_modify(|counter| *counter -= 1);
                if cnt[&chars[i]] == 0 {
                    new_char -= 1;
                }
                i += 1;
            }
            max_len = std::cmp::max(max_len, (j-i) as i32);
        }
        
        max_len
    }
}