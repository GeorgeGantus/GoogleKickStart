def getLower(n):
    num = 0
    odd_flag = False
    for c in n:
        num = num * 10
        if odd_flag:
            num += 8
            continue

        if int(c) % 2 != 0:
            num += int(c)-1
            odd_flag = True
        else:
            num += int(c)
    return num

def getHigher(n):

    i = 0
    while int(n[i]) % 2 == 0:
        i += 1
        if i == len(n):
            return int(n)

    # odd founded
    suffix = '0' * (len(n)-i-1)
    prefix = ''
    carry = 0
    while i >= 0 or carry == 1:
        #print('i: ',i)
        value = int(n[i]) + carry if i >= 0 else carry
        i -= 1
        if value == 10 or value == 9:
            currentChar = '0'
            carry = 1
        
        if value % 2 == 1 and value != 9:
            currentChar = str(value+1)
            carry = 0
        
        if value % 2 == 0:
            currentChar = str(value)
            carry = 0
        
        #print('curr: ', currentChar)
        prefix = currentChar + prefix
    
    return int(prefix + suffix)

def solution(n):
    lower = getLower(n)
    higher = getHigher(n)
    number = int(n)

    return min(higher - number, number - lower)

t = int(input())
for case in range(t):
    n = input()
    print("Case #{}: {}".format(case+1, solution(n)))

