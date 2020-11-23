from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.right_view_list = list()
    
    def rightSideView(self, root: TreeNode) -> List[int]:
        self.__traverse_tree(root)
        return self.right_view_list
    
    def __traverse_tree(self, root, level=0):
        if root == None:
            return
        if level >= len(self.right_view_list):
            self.right_view_list.append(None)
        self.__traverse_tree(root.left, level=level+1)
        self.right_view_list[level] = root.val
        self.__traverse_tree(root.right, level=level+1)
        

if __name__ == "__main__":
    t1 = TreeNode(1)
    t1.left = TreeNode(2)
    t1.right = TreeNode(3)
    t1.left.right = TreeNode(5)
    t1.right.right = TreeNode(4)
    output = Solution().rightSideView(t1)
    print("output=", output, "\n")

    t2 = TreeNode(1)
    t2.left = TreeNode(2)
    output = Solution().rightSideView(t2)
    print("output=", output)