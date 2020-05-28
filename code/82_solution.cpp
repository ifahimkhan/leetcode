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

//  1---->2---->3---->3---->4---->4---->5
// prev  trav   next  
// trav.val != next.val -> advance
//  1---->2---->3---->3---->4---->4---->5
//       prev  trav   next  
// trav.val == next.val  entering duplicated subsequence
// want to get out asap
//  1---->2---->3---->3---->4---->4---->5
//       prev              trav   next  
// then do the short
//        -------------------|
//        |                  V
//  1---->2      3---->3---->4---->4---->5
//        prev              trav   next  
//                 head
// null 1---->1---->2
// prev            trav

class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode *prev=nullptr, *trav=head;
        while (trav and trav->next) {
            if (trav->val != trav->next->val) {
                prev = trav;
                trav = trav->next;
            } else {
                while (trav->next and trav->val == trav->next->val)
                    trav = trav->next;
                trav = trav->next;
                if (prev) 
                    prev->next = trav;
                else 
                    head = trav;
            }
        }
        return head;
    }
};

//   1---->2---->3---->3---->4---->4---->5
// node    
// basecase node has no next return itself
// 1. node.val != node.next.val
//     node.next = f(node.next)
//   1---->2---->3---->3---->4---->4---->5
//                                      node          
// 2. node.val == node.next.val
//     advance node to be out side the subsequence of repetition
//     return f(node)

class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        if (not head or not head->next) return head;
        if (head->next and head->val == head->next->val) {
            while (head->next and head->val == head->next->val) 
                head = head->next;
            head = head->next;
            return deleteDuplicates(head);
        } else 
            head->next = deleteDuplicates(head->next);
        return head;
    }
};