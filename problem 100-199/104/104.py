# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.max_depth = 0

    def maxDepth(self, root: TreeNode) -> int:
        return self.__get_max_depth(root)

    def __get_max_depth(self, root, depth=0):
        if root == None:
            return self.max_depth
        if depth > self.max_depth:
            self.max_depth = depth
        self.__get_max_depth(root.right, depth + 1)
        self.__get_max_depth(root.left, depth + 1)
        return self.max_depth + 1