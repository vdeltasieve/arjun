'''
Created on 18 Jul 2021

@author: vishalmudgal
'''
import sys
import math
import decimal
from lib.get_ds_n_at_ssv import N_DS_SSV
from lib.get_quadratic_roots import Quadratic_Roots

decimal.getcontext().prec = 5000

#DSC = Delta Sum Connect
class DSC_Trapdoor(object):
    '''
    Message Encryption, Private Key Generation and Message Decryption are tested here
    '''

    def __init__(self, delta):
        
        self.delta = delta
        
        # Sum Series
        self.sum_a1 = -1
        self.sum_a2 = 0
        self.sum_v1 = 2
        self.sum_v2 = 2
        
        # Delta Series
        self.delta_v1 = 2
        self.delta_v2 = 2
        
        if delta % 4 == 0:
            self.delta_a1 = 0
            self.delta_a2 = -1
        
        elif delta % 4 == 2:
            self.delta_a1 = -1
            self.delta_a2 = 0
        
        else:
            pass
        
    '''
    def get_ssv(self, delta):
        
        static_state_val_1 = delta//2
        ssv = (static_state_val_1 * delta) + ((self.delta_v1 * self.delta_v1)//2)
        print ("SSV:", ssv)
        return (ssv)
    '''
        
    def get_p_at_ssv(self, delta):
        
        if delta % 4 == 0:
            
            p_inter_1 = (delta - 4)//4
            p_inter_2 = p_inter_1 + 1
            p_at_ssv = (2 * p_inter_1 * p_inter_2) + 1
            
            return (p_at_ssv)
        
        elif delta % 4 == 2:
            
            p_inter_1 = (delta - 4)//4
            p_inter_2 = p_inter_1 + 1
            p_at_ssv = (2 * p_inter_1 * p_inter_2) + 1
            
            return (p_at_ssv)
        
        else:
            pass
        
    def get_od6(self, p):
        
        q = p + self.delta
        n = q * p
        n_root = math.floor(decimal.Decimal(n).sqrt())
        
        if n_root % 2 == 0:
            d1 = n_root + self.delta_a1
            d2 = d1 + self.delta_v1
            
        elif n_root % 2 == 1:
            d1 = n_root + self.delta_a2
            d2 = d1 + self.delta_v1
        else:
            pass    
        
        od1 = (d1 * d1) - n
        od2 = (d2 * d2) - n
        od6_inter = (4 * n) + (od1 * od2)
        od6 = math.floor(decimal.Decimal(od6_inter).sqrt())
        
        #print ("od1=%d, od2=%d, od6=%d"%(od1, od2, od6))
        return (od6)
    
    def get_n_at_sum_series(self, od6):
        
        if self.delta % 4 == 0 :
            N = od6
            #print ("N=", N)
            return (N)
        elif self.delta % 4 == 2:
            N = od6 + 1
            #print ("N=", N)
            return (N)
        else:
            print ("Error inside n_at_sum_series, exiting")
            exit(0)
            
    def get_p_at_N_ssv(self, N):
        
        quadratic_sol = Quadratic_Roots(1, -self.delta, N)
        p, q = quadratic_sol.start()
        #print ("N_p_ssv=%d, N_q_ssv=%d" %(p,q))
        return (p, q)
    
    def get_priv_key(self, p_ss_ssv):
        
        p_sum_series = p_ss_ssv - self.p_dist
        q_sum_series = self.delta - p_sum_series
        N_sum_series = p_sum_series * q_sum_series
        private_key = N_sum_series - self.msg_od6
        
        #print ("Private Key")
        #print ("p=%d, q=%d, N=%d, priv_key=%d" 
        #       %(p_sum_series, q_sum_series, N_sum_series, private_key))
        return (private_key)

    def encrypt_message(self, message):

        p = message
        q = p + self.delta
        #print ("q=", q)
        n = p * q
        #print ("n=", n)
        self.p_dist = self.p_at_ssv - p
        #print ("p_dist=", self.p_dist)
        self.msg_od6 = self.get_od6(p)
        
    def get_N_factors_for_decrypt(self, od6, priv_key):
        
        N_fd_sum_series = od6 + priv_key
        #print ("...DECRYPTION CONTINUES")
        
        quadratic_sol = Quadratic_Roots(1, -self.delta, N_fd_sum_series)
        p, q = quadratic_sol.start()
        #print (N_fd_sum_series, p, q)
        return (p, q)
        
    def get_n_at_ssv(self, delta, ssv):
        
        #print ("Inside get_n_at_ssv")
        #n, d1 = GetN_At_SSV(delta, ssv).calculate_n_at_od4()
        
        p_eo = 1
        dial_list = [self.delta_a1, self.delta_a2]
        n = N_DS_SSV(dial_list, delta, ssv, p_eo).get_n()
        
        #print ("delta:%d, ssv:%d, n:%d, d1:%d" %(delta,ssv,n,d1))
        return (n)
        
    def encrypt(self, message):
        
        #ssv = self.get_ssv(self.delta)
        #n_at_ssv = self.get_n_at_ssv(self.delta, ssv)
        #print ("N at ssv:",n_at_ssv)
        
        self.p_at_ssv = self.get_p_at_ssv(self.delta)
        self.od6_at_ssv = self.get_od6(self.p_at_ssv)
        
        self.encrypt_message(message)
        
        self.N_at_ssv = self.get_n_at_sum_series(self.od6_at_ssv)
        self.p_ss_ssv, self.q_ss_ssv = self.get_p_at_N_ssv(self.N_at_ssv)
        self.private_key = self.get_priv_key(self.p_ss_ssv)

        #print (self.p_ss_ssv, self.q_ss_ssv)

    def decrypt(self, od6, priv_key, delta):
        
        p, q = self.get_N_factors_for_decrypt(od6, priv_key)
        
        #decrypt_ssv = self.ssv(delta)
        decrypt_p_at_ssv = self.get_p_at_ssv(delta)
        decrypt_od6_at_ssv = self.get_od6(decrypt_p_at_ssv)
        decrypt_N_at_ssv = self.get_n_at_sum_series(decrypt_od6_at_ssv)
        
        decrypt_p_ss_ssv, decrypt_q_ss_ssv = self.get_p_at_N_ssv(decrypt_N_at_ssv)
        q_dist_ss = q - decrypt_q_ss_ssv
        self.p_original = decrypt_p_at_ssv - q_dist_ss
        
        #print ("DECRYPT")
        #print ("N Factors: p=%d, q=%d" %(p, q))
        #print ("p_at_ssv=%d, od6_at_ssv=%d, N_at_ssv=%d" %(decrypt_p_at_ssv, decrypt_od6_at_ssv, decrypt_N_at_ssv))
        #print ("p_ss_ssv=%d, q_ss_ssv=%d, q_dist_ss=%d, p_original=%d" %(decrypt_p_ss_ssv, decrypt_q_ss_ssv, q_dist_ss, self.p_original))        
        
