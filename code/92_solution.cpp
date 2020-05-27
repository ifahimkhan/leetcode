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

// init 1->2->3->4->5->NULL
// 1. move to start point, grab some pointer
//       trav
//         V
//      1->2->3->4->5->NULL
//      ^  ^
//         tail (tail node for the reversal section)
//     last (last node prior to the reversal section)
// 2. reverse the section reverse(n-m) of pointer
//              prev
//               V 
//      1  2<-3<-4  5->NULL    
//      ^           ^
//     last        trav
// 3. make sure rewiring is all correct
//     last->prev
//     tail->trav
//     if last is nullptr return prev else return last
// final 1->4->3->2->5->NULL

class Solution {
public:
    ListNode* reverseBetween(ListNode* head, int m, int n) {
        ListNode *prev=nullptr, *trav=head, *last, *tail, *next;
        int k = n - m + 1;
        // move to the mth node
        while (m>1) {
            prev = trav;
            trav = trav->next;
            m--;
        } 
        last = prev;
        tail = trav;
        // reverse nodes between m and n
        while (k) {
            next = trav->next;
            trav->next = prev;
            prev = trav;
            trav = next;
            k--;
        }
        // make sure the connection is right
        if (last) last->next = prev;
        tail->next = trav;
        return last ? head : prev;
    }
};
