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



from DpList import *
from IpList import *

# It prints the list of insulated primes less than or equal to n
n = int(input("Input for range of p = "));  

D = DpList(n)
#print(D)

I = IpList(D)
print(I)


