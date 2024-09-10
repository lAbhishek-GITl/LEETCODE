# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    # FUNCTION : To find GCD of two numbers
    def gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a

    # FUNCTION : Actual function to insert and implement the GCD function in
    def insertGreatestCommonDivisors(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        #  Assign head to current variable
        current = head

        # WHILE : While true, i.e., current and next node to current
        while current and current.next:
            # Register the value of both nodes
            a = current.val
            b = current.next.val

            # Find the GCD
            gcd_value = self.gcd(a, b)

            # Create a node that stores the value of GCD
            new_node = ListNode(gcd_value)

            # Insert the GCD node in between the two nodes
            # We first put next node to GCD node as current.next & assign current.next as GCD node
            new_node.next = current.next
            current.next = new_node

            # Proceed to next node pair, skipping the new inserted node 
            current = new_node.next

        return head
        
