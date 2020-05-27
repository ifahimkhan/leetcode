struct MyListNode {
    int val;
    MyListNode *next;
    MyListNode(int x) : val(x), next(NULL) {}
};

class MyLinkedList {
private:
    MyListNode* head;
public:
    MyLinkedList() { head=nullptr;}
    
    MyListNode* getNode(int index) {
        MyListNode* trav = head;
        for (int i=0;i<index and trav;i++) trav=trav->next;
        return index >= 0 ? trav : nullptr;
    }
    
    MyListNode* getTail() {
        MyListNode* trav = head;
        MyListNode* tail = nullptr;
        while (trav) {
            if (not trav->next) tail=trav;
            trav = trav->next;
        }
        return tail;
    }
    
    int get(int index) {
        auto node = getNode(index);
        return node ? node->val : -1;
    }
    
    void addAtHead(int val) {
        MyListNode *node = new MyListNode(val);
        node->next = head;
        head = node;
    }
    
    void addAtTail(int val) {
        if (not head) { addAtHead(val); return; }
        MyListNode *tail = getTail();
        MyListNode *node = new MyListNode(val);
        tail->next = node;
    }
    
    void addAtIndex(int index, int val) {
        if (index == 0) { addAtHead(val); return; }
        MyListNode *prev = getNode(index - 1);
        if (not prev) { return; }
        MyListNode *node = new MyListNode(val);
        MyListNode *next = prev->next;
        node->next = next;
        prev->next = node;
    }

    void deleteAtIndex(int index) {
        MyListNode *node = getNode(index);
        if (not node) { return; }
        
        MyListNode *prev = getNode(index-1);
        if (prev) prev->next = node->next; 
        else head = node->next;
    }
};

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * MyLinkedList* obj = new MyLinkedList();
 * int param_1 = obj->get(index);
 * obj->addAtHead(val);
 * obj->addAtTail(val);
 * obj->addAtIndex(index,val);
 * obj->deleteAtIndex(index);
 */
