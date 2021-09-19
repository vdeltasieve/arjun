'''
@author: vishalmudgal
'''

import math
import decimal
decimal.getcontext().prec = 500

class SSV_OD_N(object):

    '''
    Get steady state value
    '''

    def __init__(self, f1, f2, a1, a2, v1, v2):
        
        #self.next_f1 = prev_f1 + 2
        #self.next_f2 = prev_f2 + 2
        self.f1 = f1
        self.f2 = f2
        self.n = self.f1 * self.f2
        self.a1 = a1
        self.a2 = a2
        self.v1 = v1
        self.v2 = v2
        
        
    def confirm(self):
        
        n_root = math.floor(decimal.Decimal(self.n).sqrt())
        
        if n_root % 2 == 0:
            d1 = n_root + self.a1 # 0 or -1
            d2 = d1 + self.v1 #2
        else:
            d1 = n_root + self.a2 # -1 or 0
            d2 = d1 + self.v2 #2
        
        d1_square = d1 * d1
        d2_square = d2 * d2
        
        od1 = math.floor(d1_square - self.n)
        od2 = math.floor(d2_square - self.n)
        od3 = math.floor(od2 - od1)
        od4 = math.floor(od2 + od1)
        od5 = od1 + od2 + od3 + od4
        
        '''
        print ("DEBUG SSV_OD2_OD4 ")
        print ("a1=%d, a2=%d, v1=%d, v2=%d" %(self.a1, self.a2, v1, v2))
        print ("d1=%d, d2=%d, d1_square=%d, d2_square=%d" %(d1, d2, d1_square, d2_square))
        print ("od1=%d,od2=%d,od3=%d,od4=%d,od5=%d"%(od1, od2, od3, od4, od5))
        '''
        return (od2, od4, od5)
    

        
        
        
