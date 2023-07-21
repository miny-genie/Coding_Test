''' -------------------- Google #1 -------------------- '''
# -------------------- Import --------------------
import sys
ipnut = sys.stdin.readline

# -------------------- Function --------------------
def MaxmizeEqualNumbers(n, k, a):
    # Val Initialization
    lst = [[] for _ in range(n)]
    
    ''' Mistake : out of padding '''
    # Dimension 2 array initialization
    for arrIndex in range(len(a)):
        for x in range(-k, k + 1):
            lst[arrIndex].append(a[arrIndex] + x)
             
    # Calculate maxinum length of the subsequence
    max_length = -1e9
    for i in range(k * 2 + 1):
        tmpArr = []
        for Xindex in range(n):
            tmpArr.append(lst[Xindex][i])
            
        # Maxlength tmpArr
        cnt, tmp = 0, 0
        for i in range(len(tmpArr)):
            if i == 0:
                tmp = tmpArr[i]
                cnt += 1

            if tmp == tmpArr[i]:
                cnt += 1
            else:
                tmp = tmpArr[i]
                cnt = 1
                    
        max_length = max(max_length, cnt)
            
    return max_length

# -------------------- Main --------------------
T = int(input())
for _ in range(T):
    # N : array size, K : int
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    n, k, a = 4, 3, [1, 5, 3, 1]
    
    out_ = MaxmizeEqualNumbers(n, k, a)
    print(out_)
    
# -------------------- Test Case --------------------
''' Test #1
2
4 2
2 2 5 6
3 2
1 5 6

2
2 '''

''' Test #2
1
4 1
3 3 3 5

4'''

''' Test #3
1
4 3
1 5 3 1

4'''




''' ------------------------------------------------------------- 2023.03.10 ------------------------------------------------------------- '''
''' -------------------- Google STEP 01 -------------------- '''
# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Function ----------
def max_length(size, gap, lst):
    # crd = coordinate
    crd_length = (max(lst) + gap) - (min(lst) - gap) + 1
    crd = [ [0 for _ in range(crd_length)] for _ in range(size)]
    
    # Coordinate Array Initialization
    for i in range(size):
        for changeIndex in range(lst.index(lst[i])-gap, lst.index(lst[i])+gap+1):
            crd[i][changeIndex] = 1
    
    # Count Max Equal Number Length
    maxCnt = 0
    
    for Yindex in range(crd_length):
        cnt = 0
        
        for Xindex in range(size):
            if crd[Xindex][Yindex]:
                cnt += 1
                maxCnt = max(maxCnt, cnt)
            else:
                cnt = 0
    
    print(crd)
    
    return maxCnt

# ---------- Main ----------
T = int(input())

for _ in range(T):
    size, gap = map(int, input().split())
    lst = list(map(int, input().split()))
    
    print(max_length(size, gap, lst))
    
    
    
''' ------------------------------------------------------------- 2023.03.10 ------------------------------------------------------------- '''
''' -------------------- Google STEP 01 -------------------- '''
# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Function ----------
def max_length(size, gap, lst):
    # crd = coordinate
    crd_length = (max(lst) + gap) - (min(lst) - gap) + 1
    crd = [ [0 for _ in range(crd_length)] for _ in range(size)]
    
    print(crd)
    
    # Coordinate Array Initialization
    for i in range(size):
        TMP = gap - lst[0]
        
        for changeIndex in range(lst[i] - gap + TMP, lst[i] + gap + 1 + TMP):    # lst[i]-gap ~ lst[i]+gap+1
            crd[i][changeIndex] = 1
    
    # Count Max Equal Number Length
    maxCnt = 0
    
    for Yindex in range(crd_length):
        cnt = 0
        
        for Xindex in range(size):
            if crd[Xindex][Yindex]:
                cnt += 1
                maxCnt = max(maxCnt, cnt)
            else:
                cnt = 0
    
    print(crd)
    
    return maxCnt

# ---------- Main ----------
T = int(input())

for _ in range(T):
    size, gap = map(int, input().split())
    lst = list(map(int, input().split()))
    
    print(max_length(size, gap, lst))
    
    
    '''
    # Coordinate Array Initialization
    for i in range(size):
        startNode=lst[i]-lst[0]
        for changeIndex in range(0, crd_length):    # lst[i]-gap ~ lst[i]+gap+1
            if(startNode<=changeIndex):
                if(changeIndex<=startNode+gap*2):
                    crd[i][changeIndex] = 1
    '''
    
    '''
     lst[i]-gap ~ lst[i]+gap+1


 3 2
 1 5 6

[ +1 ] >
-10123 > 01234
 34567 > 45678
 45678 > 56789

-1 0 1 2 3 4 5 6 7 8
---------------------
 1 1 1 1 1 0 0 0 0 0
 0 0 0 0 1 1 1 1 1 0
 0 0 0 0 0 1 1 1 1 1
---------------------
 1 1 1 0 0 0 0 0 1 1
 1 1 1 1 0 0 0 0 0 1
 1 1 1 1 1 0 0 0 0 0

==============================================

 4 0
 2 2 5 6

[ -2 ] > 
2 > 0
2 > 0
5 > 3
6 > 4

 2 3 4 5 6
--------------------
 1 0 0 0 0
 1 0 0 0 0
 0 0 0 1 0
 0 0 0 0 1
--------------------
     1 0 0 0 0
     1 0 0 0 0
     0 0 0 1 0
     0 0 0 0 1

==============================================

 4 1
 3 3 3 5

[ -2 ]
234 > 012
234 > 012
234 > 012
456 > 234

 2 3 4 5 6
--------------------
 1 1 1 0 0
 1 1 1 0 0
 1 1 1 0 0 
 0 0 1 1 1
--------------------
       1 1 1 0 0
       1 1 1 0 0
       1 1 1 0 0
       0 0 1 1 1

==============================================

 4 3
 1 5 3 1

 -2 -1 0 1 2 3 4 5 6 7 8
--------------------------
  1  1 1 1 1 1 1 0 0 0 0
  0  0 0 0 1 1 1 1 1 1 1
  0  0 1 1 1 1 1 1 1 0 0
  1  1 1 1 1 1 1 0 0 0 0
--------------------------
  1  1 1 1 1 0 0 0 0 1 1
  0  0 1 1 1 1 1 1 1 0 0
  1  1 1 1 1 1 1 0 0 0 0
  1  1 1 1 1 0 0 0 0 1 1

    '''