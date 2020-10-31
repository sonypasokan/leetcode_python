# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.node_sum = 0
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if root == None:
            return self.node_sum
        if root.val >= L and root.val <= R:
            self.node_sum += root.val
        if root.val > L:
            self.rangeSumBST(root.left, L, R)
        if root.val < R:
            self.rangeSumBST(root.right, L, R)
        return self.node_sum
        