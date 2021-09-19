'''
Created on 24 Jul 2021

@author: vishalmudgal
'''

import sys
#sys.path.append('../../')
#print (sys.path)

from lib.get_ds_n_at_ssv import N_DS_SSV
from lib.get_ds_p_at_ssv import P_DS_SSV
from lib.get_ds_ssv import SSV
from lib.get_quadratic_roots import Quadratic_Roots
from lib.get_ssv_od_n import SSV_OD_N
from lib.get_fermat import Fermat

# SSV = Static State Value
class SSV_P_Check(object):
    '''
    This tests the steady state value (ssv) hypothesis in zone0 and value of p when ssv first appears in zone0 of a delta sieve zone for any delta
    '''

    def __init__(self, dial1_list, delta_start, depth, depth_multiplier=1):
        
        self.dial_list = dial1_list
        self.a1 = dial1_list[0]
        self.a2 = dial1_list[1]
        self.v1 = 2
        self.v2 = 2
        
        self.g_id = 1
        self.p_eo_list = [1,2]
        #self.delta_start_value = 2000000000000000000000000000000000000000000000000
        #self.delta_start_value = 2876393169334930957949582465709212479869734304942
        self.delta_start_value = delta_start
        self.delta_end_value = 12
        
        self.go_deep = -depth * depth_multiplier
        #self.go_deep = -1370000 * go_deep_multiplier
        #random_large = [1000, 2000, 1245679, 98735]
        
    
    def check_via_qe(self, ssv, p_eo, p_val, n, DEBUG=False):
        
        get_ssv = ssv
        get_p = p_val
        get_n_at_ssv = n
        
        quadratic_soln = Quadratic_Roots(1, self.delta_start_value, -get_n_at_ssv).start()
        root_1 = quadratic_soln[1]
        if root_1 != get_p:
            print ("ERROR in p:", self.delta_start_value, p_eo, get_n_at_ssv, get_p, root_1)
            exit(0)
        
        elif root_1 == get_p:
            if DEBUG == True:
                print ("delta=%d, p=%d, n_at_ssv=%d, ssv=%d, p_formula=%d, root_1=%d" \
                       %(self.delta_start_value, p_eo, get_n_at_ssv, get_ssv, get_p, root_1))
        
            p = get_p
            q = get_p + self.delta_start_value
            
            # Go Deep to confirm if SSV continues
            self.ssv_confirmation(p_eo, p, q, get_ssv, DEBUG=DEBUG)
        
        
        else:
            print ("Some other error inside -> Client_SSV_P_Check, exiting")
            exit(0)       
    
    def check_via_fermat(self, ssv, p_eo, p_val, n, DEBUG=False):
        
        get_ssv = ssv
        get_p = p_val
        get_n_at_ssv = n
        
        factor = Fermat(get_n_at_ssv).factorise()
        factor_1 = factor[0]
        factor_2 = factor[1]
        
        if factor_1 != get_p:
            print ("ERROR in p:", self.delta_start_value, p_eo, get_n_at_ssv, get_p, factor_1, factor_2)
            exit(0)
        
        elif factor_1 == get_p:
            if DEBUG == True:
                print ("delta=%d, p=%d, n_at_ssv=%d, ssv=%d, p_formula=%d, p_fermat=%d" \
                       %(self.delta_start_value, p_eo, get_n_at_ssv, get_ssv, get_p, factor_1))
        
            p = get_p
            q = get_p + self.delta_start_value
            # Go Deep to confirm if SSV continues
            self.ssv_confirmation(p_eo, p, q, get_ssv, DEBUG=DEBUG)
        
        else:
            print ("Some other error inside -> Client_SSV_P_Check, exiting")
            exit(0)
    
    
    def check_via_q(self, ssv, p_eo, p_val, n, DEBUG=False):
        
        get_ssv = ssv
        p = p_eo
        get_p = p_val
        get_n_at_ssv = n
        
        q = get_p + self.delta_start_value
        n_check = q * get_p
        
        if n_check != get_n_at_ssv:
            print ("ERROR in p:", self.delta_start_value, p, get_n_at_ssv, get_p, q)
            exit(0)
            
        elif n_check == get_n_at_ssv:
            if DEBUG == True:
                print ("delta=%d, p=%d, n_at_ssv=%d, ssv=%d, p_formula=%d, q=%d" \
                       %(self.delta_start_value, p, get_n_at_ssv, get_ssv, get_p, q))
            
            # Go Deep to confirm if SSV continues
            self.ssv_confirmation(p_eo, get_p, q, get_ssv, DEBUG=DEBUG)
            
        else:
            print ("Some other error inside -> Client_SSV_P_Check, exiting")
            exit(0)
            
                
    def ssv_confirmation(self, p_eo, p, q, ssv, DEBUG=False):
        
        counter_at_ssv = -1
        while (counter_at_ssv >= self.go_deep):
            
            #print ("Inside While...")
            od2, od4, od5 = SSV_OD_N(p, q, self.a1, self.a2, self.v1, self.v2).confirm()
            
            # UC-A
            if (self.a1 == 0) and (self.a2 == -1):
                
                # OD-4
                if  ((self.delta_start_value % 4 == 2) and (p_eo % 2 == 0)) or \
                    ((self.delta_start_value % 4 == 0) and (p_eo % 2 == 1)):
                    
                    if (ssv == od4):
                        if DEBUG == True:
                            print ("delta=%d, counter=%d, p_eo=%d, ssv=%d, od2=%d, od4=%d, p=%d, q=%d, n=%d" \
                               %(self.delta_start_value, counter_at_ssv, p_eo, ssv, od2, od4, p, q, p*q)) 
                
                    else:
                        print ("ERROR: Static State Breached")
                        print ("p_eo=%d, ssv=%d, od2=%d, od4=%d, p=%d, q=%d, n=%d" \
                            %(p_eo, ssv, od2, od4, p, q, p*q)) 
                        exit(0)
                    
                # OD-2
                elif ((self.delta_start_value % 4 == 0) and (p_eo % 2 == 0)) or \
                     ((self.delta_start_value % 4 == 2) and (p_eo % 2 == 1)):
                    
                    if (ssv == od2):
                        if DEBUG == True:
                            print ("delta=%d, counter=%d, p_eo=%d, ssv=%d, od2=%d, od4=%d, p=%d, q=%d, n=%d" \
                               %(self.delta_start_value, counter_at_ssv, p_eo, ssv, od2, od4, p, q, p*q)) 
                
                    else:
                        print ("ERROR: Static State Breached")
                        print ("p_eo=%d, ssv=%d, od2=%d, od4=%d, p=%d, q=%d, n=%d" \
                            %(p_eo, ssv, od2, od4, p, q, p*q)) 
                        exit(0)
                
                else:
                    print ("Condition didn't match inside SSV, exiting")
                    exit(0)
                    
                    
            # UC-B
            elif (self.a1 == -1) and (self.a2 == 0):
                
                # OD-2
                if  ((self.delta_start_value % 4 == 2) and (p_eo % 2 == 0)) or \
                    ((self.delta_start_value % 4 == 0) and (p_eo % 2 == 1)):
                    
                    if (ssv == od2):
                        if DEBUG == True:
                            print ("delta=%d, counter=%d, p_eo=%d, ssv=%d, od2=%d, od4=%d, p=%d, q=%d, n=%d" \
                               %(self.delta_start_value, counter_at_ssv, p_eo, ssv, od2, od4, p, q, p*q)) 
                
                    else:
                        print ("ERROR: Static State Breached")
                        print ("p_eo=%d, ssv=%d, od2=%d, od4=%d, p=%d, q=%d, n=%d" \
                            %(p_eo, ssv, od2, od4, p, q, p*q)) 
                        exit(0)               

                    
                # OD-4
                elif ((self.delta_start_value % 4 == 0) and (p_eo % 2 == 0)) or \
                     ((self.delta_start_value % 4 == 2) and (p_eo % 2 == 1)):

                    if (ssv == od4):
                        if DEBUG == True:
                            print ("delta=%d, counter=%d, p_eo=%d, ssv=%d, od2=%d, od4=%d, p=%d, q=%d, n=%d" \
                               %(self.delta_start_value, counter_at_ssv, p_eo, ssv, od2, od4, p, q, p*q)) 
                
                    else:
                        print ("ERROR: Static State Breached")
                        print ("p_eo=%d, ssv=%d, od2=%d, od4=%d, p=%d, q=%d, n=%d" \
                            %(p_eo, ssv, od2, od4, p, q, p*q)) 
                        exit(0)
                
                else:
                    print ("Condition didn't match inside SSV, exiting")
                    exit(0)
                    
            else:
                print ("Condition didn't match inside SSV, exiting")
                exit(0)
                    
                                                                
            p += 2
            q += 2
            counter_at_ssv -= 1
            
        self.p_deep = p
        self.q_deep = q
        self.n_deep = self.p_deep * self.q_deep
        #print ("p_deep=%d, q_deep=%d, n_deep=%d" %(p,q,p*q))
        
    def check(self, ssv, p_eo, p_val, n, DEBUG=False):
        
        #self.check_via_q(ssv, p_eo, p_val, n, DEBUG)
        self.check_via_qe(ssv, p_eo, p_val, n, DEBUG)
        #self.check_via_fermat(ssv, p_eo, p_val, n, DEBUG)
        

    def start(self, DEBUG=False):
        
        while (self.delta_start_value >= self.delta_end_value):
            
            # Get SSV
            for p_eo in self.p_eo_list:
                
                get_ssv = SSV(self.dial_list, self.delta_start_value, p_eo).get_val()
                #print ("SSV for p=%d is=%d" %(p, get_ssv))
                
                get_p = P_DS_SSV(self.dial_list, self.delta_start_value, get_ssv, p_eo).get_p()
                #print ("P at SSV is=%d" %(get_p))
                
                get_q = get_p + self.delta_start_value
                
                get_n_at_ssv = N_DS_SSV(self.dial_list, self.delta_start_value, get_ssv, p_eo).get_n()
                #print ("n at SSV is=%d" %(get_n_at_ssv))
                
                # Confirm if p and n from formula are right
                self.check(get_ssv, p_eo, get_p, get_n_at_ssv, DEBUG=DEBUG)
            
                print ("SSV validation completed for:   id=%d, p_eo=%d, delta=%d, ssv=%d, p=%d, q=%d, n=%d"
                        %(self.g_id, p_eo, self.delta_start_value, get_ssv, get_p, get_q, get_n_at_ssv))
                
                print ("  SSV-depth check completd for: id=%d, p_eo=%d, delta=%d, ssv=%d, p=%d, q=%d, n=%d" 
                       %(self.g_id, p_eo, self.delta_start_value, get_ssv, self.p_deep, self.q_deep, self.n_deep))
            
            print ("\n")
            self.g_id += 1       
            self.delta_start_value -= 2


mode = 1

if mode == 0:
    print ("Initiated from Command Line")
    # Command line input handling
    a1 = int(sys.argv[1])
    a2 = int(sys.argv[2])
    delta = int(sys.argv[3])
    depth = int(sys.argv[4])
    depth_multiplier = int(sys.argv[5])

    dial1 = [a1, a2]
    dial1_list = [dial1]

    for dial1 in dial1_list:
        
        client = SSV_P_Check(dial1, delta, depth, depth_multiplier)
        client.start()

elif mode == 1:
    
    dial1 = [0, -1]
    dial1_list = [dial1]
    
    for dial1 in dial1_list:
        # dial1_list, delta_start, depth, depth_multiplier=1
        client = SSV_P_Check(dial1, 1000, 10000, 1)
        client.start(DEBUG=True)

else:
    print ("Mode Not Supported")
    exit(0)
        
        
