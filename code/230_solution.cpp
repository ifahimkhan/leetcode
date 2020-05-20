/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int kthSmallest(TreeNode* root, int k) {
        stack<TreeNode*> tour;
        TreeNode* trav = root;
        while (not tour.empty() or trav) {
            while (trav) {
                tour.push(trav);
                trav = trav->left;
            }
            trav = tour.top(); tour.pop();
            if (not --k) return trav->val;
            trav = trav->right;
        }
        return -1;
    }
};