# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy

        while True:
            temp = prev
            for _ in range(k):
                temp = temp.next
                if temp is None:
                    return dummy.next

            curr = prev.next

            for _ in range(k - 1):
                t1, t2 = curr, curr.next

                t1.next = t2.next
                t2.next = prev.next
                prev.next = t2

            prev = curr


        