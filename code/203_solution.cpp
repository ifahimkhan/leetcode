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

// val = 2
//  ?----->2---->3---->4
// prev trav

// short trav if trav.val == val
// else advance both prev and trav

class Solution {
public:
    ListNode* removeElements(ListNode* head, int val) {
        ListNode *dummy=new ListNode(), *prev=dummy, *trav=head;
        dummy->next = head;
        while (trav) {
            if (trav->val == val) prev->next = trav->next;
            else prev = trav;
            trav = trav->next;
        }
        return dummy->next;
    }
};