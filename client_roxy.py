'''
Created on 30 Jul 2021

@author: vishalmudgal
'''
import sys
import matplotlib.pyplot as plt
import math
import decimal
decimal.getcontext().prec = 50

from lib.get_ds_n_at_ssv import N_DS_SSV
from lib.get_ds_ssv import SSV
from lib.get_quadratic_roots import Quadratic_Roots


class ROxy(object):
    '''
    Reflection over {X,Y} is tested
    '''

    def __init__(self, v1, delta, num_of_iterations, delta_increment):

        self.g_counter = 1
        self.delta = delta
        self.num_of_iterations = num_of_iterations
        self.delta_increment = delta_increment
        self.dial1 = v1
        
        self.g_delta_array = []
        self.n_array = []
        self.delta_series_od6 = []
        self.all_n_array = []
        self.all_od6_array = []
    
    def set_dials(self):
        
        if self.delta % 4 == 0:
            self.a1 = 0
            self.a2 = -1
            self.v1 = self.dial1
            self.v2 = self.dial1
            
        elif self.delta % 4 == 2:
            self.a1 = -1
            self.a2 = 0
            self.v1 = self.dial1
            self.v2 = self.dial1
            
        else:
            print ("Delta is neither of 4k of 4k+2 form ... exiting")
            exit(0)
            
        self.dial1_list = [self.a1, self.a2]

    def get_delta_series(self):
        
        p_eo = 1
        get_ssv = SSV(self.dial1_list, self.delta, p_eo).get_val()
        #print ("STATIC_STATE_VAL:", get_ssv)
        
        get_n_at_ssv = N_DS_SSV(self.dial1_list, self.delta, get_ssv, p_eo).get_n()
                
        print ("Factorize:", get_n_at_ssv)
        quadratic_soln = Quadratic_Roots(1, self.delta, -get_n_at_ssv).start()
        factor_1 = quadratic_soln[1]
        factor_2 = factor_1 + self.delta
        print (factor_1, factor_2)
    
        while (factor_1 >= 1):
        
            n = factor_1 * factor_2
            root_n = math.floor(decimal.Decimal(n).sqrt())
            self.n_array.append(n)
            
            if root_n % 2 == 0: #Even
                d1 = root_n + self.a1
                d2 = d1 + self.v1
                d1_square = d1*d1
                d2_square = d2*d2
                od1 = d1_square - n 
                od2 = d2_square - n
                od6_inter = (self.v1 * n * self.v2) + (od1 * od2)
                od6 = math.floor(decimal.Decimal(od6_inter).sqrt())
                self.delta_series_od6.append(od6)
                
            else: #Odd
                d1 = root_n + self.a2
                d2 = d1 + self.v2
                d1_square = d1*d1
                d2_square = d2*d2
                od1 = d1_square - n
                od2 = d2_square - n
                od6_inter = (self.v1 * n * self.v2) + (od1 * od2)
                od6 = math.floor(decimal.Decimal(od6_inter).sqrt())
                self.delta_series_od6.append(od6)
                
            factor_1 -= 2
            factor_2 -= 2
                
                
    def plot_graph(self, delta, x_axis, y_axis):
        
        print ("DELTA:", delta)
        
        fig, axs = plt.subplots(2, 2)
        
        #axs[0, 0].plot(x_axis[0], y_axis[0], marker='o')
        axs[0, 0].plot(x_axis[0], y_axis[0])
        axs[0, 0].set_title('$\Delta$=%s'%(delta[0]))
        
        axs[0, 1].plot(x_axis[1], y_axis[1], 'tab:orange')
        axs[0, 1].set_title('$\Delta$=%s' %(delta[1]))
        
        axs[1, 0].plot(x_axis[2], y_axis[2], 'tab:green')
        axs[1, 0].set_title('$\Delta$=%s'%(delta[2]))
        
        axs[1, 1].plot(x_axis[3], y_axis[3], 'tab:red')
        axs[1, 1].set_title('$\Delta$=%s' %(delta[3]))
        
        for ax in axs.flat:
            ax.set(xlabel='n', ylabel='$od_6$')
            ax.grid()
            ax.set_xscale('log')
        
        # Hide x labels and tick labels for top plots and y ticks for right plots.
        for ax in axs.flat:
            ax.label_outer()
        
        plt.show()
                
        
    def start(self):

        while self.g_counter <= self.num_of_iterations:
             
            self.g_delta_array.append(self.delta)
            self.get_delta_series()
 
            self.all_n_array.append(self.n_array)
            self.all_od6_array.append(self.delta_series_od6)
            
            self.n_array = []
            self.delta_series_od6 = []
            
            self.g_counter += 1
            self.delta += self.delta_increment
            
mode = 1

if mode == 0:
    
    print ("Initiated from Command Line")
    # Command line input handling
    v1 = int(sys.argv[1])
    delta = int(sys.argv[2])
    num_of_iterations = int(sys.argv[3])
    delta_increment = int(sys.argv[4])
    
    # v1, delta, num_of_iterations, delta_increment
    roxy = ROxy(v1, delta, num_of_iterations, delta_increment)
    roxy.set_dials()
    roxy.start()
    
    print ("Delta:", roxy.g_delta_array)
    print ("ALL n:", roxy.all_n_array)
    print ("ALL od6:", roxy.all_od6_array)
    
    roxy.plot_graph(roxy.g_delta_array, roxy.all_n_array, roxy.all_od6_array)
    
elif mode == 1:

    # v1, delta, num_of_iterations, delta_increment
    roxy = ROxy(2, 28, 4, 40)
    roxy.set_dials()
    roxy.start()
    
    print ("Delta:", roxy.g_delta_array)
    print ("ALL n:", roxy.all_n_array)
    print ("ALL od6:", roxy.all_od6_array)
    
    roxy.plot_graph(roxy.g_delta_array, roxy.all_n_array, roxy.all_od6_array)
    
else:
    print ("Mode Not Supported")
    exit(0)
