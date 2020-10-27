# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def invertTree(self, root: TreeNode) -> TreeNode:
        if root == None:
            return root
        root.left, root.right = root.right, root.left
        root.left = self.invertTree(root.left)
        root.right = self.invertTree(root.right)
        return root
        
    def show_tree(self, root):
        if root == None:
            return
        self.show_tree(root.left)
        print(root.val, end=" ")
        self.show_tree(root.right)

if __name__ == "__main__":
    t = TreeNode(4)
    t.left = TreeNode(2)
    t.right = TreeNode(7)
    t.left.left = TreeNode(1)
    t.left.right = TreeNode(3)
    t.right.left = TreeNode(6)
    t.right.right = TreeNode(9)
    print("input=")
    Solution().show_tree(t)
    t = Solution().invertTree(root=t)
    print("\noutput=")
    Solution().show_tree(t)
