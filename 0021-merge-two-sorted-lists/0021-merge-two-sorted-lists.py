# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        if(list1 == None):
            return list2
        if (list2 == None):
            return list1
        if list1.val < list2.val:
            head = ListNode(list1.val)
            list1 = list1.next
        else:
            head = ListNode(list2.val)
            list2 = list2.next
        current = head
        while list1 != None or list2 != None:
            if list1 == None:
                temp = ListNode(list2.val)
                current.next = temp
                current = temp
                list2 = list2.next

            elif list2 == None:
                temp = ListNode(list1.val)
                current.next = temp
                current = temp
                list1 = list1.next

            elif list1.val < list2.val:
                temp = ListNode(list1.val)
                current.next = temp
                current = temp
                list1 = list1.next
            else:
                temp = ListNode(list2.val)
                current.next = temp
                current = temp
                list2 = list2.next

        return head