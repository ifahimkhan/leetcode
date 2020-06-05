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
    vector<int> getLonelyNodes(TreeNode* root) {
        vector<int> lonely;
        stack<TreeNode*> tour;
        tour.push(root);
        while (not tour.empty()) {
            TreeNode *node = tour.top(); tour.pop();
            if (not node->left and node->right) lonely.push_back(node->right->val);
            if (not node->right and node->left) lonely.push_back(node->left->val);
            if (node->left) tour.push(node->left);
            if (node->right) tour.push(node->right);
        }
        return lonely;
    }
};