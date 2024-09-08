# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def splitListToParts(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: List[ListNode]
        """

        # Count the number of nodes in Linked List
        # n : To keep track of number of nodes in Linked List
        n = 0
        current = head
        while current:
            n += 1
            current = current.next

        # Calculate size of each part and  remainders too
        # Base will determine how many parts every node will have
        # For example 1, base_Size = 3 % 5 = 0, i.e each part will have atleast 0 nodes
        base_Size = n // k
        remainder_Size = n % k

        # Initialize result, and we set current = head again
        result = []
        current = head

        # Loop for splitting the list
        # Each iteration will make up a part of the extracted Linked List
        for i in range(k):
            # Assigns current as base head and checks if extra value in node required or not
            base_Head = current
            size = base_Size + (1 if remainder_Size > 0 else 0)
            remainder_Size -= 1

            # INNER FOR LOOP : Traverses to the last node of the current part
            for j in range(size - 1):
                if current:
                    current = current.next
            
            # IF : To separate current path with next part
            if current: # current = 1
                next_part = current.next    # next_part = 2
                current.next = None # Cut the current part, so 1 becomes [1]
                current = next_part # Now, current = 2
            
            result.append(base_Head)

        # If extra k part left, then we add [] to the result
        while len(result) < k:
            result.append(None)
        
        return result
