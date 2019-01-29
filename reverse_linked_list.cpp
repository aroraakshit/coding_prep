/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode* prev = NULL;
        ListNode* nex = NULL;
        while(head != NULL){
            nex = head->next;
            head->next = prev;
            prev = head;
            head = nex;
        }
        return prev;
    }
};