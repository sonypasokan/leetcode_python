# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_node = l1
        l2_node = l2
        remainder = 0
        second_last_node = None
        while l1_node != None:
            #If L1 is longer than L2, then L2 could be None
            if l2_node:
                l2_value = l2_node.val
            else:
                l2_value = 0
            new_value = remainder + l1_node.val + l2_value
            l1_node.val, remainder = self.separate_digit_and_remainder(new_value)
            if l1_node.next == None:
                second_last_node = l1_node
            l1_node = l1_node.next
            if l2_node:
                l2_node = l2_node.next
        if l2_node: # If L2 is longer than L1
            second_last_node.next = l2_node
            l1_node = second_last_node.next
        while l1_node != None:
            new_value = remainder + l1_node.val
            l1_node.val, remainder = self.separate_digit_and_remainder(new_value)
            if l1_node.next == None:
                second_last_node = l1_node
            l1_node = l1_node.next
        if second_last_node and remainder == 1:
            last_node = ListNode(val=remainder)
            second_last_node.next = last_node
        return l1
    
    def separate_digit_and_remainder(self, number):
        if number > 9:
            number = number - 10
            remainder = 1
        else:
            remainder = 0
        return number, remainder