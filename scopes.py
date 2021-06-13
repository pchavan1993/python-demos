#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 17:34:16 2021

@author: pchavan
"""

x = 'global'

def f():
     #x = 'enclosing'

     def g():
         #x = 'local'
         print(x)

     g()


f()
