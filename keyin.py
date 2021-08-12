# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 15:55:20 2021

@author: Laxshmi
"""

comps = 0
Finish = False
while not Finish :
    
    n = comps
    keys = input("Key in a Number(0 to finish) :")
    comps = int(keys)
    
     
    
    if comps > n  :
        print("Up")
        
    elif comps < n :
        print("Down")
     
    
    elif comps == n :
        print("Same")
        
    elif comps == 0 : 
        print ("Terminated")
        Finish = True
        
    
        
      
        
        

        
        
        
    
    

    
        
    
    
    

    


