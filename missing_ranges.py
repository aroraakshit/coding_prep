# out of memory error
class Solution: 
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        orig = list(range(lower,upper+1))
        for i in nums:
            if i in orig:
                orig[i-lower] = lower - 1
        ans = []
        first = True
        for i in range(len(orig)):
            if first and orig[i] != lower - 1:
                first = False
                ans.append(str(orig[i]))
            
            elif not first and orig[i] == lower - 1:
                first = True
                
            elif not first and orig[i] != lower - 1:
                if '->' in ans[-1]:
                    tmp = ans[-1].split('->')
                    tmp[1] = str(orig[i])
                    ans[-1] = '->'.join(tmp)
                else:
                    ans[-1] += '->'+str(orig[i])
                
        return ans

# TLE
class Solution: 
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        if len(nums) == 0: return [str(lower)+'->'+str(upper)] if lower != upper else [str(lower)]
        ans = []
        first = True
        k = 0
        for i in range(lower,upper+1):
            if k >= len(nums):
                break
            
            if first and i != nums[k]:
                first = False
                ans.append(str(i))
            
            elif first and i == nums[k]:
                k += 1
            
            elif not first and i == nums[k]:
                k += 1
                first = True
                
            elif not first and i != nums[k]:
                if '->' in ans[-1]:
                    tmp = ans[-1].split('->')
                    tmp[1] = str(i)
                    ans[-1] = '->'.join(tmp)
                else:
                    ans[-1] += '->'+str(i)

        if i < upper and first and i != nums[k-1]:
            first = False
            ans.append(str(i)+ '->'+str(upper))
        elif k == len(nums) and i == upper and nums[k-1] != upper:
            ans.append(str(upper))
        return ans


# 36 ms - faster than 30% solutions
class Solution: 
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        if len(nums) == 0: return [str(lower)+'->'+str(upper)] if lower != upper else [str(lower)]

        if lower == upper:
            if lower in nums:
                    return []
            else:
                return [str(lower)]
            
        ans = [str(lower)+'->'+str(upper)]
        first = True
        k = 0
        for i in nums:
            j = 0
            while j < len(ans):
                if '->' in ans[j]:
                    tmp = ans[j].split('->')
                    if i in range(int(tmp[0]), int(tmp[1])+1):
                        break
                elif int(ans[j]) == i:
                    tmp = [str(i), str(i)]
                    break
                j += 1
                
            if j != len(ans):
                # found something in the range
                del ans[j]
                if tmp[0] == tmp[1]:
                    pass
                elif int(tmp[0]) == i:
                    if int(tmp[0])+1 == int(tmp[1]):
                        ans.append(str(int(tmp[0])+1)) 
                    else:
                        ans.append(str(int(tmp[0])+1)+'->'+tmp[1]) 
                elif int(tmp[1]) == i:
                    if int(tmp[1])-1 == int(tmp[0]):
                        ans.append(tmp[0])
                    else:
                        ans.append(tmp[0]+'->'+str(int(tmp[1])-1))
                else:
                    if int(tmp[0]) == i-1:
                        ans.append(tmp[0])
                    else:
                        ans.append(tmp[0]+'->'+str(i-1)) 
                    if i+1 == int(tmp[1]):
                        ans.append(tmp[1])
                    else:
                        ans.append(str(i+1)+'->'+tmp[1])
        return ans

# 32 ms, faster than 100% solutions (deleted useless if/else)
class Solution: 
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        if len(nums) == 0: return [str(lower)+'->'+str(upper)] if lower != upper else [str(lower)]

        if lower == upper:
            if lower in nums:
                    return []
            else:
                return [str(lower)]
            
        ans = [str(lower)+'->'+str(upper)]
        first = True
        k = 0
        for i in nums:
            j = 0
            while j < len(ans):
                if '->' in ans[j]:
                    tmp = ans[j].split('->')
                    if i in range(int(tmp[0]), int(tmp[1])+1):
                        break
                elif int(ans[j]) == i:
                    tmp = [str(i), str(i)]
                    break
                j += 1
                
            if j != len(ans):
                # found something in the range
                del ans[j]
                if tmp[0] == tmp[1]:
                    left = [None]
                    right = [None]
                elif int(tmp[0]) == i:
                    left = [int(tmp[0])+1]
                    right = [int(tmp[1])]
                elif int(tmp[1]) == i:
                    right = [int(tmp[1])-1]
                    left = [int(tmp[0])]
                else:
                    left = [int(tmp[0]), i+1]
                    right = [i-1, int(tmp[1])]
                
                for i in range(len(left)):
                    if left[i] != None and left[i] != right[i]:
                        ans.append(str(left[i])+'->'+str(right[i]))
                    elif left[i] != None and left[i] == right[i]:
                        ans.append(str(left[i]))
        return ans