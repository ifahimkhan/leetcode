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
// 0. init
//           1------>2----->3->4->5->NULL
//          trav    
// 1. grab a pointer to next (2)
// NULL      1------>2----->3->4->5->NULL
// prev     trav    next
// 2. rewire the link
// NULL<-----1       2----->3->4->5->NULL
// prev     trav    next
// 3. advance         
// NULL<-----1       2----->3->4->5->NULL
//          prev    next
//                  trav
// 1. grab a pointer to next (3)        
// NULL<-----1       2----->3->4->5->NULL
//          prev    trav   next
// 2. rewire the link
// NULL<-----1<-------2      3->4->5->NULL
//          prev    trav   next
// 3. advance (order: prev->next then trav->next)
// NULL<-----1<-------2      3->4->5->NULL
//                  prev    next
//                          trav
// 1. grab a pointer to next (3)        
//                 4        5----->NULL
//                prev    trav   next
// 2. rewire the link
//                 4<-------5      NULL
//                prev    trav   next
// 3. advance (order: prev->next then trav->next)
//                 4<-------5      NULL
//                                 next
//                         prev    trav


class Solution {
public:
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
};

//     1---->2---->..5--->nullptr
//    node       

// duty of myself:
// basecase:
//     if i have no next, i will return my self
// work:
//     1. ask my next to do them same as me
//         f(node->next)
//     2. to ask my next to point at me
//         node->next->next = node;
//     3. have myself points to nullptr
// return:
//     return the node from recurrsive call


// class Solution {
// public:
//     ListNode* reverseList(ListNode* head) {
//         if (not head or not head->next) return head;
//         ListNode *node = reverseList(head->next);
//         head->next->next = head;
//         head->next = nullptr;
//         return node;
//     }
// };
