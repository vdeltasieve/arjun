'''
@author: vishalmudgal
'''

#from math import ceil

class Fermat(object):

    '''
    Use Fermat Factorization method to factorize the number
    '''

    def __init__(self, number_to_factorize):
        
        self.number_to_factorize = number_to_factorize
        self.NOT_INT_VAL = True

    def isqrt(self,n):
        x = n
        y = (x + n // x) // 2
        while y < x:
            x = y
            y = (x + n // x) // 2
        return x
    
    def factorise(self, verbose=False):
        a = self.isqrt(self.number_to_factorize) # int(ceil(n**0.5))
        b2 = a*a - self.number_to_factorize
        b = self.isqrt(self.number_to_factorize) # int(b2**0.5)
        count = 0
        while b*b != b2:
            if verbose:
                print('Trying: a=%s b2=%s b=%s' % (a, b2, b))
            a = a + 1
            b2 = a*a - self.number_to_factorize
            b = self.isqrt(b2) # int(b2**0.5)
            count += 1
        p=a+b
        q=a-b
        
        assert self.number_to_factorize == p * q
        #print('a=',a)
        #print('b=',b)
        #print('p=',p)
        #print('q=',q)
        #print('pq=',p*q)
        return q, p

'''
n=137

fermat = FermatFactorization(n).factorise()
print (fermat)
'''


        
