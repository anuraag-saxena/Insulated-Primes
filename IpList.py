import sympy as sy

def IpList(D):
    I = [];
    for N in range(1, len(D)-1):
        if (D[N-1]<D[N] and D[N+1]<D[N]):
            I.append(sy.prime(N+1));
    return I