#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 04:52:50 2021

@author: pchavan
"""

#create new classes using classes that have already been defined


#base class
class Animal():
    def __init__(self):
        print('ANIMAL CREATED')
        
    def who_am_i(self):
        print('I am an animal')
        
    def eats(self):
        print('I am eating')
        

class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print('Dog created')

        
my_dog=Dog()
my_dog.eats()
my_dog.who_am_i()





import pandas as pd
#over writing older class method or adding new methods
class Clean():
    def __init__(self):
        print('ANIMAL CREATED')
    
        
    def lookup(self):
        
        
    def delete_first_column(self):
        
        del df['col1']
        print('I am an animal')
        
    def eats(self):
        print('I am eating')
        

class CSV(Clean):
    def __init__(self):
        Animal.__init__(self)
        print('Dog created')
        
    def read_csv(self):
        df=pd.read_csv('xyz.csv')
            print('I am a Dog')
        
    def delete_first_column(self):
        
            print('WOOF')
            
class XLSX(Clean):
    def __init__(self):
        Animal.__init__(self)
        print('Dog created')
        
    def read_xlsx(self):
        df=pd.read_xlsx()
            print('I am a Cat')
        
    def delete_first_column(self):
            print('MEOW')

        
my_dog=Dog()
my_dog.who_am_i()
my_dog.bark()


#POLYMORPHISM different object classes have same method names and you can call them together even though different objects are passed in

class Dog():
    def __init__(self,name):
        self.name=name
    
    def speak(self):
        return self.name+' Woof!'

class Cat():
    def __init__(self,name):
        self.name=name
    
    def speak(self):
        return self.name+' Meow!'


niko=Dog('niko')
felix=Cat('felix')


print(niko.speak())
print(felix.speak())

for pet in [niko,felix]:
    print(type(pet))
    print(type(pet.speak()))

for pet in [niko,felix]:
    print(type(pet))
    print(pet.speak())


def pet_speak(pet):
    print(pet.speak())
    
pet_speak(niko)
pet_speak(felix)




class Animal():
    def __init__(self,name):
        self.name=name
        
    def speak(): #abstract method coz it really is not doing anything but is depending on other classes 
        raise NotImplementedError('Subclass must implement this abstract method')

class Dog(Animal):
        def speak(self):
            return self.name+' says woof!'
        
class Cat(Animal):
        def speak(self):
            return self.name+' says meow!'

#myanimal=Animal('fred')
#myanimal.speak()

milo=Dog('Milo')
sox=Cat('Sox')

print(milo.speak())
print(sox.speak())


#example open files
