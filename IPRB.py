import math

def dominant(k,m,n):
    g = 4 * (math.comb(k+m+n,2))
    r = 4 * (math.comb(n,2)) + 2 * m * n + (math.comb(m,2))
    print(1-(r/g))
dominant(30,24,23)