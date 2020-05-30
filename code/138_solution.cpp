/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/ 

//          V
//    next    next
// [1]---->[2]---->[3]
//  ^       |
//  |-------|
//   random     

// Two pass
// 1. create copy with correct next links, 
//     also create mapping from old to new
//    next    next
// [1]---->[2]---->[3]
// 2. traverse the two lists at same pace
//    when we see a random pointer in the old, 
//    we set new->random = mapping[old->random]
class Solution {
public:
    Node* copyRandomList(Node* head) {
        if (not head) return head;
        Node *trav = head, *dummy=new Node(0), *copy=dummy;
        unordered_map<Node*, Node*> old_to_new;
        // first pass, create a copy with correct next links
        while (trav) {
            copy->next = new Node(trav->val);
            copy = copy->next;
            old_to_new[trav] = copy;
            trav = trav->next;
        }
        // second pass to fix the random pointers
        trav = head;
        copy = dummy->next;
        while (trav) {
            if (trav->random) copy->random = old_to_new[trav->random];
            trav = trav->next;
            copy = copy->next;
        }
        return dummy->next;
    }
};

//    next    net
// [1]---->[2]---->[3]
//  ^       |
//  |-------|
//   random     

// 1. insert a copy between old and old->next.
// [1]---->[1']----->[2]----->[2']----->[3]---->[3']
//  ^                 |
//  |-----------------|
//      random    

// 2. for node with random pointer
//     old->next->random = old->random->next
//      2    2'              2     1      1'
//          |-------------------|
//          V                   |
// [1]---->[1']----->[2]----->[2']----->[3]---->[3']
//  ^                 |
//  |-----------------|
//      random    
// 3. split the linked list
//   odd nodes are the old list
//   even nodes are the new list
class Solution {
public:
    Node* copyRandomList(Node* head) {
        if (not head) return head;
        Node *trav=head, *copy, *new_head;
        // 1 pass insert copy
        while (trav) {
            copy = new Node(trav->val);
            copy->next = trav->next;
            trav->next = copy;
            trav = copy->next;
        }
        // 2 pass to fix the random pointer
        trav = head;
        while (trav) {
            if (trav->random) trav->next->random = trav->random->next;
            trav = trav->next->next;
        }
        // 3 pass to split the list into odd even lists
        trav = head;
        copy = head->next;
        new_head = head->next;
        while (trav) {
            trav->next = trav->next->next;
            copy->next = copy->next ? copy->next->next : nullptr;
            trav = trav->next;
            copy = copy->next;
        }
        return new_head;
    }
};