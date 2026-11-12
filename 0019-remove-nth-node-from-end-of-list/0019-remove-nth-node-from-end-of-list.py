# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getLength(self,head):
        temp = head
        length = 0
        while temp:
            length += 1
            temp = temp.next
        return length

    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        final = head
        prev = ListNode()
        length,goal = self.getLength(head),self.getLength(head)-n
        if goal == 0:
            return head.next
        c = 1
        print(c,goal)
        while c <= goal:
            prev = head
            head = head.next
            c+= 1
        prev.next = head.next
        return final

