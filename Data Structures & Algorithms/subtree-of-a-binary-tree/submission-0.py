# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   

    def validate(self, root, subRoot):
        if not root and not subRoot:
            return True
        elif not root or not subRoot:
            return False
        if root.val != subRoot.val:
            return False
        left = self.validate(root.left, subRoot.left)
        right = self.validate(root.right, subRoot.right)

        return left and right
        

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        
        if self.validate(root, subRoot):
            return True
        
        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)

        return left or right