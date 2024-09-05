class Solution(object):
    def missingRolls(self, rolls, mean, n):
        """
        :type rolls: List[int]
        :type mean: int
        :type n: int
        :rtype: List[int]
        """
        # Q : To find missing observation (We can return it in equal values, just for Q)
        # Total sum is sum of sum of (m + n) rolls * mean
        # Missing sum is difference between Total sum & sum of observed rolls

        m = len(rolls)
        missing_Sum = ((mean * (m + n))) - sum(rolls)

        # CONDITION 1 : Say n = 3, if dice roll 3 times, sum >= 1 (since die has min 1)
        # CONDITION 2 : Missing sum can't exceed the 6 times dice rolled.
        # THIS IS FOR FALSE CASE
        if missing_Sum < n or missing_Sum > n * 6:
            return []
        
        # divmod(): Returns 2 value quotient & remainder
        # Quotient = missing_Sum // n ; Remainder = missing_Sum % n
        quotient, remainder = divmod(missing_Sum, n)

        # Create a list of n elements with same values (divided the missing sum equally)
        result = [quotient] * n

        # Add the remaining sum incrementing 1 to every element until remainder gets 0
        for i in range(remainder):
            result[i] += 1

        return result
