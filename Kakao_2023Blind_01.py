# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Function ----------
def solution(today, terms, privacies):
    answer = []
    
    # Changing today, str to int 
    today = int(today.replace(".", ""))
    
    # Changing terms, list to dictionary 
    term = {}
    for i in terms:
        alphabet, month = i.split(" ")
        term[alphabet] = int(month)

    # Checking each privacies
    for i, v in enumerate(privacies):
        date, alphabet = v.split(" ")
        year, month, day = map(int, date.split("."))

        # Updating year and month
        month += term[alphabet]
        year += (month // 12)
        month -= (month // 12 * 12)
        
        # Updating day
        day -= 1
        if day < 1: month -= 1; day = 28
        if month < 1: year -= 1; month = 12
        
        # Compare today and end_date
        end_date = (year*10000) + (month*100) + day
        if today - end_date > 0: answer.append(i+1)
        
    return answer

# ---------- Main ----------
today = "2022.05.19"
terms = ["A 6", "B 12", "C 3"]
privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]

result = solution(today, terms, privacies)
print(result)

# ---------- Comment ----------
# today: "2022.05.19"
# terms: ["A 6", "B 12", "C 3"]
# privacies: ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]
# result: [1, 3]

# today: "2020.01.01"
# terms: ["Z 3", "D 5"]
# privacies: ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]
# result: [1, 4, 5]

# ---------- Other Solutoin ----------
def to_days(date):
    year, month, day = map(int, date.split("."))
    return year * 28 * 12 + month * 28 + day

def solution(today, terms, privacies):
    months = {v[0]: int(v[2:]) * 28 for v in terms}
    today = to_days(today)
    expire = [
        i + 1 for i, privacy in enumerate(privacies)
        if to_days(privacy[:-2]) + months[privacy[-1]] <= today
    ]
    return expire