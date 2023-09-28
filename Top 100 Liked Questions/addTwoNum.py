'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
'''

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode()  # Dummy head of the result linked list
        current = dummy_head  # Pointer to the current node in the result linked list
        carry = 0  # Initialize carry to 0

        while l1 or l2 or carry:
            # Get the values of the current nodes in l1 and l2
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            # Calculate the sum of values and carry
            _sum = x + y + carry

            # Update carry for the next iteration
            carry = _sum // 10

            # Create a new node with the single digit result
            current.next = ListNode(_sum % 10)

            # Move to the next nodes if they exist
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

            current = current.next

        return dummy_head.next  # Return the head of the result linked list


main = Solution()
l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))
result = main.addTwoNumbers(l1, l2)
while result:
    print(result.val)
    result = result.next
