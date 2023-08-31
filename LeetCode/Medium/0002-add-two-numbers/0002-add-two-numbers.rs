impl Solution {
    pub fn add_two_numbers(l1: Option<Box<ListNode>>, l2: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut head = None;
        let mut cur = &mut head;

        let mut cur1 = &l1;
        let mut cur2 = &l2;

        let mut carry = 0;
        while let (Some(n1), Some(n2)) = (cur1.as_ref(), cur2.as_ref()) {
            let mut x = n1.val + n2.val + carry;
            carry = x / 10;
            x %= 10;

            let node = Box::new(ListNode::new(x));
            *cur = Some(node);
            cur = &mut cur.as_mut().unwrap().next;

            cur1 = &n1.next;
            cur2 = &n2.next;
        }

        while let Some(n1) = cur1.as_ref() {
            let mut x = n1.val + carry;
            carry = x / 10;
            x %= 10;

            let node = Box::new(ListNode::new(x));
            *cur = Some(node);
            cur = &mut cur.as_mut().unwrap().next;

            cur1 = &n1.next;
        }

        while let Some(n2) = cur2.as_ref() {
            let mut x = n2.val + carry;
            carry = x / 10;
            x %= 10;

            let node = Box::new(ListNode::new(x));
            *cur = Some(node);
            cur = &mut cur.as_mut().unwrap().next;

            cur2 = &n2.next;
        }
        
        if carry == 1 {
            let node = Box::new(ListNode::new(carry));
            *cur = Some(node);
            cur = &mut cur.as_mut().unwrap().next;
        }
        
        head

    }
}
