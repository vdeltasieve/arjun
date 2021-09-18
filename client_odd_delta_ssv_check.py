'''
Created on 1 Aug 2021

@author: vishalmudgal
'''

import sys
import math
import decimal
decimal.getcontext().prec = 50

class Odd_Delta_SSV_Check(object):
    '''
    classdocs
    '''

    def __init__(self, p_start, delta, delta_end, v1, v2, depth_limit):
        '''
        Constructor
        '''
        self.p_start = p_start
        self.g_id = 1
        self.delta = delta
        self.delta_end = delta_end
        self.v1 = v1
        self.v2 = v2
        self.depth_limit = depth_limit
        
        if self.delta % 2 == 0:
            print ("Even delta given as input, expecting odd delta, exiting")
            exit(0)
        else:
            pass
        
    def set_dials(self, v1, v2):
        
        self.v1 = v1
        self.v2 = v2
        
        if ((self.delta % 4 == 3) and (self.p_start % 2 == 1)) \
           or ((self.delta % 4 == 1) and (self.p_start % 2 == 0)):
            
            self.a1 = -1
            self.a2 = 0
            
        elif ((self.delta % 4 == 1) and (self.p_start % 2 == 1)) \
            or ((self.delta % 4 == 3) and (self.p_start % 2 == 0)):
            
            self.a1 = 0
            self.a2 = -1
        
        else:
            print ("Input delta is not configured to run, exit")
            exit(0)
            
    def get_ssv(self):
        
        self.ssv = (self.delta * self.delta) + 3
        
        
    def get_od5(self, p):
        
        self.q = p + self.delta
        self.n = self.q * p
        n_root = math.floor(decimal.Decimal(self.n).sqrt())
        
        if n_root % 2 == 0:
            d1 = n_root + self.a1
            d2 = d1 + self.v1
            
        elif n_root % 2 == 1:
            d1 = n_root + self.a2
            d2 = d1 + self.v1
        else:
            pass    
        
        od1 = (d1 * d1) - self.n
        od2 = (d2 * d2) - self.n
        od3 = od2 - od1
        od4 = od2 + od1
        od5 = od1 + od2 + od3 + od4
        
        return (od5)

    def start(self):
        
        while (self.delta >= self.delta_end):
            
            self.set_dials(self.v1, self.v2)
            self.get_ssv()
            
            condition = True
            p = self.p_start
            iteration_counter = 0
            while (condition):
                
                od5 = self.get_od5(p)
                
                if (od5 == self.ssv):
                    
                    iteration_counter += 1
                    print ("MATCH -> delta=%d, p=%d, q=%d, n=%d, od5=%d, ssv=%d, a1=%d, a2=%d" 
                           %(self.delta, p, self.q, self.n, od5, self.ssv, self.a1, self.a2))
                else:
                    print ("NOT-MATCH -> delta=%d, p=%d, q=%d, n=%d, od5=%d, ssv=%d, a1=%d, a2=%d" 
                           %(self.delta, p, self.q, self.n, od5, self.ssv, self.a1, self.a2))
                
                if iteration_counter >= self.depth_limit:
                    print ("\n")
                    break
                else:
                    pass
                
                p += 2
            
            self.g_id += 1       
            self.delta -= 4


mode = 1

if mode == 0:
    print ("Initiated from Command Line")
    
    #2 27 21 2 2 1000
    
    # Command line input handling
    p_start = int(sys.argv[1])
    delta = int(sys.argv[2])
    delta_end = int(sys.argv[3])
    v1 = int(sys.argv[4])
    v2 = int(sys.argv[5])
    depth_limit = int(sys.argv[6])
        
    client = Odd_Delta_SSV_Check(p_start, delta, delta_end, v1, v2, depth_limit)
    client.start()

elif mode == 1:
    
    client = Odd_Delta_SSV_Check(2, 27, 21, 2, 2, 1000)
    client.start()

else:
    print ("Mode Not Supported")
    exit(0)
        

        