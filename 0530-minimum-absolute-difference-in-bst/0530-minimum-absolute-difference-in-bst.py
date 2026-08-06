# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        if not root:
            return None
        mindiff=float('inf')
        prev=float('-inf')
        def inorder(root):
            nonlocal mindiff,prev
            if not root:
                return
            if root.left:
                inorder(root.left)
            if abs(root.val-prev)< mindiff:
                mindiff=abs(root.val -prev)
            prev=root.val
            if root.right:
                inorder(root.right)
        inorder(root)
        return mindiff
        

        