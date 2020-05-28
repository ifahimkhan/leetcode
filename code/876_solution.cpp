/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* middleNode(ListNode* head) {
        // two pass
        // ListNode *node = head;
        // int n;
        // for (n=0;node;n++) node=node->next;
        // node = head;
        // for (int i=0;i<n/2;i++) node=node->next;
        // return node;

        // one pass
        ListNode *slow=head, *fast=head;
        while (fast and fast->next) {
            slow = slow->next;
            fast = fast->next->next;
        }
        return slow;
    }
};