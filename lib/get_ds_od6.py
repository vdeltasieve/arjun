'''
Created on 25 Jul 2021

@author: vishalmudgal
'''

import math
import decimal
decimal.getcontext().prec = 500

class OD6(object):
    
    '''
    Calculate od6 for any delta
    '''

    def __init__(self, dial1_list, n):

        self.a1 = dial1_list[0]
        self.a2 = dial1_list[1]
        self.n = n
        self.v1 = 2
        self.v2 = 2
    
    def get_od6(self):
        
        n_root = math.floor(decimal.Decimal(self.n).sqrt())
        
        if n_root % 2 == 0:
            d1 = n_root + self.a1  # 0 or -1
            d2 = d1 + self.v1      #2
        elif n_root % 2 == 1:
            d1 = n_root + self.a2  # -1 or 0
            d2 = d1 + self.v2      #2
            
        else:
            print ("Some error in OD6, exiting")
            exit(0)
        
        d1_square = d1 * d1
        d2_square = d2 * d2
        
        od1 = math.floor(d1_square - self.n)
        od2 = math.floor(d2_square - self.n)
        
        od6_inter = 4*self.n + (od1 * od2)
        od6 = math.floor(decimal.Decimal(od6_inter).sqrt())
        
        return (od6)
    
