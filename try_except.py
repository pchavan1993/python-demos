#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 09:09:04 2021

@author: pchavan
"""

try:
    result=10+10
except:
    print('Hey looks like something is wrong')
else:
    print('Your code was successful')
    print(result)
    
    
    
try:
    f=open('testfile','w')
    f.write('Writing a test line')
except TypeError:
    print('There was a type error!')
except OSError:
    print('There was an OS error!')
finally:
    print('I always run')
    
    
#link https://docs.python.org/3/library/exceptions.html
    
try:
    f=open('testfile','r')
    f.write('Writing a test line')
except TypeError:
    print('There was a type error!')
except OSError:
    print('There was an OS error!')
except:
    print('Some other error that was not handled')
finally:
    print('I always run')
    


def ask_for_int():
    while True:
        try:
            result=int(input('Please provide a number: '))
        except:
            print('Whoops that is not a number')
            continue
        else:
            print('Yes thank you')
            break
        finally:
            print('Im going to ask you again!')
            
ask_for_int()

#even if the condition will succeed finally will print the statement which is why we dont mix else and finally