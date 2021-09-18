'''
Created on 27 Jul 2021

@author: vishalmudgal
'''

import sys
from lib.get_ds_ssv import SSV
from lib.get_ssv_od_n import SSV_OD_N

class OD5_DialRotationCheck(object):
    
    '''
    classdocs
    '''

    def __init__(self, dialP1, delta, delta_end, od_watch):
        
        self.p_eo = 1                               # Only odd numbers are taken for now
        #self.g_id = 1
        self.dsc_count = 0
        
        self.a1 = dialP1[0]
        self.a2 = dialP1[1]
        self.v1 = dialP1[2]
        self.v2 = dialP1[3]
        self.dial1_list = [self.a1, self.a2]
        
        self.v1_original = self.v1
        
        self.delta = delta
        self.delta_end = delta_end
        self.od_watch = od_watch
        
        self.v1_increment = 8
        self.v2_increment = 8
        
        self.number_of_dial_iterations = 0
        
        '''
        if self.a1 == -1 and self.delta % 4 != 2:
            print ("Incorrect dial combintaion for given delta, exiting")
            exit(0)
        elif self.a1 == 0 and self.delta % 4 != 0:
            print ("Incorrect dial combintaion for given delta, exiting")
            exit(0)
        else:
            pass
        '''
        
    def get_od5_ssv(self):
        
        od5_ssv = (self.delta * self.delta) + ((3 * self.v1 * self.v1)//4)
        return (od5_ssv)
        
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
            first_run = True
            self.v1 = self.v1_original
            self.v2 = self.v1
            dsc = 1
            dsc_count = 0
            p = 1
            
            '''
            Some large number, so p > prev_p is evaluated correctly.
            '''
            prev_p = self.delta * 20000000000000000000000000000000000000000000000000000000000000000000000000
            
            #second_while_flag = True
            self.number_of_dial_iterations = 0
            while (dsc > 0):
                
                self.number_of_dial_iterations += 1
                
                #print ("Second While")
                p = 1
                
                if first_run == True:
                    #print ("First Run")
                    first_run = False
                else:
                    #print ("Second Run")
                    self.v1 = self.v1 + self.v1_increment
                    self.v2 = self.v1
                    #print ("v1=%d, v2=%d" %(self.v1, self.v1))
            
                store_p_flag = True
                od_check_flag = False
                third_while_flag = True
                
                if (od_check_flag == True) or (p > prev_p) or (p == prev_p == 1):
                    
                    #print ("Setting DSC == 0 -> delta=%d, dsc_count=%d" %(self.delta, dsc_count))
                    dsc = 0
                
                while (third_while_flag):
                
                    
                    #if self.v1 == 12:
                    #    exit(0)
                    
                    #print ("Third While")
                    q = p + self.delta
                    od3, od4, od5 = SSV_OD_N(p, q, self.a1, self.a2, self.v1, self.v2).confirm()
                    
                    if self.od_watch == 'od5':
                        moving_ssv = self.get_od5_ssv()
                        od_to_check = od5
                    
                    else:
                        print ("Input OD not setup for processing, exiting")
                        exit(0)
                    
                    #print ("od_to_check=%d, p=%d, moving_ssv=%d"%(od_to_check, p, moving_ssv))
                    if od_to_check == moving_ssv:
                        
                        dsc += 1
                        dsc_count += 1
                        od_check_flag = True
                        
                        if DEBUG == True:
                            print ("OD MATCHED -> delta=%d, p=%d, q=%d, ssv=%d, od_to_check=%d, dsc=%d, v1=%d" 
                                   %(self.delta, p, q, moving_ssv, od_to_check, dsc_count, 
                                     self.v1))
                        else:
                            pass
                        
                        if store_p_flag == True:
                            temp_prev_p = p
                            store_p_flag = False
                            
                        else:
                            pass
                        
                        if run_mode == 'soz':
                            prev_p = temp_prev_p
                            third_while_flag = False
                        
                        else:
                            pass
                                            
                    elif ((od_to_check != moving_ssv) and (od_check_flag == True)):
                        third_while_flag = False
                        #second_while_flag = False
                    
                    elif ((od_check_flag == False) and (p > prev_p)):
                        third_while_flag = False
                        dsc = 0
                
                    else:
                        pass
                    
                    if DEBUG == True:
                        print (" -> delta=%d, p=%d, q=%d, ssv=%d, od_to_check=%d, dsc=%d, v1=%d" 
                               %(self.delta, p, q, moving_ssv, od_to_check, dsc_count, 
                                 self.v1))
                    else:
                        pass
                    
                    p += 2
                    
                if ((run_mode == 'all') and (od_check_flag == True)):
                    prev_p = temp_prev_p
                
                elif ((run_mode == 'all') and (od_check_flag == False) and (p > prev_p)):
                    pass
                
            print ("delta=%d, dsc=%d, dial_iterations=%d, p_at_exit=%d" 
                   %(self.delta, dsc_count, self.number_of_dial_iterations, p))
            
            #print ("\n")
            self.delta -= 4
            #self.g_id += 1 
            
mode = 1

if mode == 0:
    print ("Initiated from Command Line")
    # Command line input handling
    # -2 -1 12 12 1000 992 od5 soz
    
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
    client = OD5_DialRotationCheck(dialP1, delta, delta_end, od_watch)
    client.start(all_or_soz)
    
elif mode == 1:
    
    #dialP1 = [0, -1, 4, 4]
    #dialP1 = [-1, -2, 4, 4]   # delta = 4k + 2
    dialP1 = [-2, -1, 12, 12] # delta = 4k
    #dialP1 = [-1, 0, 4, 4]    
    # dialP1, delta, delta_end, od_watch
    client = OD5_DialRotationCheck(dialP1, 1000 , 992, 'od5')
    
    # all, soz
    client.start('soz', DEBUG=False)

else:
    print ("Mode Not Supported")
    exit(0)
