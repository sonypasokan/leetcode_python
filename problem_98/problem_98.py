# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        valid = self.validate_bst(root)
        return valid
    
    def validate_bst(self, root, lower_limit=None, upper_limit=None):
        if root == None:
            return True
        if lower_limit != None and root.val <= lower_limit:
            return False
        if upper_limit != None and root.val >= upper_limit:
            return False
        if root.right:
            valid = self.validate_bst(root=root.right, upper_limit=upper_limit, lower_limit=root.val)
            if valid == False:
                return valid
        if root.left:
            valid = self.validate_bst(root=root.left, lower_limit=lower_limit, upper_limit=root.val)
            if valid == False:
                return valid
        return True

    def show_tree(self, root):
        if root == None:
            return
        self.show_tree(root.left)
        print(root.val, end=" ")
        self.show_tree(root.right)

if __name__ == "__main__":
    # Test case 1
    t = TreeNode(4)
    t.left = TreeNode(2)
    t.right = TreeNode(7)
    t.left.left = TreeNode(1)
    t.left.right = TreeNode(3)
    t.right.left = TreeNode(6)
    t.right.right = TreeNode(9)
    print("input=", end=" ")
    Solution().show_tree(t)
    output = Solution().isValidBST(root=t)
    print("\noutput=", output)

    # Test case 2
    t = TreeNode(2)
    t.left = TreeNode(1)
    t.right = TreeNode(3)
    print("\ninput=", end=" ")
    Solution().show_tree(t)
    output = Solution().isValidBST(root=t)
    print("\noutput=", output)

    # Test case 3
    t = TreeNode(5)
    t.left = TreeNode(1)
    t.right = TreeNode(4)
    t.right.left = TreeNode(3)
    t.right.right = TreeNode(6)
    print("\ninput=", end=" ")
    Solution().show_tree(t)
    output = Solution().isValidBST(root=t)
    print("\noutput=", output)

    # Test case 4
    t = TreeNode(10)
    t.left = TreeNode(5)
    t.right = TreeNode(15)
    t.right.left = TreeNode(6)
    t.right.right = TreeNode(20)
    print("\ninput=", end=" ")
    Solution().show_tree(t)
    output = Solution().isValidBST(root=t)
    print("\noutput=", output)

    # Test case 5
    t = TreeNode(1)
    t.left = TreeNode(1)
    print("\ninput=", end=" ")
    Solution().show_tree(t)
    output = Solution().isValidBST(root=t)
    print("\noutput=", output)

    # Test case 5
    t = TreeNode(0)
    t.right = TreeNode(-1)
    print("\ninput=", end=" ")
    Solution().show_tree(t)
    output = Solution().isValidBST(root=t)
    print("\noutput=", output)
        