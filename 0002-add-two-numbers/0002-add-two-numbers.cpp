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
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        int carry = 0;
        ListNode* node = new ListNode((l1->val + l2->val) % 10);
        ListNode* head = node;
        carry = (l1->val + l2->val) / 10;
        l1 = l1->next;
        l2 = l2->next;
        while (l1 && l2) {
            // add numbers
            ListNode* newNode = new ListNode((l1->val + l2->val + carry) % 10);
            carry = (l1->val + l2->val + carry)/10;
            node->next = newNode;
            node = newNode;
            l1 = l1->next;
            l2 = l2->next;
        }
        while (l1) {
            // finish the number
            ListNode* newNode = new ListNode((l1->val + carry) % 10);
            carry = (l1->val + carry)/10;
            node->next = newNode;
            node = newNode;
            l1 = l1->next;
        }
        while (l2) {
            // finish the number
            ListNode* newNode = new ListNode((l2->val + carry) % 10);
            carry = (l2->val + carry)/10;
            node->next = newNode;
            node = newNode;
            l2 = l2->next;
        }
        if (carry) {
            // finish the number
            ListNode* newNode = new ListNode(carry);
            node->next = newNode;
            node = newNode;
        }
        return head;
    }
};