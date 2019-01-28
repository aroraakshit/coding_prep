# work in progress

class Solution:
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        if (len(nums) == 0):
            if abs(upper - lower) > 0:
                return [str(lower)+"->"+str(upper)]
            else:
                return [str(lower)]
        elif (nums[-1] < lower) or (nums[0] > upper):
            if abs(upper - lower) > 0:
                return [str(lower)+"->"+str(upper)]
            else:
                return [str(lower)]
        
        ans = []
        temp = []
        j = 0
        for i in range(lower, upper+1):
            if j >= len(nums):
                break
            if nums[j] == i:
                if temp and len(temp) == 1:
                    ans.append(str(temp[0]))
                    temp = []
                elif temp and len(temp) > 1:
                    ans.append(str(temp[0])+"->"+str(temp[-1]))
                    temp = []
                j += 1
            elif nums[j] != i:
                if len(temp) == 0:
                    temp = [i]
                else:
                    temp.append(i)
        if upper - lower > 0 and abs(upper - nums[-1] - 1) > 0 and abs(lower - nums[-1] - 1) > 0:
            ans.append(str(nums[-1]+1)+"->"+str(upper))
        elif upper - lower > 0:
            ans.append(str(nums[-1]+1))
        return ans