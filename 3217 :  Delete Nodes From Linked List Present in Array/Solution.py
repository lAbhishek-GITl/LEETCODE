# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def modifiedList(self, nums, head):
        """
        :type nums: List[int]
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Q: To remove elements from Linked List and return remaining elements

        # Create a set to easily traverse unique elemts which are to be removed
        nums_set = set(nums)
        
        # Create a dummy linked list to handle edge cases like removal of head node, etc
        # Dummy linked list is initialized with value 0 and points to head of the LL
        dummyList = ListNode(0)
        dummyList.next = head

        # Initialized to update LL after deletion of required elements
        current = dummyList
        
        # WHILE : Traversal
        while current.next:
            # CONDIITON : If found in nums_set, we skip the element and move to next
            if current.next.val in nums_set:
                current.next = current.next.next
            # CONDITION : If not in nums_set, we move current to next node
            else:
                current = current.next
        # We return new Linked List after deleition
        return dummyList.next
