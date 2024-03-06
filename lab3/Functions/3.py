def solve(numhead, numlegs):
    chick = 0
    rabbit = 0
    
    for chick in range(numhead+1):
        rabbit = numhead - chick
        if (2*chick + 4*rabbit == numlegs):
            return chick, rabbit
        
    return 0, 0

h = int(input())
l = int(input())
c , r = solve(h, l)

if (c != 0) and (l != 0):
    print(c, r)
else:
    print("No solution")
