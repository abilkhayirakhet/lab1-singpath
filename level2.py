# SingPath's level_2 task
# Implementer: Abilkhayir Akhet

'''
Во 2 уровне решил не все подряд делать, а выборочно, так как выполнение определенных тасков
включает в себе выполнение более ранних тасков
'''

from commonmethods import get_task_description
from commonmethods import get_task_result
from commonmethods import put_empty_line
from commonmethods import get_level_number

get_level_number(2)
put_empty_line()

# task 5
get_task_description(5, 'Python Math')
a = 1
b = 2
c = a+b
get_task_result(5, c)
put_empty_line()

# task 6
get_task_description(6, 'More Python Math')
seconds_in_year = 60*60*24*365
get_task_result(6, seconds_in_year);
put_empty_line()

# task 7
'''
the final count of grains will be calculated
using formula 2 in the power 64 minus 1
'''
get_task_description(7, 'Python Math - Again')
totalGrainCount = 0
import math
for x in range(0, 63):
    totalGrainCount+=math.pow(2, x)
get_task_result(7, totalGrainCount)
put_empty_line()

# task 8
get_task_description(8, 'Converting Measurements')
inches=69
foot = 12
feet = inches/foot
get_task_result(8, feet)
put_empty_line()

# task 9
get_task_description(9, 'String Operators')
a = 'spam'
b = 'eggs'
breakfast = a + b
get_task_result(9, breakfast)
put_empty_line()

#task 10
get_task_description(10, 'String Operators Part Two')
spam = 'spam'
email = ''
for x in range(0, 57):
    email += spam
get_task_result(10, email)
put_empty_line()

# task 12
get_task_description(12, 'Datatypes - Boolean')
singpath_is_great = True
singpath_is_terrible = False
get_task_result(12, singpath_is_great)
get_task_result(12, singpath_is_terrible)
put_empty_line()

