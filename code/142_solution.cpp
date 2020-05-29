/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
//                   fast catch up with slow here 
//                   V
//               x-.-x
// h            /     \
// x---x-.-x---x <-r   x
//              \     /
//               x---x

// l links before cycle
// c links inside cycle
// t links from cycle start to catch up

// slow moved l+t    links 
// fast moved 2(l+t) = l + t + ?*c

// l + t = + ?c
// l = ?c - t
// so if we have a new runner starting from head,
// when it reach the start of the cycle, the slow would meet it there. 
// because l+t +?c - t = l + ?c

class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
        ListNode *slow=head, *fast=head;
        while (fast and fast->next) {
            slow = slow->next;
            fast = fast->next->next;
            if (slow == fast) break;
        }
        if (not fast or not fast->next) return nullptr;
        while (head != slow) {
            head = head->next;
            slow = slow->next;
        }            
        return slow;
    }
};