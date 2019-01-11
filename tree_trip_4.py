# 46% Task Score, 75% Correctness, 0% Performance
# https://app.codility.com/programmers/task/tree_trip/

from collections import defaultdict
def solution(K, C, D):
    # write your code in Python 3.6
    # conditional BFS
    if K <= 0: return 0
    if len(C)== 1 and K==1: return 1
    adj_lst = defaultdict(list)
    for i in range(len(C)):
        if i not in adj_lst or C[i] not in adj_lst[i]:
            adj_lst[i].append(C[i])
        if C[i] not in adj_lst or i not in adj_lst[C[i]]:
            adj_lst[C[i]].append(i)
    # print(adj_lst)   
    asc_att = [x for x,y in sorted(enumerate(D), key = lambda x: x[1])][-K:]
    asc_attraction = sorted(D)[-K:]
    visited = [False for i in C]
    queue = []
    queue.append(asc_att[-1])
    visited[asc_att[-1]] = True
    num = 0
    final = []
    while queue and asc_attraction and num < K:
        s = queue.pop(0)
        if D[s] in asc_attraction:
            # print(s)
            final.append(s)
            asc_attraction.remove(D[s])
            num += 1
            for i in adj_lst[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
    
    if asc_attraction:
        for i in final:
            if D[i] < max(asc_attraction):
                num -= 1
    # print(asc_attraction)
    return num