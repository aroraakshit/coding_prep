class Solution(object): #64ms
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        if not logs or logs == []:
            return [0]*n
        
        stack = []
        ans = [0 for i in range(n)]
        lastEnd = None
        for i in range(len(logs)):
            # print(stack, ans)
            s = logs[i].split(':')
            if s[1] == "start":
                if lastEnd and stack!=[]:
                    stack[-1][3] += int(s[2]) - lastEnd-1
                    lastEnd = None
                elif stack != []:
                    stack[-1][3] += int(s[2]) - stack[-1][1]
                stack.append([int(s[0]),int(s[2]),None,0])
            else: # s[1] == "end"
                [fn, start, end, ex] = stack.pop()
                if(int(s[0]) != fn):
                    print("oops")
                if lastEnd:
                    ex += (int(s[2])-lastEnd)
                    lastEnd = None
                else:
                    ex += (int(s[2])+1-start)
                lastEnd = int(s[2])
                ans[int(fn)] += ex
        return ans

# 48ms submission, Credits-LeetCode
class Solution:
    def exclusiveTime(self, n: 'int', logs: 'List[str]') -> 'List[int]':
        if not logs:
            return [0] * n
        rsp = [0] * n
        
        start_line = logs[0].split(":")
        curr_time = int(start_line[2])
        stack = [int(start_line[0])]
        
        for l in logs:
            log = l.split(":") 
            ntime = int(log[2])
            
            if log[1] == "start":
                rsp[stack[-1]] += ntime - curr_time
                stack.append(int(log[0]))
                curr_time = ntime
            else:
                rsp[stack[-1]] += ntime - curr_time + 1
                stack.pop()
                curr_time = ntime + 1
        return rsp