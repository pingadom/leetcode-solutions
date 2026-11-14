# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        if head is None:
            return None

        while head.next is not None:
            first = head
            second = head.next
            prev.next = second
            head.next = second.next
            second.next = head

            prev = head

            if head.next is not None:
                head = head.next
            else:
                break
        
        return dummy.next

        