'''
Created on 25 Jul 2021

@author: vishalmudgal
'''
import sys
from lib.get_ds_ssv import SSV
from lib.get_ds_n_at_ssv import N_DS_SSV
from lib.get_ds_od6 import OD6

# DSSC = Delta Sum Series Connect
class DSSC(object):
    '''
    This checks how delta and sum series connect to each other
    '''

    def __init__(self, delta, num_of_iterations):
        
        self.delta = delta
        self.delta_end = 12                         # Check will end when delta reaches this value
        self.g_id = 1                               # To track number of iterations 
        self.p_eo_list = [1,2]                      # Even and Odd Numbers
        self.num_of_iterations = num_of_iterations

    def set_dials(self, p_eo):
        
        # Sum Series Dials
        self.sum_a1 = -1
        self.sum_a2 = 0
        self.sum_v1 = 2
        self.sum_v2 = 2
        
        # Delta Series
        self.delta_v1 = 2
        self.delta_v2 = 2
        
        if ((self.delta % 4 == 0) and (p_eo % 2 == 1)) or \
           ((self.delta % 4 == 2) and (p_eo % 2 == 0)):
            
            self.delta_a1 = 0
            self.delta_a2 = -1
        
        elif ((self.delta % 4 == 2) and (p_eo % 2 == 1)) or \
             ((self.delta % 4 == 0) and (p_eo % 2 == 0)):
              
            self.delta_a1 = -1
            self.delta_a2 = 0
        
        else:
            print ("Delta is neither of 4k of 4k+2 form ... exiting")
            exit(0)
            
        self.dial_list = [self.delta_a1, self.delta_a2]
            
    def get_ssv(self, p_eo):
        
        get_ssv = SSV(self.dial_list, self.delta, p_eo).get_val()
        return (get_ssv)
        
    def get_n_at_ssv(self, ssv, p_eo):
        
        get_n_at_ssv = N_DS_SSV(self.dial_list, self.delta, ssv, p_eo).get_n()
        return (get_n_at_ssv)
    
    def get_od6(self, n):
        
        od6_at_ssv = OD6(self.dial_list, n)
        return (od6_at_ssv)
    
    
    def get_single_center(self):
        
        p_center =  self.delta // 2
        q_center = self.delta // 2
        N_center = p_center * q_center
        
        p_next_down = p_center + 2
        q_next_down = q_center - 2
        N_next_down = p_next_down * q_next_down
        
        p_next_up = p_center - 2
        q_next_up = q_center + 2
        N_next_up = p_next_up * q_next_up
        
        if (N_next_down > N_center) or (N_next_up > N_center):
            print ("Sum Center State Breached")
            exit(0)
    
        else:
            return (N_center)
        
    def get_double_center(self):
        
        p_center_1 =  (self.delta // 2) - 1
        q_center_1 =  (self.delta // 2) + 1
        N_center_1 = p_center_1 * q_center_1
        
        p_center_2 =  (self.delta // 2) + 1
        q_center_2 =  (self.delta // 2) - 1
        N_center_2 = p_center_2 * q_center_2
        
        p_next_down = p_center_1 + 4
        q_next_down = q_center_1 - 4
        N_next_down = p_next_down * q_next_down
        
        p_next_up = p_center_1 - 2
        q_next_up = q_center_1 + 2
        N_next_up = p_next_up * q_next_up
        
        if (N_next_down > N_center_1) or (N_next_up > N_center_1):
            print ("Sum Center State Breached")
            exit(0)
    
        elif (N_center_1 != N_center_2):
            print ("Sum Center State Breached")
            exit(0)
        
        elif N_center_1 == N_center_2:
            return (N_center_1)
    
        else:
            print ("Some errror. Sum Center State Breached")
            exit(0)
         
    
    def get_sum_series_center(self, p_eo, od6):
    
        if p_eo % 2 == 1:
            
            if self.delta % 4 == 2:
                
                N = self.get_single_center()
                
                if (N != od6+1):
                    print ("Some errror. Sum Center State Breached")
                    exit(0)
                elif (N == od6+1):
                    return (N)
                else:
                    print ("Some errror. Sum Center State Breached")
                    exit(0)
            
            elif self.delta % 4 == 0:
                
                N = self.get_double_center()

                if (N != od6):
                    print ("Some errror. Sum Center State Breached")
                    exit(0)
                elif (N == od6):
                    return (N)
                else:
                    print ("Some errror. Sum Center State Breached")
                    exit(0)
            
            else:
                print ("Some errror. Sum Center State Breached")
                exit(0)
 
        elif p_eo % 2 == 0:
            
            if self.delta % 4 == 2:
                
                N = self.get_double_center()

                if (N != od6):
                    print ("Some errror. Sum Center State Breached")
                    exit(0)
                elif (N == od6):
                    return (N)
                else:
                    print ("Some errror. Sum Center State Breached")
                    exit(0)
            
            elif self.delta % 4 == 0:
                
                N = self.get_single_center()

                if (N != od6+1):
                    print ("Some errror. Sum Center State Breached")
                    exit(0)
                elif (N == od6+1):
                    return (N)
                else:
                    print ("Some errror. Sum Center State Breached")
                    exit(0)
            
            else:
                print ("Some errror. Sum Center State Breached")
                exit(0)
               
        else:
            print ("Some errror. Sum Center State Breached")
            exit(0)
                   
            
    def check(self, p_eo):
        
        # Set the Dials
        self.set_dials(p_eo)
        
        # Get SSV
        ssv = self.get_ssv(p_eo)
        #print ("SSV:", ssv)
        
        # Get N at SSV
        n_at_ssv = self.get_n_at_ssv(ssv, p_eo)
        #print ("n:",n_at_ssv)
        
        # Get OD6 at SSV
        od6 = self.get_od6(n_at_ssv).get_od6()
        #print ("od6:",od6)
        
        # Get N_center
        N_center = self.get_sum_series_center(p_eo, od6)
        
        return (n_at_ssv, ssv, od6, N_center)
    
    def start(self):
        
        counter = 0
        while (self.delta >= self.delta_end):
            
            # Get SSV
            for p_eo in self.p_eo_list:
                
                n_at_ssv, ssv, od6, N_center = self.check(p_eo)
                print ("delta=%d, p_eo=%d, n_at_ssv=%d, ssv=%d, od6_at_ssv=%d, N_center=%d" 
                       %(self.delta, p_eo, n_at_ssv, ssv, od6, N_center))
            
            if counter >= self.num_of_iterations:
                break
              
            #print ("\n")
            self.g_id += 1       
            self.delta -= 2
            counter += 1

mode = 1

if mode == 0:
    
    # Command line input handling
    print ("Initiated from Command Line")
    delta = int(sys.argv[1])
    num_of_iterations = int(sys.argv[2])
    
    client = DSSC(delta, num_of_iterations)
    client.start()

elif mode == 1:
    
    delta = 12868443246892828374658291028375758920384759393939939394848472
    client = DSSC(delta, 2)
    client.start()

else:
    print ("Mode Not Supported")
    exit(0)
        
