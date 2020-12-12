# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.max_sum = float('-inf')
    
    def maxPathSum(self, root: TreeNode) -> int:
        self.__max_gain(root)
        return self.max_sum
    
    def __max_gain(self, root):
        if root == None:
            return 0
        left_tree_gain = max(self.__max_gain(root.left), 0)
        right_tree_gain = max(self.__max_gain(root.right), 0)

        root_gain = root.val + left_tree_gain + right_tree_gain
        self.max_sum = max(root_gain, self.max_sum)

        return root.val + max(left_tree_gain, right_tree_gain)

if __name__ == "__main__":
    t1 = TreeNode(16)
    t1.left = TreeNode(-3)
    t1.right = TreeNode(20)
    t1.right.left = TreeNode(15)
    t1.right.right = TreeNode(7)

    output = Solution().maxPathSum(t1)
    print("output=", output)