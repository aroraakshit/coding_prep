import sys
class Solution: # 2212ms, dp based
    def __init__(self):
        self.mem = {}
        
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        elif amount in self.mem:
            return self.mem[amount]
        
        res = sys.maxsize
        for i in range(len(coins)):
            if coins[i] <= amount:
                sub_res = self.coinChange(coins, amount-coins[i])
                if sub_res != -1 and sub_res + 1 < res:
                    res = sub_res + 1
        self.mem[amount] = -1 if res == sys.maxsize else res
        return self.mem[amount]

class Solution: # dfs based, Credits - LeetCode
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        def dfs(amount, current_count, start_index):
            if current_count - (-amount//coins[start_index]) >= result[0]:
                return
            if amount % coins[start_index] == 0:
                result[0] = min(result[0], current_count + amount // coins[start_index])
                return
            if start_index == len(coins) - 1:
                return
            for i in range(amount//coins[start_index], -1, -1):
                dfs(amount - i*coins[start_index], current_count + i, start_index + 1)
            return  
        coins.sort(reverse = True)
        result = [amount + 1]
        dfs(amount, 0, 0)
        return result[0] if result[0] < amount + 1 else -1