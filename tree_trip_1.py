# 7% Task Score, 12% Correctness, 0% Performance
# https://app.codility.com/programmers/task/tree_trip/

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from collections import defaultdict

def solution(K, C, D):
    # write your code in Python 3.6
    if K == 0: return 0
    adj_lst = defaultdict(list)
    for j in range(len(C)):
        if j not in adj_lst or C[j] not in adj_lst[j]:
            adj_lst[j].append(C[j])
        if C[j] not in adj_lst or j not in adj_lst[C[j]]:
            adj_lst[C[j]].append(j)
    cities = [x for x,y in sorted(enumerate(D), key = lambda x: x[1])]
    num = 1
    # print(cities)
    # print(adj_lst)
    i = len(cities) - 1
    # queue = [cities[i]]
    minimum_attractiveness = D[cities[i]]
    connected = []
    connected += adj_lst[cities[i]]
    final = [cities[i]]
    flag = True
    while num < K:
        # print(final, minimum_attractiveness, i)
        # print(connected)
        if D[cities[i-1]] == minimum_attractiveness and cities[i-1] in connected:
            num +=1
            final.append(cities[i-1])
            connected += adj_lst[cities[i-1]]
            connected = list(set(connected))
            i -= 1
        elif D[cities[i-1]] == minimum_attractiveness and cities[i-1] not in connected:
            i -= 1
            flag = False
        elif D[cities[i-1]] < minimum_attractiveness and cities[i-1] in connected:
            if flag == False:
                break
            else:
                num += 1
                final.append(cities[i-1])
                minimum_attractiveness = D[cities[i-1]]
                connected += adj_lst[cities[i-1]]
                connected = list(set(connected))
                i -= 1
        elif D[cities[i-1]] < minimum_attractiveness and cities[i-1] not in connected:
            break
        
    # print(final)
    return num
        # candidate_city = queue.pop()
        # if D[candidate_city] >= minimum_attractiveness:
        #     final.append(candidate_city)
        #     num += 1
        #     i -= 1
        #     minimum_attractiveness = D[cities[i-1]]
        #     for city in adj_lst[candidate_city]:
        #         if city not in final:
        #             queue.append(city)
                  
    return num