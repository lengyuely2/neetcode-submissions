# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    left_check = staticmethod(lambda val,limit: val < limit)
    right_check = staticmethod(lambda val,limit: val > limit)
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        if (not self.isvalid(root.left,root.val,self.left_check) or
        not self.isvalid(root.right,root.val,self.right_check)):
            return False
        
        return self.isValidBST(root.left) and self.isValidBST(root.right)

    def isvalid(self,root: Optional[TreeNode],limit:int,check)->bool:
        if not root:
            return True
        if not check(root.val,limit):
            return False
        
        return (self.isvalid(root.left,limit,check) and 
        self.isvalid(root.right,limit,check))