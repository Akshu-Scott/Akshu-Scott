# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 13:11:06 2021

@author: Laxshmi
"""

#concatenate -this term is very frequently asked in python programming

##counter object is going to give the count of the number of striings
def longest_palindrome(s : str ,self) -> str :
    res = " "
    reslen = 0
    
    for i in range(len(s)) :
        #odd length
        l, r = i ,i
        while l >= 0 and r <=len(s) and s[l] == s[r] :
            
    