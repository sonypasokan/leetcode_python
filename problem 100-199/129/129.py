# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.total_sum = 0
    def sumNumbers(self, root: TreeNode) -> int:
        self.__sum_of_branch(root)
        return self.total_sum
    def __sum_of_branch(self, root, branch_sum=0):
        if root == None:
            return
        branch_sum = branch_sum * 10 + root.val
        if root.right == None and root.left == None:
            self.total_sum += branch_sum
        self.__sum_of_branch(root.left, branch_sum=branch_sum)
        self.__sum_of_branch(root.right, branch_sum=branch_sum)


if __name__ == "__main__":
    t1 = TreeNode(1)
    t1.left = TreeNode(2)
    t1.right = TreeNode(3)
    output = Solution().sumNumbers(t1)
    print("output=", output)

    t2 = TreeNode(4)
    t2.left = TreeNode(9)
    t2.right = TreeNode(0)
    t2.left.left = TreeNode(5)
    t2.left.right = TreeNode(1)
    output = Solution().sumNumbers(t2)
    print("output=", output)