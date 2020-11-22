# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        visited_node = set()
        node_A = headA
        while node_A != None:
            visited_node.add(node_A)
            node_A = node_A.next
        node_B = headB
        while node_B != None:
            if node_B in visited_node:
                return node_B
            node_B = node_B.next
        return None

