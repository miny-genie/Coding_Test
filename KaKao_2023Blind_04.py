def solution(numbers):
    def proof(num):
        bnum = bin(num)[2:]
        len_bin = len(bin(num)[2:])
        next_squ2minus1 = (2 ** (len(bin(len_bin)[2:]))) - 1

        fill = bnum.zfill(next_squ2minus1)
        
        for idx, val in enumerate(fill, 1):
            if idx % 2 == 0 and val == "0":
                half = (idx & (-idx)) // 2
                bef_idx = idx - half - 1
                aft_idx = idx + half - 1
                
                if int(fill[bef_idx]) + int(fill[aft_idx]):
                    return 0 
                
        return 1
    
    answer = []
    for num in numbers:
        answer.append(proof(num))
        
    return answer