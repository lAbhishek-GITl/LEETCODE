class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        # Q : Return boolean array after comparing which kids (index) have max number
        # of candies after getting all the extra Candies

        result = []
        max_Candies = max(candies)

        # FOR : Traversing every element
        for i in range(len(candies)):
            # CONDITION : If every element after getting extraCandies >= Max Candies
            if candies[i] + extraCandies >= max_Candies:
                result.append(True)
            else:
                result.append(False)
        
        return result
