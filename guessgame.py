# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 20:21:12 2021

@author: Laxshmi
"""

import random 

def guess(x) :
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a Number between 1 and {x} :'))
        if guess < random_number :
            print('Sorry,guess again.Too low')
        elif guess > random_number :
            print('Sorry,guess again. Too high')
        else :
            print('Your answer is correct, Congratulations!')
            
            
guess(10)            




#the loop will go on until the user's guess is correct            