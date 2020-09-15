/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* left;
    Node* right;
    Node* parent;
};
*/

class Solution {
public:
    Node* inorderSuccessor(Node* node) {
        // inorder: left sub -> node -> right sub
        
        // has right sub tree
        // successor is left most leaf child in query node's right sub tree
        if (node->right) {
            node = node->right;
            while (node->left) node = node->left;
            return node;
        }
        
        // has no right sub tree
        // successor is a parent node which the query node is in its left subtree
        while (node->parent and node == node->parent->right) node = node->parent;
        return node->parent;
    }
};
