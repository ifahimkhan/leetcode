/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;

    Node() {}

    Node(int _val) {
        val = _val;
        next = NULL;
    }

    Node(int _val, Node* _next) {
        val = _val;
        next = _next;
    }
};
*/
class Solution {
public:
    Node* insert(Node* head, int insertVal) {
        if (not head) {
            Node *node = new Node(insertVal);
            node->next = node;
            return node;
        }

        Node *prev=head, *trav=head->next;
        while (trav != head) {
            if (prev->val <= insertVal and insertVal <= trav->val) break;
            if (prev->val > trav->val and insertVal >= prev->val) break;
            if (prev->val > trav->val and insertVal <= trav->val) break;
            prev = trav;
            trav = trav->next;
        }
        prev->next = new Node(insertVal, trav);
        return head;
    }
};
