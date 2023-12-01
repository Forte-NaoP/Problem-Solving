impl Solution {
    pub fn my_atoi(s: String) -> i32 {
        
        let trim = s.trim();
        let mut ans: i64 = 0;
        let mut sign: i64 = 0;

        for (i, c) in trim.chars().enumerate() {
            if !c.is_digit(10) {
                match i {
                    0 => match c {
                        '-' => sign = -1,
                        '+' => sign = 1,
                        _ => break,
                    },
                    _ => break,
                }
            } 
        }

        let skip = match sign {
            0 => 0,
            _ => 1,
        };

        sign = match sign {
            0 => 1,
            _ => sign,
        };

        let trim = trim.chars().skip(skip).skip_while(|c| c == &'0').collect::<String>();
        let len = trim.chars().position(|c| !c.is_digit(10)).unwrap_or(trim.len());

        if len > 10 {
            return match sign {
                -1 => i32::MIN,
                _ => i32::MAX
            };
        }

        for(i, c) in trim.chars().enumerate() {
            if !c.is_digit(10) {
                break;
            }
            ans += sign * c.to_digit(10).unwrap() as i64 * 10_i64.pow((len-i) as u32-1);
        }

        return match ans {
            _ if ans > i32::MAX as i64 => i32::MAX,
            _ if ans < i32::MIN as i64 => i32::MIN,
            _ => ans as i32,
        };
        
    }
}