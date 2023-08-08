# ---------- Import ----------
from itertools import product

# ---------- Function ----------
def solution(users, emoticons):
    answer = [0, 0]
    sales = [10, 20, 30, 40]
    
    for sale in product(sales, repeat=len(emoticons)):
        subscribe = 0
        people = [0] * len(users)
        
        # print(list(zip(emoticons, sale)), end=" ")
        for idx, (personal_percent, total) in enumerate(users):
            for price, sale_percent in zip(emoticons, sale):
                if personal_percent <= sale_percent:
                    people[idx] += price * (100 - sale_percent) // 100
                    
            if total <= people[idx]:
                # print(idx, personal_percent, total, people[idx], end=" ")
                people[idx] = 0
                subscribe += 1
                
        # print(subscribe, sum(people))
        answer.append((subscribe, sum(people)))
    
    return list(sorted(answer, key=lambda x: (-x[0], -x[1]))[0])

# ---------- Main ----------
list_ = [
    [[[40, 10000],
      [25, 10000]],
     [7000, 9000]],              # [1, 5400]
    [[[40, 2900], 
      [23, 10000], 
      [11, 5200], 
      [5, 5900], 
      [40, 3100], 
      [27, 9200], 
      [32, 6900]],
     [1300, 1500, 1600, 4900]]    # [4, 13860]
]

for users, emoticons in list_:
    result = solution(users, emoticons)
    print(result)