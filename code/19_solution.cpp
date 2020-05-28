/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

// n = 2
// init
// s
// d
//   f
//   1->2->3->4->5->null
// 1. advance fast by two links
// s
// d
//         f
//   1->2->3->4->5->null
// 2. advance fast and slow at the same speed until fast is null
//         s
//         d
//                   f
//   1->2->3->4->5->null
// 3. short slow.next
//         s
//         d         f
//   1->2->3  4->5->null
//         |     ^
//         |_____|

class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode *fast=head, *slow=new ListNode(), *dummy=slow;
        dummy->next = head;
        while (fast and n) {
            fast = fast->next;
            n--;
        }
        
        while (fast) {
            slow = slow->next;
            fast = fast->next;
        }
        slow->next = slow->next->next;
        return dummy->next;
    }
};