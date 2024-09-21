class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        # Q : We have to print the number range in lexicographical order
        # For n = 13 : 1 -> 10 -> 11 -> 12 -> 13 -> (14 out of range) 2 -> 3 -> ..... 

        # Stores the result
        result = []

        # We take DFS approach, because if in the range, we go depth for search
        def dfs(c):
            # CONDITION : To check if the number is in range
            if c > n:
                return

            # We store the number in result
            result.append(c)

            # To check all possible next digits appended to that particular integer from 1 to 9
            for i in range(10):
                # We increase the number in terms of lexicographical approach
                next_num = c * 10 + i
                # We check if the new number is in range
                if next_num > n:
                    break
                # If in range, we perform dfs function again, else break
                dfs(next_num)
        
        # Perform the dfs loop 1-9 range and store result in the result
        for i in range(1, 10):
            dfs(i)

        return result
        
