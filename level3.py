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

def get_radian(angle):
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

# task 12
get_task_description(12, 'Subtract Last Digit')

def get_last_digit(number):
    digits = [int(x) for x in str(number)]
    return int(digits[-1])

def subtract_last_digit(num1, num2):
    return num1 - get_last_digit(num2)

get_task_result(12, subtract_last_digit(25, 17))
put_empty_line()

# task 14
get_task_description(14, 'String Length')

word = get_rand_word();

def getStringLength(word):
    stringLentgh = len(word)
    return stringLentgh

print("Word is: " + word)
get_task_result(14, repeat_string(getStringLength(word), word))
put_empty_line()

# task 17
get_task_description(17, 'str_int')

def str_int(param1, param2):
    param1_type = type(param1).__name__
    param2_type = type(param2).__name__

    if param1_type == 'str' and param2_type == 'int' or param1_type == 'int' and param2_type == 'str':

        if param1_type == 'int':
            get_task_result(17, repeat_string(param1, param2))
        else:
            get_task_result(17, repeat_string(param2, param1))
    else:
        if param1_type == 'int' and param2_type == int:
            get_task_result(17, get_sum(param1, param2))
        else:
            get_task_result(17, param1 + param2)

str_int(2, 5)
str_int(2, 'perfect')
str_int('perfect', 2)
str_int('perfect', 'discipline')
put_empty_line()

