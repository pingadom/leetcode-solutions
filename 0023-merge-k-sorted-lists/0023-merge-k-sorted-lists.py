# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        dummy = ListNode(0)
        tail = dummy
        heap = []

        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap,(node.val,i,node))

        while heap:
            val,x,top = heapq.heappop(heap)
            tail.next = top
            tail = tail.next
            if top.next:
                heapq.heappush(heap,(top.next.val,x,top.next))
        
        return dummy.next
            



        