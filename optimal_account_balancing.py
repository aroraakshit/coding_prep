'''
Question: https://leetcode.com/problems/optimal-account-balancing/ 
A group of friends went on holiday and sometimes lent each other money. For example, Alice paid for Bill's lunch for $10. Then later Chris gave Alice $5 for a taxi ride. We can model each transaction as a tuple (x, y, z) which means person x gave person y $z. Assuming Alice, Bill, and Chris are person 0, 1, and 2 respectively (0, 1, 2 are the person's ID), the transactions can be represented as [[0, 1, 10], [2, 0, 5]].

Given a list of transactions between a group of people, return the minimum number of transactions required to settle the debt.

Note:

A transaction will be given as a tuple (x, y, z). Note that x ≠ y and z > 0.
Person's IDs may not be linear, e.g. we could have the persons 0, 1, 2 or we could also have the persons 0, 2, 6.
Example 1:

Input:
[[0,1,10], [2,0,5]]

Output:
2

Explanation:
Person #0 gave person #1 $10.
Person #2 gave person #0 $5.

Two transactions are needed. One way to settle the debt is person #1 pays person #0 and #2 $5 each.
Example 2:

Input:
[[0,1,10], [1,0,1], [1,2,5], [2,0,5]]

Output:
1

Explanation:
Person #0 gave person #1 $10.
Person #1 gave person #0 $1.
Person #1 gave person #2 $5.
Person #2 gave person #0 $5.

Therefore, person #1 only need to give person #0 $4, and all debt is settled.
'''
'''
Credits - https://leetcode.com/problems/optimal-account-balancing/discuss/95355/11-liner-9ms-DFS-solution-(detailed-explanation) 
With all the given transactions, in the end, each person with ID = id will have an overall balance bal[id]. Note that the id value or any person coincidentally with 0 balance is irrelevant to debt settling count, so we can simply use an array debt[] to store all non-zero balances, where

debt[i] > 0 means a person needs to pay $ debt[i] to other person(s);
debt[i] < 0 means a person needs to collect $ debt[i] back from other person(s).
Starting from first debt debt[0], we look for all other debts debt[i] (i>0) which have opposite sign to debt[0]. Then each such debt[i] can make one transaction debt[i] += debt[0] to clear the person with debt debt[0]. From now on, the person with debt debt[0] is dropped out of the problem and we recursively drop persons one by one until everyone's debt is cleared meanwhile updating the minimum number of transactions during DFS.

Note: Thanks to @KircheisHe who found the following great paper about the debt settling problem:

Settling Multiple Debts Efficiently: An Invitation to Computing Science by T. Verhoeff, June 2003.
The question can be transferred to a 3-partition problem, which is NP-Complete.

Code was given in Java, here is my ported version in Python3
'''

import sys
from collections import defaultdict
class Solution: # 2280ms, 13.1MB
    def dfs(self, debt, s):
        while(s < len(debt) and debt[s]==0):
            s += 1
            
        if s == len(debt):
            return 0
        res = sys.maxsize
        for i in range(s+1, len(debt)):
            if debt[i]*debt[s]<0:
                debt[i] += debt[s]
                res = min(res, 1+self.dfs(debt,s+1))
                debt[i]-=debt[s]
        return res 
    
    def minTransfers(self, transactions: List[List[int]]) -> int:        
        t = defaultdict(int) #balances
        for i in transactions:
            t[i[0]] -= i[2]
            t[i[1]] += i[2]
        debt = [t[i] for i in t.keys() if t[i]!=0]
        return self.dfs(debt, 0)


'''
Clique approach: https://leetcode.com/problems/optimal-account-balancing/discuss/173299/Python-BFS-beats-100 
First step is quite clear. We need to exclude those people who ends up not owing or owed money.

Then we will have an array of non-zero numbers, which sums to be zero. For example

[4, -2, -2, 6, -6]

This can be converted into finding the minimal clique such that the elements sum up to be zero. Minimal means there is no subset which sums up to zero. In the example above, there are two minimal such cliques.

[4, -2, -2] and [6, -6]

The beautiful part of those cliques are that we only need to resolve the balance inside the clique. There will be no inter-clique transactions.

The final number of transactions will be 5 - 2, which is num_non_zero - num_clique.

To find the minimal clique is the perfect problem to be solved by BFS. We will start with one element in the set as the root, find the minimal length path in the tree which sum up to be zero. Remove that zero sum set and pick another root.
'''
# Remove one-zero clique, 28ms solution
class Solution:
    def minTransfers(self, transactions: 'List[List[int]]') -> 'int':
        def remove_one_zero_clique(non_zero):
            n = len(non_zero)
            q = collections.deque()            
            # q store ([index set], sum of set)
            q.append(([0], non_zero[0]))
            min_zero_set = None

            while q:
                cur_set, cur_sum = q.popleft()
                if cur_sum == 0:
                    min_zero_set = cur_set
                    break
                for j in range(cur_set[-1] + 1, n):
                    q.append((cur_set + [j], cur_sum + non_zero[j]))
            
            min_zero_set = set(min_zero_set)
            return [non_zero[i] for i in range(n) if i not in min_zero_set]
        
        
        bal = collections.defaultdict(int)
        for t in transactions:
            bal[t[0]] -= t[2]
            bal[t[1]] += t[2]
        non_zero = [bal[k] for k in bal if bal[k] != 0]
        
        bal_cnt = len(non_zero)
        while len(non_zero) > 0:
            non_zero = remove_one_zero_clique(non_zero)
            bal_cnt -= 1
        return bal_cnt

# Cleaner implementation, Credits - LeetCode
import sys
from collections import deque, defaultdict
class Solution:
    
    def minTransfers(self, trans):
        debt = defaultdict(int)
        for i, j, k in trans: debt[i] -= k; debt[j] += k
        debt = list(filter(None, debt.values()))

        def SplitDebt():
            cset, Q = set(), deque([([0], debt[0])])
            while Q:
                cset, csum = Q.popleft()
                if csum == 0: break
                for j in range(cset[-1] + 1, len(debt)):
                    Q.append((cset + [j], csum + debt[j]))
            if not cset: return False
            debt[:] = [debt[i] for i in set(range(len(debt))) - set(cset)]
            return True

        res = len(debt)
        while debt and SplitDebt(): res -= 1
        return res