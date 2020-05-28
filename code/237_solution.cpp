/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
// 0. init
// 1--->2--->3--->4
//     node next
// 1. copy next value to node
// 1--->3--->3--->4
//     node next
// 2. short the link
//      ___________
//      |         |
//      |         V
// 1--->3    3--->4
//     node next
class Solution {
public:
    void deleteNode(ListNode* node) {
        node->val = node->next->val;
        node->next = node->next->next;
    }
};