#Python 3 defines 63 built-in exceptions
'''
                        BaseException
                        ↑
                        Exception
                        ↑
    LookupError         ArithmeticError
                        ↑
                        ZeroDivisionError
'''
'''try:
    x = int(input("Enter value \t: ",))
    answer = 100/x
    print(answer)
except ZeroDivisionError:
    print('Cannot divide by zero')

except ValueError:
    print('Must be a number')

except:
    print('Something went wrong')'''



try:
    answer = 100/0
    
except ZeroDivisionError:
    print('Zeror Division Eroor')
except ArithmeticError:
    print('Arithmentic Error')
    

def badFunc(x):
    try:
        return x/'HJJH'
    except:
        print('I did it again')
        raise #we are raising an error because so that we handle it when the function is called


try:
    print(badFunc(100))
except ZeroDivisionError:
    print('I see')
except ValueError:
    print('Value error')
except:
    print('Bad data')

print('END!!')

print('***********************************\n\n\n')
def readint(prompt, min, max):
    x = int(input(prompt))
    try:
        assert (x >= min and x<=max)
    except AssertionError:
        print('the value is not within permitted range (-10..10)')
    
    except ValueError:
        print('wrong input')
#
# put your code here
#

v = readint("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)