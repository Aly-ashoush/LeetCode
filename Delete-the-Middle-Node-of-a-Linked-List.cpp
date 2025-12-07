1class Solution {
2public:
3    ListNode* deleteMiddle(ListNode* head) {
4        if (!head || !head->next)
5            return nullptr;
6
7
8        int counter = 0;
9        ListNode* temp = head;
10        while (temp) {
11            counter++;
12            temp = temp->next;
13        }
14        int mid = counter / 2;
15        temp = head;
16        ListNode* prev = nullptr;
17
18        for (int i = 0; i < mid; i++) {
19            prev = temp;
20            temp = temp->next;
21        }
22        prev->next = temp->next;
23        delete temp;
24
25        return head;
26    }
27};