

#name of the class Camel Case 
#init method creates an instance of the actual object. self keyword, parameters that you are going to use
#you write self.{variable_name} so that you access the variable within the 'Scope' and not the variable declared elsewhere in the program
#self is written in the method some_method(self) to connect it to the class NameofClass

class NameofClass():
    
    
    def __init__(self,param1,param2):
        self.param1=param1
        self.param2=param2
        
        
    def clean_zip(self):
        #logic to clean zip
        print(self.param1)
    
        
 #creation of the class       
        
class Sample():
    
    
    
    pass

#create instance of a class

my_sample=Sample()

type(my_sample)



#attribute is a characteristic of the object
#init can be thought of constructor of the class
#self instance of the object, it can be named anything but is named self by convention
#its cleaner to name breed 3 times rather than naming the parameters differently
class Dog():
    def __init__(self,breed):
        self.breed=breed

#create instance of a class

#my_dog=Dog(breed) #errors out


my_dog=Dog(breed='Lab')

type(my_dog)
my_dog.breed



class Dog():
    def __init__(self,breed,name,spots):
        self.breed=breed
        self.name=name
        self.spots=spots #expected boolean

#create instance of a class

my_dog=Dog('Lab','Sam',False) 


my_dog.breed


class Dog():
    
    #class object attributes, it is same for all instances of the class
    species='mammal'
    
    
    def __init__(self,breed,name,spots):
        self.breed=breed
        self.name=name
        self.spots=spots #expected boolean

#create instance of a class

my_dog=Dog('Lab','Sam',False) 


my_dog.species




class Dog():
    
    #class object attributes, it is same for all instances of the class
    species='mammal'
    
    
    def __init__(self,breed,name,spots):
        self.breed=breed
        self.name=name
        self.spots=spots #expected boolean
    
    def bark(self):
        print('WOOF my name is {}'.format(name))
#create instance of a class

my_dog=Dog('Lab','Frankie',False) #errors out

#methods need to be executed 
#my_dog.bark
my_dog.bark()



class Dog():
    
    #class object attributes, it is same for all instances of the class
    species='mammal'
    
    
    def __init__(self,breed,name,spots):
        self.breed=breed
        self.name=name
        self.spots=spots #expected boolean
    
    def bark(self):
        print('WOOF my name is {}'.format(self.name))
#create instance of a class

my_dog=Dog('Lab','Frankie',False) #errors out

#methods need to be executed 
my_dog.bark
my_dog.bark()




class Dog():
    
    #class object attributes, it is same for all instances of the class
    species='mammal'
    
    
    def __init__(self,breed,name,spots):
        self.breed=breed
        self.name=name
        self.spots=spots #expected boolean
    
    def bark(self,number):
        self.number=number
        
        print('WOOF my name is {} and  the number is {}'.format(self.name,self.number))
        #we do not write self.number because it is not attached to the instance of the class and is expected from the user
#create instance of a class

my_dog=Dog('Lab','Frankie',False) #errors out

#methods need to be executed 
#my_dog.bark
my_dog.bark(10)










class Circle():
    pi=3.14
    
    def __init__(self,radius=1):#note that radius has a default value 
        self.radius=radius
        
    def get_circumference(self):
        return 2*self.pi*self.radius
    
my_circle=Circle()
my_circle.pi
my_circle.radius
my_circle.get_circumference()


class Circle():
    pi=3.14
    
    def __init__(self,radius=1):#note that radius has a default value 
        self.radius=radius 
        self.area=self.pi*radius*radius  #or Circle.pi
        
    def get_circumference(self):
        return 2*self.pi*self.radius
    
my_circle=Circle(30)
my_circle.pi
my_circle.radius
my_circle.get_circumference()











