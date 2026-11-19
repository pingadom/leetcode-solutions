# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        levels = []
        dq = deque()
        if root:
            dq.append(root)
        else:
            return []

        while dq:
            level = []
            for _ in range(0,len(dq)):
                node = dq.popleft()
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
                level.append(node.val)
            levels.append(level)
        
        return levels

            


            

        