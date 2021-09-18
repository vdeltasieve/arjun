'''
Created on 26 Jul 2021

@author: vishalmudgal
'''
import sys
import math
import decimal

decimal.getcontext().prec = 50
import matplotlib.pyplot as plt

class OD_Constants_Check(object):
    
    def __init__(self, delta_start, delta_limit):
    
        self.delta = delta_start
        self.delta_limit = delta_limit
        
        self.p_min = []
        self.p_max = []
        
        self.od1_list = ['od1',False,0,0,0,0]
        self.od2_list = ['od2',False,0,0,0,0]
        self.od4_list = ['od4',False,0,0,0,0]
        self.od5_list = ['od5',False,0,0,0,0]
        self.od7_list = ['od7',False,0,0,0,0]
        self.od8_list = ['od8',False,0,0,0,0]
        self.od9a_list = ['od9a',False,0,0,0,0]
        self.od9b_list = ['od9b',False,0,0,0,0]
        self.od10_list = ['od10',False,0,0,0,0]
        self.od11_list = ['od11',False,0,0,0,0]
    
    def set_dials(self):
        
        
        if self.delta % 4 == 0:
            
            # dial_p1_ = [a1, a2, v1, v2]
            self.dial_p1 = [0,-1,6,6]
            self.dial_p2 = [-2,1,16,16]
            
        elif self.delta % 4 == 2:
            
            self.dial_p1 = [0,-1,6,6]
            self.dial_p2 = [-2,1,16,16]
        
        else:
            print ("Delta is neither 4k nor 4k+2, exiting ...")
            exit(0)            
        
    def get_n_root_n(self, p, q):

        self.n = p * q
        self.root_n = math.floor(decimal.Decimal(self.n).sqrt())
        #return (self.n, self.root_n)
        
    def get_ods(self, dial_pair, dial_p1, dial_p2):
        
        if self.root_n % 2 == 0:
            
            d1 = self.root_n + dial_p1[0]           #dp1_a1
            d2 = d1 + dial_p1[2]                    #dp1_v1
            
            if dial_pair == 2:                     
                d3 = self.root_n + dial_p2[0]       #dp2_a1
                d4 = d3 + dial_p2[2]       #dp2_v1
            else:
                pass
            
        elif self.root_n % 2 == 1:
            d1 = self.root_n + dial_p1[1]           #dp1_a2
            d2 = d1 + dial_p1[3]                    #dp1_v2
            
            if dial_pair == 2:                                  
                d3 = self.root_n + dial_p2[1]       #dp2_a2
                d4 = d3 + dial_p2[3]                #dp2_v2
                    
            else:
                pass
            
        else:
            print ("INPUT ERROR. We possibly got 0 for 'self.root_n % 2'?")
            exit(0)
        
        d1_square = d1 * d1
        d2_square = d2 * d2
        
        if dial_pair == 2:
            d3_square = d3 * d3
            d4_square = d4 * d4
        else:
            pass
        
        if dial_pair >= 1:
            self.od1 = d1_square - self.n
            self.od2 = d2_square - self.n
            self.od3 = self.od2 - self.od1
            self.od4 = self.od2 + self.od1
            self.od5 = self.od1 + self.od2 + self.od3 + self.od4
            #self.od6 = decimal.Decimal((4*self.n)+(self.od1*self.od2)).sqrt()
            
        if dial_pair >= 2:
            self.od7 = d3_square - self.n
            self.od8 = d4_square - self.n
            self.od9 = self.od2 + self.od8
            self.od10 = self.od4 + self.od8
            self.od11 = self.od2 + (2 * self.od8) + self.od4
            self.od12 = self.od4 + self.od7
        
    
    def ssv_square(self, od_1_2_7_8):
    
        #print ("OD2 Inside Function:", od_1_2_7_8)
        ssv = ( (self.delta//2) * (self.delta//2) ) 
        if ssv == od_1_2_7_8:
            #print ("delta=%d, p=%d, q=%d" %(self.delta, self.p, self.q))
            return True
        else:
            return False
    
    
    def ssv_od_4(self, od4, v1):
        
        #print ("Inside OD4")
        ssv = ((self.delta * self.delta)//2) + ((v1 * v1)//2) 
        if ssv == od4:
            return True
        else:
            return False
    
    def ssv_od_5(self, od5, v1):
        
        ssv = (self.delta * self.delta) + ((3 * v1 * v1)//4) 
        if ssv == od5:
            return True
        else:
            return False
    
    def ssv_od_6(self, od1, od2):
        
        od6 = decimal.Decimal((4*self.n)+(od1*od2)).sqrt()
        return (od6)
    
    def ssv_od_9a(self, od9):
        
        ssv = ((self.delta * self.delta)//2) + 72
        if ssv == od9:
            return True
        else:
            return False
        
    def ssv_od_9b(self, od9):
        
        ssv = ((self.delta * self.delta)//2) + 32
        if ssv == od9:
            return True
        else:
            return False
        
    def ssv_od_10(self, od10):
        
        ssv = ((self.delta * self.delta)//2) + ((self.delta//2)*(self.delta//2)) + 168
        if ssv == od10:
            return True
        else:
            return False
        
    def ssv_od_11(self, od11):
        
        ssv = (self.delta * self.delta) + ((self.delta//2)*(self.delta//2)) + 144
        if ssv == od11:
            return True
        else:
            return False
        
    def ssv_od_12(self, od12):
        
        ssv = ((self.delta * self.delta)//2) + ((self.delta//2)*(self.delta//2)) + 56
        if ssv == od12:
            return True
        else:
            return False
        
    def start(self, obj, od_sieving_limit_zone, DEBUG='default'):
        
        self.mpl_delta = []
        self.mpl_dsc = []

        while (self.delta <= self.delta_limit):

            # A. Set Dials
            self.set_dials()
            
            total_delta_sieve_coverage = []
            self.p = 1
            counter_id = 1
            
            od_limit = od_sieving_limit_zone + '_list'
            
            while not obj.__dict__[od_limit][1]:
                
                self.q = self.p + self.delta
            
                # B. n and sqrt_n
                self.get_n_root_n(self.p, self.q)
                
                # C. Get ODs
                self.get_ods(2,
                             self.dial_p1,
                             self.dial_p2
                             )
                
                '''
                # 1. OD1
                od1 = self.ssv_square(self.od1)
                if od1:
                    if self.od1_list[2] == 0:
                        self.od1_list[2] = counter_id
                        self.od1_list[5] = self.od1
                    
                    self.od1_list[3] = counter_id
                    self.od1_list[4] = self.od1_list[3] - self.od1_list[2] + 1
                
                if not od1 and self.od1_list[2] > 1:
                    if self.od1_list[0] == od_sieving_limit_zone:
                        obj.__dict__[od_limit][1] = True
                        if DEBUG == 'dsc_zones':
                            print ("delta:%d, od1:%s, dial_p1:%s, dial_p2:%s"%(self.delta, self.od1_list, self.dial_p1, self.dial_p2))
                        self.od1_list[2] = 0
                        total_delta_sieve_coverage.append(self.od1_list[4])
                    else:
                        if DEBUG == 'dsc_zones':
                            print ("delta:%d, od1:%s, dial_p1:%s, dial_p2:%s"%(self.delta, self.od1_list, self.dial_p1, self.dial_p2))
                        self.od1_list[2] = 0
                        total_delta_sieve_coverage.append(self.od1_list[4])
                '''
                
                '''
                # 2. OD2
                od2 = self.ssv_square(self.od2)
                if od2:
                    if self.od2_list[2] == 0:
                        self.od2_list[2] = counter_id
                        self.od2_list[5] = self.od2
                    
                    self.od2_list[3] = counter_id
                    self.od2_list[4] = self.od2_list[3] - self.od2_list[2] + 1
                
                if not od2 and self.od2_list[2] > 1:
                    if self.od2_list[0] == od_sieving_limit_zone:
                        obj.__dict__[od_limit][1] = True
                        if DEBUG == 'dsc_zones':
                            print ("delta:%d, od2:%s, dial_p1:%s, dial_p2:%s"%(self.delta, self.od2_list, self.dial_p1, self.dial_p2))
                        self.od2_list[2] = 0
                        total_delta_sieve_coverage.append(self.od2_list[4])
                    else:
                        if DEBUG == 'dsc_zones':
                            print ("delta:%d, od2:%s, dial_p1:%s, dial_p2:%s"%(self.delta, self.od2_list, self.dial_p1, self.dial_p2))
                        self.od2_list[2] = 0
                        total_delta_sieve_coverage.append(self.od2_list[4])
               
                '''
                
                '''
                # 4. OD4
                od4 = self.ssv_od_4(self.od4, self.dial_p1[2])
                if od4:
                    if self.od4_list[2] == 0:
                        self.od4_list[2] = counter_id
                        self.od4_list[5] = self.od4
                    
                    self.od4_list[3] = counter_id
                    self.od4_list[4] = self.od4_list[3] - self.od4_list[2] + 1
                
                if not od4 and self.od4_list[2] > 1:
                    if self.od4_list[0] == od_sieving_limit_zone:
                        obj.__dict__[od_limit][1] = True
                        if DEBUG == 'dsc_zones':
                            print ("delta:%d, od4:%s, dial_p1:%s, dial_p2:%s"%(self.delta, self.od4_list, self.dial_p1, self.dial_p2))
                        self.od4_list[2] = 0
                        total_delta_sieve_coverage.append(self.od4_list[4])
                    else:
                        if DEBUG == 'dsc_zones':
                            print ("delta:%d, od4:%s, dial_p1:%s, dial_p2:%s"%(self.delta, self.od4_list, self.dial_p1, self.dial_p2))
                        self.od4_list[2] = 0
                        total_delta_sieve_coverage.append(self.od4_list[4])

                '''
                
                '''
                # 5. OD5
                od5 = self.ssv_od_5(self.od5, self.dial_p1[2])
                if od5:
                    if self.od5_list[2] == 0:
                        self.od5_list[2] = counter_id
                        self.od5_list[5] = self.od5
                    
                    self.od5_list[3] = counter_id
                    self.od5_list[4] = self.od5_list[3] - self.od5_list[2] + 1
                
                if not od5 and self.od5_list[2] > 1:
                    if self.od5_list[0] == od_sieving_limit_zone:
                        obj.__dict__[od_limit][1] = True
                        if DEBUG == 'dsc_zones':
                            print ("delta:%d, od5:%s, dial_p1:%s, dial_p2:%s"%(self.delta, self.od5_list, self.dial_p1, self.dial_p2))
                        self.od5_list[2] = 0
                        total_delta_sieve_coverage.append(self.od5_list[4])
                    else:
                        if DEBUG == 'dsc_zones':
                            print ("delta:%d, od5:%s, dial_p1:%s, dial_p2:%s"%(self.delta, self.od5_list, self.dial_p1, self.dial_p2))
                        self.od5_list[2] = 0
                        total_delta_sieve_coverage.append(self.od5_list[4])

                '''
                
                '''
                # 6. OD6
                od6 = self.ssv_od_6(self.od6, self.dial_p1[2])
                if od6:
                    if self.od6_list[2] == 0:
                        self.od6_list[2] = counter_id
                        self.od6_list[5] = self.od6
                    
                    self.od6_list[3] = counter_id
                    self.od6_list[4] = self.od6_list[3] - self.od6_list[2]
                
                if not od6 and self.od6_list[2] > 1:
                    if self.od6_list[0] == od_sieving_limit_zone:
                        obj.__dict__[od_limit][1] = True
                        print ("delta:%d, od6:%s, dial_p1:%s, dial_p2:%s"
                               %(self.delta, self.od6_list, self.dial_p1, self.dial_p2))
                        self.od6_list[2] = 0
                    else:
                        print ("delta:%d, od6:%s, dial_p1:%s, dial_p2:%s"
                               %(self.delta, self.od6_list, self.dial_p1, self.dial_p2))
                        self.od6_list[2] = 0
                '''
                
                '''
                # 7. OD7
                od7 = self.ssv_square(self.od7)
                if od7:
                    if self.od7_list[2] == 0:
                        self.od7_list[2] = counter_id
                        self.od7_list[5] = self.od7
                    
                    self.od7_list[3] = counter_id
                    self.od7_list[4] = self.od7_list[3] - self.od7_list[2] + 1
                
                if not od7 and self.od7_list[2] > 1:
                    if self.od7_list[0] == od_sieving_limit_zone:
                        obj.__dict__[od_limit][1] = True
                        if DEBUG == 'dsc_zones':
                            print ("delta:%d, od7:%s, dial_p1:%s, dial_p2:%s"%(self.delta, self.od7_list, self.dial_p1, self.dial_p2))
                        self.od7_list[2] = 0
                        total_delta_sieve_coverage.append(self.od7_list[4])
                    else:
                        if DEBUG == 'dsc_zones':
                            print ("delta:%d, od7:%s, dial_p1:%s, dial_p2:%s"%(self.delta, self.od7_list, self.dial_p1, self.dial_p2))
                        self.od7_list[2] = 0
                        total_delta_sieve_coverage.append(self.od7_list[4])
                '''
                
                '''
                # 8. OD8
                od8 = self.ssv_square(self.od8)
                if od8:
                    if self.od8_list[2] == 0:
                        self.od8_list[2] = counter_id
                        self.od8_list[5] = self.od8
                    
                    self.od8_list[3] = counter_id
                    self.od8_list[4] = self.od8_list[3] - self.od8_list[2]
                
                if not od8 and self.od8_list[2] > 1:
                    if self.od8_list[0] == od_sieving_limit_zone:
                        obj.__dict__[od_limit][1] = True
                        if DEBUG == 'dsc_zones':
                            print ("delta:%d, od8:%s, dial_p1:%s, dial_p2:%s"%(self.delta, self.od8_list, self.dial_p1, self.dial_p2))
                        self.od8_list[2] = 0
                        total_delta_sieve_coverage.append(self.od8_list[4])
                    else:
                        if DEBUG == 'dsc_zones':
                            print ("delta:%d, od8:%s, dial_p1:%s, dial_p2:%s"%(self.delta, self.od8_list, self.dial_p1, self.dial_p2))
                        self.od8_list[2] = 0
                        total_delta_sieve_coverage.append(self.od8_list[4])
                '''

                # 9a. OD9a
                od9a = self.ssv_od_9a(self.od9)
                if od9a:
                    if self.od9a_list[2] == 0:
                        self.od9a_list[2] = counter_id
                        self.od9a_list[5] = self.od9
                    
                    self.od9a_list[3] = counter_id
                    self.od9a_list[4] = self.od9a_list[3] - self.od9a_list[2] + 1
                
                if not od9a and self.od9a_list[2] > 1:
                    if self.od9a_list[0] == od_sieving_limit_zone:
                        obj.__dict__[od_limit][1] = True
                        if DEBUG == 'dsc_zones':
                            print ("delta:%d, od9a:%s, dial_p1:%s, dial_p2:%s"%(self.delta, self.od9a_list, self.dial_p1, self.dial_p2))
                        self.od9a_list[2] = 0
                        total_delta_sieve_coverage.append(self.od9a_list[4])
                    else:
                        if DEBUG == 'dsc_zones':
                            print ("delta:%d, od9a:%s, dial_p1:%s, dial_p2:%s"%(self.delta, self.od9a_list, self.dial_p1, self.dial_p2))
                        self.od9a_list[2] = 0
                        total_delta_sieve_coverage.append(self.od9a_list[4])

                # 9b. OD9b
                od9b = self.ssv_od_9b(self.od9)
                if od9b:
                    if self.od9b_list[2] == 0:
                        self.od9b_list[2] = counter_id
                        self.od9b_list[5] = self.od9
                    
                    self.od9b_list[3] = counter_id
                    self.od9b_list[4] = self.od9b_list[3] - self.od9b_list[2] + 1
                
                if not od9b and self.od9b_list[2] > 1:
                    if self.od9b_list[0] == od_sieving_limit_zone:
                        obj.__dict__[od_limit][1] = True
                        if DEBUG == 'dsc_zones':
                            print ("delta:%d, od9b:%s, dial_p1:%s, dial_p2:%s"%(self.delta, self.od9b_list, self.dial_p1, self.dial_p2))
                        self.od9b_list[2] = 0
                        total_delta_sieve_coverage.append(self.od9b_list[4])
                    else:
                        if DEBUG == 'dsc_zones':
                            print ("delta:%d, od9b:%s, dial_p1:%s, dial_p2:%s"%(self.delta, self.od9b_list, self.dial_p1, self.dial_p2))
                        self.od9b_list[2] = 0
                        total_delta_sieve_coverage.append(self.od9b_list[4])


                # 10. OD10
                od10 = self.ssv_od_10(self.od10)
                if od10:
                    if self.od10_list[2] == 0:
                        self.od10_list[2] = counter_id
                        self.od10_list[5] = self.od10
                    
                    self.od10_list[3] = counter_id
                    self.od10_list[4] = self.od10_list[3] - self.od10_list[2] + 1
                
                if not od10 and self.od10_list[2] > 1:
                    if self.od10_list[0] == od_sieving_limit_zone:
                        obj.__dict__[od_limit][1] = True
                        if DEBUG == 'dsc_zones':
                            print ("delta:%d, od10:%s, dial_p1:%s, dial_p2:%s"%(self.delta, self.od10_list, self.dial_p1, self.dial_p2))
                        self.od10_list[2] = 0
                        total_delta_sieve_coverage.append(self.od10_list[4])
                    else:
                        if DEBUG == 'dsc_zones':
                            print ("delta:%d, od10:%s, dial_p1:%s, dial_p2:%s"%(self.delta, self.od10_list, self.dial_p1, self.dial_p2))
                        self.od10_list[2] = 0
                        total_delta_sieve_coverage.append(self.od10_list[4])

                # 11. OD11
                od11 = self.ssv_od_11(self.od11)
                if od11:
                    if self.od11_list[2] == 0:
                        self.od11_list[2] = counter_id
                        self.od11_list[5] = self.od11
                    
                    self.od11_list[3] = counter_id
                    self.od11_list[4] = self.od11_list[3] - self.od11_list[2] + 1
                
                if not od11 and self.od11_list[2] > 1:
                    if self.od11_list[0] == od_sieving_limit_zone:
                        obj.__dict__[od_limit][1] = True
                        if DEBUG == 'dsc_zones':
                            print ("delta:%d, od11:%s, dial_p1:%s, dial_p2:%s"%(self.delta, self.od11_list, self.dial_p1, self.dial_p2))
                        self.od11_list[2] = 0
                        total_delta_sieve_coverage.append(self.od11_list[4])
                    else:
                        if DEBUG == 'dsc_zones':
                            print ("delta:%d, od11:%s, dial_p1:%s, dial_p2:%s"%(self.delta, self.od11_list, self.dial_p1, self.dial_p2))
                        self.od11_list[2] = 0
                        total_delta_sieve_coverage.append(self.od11_list[4])

                
                '''
                # 12. OD12
                od12 = self.ssv_od_10(self.od12)
                if od12:
                    if self.od12_list[2] == 0:
                        self.od12_list[2] = counter_id
                        self.od12_list[5] = self.od12
                    
                    self.od12_list[3] = counter_id
                    self.od12_list[4] = self.od12_list[3] - self.od12_list[2] + 1
                
                if not od12 and self.od12_list[2] > 1:
                    if self.od12_list[0] == od_sieving_limit_zone:
                        obj.__dict__[od_limit][1] = True
                        if DEBUG == 'dsc_zones':
                            print ("delta:%d, od12:%s, dial_p1:%s, dial_p2:%s"%(self.delta, self.od12_list, self.dial_p1, self.dial_p2))
                        self.od12_list[2] = 0
                        total_delta_sieve_coverage.append(self.od12_list[4])
                    else:
                        if DEBUG == 'dsc_zones':
                            print ("delta:%d, od12:%s, dial_p1:%s, dial_p2:%s"%(self.delta, self.od12_list, self.dial_p1, self.dial_p2))
                        self.od12_list[2] = 0
                        total_delta_sieve_coverage.append(self.od12_list[4])
                '''
                        
                #print (counter_id, self.p, self.q, self.n, self.root_n, self.od8)
                
                self.p += 2
                counter_id += 1
                
            # Sum of Total Delta Sieve Coverage Area
            sum_tdsc = 0
            for x in total_delta_sieve_coverage:
                sum_tdsc += x
            
            print ("delta=%d, total_delta_sieve_coverage=%d" %(self.delta, sum_tdsc))
            
            self.mpl_delta.append(self.delta)
            self.mpl_dsc.append(sum_tdsc)
            
            #print ("")
            self.od1_list = ['od1',False,0,0,0,0]
            self.od2_list = ['od2',False,0,0,0,0]
            self.od4_list = ['od4',False,0,0,0,0]
            self.od5_list = ['od5',False,0,0,0,0]
            self.od7_list = ['od7',False,0,0,0,0]
            self.od8_list = ['od8',False,0,0,0,0]
            self.od9a_list = ['od9a',False,0,0,0,0]
            self.od9b_list = ['od9b',False,0,0,0,0]
            self.od10_list = ['od10',False,0,0,0,0]
            self.od11_list = ['od11',False,0,0,0,0]
            
            counter_id = 1
            self.delta += 4


mode = 1

if mode == 0:
    print ("Initiated from Command Line")
    # Command line input handling
    # 38 42 od10 default
    
    delta_start = int(sys.argv[1])
    delta_limit = int(sys.argv[2])
    od_sieving_limit_zone = sys.argv[3]
    debug_mode = sys.argv[4]

    od_constants_check = OD_Constants_Check(delta_start, delta_limit)
    od_constants_check.start(od_constants_check, od_sieving_limit_zone, debug_mode) 
    
    # Data for plotting
    x_axis = od_constants_check.mpl_delta
    y_axis = od_constants_check.mpl_dsc
    
    fig, ax = plt.subplots()
    
    ax.plot(x_axis, y_axis)
    
    ax.set(xlabel='$\Delta_{|p-q|}$', ylabel='Total $\Delta$ Sieve Coverage',
           title='Delta sieve coverage growth with increasing $\Delta$\n (observed from $od_{9a}$, $od_{9b}$, $od_{10}$, $od_{11}$)\n')
    ax.grid()
    
    fig.savefig("DSC.png")
    plt.show()
    
elif mode == 1:
    
    #MAIN 
    #od_constants_check = OD_Constants_Check(38, 52) #38
    od_constants_check = OD_Constants_Check(38, 5002) #38
    #od_constants_check = OD_Constants_Check(382, 500) #38
    od_constants_check.start(od_constants_check, 'od10', 'default') 
    
    # Data for plotting
    x_axis = od_constants_check.mpl_delta
    y_axis = od_constants_check.mpl_dsc
    
    fig, ax = plt.subplots()
    ax.plot(x_axis, y_axis, color="gray")
    
    #plt.rcParams.update({'axes.titlesize': '16','font.weight': 'bold'})
    
    axes = plt.gca()
    #plt.plot(x, y)
    axes.set_title('$\Delta$ Sieve Coverage Growth')
    axes.set_xlabel('\n$\Delta$(Delta)')
    axes.set_ylabel('Total $\Delta$ Sieve Coverage')
    
    axes.title.set_size(16)
    axes.xaxis.label.set_size(16)
    axes.yaxis.label.set_size(16)
    
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    
    #ax.set(xlabel='$\Delta_{|p-q|}$', ylabel='Total $\Delta$ Sieve Coverage',
           #title='Delta sieve coverage growth with increasing $\Delta$\n (observed from $od_{9a}$, $od_{9b}$, $od_{10}$, $od_{11}$)\n')
    #       title='Delta sieve coverage growth with increasing $\Delta$')
    #ax.grid()
    
    fig.savefig("DSC.png")
    plt.show()


else:
    print ("Mode Not Supported")
    exit(0)
        
