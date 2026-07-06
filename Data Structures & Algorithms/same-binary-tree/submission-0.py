# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        ans = False
        if p and q:
            check_left = self.isSameTree(p.left, q.left)
            check_right = self.isSameTree(p.right, q.right)
            ans = (p.val == q.val)
        elif not p and not q:
            ans = True
            return True
        else:
            return False

        return ans and check_left and check_right
        