'''
Created on 27 Jul 2021

@author: vishalmudgal
'''

import sys
from lib.get_ds_ssv import SSV
from lib.get_ssv_od_n import SSV_OD_N
from lib.get_ds_p_at_ssv import P_DS_SSV

class OD4_DialRotationCheck(object):
    
    '''
    Testing the delta sieve coverage when v1 changes and sieving is done in od4
    '''

    def __init__(self, dialP1, delta, delta_end, od_watch):
        
        self.p_eo = 1                               # Only odd numbers are taken for now
        self.dsc_count = 0
        
        self.a1 = dialP1[0]
        self.a2 = dialP1[1]
        self.v1 = dialP1[2]
        self.v2 = dialP1[3]
        self.dial1_list = [self.a1, self.a2]
        
        self.delta = delta
        self.delta_end = delta_end
        self.od_watch = od_watch
        
        self.v1_increment = 4
        self.v2_increment = 4
        
        self.number_of_dial_iterations = 0
        
        if self.a1 == 0 and self.delta % 4 != 0:
            print ("Incorrect dial combintaion for given delta, exiting")
            exit(0)
        elif self.a1 == -1 and self.delta % 4 != 2:
            print ("Incorrect dial combintaion for given delta, exiting")
            exit(0)
        else:
            pass
        
    def get_od4_ssv(self):
        
        od4_ssv = ((self.delta * self.delta)//2) + ((self.v1 * self.v1)//2)
        return (od4_ssv)
        
    def get_ssv(self):
        
        get_ssv = SSV(self.dial1_list, self.delta, self.p_eo).get_val()
        return (get_ssv)
    
    def start(self, run_mode, DEBUG=False):
        
        if (run_mode == 'soz') or (run_mode == 'all'):
            pass
        else:
            print ("Not a valid run mode, exiting")
            exit(0) 
        
        while (self.delta >= self.delta_end):
            
            #print ("First While")
            
            self.v1 = 2
            self.v2 = self.v1
            dsc = 1
            dsc_count = 0
            
            get_ssv = SSV(self.dial1_list, self.delta, self.p_eo).get_val()
            #print ("SSV for p=%d is=%d" %(p, get_ssv))
                
            get_p_at_ssv = P_DS_SSV(self.dial1_list, self.delta, get_ssv, self.p_eo).get_p()
            #print ("P at SSV is=%d" %(get_p))
            
            prev_p = get_p_at_ssv
            
            self.number_of_dial_iterations = 0
            while (dsc > 0):
                
                #print ("Second While")
                p = 1
                self.number_of_dial_iterations += 1
                self.v1 = self.v1 + self.v1_increment
                self.v2 = self.v1
            
                store_p_flag = True
                od_check_flag = False
                
                if (od_check_flag == True) or (p > prev_p) or (p == prev_p == 1):
                    
                    #print ("Setting DSC == 0 -> delta=%d, dsc_count=%d" %(self.delta, dsc_count))
                    dsc = 0
            
                while (p < prev_p):
                    
                    #print ("Third While")
                    q = p + self.delta
                    od3, od4, od5 = SSV_OD_N(p, q, self.a1, self.a2, self.v1, self.v2).confirm()
                    
                    if self.od_watch == 'od4':
                        moving_ssv = self.get_od4_ssv()
                        od_to_check = od4
                    
                    else:
                        print ("Input OD not setup for processing, exiting")
                        exit(0)
                    
                    #print ("od_to_check=%d, p=%d, moving_ssv=%d"%(od_to_check, p, moving_ssv))
                    if od_to_check == moving_ssv:
                        
                        dsc += 1
                        dsc_count += 1
                        od_check_flag = True
                        
                        if DEBUG == True:
                            print ("OD MATCHED -> delta=%d, p=%d, q=%d, ssv=%d, od_to_check=%d, dsc=%d, v1=%d, prev_p=%d" 
                                   %(self.delta, p, q, moving_ssv, od_to_check, dsc_count, 
                                     self.v1, prev_p))
                        else:
                            pass
                        
                        if store_p_flag == True:
                            temp_prev_p = p
                            store_p_flag = False
                            
                        else:
                            pass
                        
                        if run_mode == 'soz':
                            prev_p = temp_prev_p
                            
                        else:
                            pass
                    
                    else:
                        pass
                    
                    if DEBUG == True:
                        print (" -> delta=%d, p=%d, q=%d, ssv=%d, od_to_check=%d, dsc=%d, v1=%d, prev_p=%d" 
                               %(self.delta, p, q, moving_ssv, od_to_check, dsc_count, 
                                 self.v1, prev_p))
                    else:
                        pass
                    
                    p += 2
                
                if run_mode == 'all':
                    prev_p = temp_prev_p
            
            print ("delta=%d, dsc=%d, dial_iterations=%d, p_at_exit=%d" 
                   %(self.delta, dsc_count, self.number_of_dial_iterations, p))
            
            #self.g_id += 1       
            self.delta -= 4

mode = 1

if mode == 0:
    print ("Initiated from Command Line")
    # Command line input handling
    # 0 -1 2 2 1000 992 od4 soz
    
    a1 = int(sys.argv[1])
    a2 = int(sys.argv[2])
    v1 = int(sys.argv[3])
    v2 = int(sys.argv[4])
    delta = int(sys.argv[5])
    delta_end = int(sys.argv[6])
    od_watch = sys.argv[7]
    all_or_soz = sys.argv[8]
    
    dialP1 = [a1, a2, v1, v2]
    
    # dialP1, delta, delta_end, od_watch
    client = OD4_DialRotationCheck(dialP1, delta, delta_end, od_watch)
    client.start(all_or_soz)
    
elif mode == 1:
    
    #dialP1 = [-1, 0, 2, 2]
    dialP1 = [0, -1, 2, 2]    
    # dialP1, delta, delta_end, od_watch
    client = OD4_DialRotationCheck(dialP1, 40, 32, 'od4')
    client.start('soz', DEBUG=False)

else:
    print ("Mode Not Supported")
    exit(0)
