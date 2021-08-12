# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 13:02:08 2021

@author: Laxshmi
"""

lists = [ ]


n = int(input("Enter the number of Elements in array :"))

for i in range(0,n) :
    num = input("Enter the element:")
    b = int(num)
    lists.append(b)
    
    
print(lists)



def insertion_sort(lis):
    indexing_element = range(1,len(lis))
    for  i in indexing_element :
        value_to_sort = lis[i]
        
        while lis[i-1] > value_to_sort and i > 0 :
            lis[i-1] , lis[i] = lis[i] , lis[i-1]
            i = i-1
            
    return lis



print("The sorted list is :",end="")  
lt = insertion_sort(lists)
print(lt)
      
            
    
    


    
    
    
    



