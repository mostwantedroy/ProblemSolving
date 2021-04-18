# # -*- coding: utf-8 -*-
# # UTF-8 encoding when using korean

# N = int(input())

# times = []

# for _ in range(N):
#     times.append(input())

# times = list(map(lambda x:x.split(' ~ '), times))

# # for element in times_new : element[0], element[1]

# times.sort(key = lambda x:x[0], reverse = True)

# start = -1

# for i in range(N):
#     is_start = True
    
#     for j in range(N):
#         if i == j:
#             continue
#         if times[i][0] < times[j][0] or times[i][0] > times[j][1]:
#             is_start = False
#             break
    
#     if is_start:
#         start = i
#         break

# end = -1

# for i in range(N):
#     is_end = True

#     for j in range(N):
#         if i == j:
#             continue
#         if times[i][1] > times[j][1] or times[i][1] < times[j][0]:
#             is_end = False
#             break
    
#     if is_end:
#         end = i
#         break

# if start == -1 or end == -1:
#     print(-1)
# else:
#     answer = times[start][0] + " ~ " + times[end][1]
#     print(answer)

s = 'Tassadar'

print(s)