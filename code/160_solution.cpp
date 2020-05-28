/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */

// AACCCBBB | C
// BBBCCCAA | C

class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        ListNode *travA=headA, *travB=headB;
        while (travA != travB) {
            travA = travA ? travA->next : headB;
            travB = travB ? travB->next : headA;
        }
        return travA;
    }
};