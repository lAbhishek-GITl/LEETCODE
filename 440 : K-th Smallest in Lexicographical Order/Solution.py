class Solution(object):
    def findKthNumber(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        # FUNCTION : Calculate number of lexicographical numbers between curr and next number in same level
        def count_steps(curr, n):
            # Keep track of steps (numbers) in current sub tree
            steps = 0
            # To keep counter of first, last number in current sub tree
            first, last = curr, curr
            
            # WHILE : Counting Steps in the Subtree
            while first <= n:
                # Calculates the number of valid numbers within the current range 
                steps += min(n + 1, last + 1) - first
                # We move down the level in dfs order
                first *= 10
                last = last * 10 + 9
            
            return steps

        # Start with first lexicographical number
        curr = 1
        # Decrement value by 1 so we start with first number (since 0 is not lexicographical number)
        k -= 1

        # WHILE : Main loop to traverse the tree
        while k > 0:
            # Calculates the number of steps (numbers) in the current subtree.
            steps = count_steps(curr, n)
            # CONDITION : If number of elements <= k, therefore, desired number not in this sub tree
            if steps <= k:
                # Moves to next sibling
                curr += 1
                # Decrement the k by number of elements present in this sub tree
                k -= steps
            # CONDITION : If number desired is present
            else:
                #  Moves deeper into the subtree & Decrements k by 1 because we're moving to the next number in the sequence.
                curr *= 10
                k -= 1

        return curr

        
