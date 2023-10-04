# -------------------- Case 1: 13/30 -------------------- 
# def solution(queue1, queue2):
#     all_sum = sum(queue1) + sum(queue2)
    
#     if all_sum % 2 == 1:
#         return -1
    
#     count = 0
#     answer = all_sum // 2
#     prefix = queue1 + queue2
#     length = len(prefix)
        
#     # Calculating prefix sum
#     for i in range(1, length):
#         prefix[i] += prefix[i-1]
        
#     # Calculating min len dif
#     for start in range(length-1):
#         for end in range(start+1, length):
#             if prefix[end] - prefix[start] == answer:
#                 count = start + end - len(queue1) + 2
#                 return count
                
#     return -1


# -------------------- Case 2: 28/30(9, 14) --------------------
# def solution(queue1, queue2):
#     mid_sum, ep = 0, 0
#     full_que = queue1 + queue2
    
#     if sum(full_que) % 2 == 1:
#         return -1
        
#     half = sum(full_que) // 2
    
#     for sp in range(len(full_que)):
#         while mid_sum < half and ep < len(full_que):
#             mid_sum += full_que[ep]
#             ep += 1
            
#         if mid_sum == half:
#             return sp + ep - len(queue1)
        
#         mid_sum -= full_que[sp]
    
#     return -1


# -------------------- Case 3: 28/30(9, 14) --------------------
# def solution(queue1, queue2):    
#     mid_sum, ep = 0, 0
#     fullQ = queue1 + queue2
#     length = len(queue1)
    
#     half = sum(fullQ) // 2
    
#     for sp in range(len(fullQ)):
#         while mid_sum < half and ep < len(fullQ):
#             mid_sum += fullQ[ep]
#             ep += 1
            
#         if mid_sum == half:
#             if sp >= length and ep >= length:
#                 sp -= length
#                 ep -= length
            
#             if sp < length and ep < length:
#                 if sp == 0:
#                     return ep + length
#                 elif ep == length - 1:
#                     return sp
#                 else:
#                     return ep + sp + length
            
#             else:
#                 return sp + ep - length
        
#         mid_sum -= fullQ[sp]
    
#     return -1


# -------------------- Case 4: AC --------------------
from collections import deque

def solution(queue1, queue2):
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    sumQ1 = sum(queue1)
    sumQ2 = sum(queue2)
    
    count = 0
    
    for _ in range(len(queue1) * 3):
        if sumQ1 == sumQ2:
            return count
        
        if sumQ1 > sumQ2:
            count += 1
            sumQ1 -= queue1[0]
            sumQ2 += queue1[0]
            queue2.append(queue1.popleft())
            
        else:
            count += 1
            sumQ1 += queue2[0]
            sumQ2 -= queue2[0]
            queue1.append(queue2.popleft())
    
    return -1