# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        node = head
        while node != None:
            next_node = node.next
            while next_node and next_node.val == node.val:
                next_node = next_node.next
            node.next = next_node
            node = node.next
        return head
    
    def print_linkedlist(self, node):
        if node == None:
            return
        print(node.val, end=" ")
        self.print_linkedlist(node.next)

if __name__ == "__main__":
    # Test case 1
    ll = ListNode(1)
    ll.next = ListNode(1)
    ll.next.next = ListNode(2)
    ll.next.next.next = ListNode(3)
    ll.next.next.next.next = ListNode(3)
    print("input=", end=" ")
    Solution().print_linkedlist(ll)
    ll = Solution().deleteDuplicates(ll)
    print("\noutput=", end=" ")
    Solution().print_linkedlist(ll)

    # Test case 2
    ll = ListNode(1)
    ll.next = ListNode(1)
    ll.next.next = ListNode(1)
    ll.next.next.next = ListNode(3)
    ll.next.next.next.next = ListNode(4)
    print("\ninput=", end=" ")
    Solution().print_linkedlist(ll)
    ll = Solution().deleteDuplicates(ll)
    print("\noutput=", end=" ")
    Solution().print_linkedlist(ll)

    # Test case 3
    ll = ListNode(1)
    print("\ninput=", end=" ")
    Solution().print_linkedlist(ll)
    ll = Solution().deleteDuplicates(ll)
    print("\noutput=", end=" ")
    Solution().print_linkedlist(ll)

    # Test case 4
    ll = ListNode(1)
    ll.next = ListNode(2)
    ll.next.next = ListNode(3)
    ll.next.next.next = ListNode(4)
    ll.next.next.next.next = ListNode(5)
    print("\ninput=", end=" ")
    Solution().print_linkedlist(ll)
    ll = Solution().deleteDuplicates(ll)
    print("\noutput=", end=" ")
    Solution().print_linkedlist(ll)