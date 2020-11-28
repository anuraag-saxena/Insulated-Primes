"""_____________________________________________________________
    
    Insulated Primes source code
    
    Developed in Python 3.8
    
    Programmers : A. Saxena and A. Kumar
    
    Main paper  : A. Kumar and A. Saxena, Insulated Primes,
                  Bull. Belgian Math. Soc. - Simon Stevin (2020)
    
    E-mail      : akumar2307@outlook.com 
                  anuraagsaxena28@gmail.com
    
    Date        : 18 October, 2020
    
    _____________________________________________________________  
"""

import sympy as sy
import math as mh

# p is a Global prime
p = 0 

def func(c):
    return sy.primepi(p+c) - sy.primepi(p-c) - 1 
   
    
def D(p):
    m = 0.5*mh.log(2*p + mh.log(2))-0.5*mh.log(2)
    m = mh.ceil(m)                
    if (func(m) == 0):
        m0 = m
        m1 = p
    else:
        m0 = 1
        m1 = m
    return bisection(m0, m1)
    

def bisection(a,b): 
    c = 0
    while (abs(b-a) > 1): 
        # Find middle point 
        c = int((a+b)/2)
        # Check if middle point is 
        if (func(c) == 0.0): 
            a = c
        else:
            b = c
    return a




# Modified code for faster evaluation of Degree of insulation
p = int(input("Input a prime = "));  
print(D(p))




    
    
    