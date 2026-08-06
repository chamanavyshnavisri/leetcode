# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def caldepth(self,root,depth):
        if not root:
            return depth
        leftsubtree=self.caldepth(root.left,depth+1)
        rightsubtree=self.caldepth(root.right,depth+1)
        return max(leftsubtree,rightsubtree)
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return self.caldepth(root,0)

        


        