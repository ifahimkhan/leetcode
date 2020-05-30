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
public:
    ListNode* rotateRight(ListNode* head, int k) {
        if (not head or not head->next) return head;
        ListNode *trav = head, *tail, *prev;
        
        // count node, grab tail, make cycle
        int n = 1;
        while (trav->next) {
            trav = trav->next;
            n++;
        }
        tail = trav;
        tail->next = head;
        
        // find split point
        trav = head;        
        k %= n;
        while (k < n) {
            prev = trav;
            trav = trav->next;
            k++;
        }
        
        // split
        prev->next = nullptr;
        return trav;
    }
};