table = [[0 for i in range(253)] for j in range(53)] 
cal = [[False for i in range(253)] for j in range(53)] 

def coins(i, value,numberofcoins,c):
    if value==0:
        return 1
    if value<0:
        return 0
    if i>numberofcoins:
        return 0
    if cal[i][value]!=True:
        table[i][value] = coins(i,value-c[i-1],numberofcoins,c)+coins(i+1,value,numberofcoins,c)
        cal[i][value] = True
    
    return table[i][value]
    

c1 = list(map(int, input().split()))
value = c1[0]
numberofcoins = c1[1]

c = list(map(int, input().split()))
print(coins(1,value,numberofcoins,c))
