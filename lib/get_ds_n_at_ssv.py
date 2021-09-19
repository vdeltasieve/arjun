'''
Created on 20 Jul 2021

@author: vishalmudgal
'''

class N_DS_SSV(object):
    '''
    Calculate N on sum series when steady state is achieved on the delta series
    '''

    def __init__(self, dial1_list, delta, ssv, p_eo):
        
        self.a1 = dial1_list[0]
        self.a2 = dial1_list[1]
        self.delta = delta
        self.ssv = ssv
        self.p_eo = p_eo
        
    def get_n(self):
        
        # UC-A
        if (self.a1 == 0) and (self.a2 == -1):
        
            # UC-1
            if (self.delta % 4 == 2) and (self.p_eo % 2 == 0):
                
                d1 = (self.ssv//4) - 1
                n = (d1 * d1)
                return (n)
            
            # UC-2
            elif (self.delta % 4 == 0) and (self.p_eo % 2 == 0):
                
                dividend = self.delta//4
                
                if dividend % 2 == 1:
                    d1 = (self.ssv//4) - 1
                    n = (d1 * d1)
                    return (n)
            
                elif dividend % 2 == 0:
                    d1 = self.ssv//4
                    n = (d1 * d1) + 4
                    return (n)
                    
                else:
                    print ("dividend % 2 is neither 0 nor 1, exiting")
                    exit(0)
            
            # UC-3
            elif (self.delta % 4 == 2) and (self.p_eo % 2 == 1):
                
                d1 = (self.ssv - 1)//4
                n = (d1 * d1) + 3
                return (n)
            
            # UC-4
            elif (self.delta % 4 == 0) and (self.p_eo % 2 == 1):
                
                d1 = (self.ssv - 2)//4
                n = (d1 * d1) + 1
                return (n)
        
        # UC-B
        elif (self.a1 == -1) and (self.a2 == 0):

            # UC-1
            if (self.delta % 4 == 2) and (self.p_eo % 2 == 0):
                
                d1 = ((self.ssv - 1)//4) + 1
                n = (d1 * d1) + 7
                return (n)
            
            # UC-2
            elif (self.delta % 4 == 0) and (self.p_eo % 2 == 0):
                
                d1 = ((self.ssv - 2)//4) + 1
                n = (d1 * d1) + 3
                return (n)

            
            # UC-3
            elif (self.delta % 4 == 2) and (self.p_eo % 2 == 1):
                
                d1 = self.ssv//4
                n = (d1 * d1) + 2
                return (n)
            
            # UC-4
            elif (self.delta % 4 == 0) and (self.p_eo % 2 == 1):
                
                dividend = self.delta//4
                
                if dividend % 2 == 1:
                    d1 = self.ssv//4
                    n = (d1 * d1) + 4
                    return (n)
            
                elif dividend % 2 == 0:
                    d1 = (self.ssv//4) - 1
                    n = (d1 * d1)
                    return (n)
                    
                else:
                    print ("dividend % 2 is neither 0 nor 1, exiting")
                    exit(0)
                    
                
        else:
            print ('Given a1 and a2 are not configured, exiting')
            exit(0)
            
