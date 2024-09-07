# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Q: Given Binary Tree, is head available as a subpath of the BT downward direction


class Solution(object):
    def isSubPath(self, head, root):
        """
        :type head: ListNode
        :type root: TreeNode
        :rtype: bool
        """
        # Base Case to check if root exists. If not, return False there is no path available
        if not root:
            return False

        # Check if Linked List path matches root node
        # OR : If it doesn't match, we recursively call Function with left & right children of the BT to check for match
        return self.dfs(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)

    # This is a helper function to match sub path of the binary tree
    def dfs(self, head, root):
        # Base Case: If head = None, we have matched entire Linked List and returning true
        if not head:
            return True
        # Base Case: If root = None, and linked list is not complete, we return False since all the nodes are not yet matched but root is all traversed
        if not root:
            return False

        # If the head value matches the root value, we move onto the next element
        if head.val == root.val:
            return self.dfs(head.next, root.left) or self.dfs(head.next, root.right)

        return False
