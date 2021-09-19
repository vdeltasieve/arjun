'''
Created on 20 Jul 2021

@author: vishalmudgal
'''

class P_DS_SSV(object):
    '''
    Calculates p at SSV for any delta
    '''

    def __init__(self, dial1_list, delta, ssv, p):
        
        self.a1 = dial1_list[0]
        self.a2 = dial1_list[1]
        self.delta = delta
        self.ssv = ssv
        self.p = p
        
    def get_p(self):
        
        # UC-A
        if (self.a1 == 0) and (self.a2 == -1):
        
            # UC-1
            if (self.delta % 4 == 2) and (self.p % 2 == 0):
                
                inter_1 = ((self.delta - 6)//4) + 1
                p = (2 * ((inter_1 * inter_1) - 1)) + 2
                return (p)
            
            # UC-2
            elif (self.delta % 4 == 0) and (self.p % 2 == 0):
                
                dividend = self.delta//4
                
                # UC-2A
                if dividend % 2 == 1:
                    inter_1 = (self.delta - 4)//4
                    p = (inter_1 * inter_1)
                    return (p)
                
                # UC-2B
                elif dividend % 2 == 0:
                    inter_1 = (self.delta - 4)//4
                    p = (inter_1 * (inter_1 + 1)) - (inter_1 - 1)
                    return (p)
                
                else:
                    print ("dividend % 2 is neither 0 nor 1, exiting")
                    exit(0)
            
            # UC-3
            elif (self.delta % 4 == 2) and (self.p % 2 == 1):
                
                inter_1 = (self.delta - 6)//4
                p = ((inter_1 + 1) * (inter_1 + 1)) - inter_1
                return (p)
            
            
            # UC-4
            elif (self.delta % 4 == 0) and (self.p % 2 == 1):
        
                inter_1 = (self.delta - 4)//4
                p = (2 * (inter_1) * (inter_1 + 1)) + 1
                return (p)
            
        # UC-B
        elif (self.a1 == -1) and (self.a2 == 0):

            # UC-1
            if (self.delta % 4 == 2) and (self.p % 2 == 0):
                
                inter_1 = (self.delta - 6)//4
                p = ((inter_1) * (inter_1 + 1)) + 2
                return (p)
            
            # UC-2
            elif (self.delta % 4 == 0) and (self.p % 2 == 0):
                
                inter_1 = (self.delta - 4)//4
                p = (2 * (inter_1) * (inter_1 + 1)) + 2
                return (p)

            
            # UC-3
            elif (self.delta % 4 == 2) and (self.p % 2 == 1):
                
                inter_1 = ((self.delta - 6)//4) + 1
                p = (2 * ((inter_1 * inter_1) - 1)) + 3
                return (p)
            

            # UC-4
            elif (self.delta % 4 == 0) and (self.p % 2 == 1):
                
                dividend = self.delta//4
                
                # UC-4A
                if dividend % 2 == 1:
                    inter_1 = (self.delta - 4)//4
                    p = (inter_1 * (inter_1 + 1)) - (inter_1 - 1)
                    return (p)
            
                # UC-4B
                elif dividend % 2 == 0:
                    inter_1 = (self.delta - 4)//4
                    p = (inter_1 * inter_1)
                    return (p)
                    
                else:
                    print ("dividend % 2 is neither 0 nor 1, exiting")
                    exit(0)
                
        else:
            print ('Given a1 and a2 are not configured, exiting')
            exit(0)
            
