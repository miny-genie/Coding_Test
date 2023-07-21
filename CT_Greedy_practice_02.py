# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Main ----------
N, M, K = map(int, input().split())
num = list(map(int, input().split()))

num.sort()
fir, sec = num[-1], num[-2]

sec_times = (M // K)
fir_times = M - sec_times

print(fir * fir_times + sec * sec_times)
