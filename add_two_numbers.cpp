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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* l3_head = new ListNode(0);
        auto l3 = l3_head;
        int carry = 0;
        while (l1 != NULL and l2 != NULL){
            l3->next = new ListNode( l1->val + l2->val + carry );
            carry = l3->next->val / 10;
            l3->next->val -= carry * 10;
            l3 = l3->next;
            l1 = l1->next;
            l2 = l2->next;
        }
        
        ListNode* temp;
        if (l1 == NULL)
            temp = l2;
        else 
            temp = l1;
        
        while (temp != NULL){
            l3->next = new ListNode( temp->val + carry );
            carry = l3->next->val / 10;
            l3->next->val -= carry * 10;
            temp = temp->next;
            l3 = l3->next;
        }
        
        if (carry > 0){
            l3->next = new ListNode( carry );
        }
        
        l3_head = l3_head->next;
        
        return l3_head;
    }
};