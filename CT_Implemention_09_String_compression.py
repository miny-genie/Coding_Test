# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Function ----------
def solution(s):
    answer = len(s)
    
    for step in range(1, len(s) // 2 + 1):
        cnt = 1
        length = ""
        tmp = s[0:step]
        
        for i in range(step, len(s), step):
            if tmp == s[i:i + step]:
                cnt += 1
            else:
                length += str(cnt) + tmp if cnt > 1 else tmp
                cnt = 1
                tmp = s[i:i + step]
        
        length += str(cnt) + tmp if cnt > 1 else tmp
        answer = min(answer, len(length))
    
    return answer

# ---------- Main ----------
N = input()
print(solution(N))