class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        # Q: To return Boolean if we could place plants in plots iff the adjacent plots 
        # are empty (both previous and next)

        # FOR : Traverse entire loop
        for i in range(len(flowerbed)):
            # CONDITION
            if flowerbed[i] == 0:
                # TWO CONDITIONS for previous and next
                previous = (i == 0) or (flowerbed[i - 1] == 0)
                nexts = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)
                
                # IF TRUE
                if previous and nexts:
                    flowerbed[i] = 1
                    n -= 1

                    if n <= 0:
                        return True
        return n == 0
