'''
Created on 20 Jun 2021

@author: vishalmudgal
'''
import random


class MillerRabin(object):

    def __init__(self, num, k):
        self.n = num
        self.k = k
        
    def mrt_start(self):
    
        # Implementation uses the Miller-Rabin Primality Test
        # The optimal number of rounds for this test is 40
        # See http://stackoverflow.com/questions/6325576/how-many-iterations-of-rabin-miller-should-i-use-for-cryptographic-safe-primes
        # for justification
    
        # If number is even, it's a composite number
    
        if self.n == 2 or self.n == 3:
            return True
     
        if self.n == 1:
            return False
        
        if self.n % 2 == 0:
            return False
    
        r, s = 0, self.n - 1
        while s % 2 == 0:
            r += 1
            s //= 2
        for _ in range(self.k):
            a = random.randrange(2, self.n - 1)
            x = pow(a, s, self.n)
            if x == 1 or x == self.n - 1:
                continue
            for _ in range(r - 1):
                x = pow(x, 2, self.n)
                if x == self.n - 1:
                    break
            else:
                return False
        return True
    
check_primality = MillerRabin(1,40).mrt_start()
print (check_primality)
    