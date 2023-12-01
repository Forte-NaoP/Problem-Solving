use std::collections::HashMap;

impl Solution {
    pub fn group_strings(strings: Vec<String>) -> Vec<Vec<String>> {
        
        let mut len_dict: HashMap<usize, Vec<String>> = HashMap::new();
        for string in strings {
            let len = string.len();
            len_dict.entry(len).or_insert(vec![]).push(string);
        }

        let mut ans = vec![];

        for (_, strings) in len_dict.iter() {
            let mut shift_seq_dict: HashMap<String, Vec<String>> = HashMap::new();
            for string in strings.iter().map(|s| s.chars().collect::<Vec<char>>()) {
                let mut shift_seq = String::from("0");
                for i in 1..string.len() {
                    let diff = (string[i] as i32 - string[i-1] as i32 + 26) % 26;
                    shift_seq.push_str(diff.to_string().as_str());
                }
                shift_seq_dict.entry(shift_seq).or_insert(vec![]).push(string.iter().collect());
            }
            for strs in shift_seq_dict.into_values() {
                ans.push(strs);
            }
        }
        ans
    }
}
