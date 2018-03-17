# SingPath's level_3 task
# Implementer: Abilkhayir Akhet

'''
В 3 уровне решил не все подряд делать, а выборочно, так как выполнение определенных тасков
включает в себе выполнение более ранних тасков
'''

from commonmethods import get_task_description
from commonmethods import get_task_result
from commonmethods import put_empty_line
from commonmethods import get_level_number
from commonmethods import get_rand_word


get_level_number(3)
put_empty_line()

import random
import math

# task1
get_task_description(1, 'Functions')
rand_number = random.randint(1, 9)

def square(int):
    return int*int

print('Input integer is: ' + str(rand_number))
get_task_result(1, square(rand_number))
put_empty_line()

# task 2
get_task_description(2, 'Increment')
rand_number = random.randint(0, 1000)

def getIncrement(int):
    return int+1

print('Input integer is: ' + str(rand_number))
get_task_result(2, getIncrement(rand_number))
put_empty_line()

# task 3
get_task_description(3, 'Product')

a = random.randint(1, 1000)
b = random.randint(1, 1000)

def product(a, b):
    return a*b


print('number a is :' + str(a))
print('number b is :' + str(b))
get_task_result(3, product(a, b))
put_empty_line()

# task 4
get_task_description(4, 'Add two numbers')
a = random.randint(1, 1000)
b = random.randint(1, 1000)

def get_sum(a, b):
    return a+b


print('number a is :' + str(a))
print('number b is :' + str(b))
get_task_result(4, get_sum(a, b))
put_empty_line()

# task 5
get_task_description(5, 'Double String')
word = get_rand_word()
print(word)

def double_word(word):
    return str(word)+str(word)

get_task_result(5, double_word(word))
put_empty_line()

# task 6
get_task_description(6, 'Repeat String')
number = random.randint(1, 10)
word   = get_rand_word()

def repeat_string(number, word):
    str = ''
    for x in range(0, number):
        str += word

    return str

print('rand number is: ' + str(number))
print('rand word is ' + str(word))
get_task_result(6, repeat_string(number, word))
put_empty_line()

# task 7
get_task_description(7, 'Math Module')

radius = random.randint(1, 100)

def calc_circle_area(radius):
    return math.pi * math.pow(radius, 2)


print('Rand raduis is: ' + str(radius))
get_task_result(7, calc_circle_area(radius))
put_empty_line()

# task 8
get_task_description(8, 'Radians')

angle = random.randint(1, 360)

def get_radian(ange):
    return (angle * math.pi) / 180


print('Rand angle is: ' + str(angle))
get_task_result(8, get_radian(angle))
put_empty_line()


# task 9
get_task_description(9, 'Math Functions - cosine')

angle = random.randint(1, 360)

def get_cosine(angle):
    return math.cos(get_radian(angle))


print('Rand angle is: ' + str(angle))
get_task_result(9, get_cosine(angle))
put_empty_line()

# task 10
'''
get_task_description(10, 'Keyword Arguments')

def sandwich(bread, meat="mutton", cheese=None):
    result_string = bread + " bread sandwitch with " + meat
    if cheese != str(None):
        result_string += " and " + str(cheese) + " cheese"
    return result_string


print("sandwich with cheese : " + get_task_result(10, sandwich('Rye')))
put_empty_line()
'''

# task 11
get_task_description(11, 'Curry Puff')

def get_curry_puff_cost(type = 'Chicken'):
    if type == 'Fish':
        return 1.4
    return 1.2

get_task_result(11, get_curry_puff_cost('Fish'))
put_empty_line()