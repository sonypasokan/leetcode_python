# Definition for singly-linked list.
from typing import List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        ll_node = head
        connected_node_count = 0
        connection_map = frozenset(G)
        while ll_node:
            if ll_node.val in connection_map and (ll_node.next == None or \
            (ll_node.next and ll_node.next.val not in connection_map)):
                connected_node_count += 1
            ll_node = ll_node.next
        return connected_node_count