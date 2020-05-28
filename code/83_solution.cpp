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

// iterative
//  1---->1---->2
// trav  next   

//  ------------|
//  |           V
//  1     1---->2
// trav  next   

//  ------------|
//  |           V
//  1     1---->2
//             trav  next   

class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode *trav = head;
        while (trav and trav->next) {
            if (trav->val != trav->next->val) 
                trav = trav->next;
            else 
                trav->next = trav->next->next;
        }
        return head;
    }
};
    
// rescurrsive
//     1---->1---->2
//    node

// basecase terminal node / nullptr return self.

// 1. if node.val == node.next.val
//     i want to give myself up and return f(node.next)
// 2. if node.val != node.next.val
//     i want to connect myself to f(node.next)
   
class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        if (not head or not head->next) return head;
        if (head->val == head->next->val) 
            return deleteDuplicates(head->next);
        else 
            head->next = deleteDuplicates(head->next);
        return head;
    }
};

