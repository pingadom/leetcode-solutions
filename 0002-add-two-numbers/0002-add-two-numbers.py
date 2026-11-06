# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:

        sum = ListNode()
        head = sum

        for n in range(0,100):
            total = l1.val+l2.val+sum.val
            sum.val = (total)%10

            if (total) >= 10:
                sum.next = ListNode(1)

            if l1.next is None and l2.next is None:
                break
            if l1.next is None:
                l1.next = ListNode(0)
            elif l2.next is None:
                l2.next = ListNode(0)

            if total < 10:
                sum.next = ListNode()
            sum = sum.next
            l1,l2 = l1.next,l2.next
        
        return head
            
                