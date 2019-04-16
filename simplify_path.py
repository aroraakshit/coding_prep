class Solution: # 40ms, based on stack
    def simplifyPath(self, path: str) -> str:
        stack = ['/']
        if path == '':
            return ''
        path_lst = path.split('/')
        for i in range(len(path_lst)):
            if path_lst[i] == '..':
                if stack[-1] != '/':
                    stack.pop()
            elif path_lst[i] != '' and path_lst[i] != '.':
                stack.append(path_lst[i])
        return '/'+'/'.join(stack[1:])