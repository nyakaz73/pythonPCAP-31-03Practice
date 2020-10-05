
from random import random, seed, randint, randrange, choice,sample
from datetime import datetime

#1. random shnowng rand numbers between 0 < x < 1
for _ in range(5):
    print(random(), end= ' ')

#2. seeding showing the generated rand numbers doe not change if the see number its the same
seed(20)
print ("first Number ", randint(25,50))

seed(30)
print ("Second Number ", randint(25,50))

seed(20)
print ("Third Number ",randint(25,50))

print('------------------------randrange with seed and step-----------------------------')

#3. randrange with seed and step over of 2
seed(10)
for _ in range(10):
    print(randrange(0,5,2), end=' ')
print('\n')
seed(10)
for _ in range(10):
    print(randrange(0,5,2), end=' ')

print('\n')
print('------------------------SAMPLE AND CHOICE-----------------------------')

#4. DISADVANTAGE OF THE ABOVE INVOCATIONS IS THAT THEY RETURN REPETED SAMPLES
    # WHAT IF YOU WANT TO RETURN A UNQIUE SAMPLE EVERYTIME THERE IS A DRAW LIKE A LOOTTTTTOOOO WE WOULDNT WANT THE DRAWN ELEMENT TO BE REPEATED IN A SINGLE OUTPUT

#choice , and sample

draw_list = [1,2,3,4,5,6,7,8,9,10]

print(choice(draw_list)) #select a random element from the list

print(sample(draw_list,5)) #sample or draw five items from the list

print(sample(draw_list,8)) #draw 8 items from the list