class ExampleClass:

    def __init__(self,value=1):
        #INSTANCE VARIABLES ARE MUCH CLOSER TO THE OBJECT
        self.__first = value
        self.fifth = value
    
    def setSecond(self, value):
        self.__second = value

class ExampleClass2:
    ##CLASS VARIABLE COUNT ALWAYS PRESENT THE SAME VALUES IN ALL INSTANCES OF THIS CLASS
    count = 0
    def __init__(self,value=1):
        self.__first = value
        ExampleClass2.count +=1


if __name__ == '__main__':
    exampleObject1 = ExampleClass()
    exampleObject2 = ExampleClass(2)

    exampleObject2.setSecond(3)

    exampleObject3 = ExampleClass(4)
    exampleObject3.__third = 5 # this however will be aded as a normal property with underscored but no class name before the __ property
    exampleObject1.fifth = 100

    print(exampleObject1.__dict__)
    print(exampleObject2.__dict__)
    print(exampleObject3.__dict__)

    #to access the private instance variabl

    print(exampleObject1._ExampleClass__first) #prints the private variable.
    print('\n\n ############################################class variable###################')
    example1 = ExampleClass2()
    example2 = ExampleClass2(2)
    example3 = ExampleClass2(3)
    #a class variable always presents the same value in all class instances (objects)
    print(example1.__dict__, ExampleClass2.count)
    print(example2.__dict__, example2.count)
    print(example3.__dict__, example3.count)

print('\n\n\n')
print('####################check attribute existence hasattr()############')

class ExampleClass3:
    count = 0
    '''
    If a class has a constructor, it is invoked automatically and implicitly when the object of the class is instantiated.
    '''
    def __init__(self,value):
        if value %2 == 0:
            self.a = value
        else:
            self.b = value

    #self it identifies the object for which the method is invoked.ie
    def method(self):
        print('method')

print('#############hasattr works on both class variables and class instance variables##################')
exampleObject = ExampleClass3(1)
if hasattr(exampleObject,'a'):
    print(exampleObject.a)
else:
    print('No objhect a found')

print(exampleObject.b)

print(hasattr(ExampleClass3, 'count')) #Reutnes true coz the class has a class variable attr count

print('\n\n\n\n ###################Invoke a method in a class with a self through an object ######################')

exampleObject = ExampleClass3(1)
exampleObject.method()

print('Invoking it dureclty using a class name if it has a self wont work')

#print(ExampleClass3.method()) #this raised a type error

print('\n\n\n\n################HIDEN METHODS')

class ExampleClass:
    def __init__(self,value=1):
        self.first = value

    def __hidden(self):
        return 'this is a hidden method'
    
    def unhidden(self):
        pass


example = ExampleClass()

print(example.__dict__)
print(ExampleClass.__dict__)
print(example._ExampleClass__hidden) #this iwll simply give a reference , to run it put parethises
print(example._ExampleClass__hidden()) ##To access the private method you use class name with an underscore

print("####################__name__ and type on object###############\n\n")

print(ExampleClass.__name__)   #these returnes the names of the classes
print(type(example).__name__)


print('##############the __module__ contains the name of the module that the class belongs to###########\n\n\n')

print(type(example).__module__) #this returns __main__ if it was imported from another module/file it was going to return the name of that module.eg employees
print(example.__module__) #retunes the name of the module/filename to which its class is being ran from


print('#########################__bases__ is a tuple. The tuple contains classes (not class names) which are direct superclasses for the class.\n\n')

print(type(example))
print('\n########Inheritence##########n\n')
class A:
    pass
        
class B(A):
    pass

class C(B):
    pass

print(A.__bases__)
print(C.__bases__)

for i in C.__bases__ :
    print(i.__name__)

def printBaes(cls):
    for i in cls.__bases__:
        print(i.__name__)

printBaes(C)

print('######################## issubclass()     vs              isinstance()  ##########################\n')
print(issubclass(C,A)) #returns True C is a subclass of A

class G:
    def __init__(self,name):
        print('Now in G')
        self.name = 'Mufindisi'
    
    def __str__(self):
        print('Now in here')
        return "My name is {}".format(self.name)
    

class F(G):
    def __init__(self,name):
        self.name = name
    
    

class D(F):
    def __init__(self,name):
        super().__init__(name) #Inerit the super constructor if you want to have access to in instance varaibles

a = A()
b = B()
c = C()

print(isinstance(b,A)) #returns true since b class B is inheriting fdrom A
print(isinstance(c,A)) #RETUENS TRUE since c belong to C which belong to B which belong to A

print("############## superclass ########################")

d = D('John')

print(d) #Printing from the __str__ in super class F
print(d.name)


print("############# INHERITENCE HIERACHY#@#################\n\n\n")
print('#############    POLYMOPHISM ###########################') #WHERE a sublcass is alteringthe behavior of a superclass

class One:
    def __init__(self):
        self.name = 'One'

    def doit(self):
        print("doit from One")

    def doanything(self):
        self.doit()

class Two(One):
    def __init__(self):
        super().__init__()
        self.name = self.name

    def doit(self):
        print("doit from Two")

one = One()
two = Two()

