# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # If head is not None or only one node in head, return head.
        if not head or head.next is None:
            return head
        
        previous_node = head
        current_node = head.next

        while current_node is not None:
            temp_node = ListNode(current_node.val)
            temp_node.next = previous_node
            previous_node = temp_node
            current_node = current_node.next
        
        head.next = None
        return temp_node
    
    @staticmethod
    def show_linkedlist(root):
        while root is not None:
            print(root.val)
            root = root.next
        
if __name__ == "__main__":
    l1 = ListNode(10)
    l1.next = ListNode(5)
    l1.next.next = ListNode(13)
    l1.next.next.next = ListNode(34)

    reversed_ll = Solution().reverseList(l1)
    Solution.show_linkedlist(reversed_ll)