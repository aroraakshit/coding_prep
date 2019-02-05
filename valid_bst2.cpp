/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution { // based on in-order traversal
public:
    bool isValidBST(TreeNode* root) {
        if(root == NULL){
            return true;
        }
        
        stack<TreeNode*> s{};
        int prev = INT_MIN;
        bool first=true;
        while(s.size() != 0 || root!=NULL){
            while(root!=NULL){
                s.push(root);
                root = root->left;
            }
            root = s.top();
            s.pop();
            if (root->val <= prev and !first){
                return false;
            }
            first = false;
            prev = root->val;
            root = root->right;
        }
    return true;
    }
};

// another variation

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

// class Solution {
// public:
//     bool isValidBST(TreeNode* root) {
//         if(root == NULL) return true;
//         auto res = helper(root);
//         return res.first <= res.second; 
//     }
// private:
//     pair<int, int> helper(TreeNode* root){
//         pair<int, int> l,r;
//         int lb = root->val;
//         int rb = root->val;
//         if(root->left != NULL){
//             l = helper(root->left);
//             if(l.first > l.second) return l;
//             if(l.second >= root->val)
//                 return make_pair(INT_MAX, INT_MIN);
//             lb=l.first;
//         }
//         if(root->right != NULL){
//             r=helper(root->right);
//             if(r.first > r.second) return r;
//             if(r.first <= root->val)
//                 return make_pair(INT_MAX, INT_MIN);
//             rb=r.second;
//         }
//         return make_pair(lb, rb);
//     }
// };