#delta   = 83713882446892864889068083713882448684837138824468928648890680837138824488837138824468928648890680837138824486848371388244689286488906808371388244888371388244689286488906808371388244868483713882446892864889068083713882448883713882446892864889068083713882448684837138824468928648890680837138824488
#message = 65857788448688988488448088998648448658577884486889884884480889986484488666585778844868898848844808899864844865857788448688988488448088998648448866658577884486889884884480889986484486585778844868898848844808899864844886665857788448688988488448088998648448658577884486889884884480889986484488666585778844868898848844808899864844865857788448688988488448088998648448866658577884486889884884480889986484486585778844868898848844808899864844886665857788448688988488448088998648448658577884486889884884480889986484488666585778844868898848844808899864844865857788448688988488448088998648448866

mode = 1

if mode == 0:
    print ("Initiated from Command Line")
    # Command line input handling
    # 0 -1 2 2 1000 992 od4 soz
    
    delta = int(sys.argv[1])
    message = int(sys.argv[2])

    dse = DSC_Trapdoor(delta)
    dse.encrypt(message)
    #print ("Steady State Value:", dse.ssv)
    #print ("p at SSV:", dse.p_at_ssv)
    #print ("OD6 at SSV:", dse.od6_at_ssv)
    print ("Original Message:", message)
    print ("Encrypted Message:", dse.msg_od6)
    print ("Private Key:", dse.private_key)
    
    #print ("Len of Delta: %s, Len of Message: %s, Len of private key: %s" \
    #       %(len(str(delta)), len(str(message)), len(str(dse.private_key))))
    
    dse.decrypt(dse.msg_od6, dse.private_key, delta)
    print ("Decrypted Message:", dse.p_original)
    
    #print ("\n")
    #print ("Different between p_at_ssv and message:", dse.p_at_ssv - message)
    print ("Two Messages:%d, %d, %d" %(message-dse.p_original, message, dse.p_original))
    

elif mode == 1:
    
    delta = 136
    message = 65
    
    dse = DSC_Trapdoor(delta)
    dse.encrypt(message)
    #print ("Steady State Value:", dse.ssv)
    #print ("p at SSV:", dse.p_at_ssv)
    #print ("OD6 at SSV:", dse.od6_at_ssv)
    print ("Original Message:", message)
    print ("Encrypted Message:", dse.msg_od6)
    print ("Private Key:", dse.private_key)
    
    #print ("Len of Delta: %s, Len of Message: %s, Len of private key: %s" \
    #       %(len(str(delta)), len(str(message)), len(str(dse.private_key))))
    
    dse.decrypt(dse.msg_od6, dse.private_key, delta)
    print ("Decrypted Message:", dse.p_original)
    #print ("\n")
    #print ("Different between p_at_ssv and message:", dse.p_at_ssv - message)
    print ("Two Messages:%d, %d, %d" %(message-dse.p_original, message, dse.p_original))
    

else:
    print ("Mode Not Supported")
    exit(0)

