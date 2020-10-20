# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.node_counter = 1
        
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        print("k=", k, end=" ")
        return self.__get_kth_node(root, k)
    
    def __get_kth_node(self, root, k):
        if root == None:
            return None
        counter_hit = self.__get_kth_node(root.left, k)
        if counter_hit != None:
            return counter_hit
        if self.node_counter == k:
            return root.val
        self.node_counter += 1
        counter_hit = self.__get_kth_node(root.right, k)
        if counter_hit != None:
            return counter_hit
        return

    def print_in_order(self, root):
        return self.__print_in_order(root)

    def __print_in_order(self, root):
        if root == None:
            return
        self.__print_in_order(root.left)
        print(root.val, end=" ")
        self.__print_in_order(root.right)

if __name__ == "__main__":
    t = TreeNode(3)
    t.left = TreeNode(1)
    t.right = TreeNode(4)
    t.left.right = TreeNode(2)
    Solution().print_in_order(t)
    output = Solution().kthSmallest(t, 1)
    print("output=", output)

    output = Solution().kthSmallest(t, 2)
    print("output=", output)

    output = Solution().kthSmallest(t, 3)
    print("output=", output)

    output = Solution().kthSmallest(t, 4)
    print("output=", output)

    output = Solution().kthSmallest(t, 5)
    print("output=", output)
