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
class Solution {
    ListNode* reverseList(ListNode* head) {
        ListNode *prev=nullptr, *trav=head, *next;
        while (trav) {
            next = trav->next;
            trav->next = prev;
            prev = trav;
            trav = next;
        }
        return prev;
    }    
public:
    ListNode* plusOne(ListNode* head) {
        head = reverseList(head);
        ListNode *trav=head;
        int carry = 0;
        trav->val++; // change to other values if problem changes
        while (trav) {
            carry += trav->val;
            trav->val = carry % 10;
            carry /= 10;
            if (not trav->next and carry) trav->next = new ListNode(0);
            trav = trav->next;
        }
        return reverseList(head);
    }
};