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
private:
    ListNode* middleNode(ListNode* head) {
        ListNode *slow=head, *fast=head;
        while (fast and fast->next) {
            slow = slow->next;
            fast = fast->next->next;
        }
        return slow;
    }
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
    bool isPalindrome(ListNode* head) {
        ListNode *mid = reverseList(middleNode(head));
        ListNode *h1 = head, *h2 = mid;
        while (h1 and h2 and h1 != h2) {
            if (h1->val != h2->val) {
                reverseList(mid);
                return false;
            } else {
                h1 = h1->next;
                h2 = h2->next;
            }
        }
        reverseList(mid);
        return true;
    }
};