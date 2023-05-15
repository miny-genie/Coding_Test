''' -------------------- Google #2 -------------------- '''
# -------------------- Import --------------------
import sys
input = sys.stdin.readline

# -------------------- Function --------------------
def solve(N, A):
    # Value Initialization
    maxCnt = -1e9
    
    # Not Change 1 to 0
    tmpTotalArr, tmpArr = [], []
    for i in range(1,  N + 1):
        for index in range(0, len(A) - i + 1):
            tmpArr.append(A[index])
            
        tmpTotalArr.append(tmpArr)
        
        maxCnt = max(maxCnt, len(tmpTotalArr))
        
    ''' Change 1 to 0 pesudo code '''
    for index in A:
        if index == 1:
            A[index] = 0
            
            ''' Counting same code 'not change 1 to 0' '''
            
    return maxCnt

# -------------------- Main --------------------
T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    
    out_ = solve(N, A)
    print(out_)

# -------------------- Comment --------------------
# There is an ERROR in Explanation
# NOT [1, 0, 0, 0, 0, 1], RIGHT [1, 0, 0, 0, 1]

# -------------------- Test Case --------------------
''' Test #1
2
5
1 0 0 1 1
7
1 0 1 1 1 0 1

13
24'''

''' Test #2
4
7
1 1 1 1 1 1 1
6
0 0 0 0 1 1
6l
0 1 0 1 0 1
6
1 1 0 0 1 1

16
20
19
17'''