'''
Created on 19 Jul 2021

@author: vishalmudgal
'''
import math
import decimal
decimal.getcontext().prec = 500

class Quadratic_Roots(object):

    def __init__(self, a, b, c):
        
        self.a = a
        self.b = b
        self.c = c
        
    def get_discriminant(self):
        
        self.d = (self.b**2) - (4 * self.a * self.c)
        
    def get_solutions(self):
        
        # find two solutions
        d_sqrt = math.floor(decimal.Decimal(self.d).sqrt())
        self.sol1 = (-self.b - d_sqrt)//(2*self.a)
        self.sol2 = (-self.b + d_sqrt)//(2*self.a)
        
        p = math.floor(self.sol1.real)
        q = math.floor(self.sol2.real)
        
        return (p, q)
        #print('The solution are {0} and {1}'.format(self.sol1,self.sol2))
    
    def start(self):
        
        self.get_discriminant()
        p, q = self.get_solutions()
        
        return (p, q)

#quadratic_obj = Solve_Quadratic(1, -9, 20)
#p, q = quadratic_obj.start()
#print (p, q)
    
    
     