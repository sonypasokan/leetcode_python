# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if (p != None and q == None) or (p == None and q != None):
            return False
        if p == q == None:
            return True
        if p.val != q.val:
            return False
        status = self.isSameTree(p.left, q.left)
        if status == False:
            return False
        status = self.isSameTree(p.right, q.right)
        if status == False:
            return False
        return True
        
        
if __name__ == "__main__":
    t = TreeNode(3)
    t.left = TreeNode(1)
    t.right = TreeNode(4)
    t.left.right = TreeNode(2)

    t1 = TreeNode(4)
    t1.left = TreeNode(3)
    t1.right = TreeNode(5)

    t2 = TreeNode(4)
    t2.left = TreeNode(3)
    t2.right = TreeNode(5)

    output = Solution().isSameTree(t, t1)
    print("output=", output)

    output = Solution().isSameTree(t1, t)
    print("output=", output)

    output = Solution().isSameTree(t, t)
    print("output=", output)

    output = Solution().isSameTree(t1, t1)
    print("output=", output)

    output = Solution().isSameTree(t1, t2)
    print("output=", output)