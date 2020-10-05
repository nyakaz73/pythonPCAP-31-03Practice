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
