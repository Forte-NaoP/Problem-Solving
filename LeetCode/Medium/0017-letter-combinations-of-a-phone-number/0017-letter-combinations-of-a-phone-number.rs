use std::collections::HashMap;

impl Solution {
    pub fn letter_combinations(digits: String) -> Vec<String> {
        if digits.len() < 1 {
            return vec![];
        }
        
        let keypad = HashMap::from([
            ('2', "abc"), ('3', "def"), ('4', "ghi"),
            ('5', "jkl"), ('6', "mno"), ('7', "pqrs"),
            ('8', "tuv"), ('9', "wxyz"),
        ]);
        let mut ans = vec![];
        Solution::_letter_combinations(&keypad, digits.as_str(), "".to_string(), ans.as_mut());
        ans
    }

    fn _letter_combinations(keypad: &HashMap<char, &str>, digit: &str, mut comb: String, comb_vec: &mut Vec<String>) {
        for letter in keypad.get(&digit.chars().nth(0).unwrap()).unwrap().chars() {
            comb.push(letter);
            if digit.len() > 1 {
                Solution::_letter_combinations(keypad, &digit[1..], comb.to_owned(), comb_vec);
            } else {
                comb_vec.push(comb.to_owned());
            }
            comb.pop();
        }
    }
}