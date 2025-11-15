

class Solution:
    # O(n**2) two nested loops, naive methode 
    def maxProfit(self, prices: List[int]) -> int:
        #[10,1,5,6,7,1]

        #buy - identify min 
        maxgain = 0
    
        gain = [[0] * len(prices) for _ in range(len(prices))]

        for i in range(len(prices)) : 
            for j in range(i+1 , len(prices)) :
                if i == j or prices[j] - prices[i] <= 0: 
                    gain[i][j] = 0
                else :
                    gain[i][j] = prices[j] - prices[i]
                    if gain[i][j] > maxgain : 
                        maxgain = gain[i][j]
        return maxgain

    # O(n)time , O(1) space ,  TWO POINTERS methode :
    def maxProfit(self, prices: List[int]) -> int:
        if not prices : 
            return 0

        min_price = float('inf')
        max_profite = 0

        for p in prices :
            if p < min_price : 
                min_price = p
            elif p - min_price > max_profite :
                max_profite = p - min_price
        
        return max_profite