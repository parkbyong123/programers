def solution(s):
    if len(s) == 1:
        return 1
    lens = int(len(s)/2)
    comp = []
    for i in range(1, lens + 1): #나누는 수
        string_s = ""
        count_n = 1
        for j in range(0, len(s), i): # 문자열 비교
            if s[j:j+i] == s[j+i:j+i+i]:
                count_n += 1
            else:
                if count_n >= 2:
                    string_s = string_s + str(count_n) + s[j:j+i]
                    count_n = 1
                else:
                    string_s = string_s + s[j:j+i]
        comp.append(len(string_s))
    answer = min(comp)
    
    return answer
