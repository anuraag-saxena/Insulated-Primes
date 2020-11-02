import sympy as sy

def DpList(n):
    D = [];
    for p in sy.primerange(1,n+3):
        m = 1;
        while (sy.primepi(p-m) == sy.primepi(p+m)-1):
            m=m+1;
        D.append(m-1);
    return D
