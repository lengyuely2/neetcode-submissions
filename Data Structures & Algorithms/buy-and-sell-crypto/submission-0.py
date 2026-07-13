class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp = 0
        minbuy = prices[0]

        for sell in prices:
            maxp = max(maxp,sell-minbuy)
            minbuy = min(minbuy,sell)
        return maxp