one.doanything() #prints do it from One
two.doanything() #prints do it from Two  , sincce it is being invoked from Two | POLYMOPHISM when a child class is altering the behavior of a super class

print(one.name)
print(two.name)

print('#################### COMPOSITION #####################################\n\n')
print('This is a techinique of composing an object using a different object')
import time

class Tracks:
    def changedirection(self, left, on):
        print("tracks: ", left, on)

class Wheels:
    def changedirection(self, left, on):
        print("wheels: ", left, on)

class Vehicle:
    def __init__(self, controller):
        self.controller = controller

    def turn(self, left):
        self.controller.changedirection(left, True)
        time.sleep(0.25)
        self.controller.changedirection(left, False)

wheeled = Vehicle(Wheels())
tracked = Vehicle(Tracks())

wheeled.turn(True)
tracked.turn(False)



print(' Multiple Inheitence violates : single responsibility principle -> thus is not really encouraged')
print('Always chose COMPOSITION OVER Multiple Inheritence')

print('######################### try except else finally ##################\n\n')

def reciprocal(n):
    try:
        n = 1 / n
    except ZeroDivisionError:
        print("Division failed")
        n = None
    else:
        print("Everything went fine")
    finally:                            #finally is always printed unline else which is exceted if there are no errors
        print("It's time to say goodbye")
        return n

print(reciprocal(2))
print(reciprocal(0))

print("############### Making OWN exceptiona ########################## \n\n")
class PizzaError(Exception):
    def __init__(self, pizza, message):
        Exception.__init__(self, message)
        self.pizza = pizza


class TooMuchCheeseError(PizzaError):
    def __init__(self, pizza, cheese, message):
        PizzaError.__init__(self, pizza, message)
        self.cheese = cheese


def makePizza(pizza, cheese):
	if pizza not in ['margherita', 'capricciosa', 'calzone']:
		raise PizzaError(pizza, "no such pizza on the menu")
	if cheese > 100:
		raise TooMuchCheeseError(pizza, cheese, "too much cheese")
	print("Pizza ready!")


for (pz, ch) in [('calzone', 0), ('margherita', 110), ('mafia', 20)]:
	try:
		makePizza(pz, ch)
	except TooMuchCheeseError as tmce:
		print(tmce, ':', tmce.cheese)
	except PizzaError as pe:
		print(pe, ':', pe.pizza)


print('################ GENERATORS #################')

class Squar:
    def __init__(self, number):
        self.__number = number
        self.__result = 1
        self.__count = 0
    

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.__count > self.__number:
            raise StopIteration

        self.__result *= self.__result
        self.__count +=1
        return self.__result


x = Squar(2)

for i in Squar(2):
    print(i)

print('####################   yeild   keyword###########################\n\n')
'''
class based generator are not an issue but the invcovinience they come with really need us to think twice before implementing it in a class format way
The main discomfort it brings is the need to save the state of the iteration between subsequent __iter__ invocations.
'''
print('A function cannot be used as a generator becoz of its return statement , howver we can convert it to a generator by adding the yeild stmt')
print('Note that is isint a function anymoere but a generator object')

def my_generator_multiples_of_two(n):
    mult = 1
    for _ in range(n):
        yield mult
        mult *=2

print(my_generator_multiples_of_two(10)) #returns a generator object

multiplesof_list = [_ for _ in my_generator_multiples_of_two(8) ]

print(multiplesof_list)

'''
THE ABOUVE LIST COMPREHENSION IS JUST THE SAME AS THE FOLLOWING
'''
multiplesof_list = []
for _ in my_generator_multiples_of_two(8):
    multiplesof_list.append(_)

print(multiplesof_list)



list_odd_even = ['even' if _%2 == 0 else 'odd' for _ in range(10)]
print(list_odd_even)

'''
Now a Tuple Comprehension is used to create a GENERATOR
'''

generator_odd_even = ( 'even' if _%2 == 0 else 'odd' for _ in range(10))

print(generator_odd_even) #returns a generator object

for _ in generator_odd_even:
    print(_)


print('################ LAMBDA FUNCTION ###################################\n\n')

add = lambda x,y : x+y

print(add) #returns lamba function object

print(add(1,2)) #returns 3

sqr = lambda x : x**2

print(sqr(5)) #returns 25

'''
lAMDA FUNCTION THAT RETURNS A GENERATOR
'''
generator_pwr = lambda n : ( _**2 for _ in range(n))

print(generator_pwr(6))

for _ in generator_pwr(6):
    print(_)

'''
The above code is the same as
'''
def generator_pwr(n):
    for _ in range(n):
        yield _**2

print('################################## map #####################')
'''
Returns a map object which is an iterator applied of a given function and an iterable
'''

list_double = map(lambda x: 2*x, (1,2,3,4,5)) #this returns an iterable map object 
print(list(list_double)) #this converts the iterable map object to a list with [2,4,6,8,10]
numbers = (1, 2, 3, 4) 
result = map(lambda x: x + x, numbers) 
print(result) 


'''
Listify the string elements in a List of strings
'''

listified_list = list(map(list, ['hello','world','here']))
print(listified_list)

#this list function is similar to this
def listify(string_elemment):
    return list(string_elemment)  # ==> 'hello' => ['h','e','l','l','o'] listfifying  string