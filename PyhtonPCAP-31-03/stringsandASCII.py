'''
The capitals comes first in ASCII American Standarard Code for Information Interchange
A B C D---Z
ab c...z

'''

x= "zxaAbgZCfgksK"

print(ord(x[2])) #a => 97
print(ord(x[3])) #A => 65

print(ord(x[2]) -ord(x[3]) ) #difference is 32 meaning 

print(min(x)) #A is the min not its A not a coz of ASCII code A comes before a

print(max(x))# Z same here Z before z

print(x.index('z')) #=> 0th positino

print(list(x)) # => ['z','x','a',...]

print(x.count('g')) # => 2

print(x.capitalize()) #Zxa... not everything else will be lower cased inlcuding ince were capitalized like AZX..
print("gocdhoope".find('o',2)) #find the index position of first occurence of o starting from index 2

print('Hello World'.isalnum()) #thiis retunts False coz space is nether a digit nor a leter
t = 'ΑβΓδ'
print(t.isalnum()) #returns True coz these are all greek letters

print('avc3'.isalpha()) #returns False coz 3 is not an Alfa

print('232'.isdigit()) #returns True coz they are all digits

print('2.344'.isdecimal()) #returns False coz they are all floating

print('2.342'.isupper())

print(','.join("hjhjhjhh")) #the join expects an iterable list that why the result looks like this h,j,j,... coz the parsed string was first converted to a list then join operator perfomed

print('\''.join(['1','2','3','4','5'])) #joining with a escaped ' character # rember the list should contain strings otherwise a TypeError will be raised

print('aSdFDd'.lower()) #returns a lower cased string

print("HelloWorld.org.com".lstrip("lo."))
print("www.cisco.com".lstrip("w."))
print("pythoninstitute.orgpo".lstrip(".org"))

print("This is it".replace("is","surely",1)) #argument 1 minimizes the number of replacement in this case to 1

print("ta ta rf ta".rfind("ta")) #gets the highest ta to the far right at pos 9 

print("ta ta rf ta".rfind("rf",7)) #return -1 meaning not found since we are finding rf from position 7

print("h jh jh jhh".split())

print("dfdfd".isalpha())

print(" ".strip().split())

print('a'>'A') #return True remember is used lexagraphic irder of ASCII AND UNICODE A comes before a

print('a'.isupper())





strng = input("Enter the text to encrypt: ")
assert 1 >2


def cipher(strng):
    ciphered = ''
    shift  = int(input("Enter shift value: "))
    for char in strng:
        '''if not char.isalpha():
            continue'''
        #char = char.upper()
        if shift in range(1,26):
            code = ord(char) + shift
            if char.isupper():
                if code > ord('Z'):
                    code = ord('A')
            else:
                if code > ord('z'):
                    code = ord('a') 

            if char.isalpha():
                ciphered += chr(code)
            else:
                ciphered += char
    return ciphered


print(cipher(strng))
            
            
            
            




'''
# Caesar cipher
text = input("Enter your message: ")
cipher = ''
for char in text:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) + 1
    if code > ord('Z'):
        code = ord('A')
    cipher += chr(code)

print(cipher)

def decipher(cipher):
    deciphered_result = ''
    for char in cipher:
        if not char.isupper():
            continue
        code = ord(char) - 1
        if code < ord('A'):
            code = ord('Z')
        
        deciphered_result += chr(code)
        
    return deciphered_result

print(decipher(cipher))'''