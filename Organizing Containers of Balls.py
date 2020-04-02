q = int(input().strip())
def swap(M, n):
    boxCount = [sum(row) for row in M]
    ballCount = [0 for row in M]
    for i in range(n):
        for row in M:
            ballCount[i] += row[i]
    for ballC in ballCount:
        if ballC not in boxCount:
            return "Impossible"
    for boxC in boxCount:
        if boxC not in ballCount:
            return "Impossible"
    return "Possible"
for a0 in range(q):
    n = int(input().strip())
    M = []
    for M_i in range(n):
       M_t = [int(M_temp) for M_temp in input().strip().split(' ')]
       M.append(M_t)
    # your code goes here
    print(swap(M, n))
        
