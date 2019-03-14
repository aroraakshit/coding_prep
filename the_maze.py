class Solution: # 96ms
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        d = {"down":1,"up":2,"left":3,"right":4}
        seen = set()
        queue = [start]
        while queue!=[]:
            # print(queue)
            [i,j]  = queue[0]
            del queue[0]
            if (i,j) not in seen:
                seen.add((i,j))
            else:
                continue
            if [i,j] == destination:
                return True
            for direction in d.values():
                tmp_i = i
                tmp_j = j
                while (direction == 1 and tmp_i+1 < len(maze) and maze[tmp_i+1][tmp_j] == 0):
                    tmp_i += 1
                while (direction == 2 and tmp_i>0 and maze[tmp_i-1][tmp_j] == 0):
                    tmp_i -= 1
                while (direction == 3 and tmp_j>0 and maze[tmp_i][tmp_j-1] == 0):
                    tmp_j -= 1
                while (direction == 4 and tmp_j+1<len(maze[0]) and maze[tmp_i][tmp_j+1] == 0):
                    tmp_j += 1
                if [i,j] != [tmp_i,tmp_j]:
                    queue.append([tmp_i,tmp_j])
        return False
            