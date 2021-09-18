'''
Created on 20 Jul 2021

@author: vishalmudgal
'''

class SSV(object):
    '''
    classdocs
    '''

    def __init__(self, dial1_list, delta, p):
        
        self.a1 = dial1_list[0]
        self.a2 = dial1_list[1]
        self.delta = delta
        self.p = p
        
    def get_val(self):
        

        # UC-A
        if (self.a1 == 0) and (self.a2 == -1):
            
            # OD-4
            if  ((self.delta % 4 == 2) and (self.p % 2 == 0)) or ((self.delta % 4 == 0) and (self.p % 2 == 1)):
                
                od4_ssv = ((self.delta * self.delta)//2) + 2
                return (od4_ssv)
            
            # OD-2
            elif ((self.delta % 4 == 0) and (self.p % 2 == 0)) or ((self.delta % 4 == 2) and (self.p % 2 == 1)):
                
                od2_ssv = (self.delta//2) * (self.delta//2)
                return (od2_ssv)
            
            else:
                print ("Condition didn't match inside SSV, exiting")
                exit(0)
                
                
        # UC-B
        elif (self.a1 == -1) and (self.a2 == 0):
            
            # OD-2
            if  ((self.delta % 4 == 2) and (self.p % 2 == 0)) or ((self.delta % 4 == 0) and (self.p % 2 == 1)):
                
                od2_ssv = (self.delta//2) * (self.delta//2)
                return (od2_ssv)
                
            # OD-2
            elif ((self.delta % 4 == 0) and (self.p % 2 == 0)) or ((self.delta % 4 == 2) and (self.p % 2 == 1)):
                
                od4_ssv = ((self.delta * self.delta)//2) + 2
                return (od4_ssv)
            
            else:
                print ("Condition didn't match inside SSV, exiting")
                exit(0)
                
        else:
            print ("Condition didn't match inside SSV, exiting")
            exit(0)
                