// Definition for singly-linked list.
// #[derive(PartialEq, Eq, Clone, Debug)]
// pub struct ListNode {
//   pub val: i32,
//   pub next: Option<Box<ListNode>>
// }
// 
// impl ListNode {
//   #[inline]
//   fn new(val: i32) -> Self {
//     ListNode {
//       next: None,
//       val
//     }
//   }
// }
impl Solution {
    pub fn reverse_k_group(head: Option<Box<ListNode>>, k: i32) -> Option<Box<ListNode>> {

        let k = k as usize;

        if head.is_none() {
            return head;
        }

        let mut v = vec![];
        let mut head = head;
        while let Some(mut node) = head {
            head = node.next.clone();
            node.next = None;
            v.push(node);
        }

        if v.len() < 2 {
            head = Some(v[0].clone());
            return head;
        }

        for i in (0..v.len()).step_by(k) {
            if v.len()-i < k {
                break;
            }
            for j in 0..k/2 {
                v.swap(i+j, i+k-j-1);
            }   
        }

        for i in (1..=v.len()-1).rev() {
            v[i-1].next = Some(v[i].clone());
        }


        Some(v[0].clone())
    }
}