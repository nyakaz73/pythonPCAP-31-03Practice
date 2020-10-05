class ExampleClass:
    def __init__(self,value=1):
        self.__first = value
        self.fifth = value
    
    def setSecond(self, value):
        self.__second = value
    

if __name__ == '__main__':
    exampleObject1 = ExampleClass()
    exampleObject2 = ExampleClass(2)

    exampleObject2.setSecond(3)

    exampleObject3 = ExampleClass(4)
    exampleObject3.__third = 5
    exampleObject1.fifth = 100

    print(exampleObject1.__dict__)
    print(exampleObject2.__dict__)
    print(exampleObject3.__dict__)

    #to access the private instance variabl

    print(exampleObject1._ExampleClass__first)