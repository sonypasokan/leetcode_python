# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None:
            return True
        return self.is_symmetric(root, root)
    
    def is_symmetric(self, root_1, root_2):
        if root_1 == root_2 == None:
            return True
        if root_1 == None or root_2 == None:
            return False
        if root_1.val != root_2.val:
            return False
        status = self.is_symmetric(root_1.right, root_2.left)
        if status == False:
            return False
        status = self.is_symmetric(root_1.left, root_2.right)
        if status == False:
            return False
        return True
        
if __name__ == "__main__":
    t = TreeNode(1)
    t.left = TreeNode(2)
    output = Solution().isSymmetric(t)
    print(output)

    t = TreeNode(1)
    t.left = TreeNode(2)
    t.right = TreeNode(3)
    output = Solution().isSymmetric(t)
    print(output)

    t = TreeNode(1)
    t.left = TreeNode(2)
    t.right = TreeNode(2)
    output = Solution().isSymmetric(t)
    print(output)

    t = TreeNode(1)
    t.left = TreeNode(2)
    t.right = TreeNode(2)
    t.left.left = TreeNode(3)
    t.right.right = TreeNode(3)
    t.right.left = TreeNode(5)
    output = Solution().isSymmetric(t)
    print(output)