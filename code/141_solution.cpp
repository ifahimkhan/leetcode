/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */           
//               f
//               x---x
//              /     \
// x---x---x---x s     x
//              \     /
//               x---x
              
// s/f
// s move 1 link / iteration
// f move 2 links/ iteration

// after 5 iteration            
//               x---x
//              /     \
// x---x---x---x       x 
//              \     /
//               x---x
//               s/f    
// O(n)
class Solution {
public:
    bool hasCycle(ListNode *head) {
        ListNode *slow=head, *fast=head;
        while (fast and fast->next) {
            slow = slow->next;
            fast = fast->next->next;
            if (slow == fast) return true;
        }
        return false;
    }
};