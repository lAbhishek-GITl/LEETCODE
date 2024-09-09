# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def spiralMatrix(self, m, n, head):
        """
        :type m: int
        :type n: int
        :type head: Optional[ListNode]
        :rtype: List[List[int]]
        """

        # Directions for right, down, left, up
        directions = [(0,1), (1, 0), (0, -1), (-1, 0)]
        # Initialise every cell in matrix to -1
        result = [[-1] * n for i in range(m)]

        # x,y : Current position of the traversal; d: direction
        x,y, d = 0, 0, 0

        # Directs to current position head of the matrix
        current = head
        
        while current:
            # Assigns current value in Linked List to result
            result[x][y] = current.val

            # For next position
            next_x, next_y = x + directions[d][0], y + directions[d][1]
            
            # next_x < 0 or next_x >= m : Checks if the next row is out of bounds
            # next_y < 0 or next_y >= n : Checks if the next column is out of bounds
            # result[next_x][next_y] != -1 : Ensures the next position isn't already filled
            if next_x < 0 or next_x >= m or next_y < 0 or next_y >= n or result[next_x][next_y] != -1:
                d = (d + 1) % 4
            
            # Moves x,y to next valid position and changes current to next node
            x += directions[d][0]
            y += directions[d][1]
            current = current.next

        return result
