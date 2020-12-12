# Definition for a binary tree node.
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.index_map_inorder = dict()
        self.preorder_index = 0
        self.preorder = list()
    
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        for index, node in enumerate(inorder):
            self.index_map_inorder[node] = index
        self.preorder = preorder
        return self.__build_tree(0, len(inorder))
    
    def __build_tree(self, inorder_min_index, inorder_max_index):
        if inorder_max_index - inorder_min_index == 0:
            return
        root = TreeNode(self.preorder[self.preorder_index])
        self.preorder_index += 1
        root_index = self.index_map_inorder[root.val]
        root.left = self.__build_tree(inorder_min_index, root_index)
        root.right = self.__build_tree(root_index + 1, inorder_max_index)
        return root
    
    @staticmethod
    def show_inorder(root):
        if root == None:
            return
        Solution.show_inorder(root.left)
        print(root.val)
        Solution.show_inorder(root.right)

if __name__ == "__main__":
    input_list = [
        [[3,9,20,15,7], [9,3,15,20,7]],
        [[10,5,6,30,7,4,15,20], [6,30,5,10,4,7,15,20]],
        [[20,10,9,11,22,21,23], [9,10,11,20,21,22,23]]
    ]
    for input_item in input_list:
        output_tree = Solution().buildTree(input_item[0], input_item[1])
        print("------------------------")
        Solution.show_inorder(output_tree)


        
