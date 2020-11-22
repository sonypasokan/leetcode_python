from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    def __init__(self):
        self.output_node_list = list()
    
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        self.__traverse_tree(root)
        return self.output_node_list
    
    def __traverse_tree(self, root, level=0):
        if root == None:
            return
        if len(self.output_node_list) <= level:
            self.output_node_list.append([])
        self.output_node_list[level].append(root.val)
        self.__traverse_tree(root.left, level=level+1)
        self.__traverse_tree(root.right, level=level+1)
        

if __name__ == "__main__":
    t1 = TreeNode(3)
    t1.left = TreeNode(9)
    t1.right = TreeNode(20)
    t1.right.left = TreeNode(15)
    t1.right.right = TreeNode(7)

    output = Solution().levelOrder(t1)
    print(output)