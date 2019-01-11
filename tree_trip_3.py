# 15% Task Score, 25% Correctness, 0% Performance
# https://app.codility.com/programmers/task/tree_trip/

from collections import defaultdict
def solution(K, C, D):
    # write your code in Python 3.6
    # conditional BFS
    if K <= 0: return 0
    if len(C)==K: return K
    adj_lst = defaultdict(list)
    for i in range(len(C)):
        if i not in adj_lst or C[i] not in adj_lst[i]:
            adj_lst[i].append(C[i])
        if C[i] not in adj_lst or i not in adj_lst[C[i]]:
            adj_lst[C[i]].append(i)
    asc_att = [x for x,y in sorted(enumerate(D), key = lambda x: x[1])]
    ind = len(asc_att) - 1
    num = 0
    visited = [False for i in C]
    queue = []
    queue.append(asc_att[ind])
    visited[asc_att[ind]] = True
    while queue and num < K:
        s = queue.pop(0)
        if D[s] >= D[asc_att[ind-1]]:
            num += 1
            if D[s] == D[asc_att[ind-1]]:
                ind -= 1
            for i in adj_lst[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
        else:
            if asc_att[ind-1] not in queue: # not connected
                break
            else:
                queue.append(s)
    return num