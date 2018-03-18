# SingPath's level_5 task
# Implementer: Abilkhayir Akhet

'''
В 5 уровне решил не все подряд делать, а выборочно, так как выполнение определенных тасков
включает в себе выполнение более ранних тасков
'''

from commonmethods import get_task_description
from commonmethods import get_task_result
from commonmethods import put_empty_line
from commonmethods import get_level_number

get_level_number(5)
put_empty_line()

import random
import math

# task 1
get_task_description(1, 'While Loop')
def get_sum_using_while_loop(number):
    count = 0
    sum = 0
    while (count < number):
        count += 1
        sum += count

    return sum


get_task_result(1, get_sum_using_while_loop(15))
put_empty_line()

#task 2
get_task_description(2, 'Sum range')
def get_sum_range(numb1, numb2):
    sum = 0
    while numb1 <= numb2:
        sum += numb1
        numb1 += 1
    return sum


get_task_result(2, get_sum_range(2, 5))
put_empty_line()

#task 3
get_task_description(3, 'Sum range by Step')
def get_range_sum_by_step(a, b, step):
    sum = 0
    while a <= b:
        sum += a
        a += step
    return sum
get_task_result(3, get_range_sum_by_step(3, 10, 2))
put_empty_line()

#task 4
get_task_description(4, 'For Loops')
def get_sum_of_squares(number):
    sum = 0
    for x in range(number + 1):
        sum += x*x
    return sum
rand_number = random.randint(1, 9)
print('selected number is ' + str(rand_number))
get_task_result(4, get_sum_of_squares(rand_number))
put_empty_line()

#task 5
get_task_description(5, 'Square Roots')
def sum_of_sqr_roots(number):
    sum = 0
    for x in range(1, number+1):
        sum += math.sqrt(x)

    return sum

rand_number = random.randint(1, 9)
print('selected number is ' + str(rand_number))
get_task_result(5, sum_of_sqr_roots(rand_number))
put_empty_line()

#task 6
get_task_description(6, 'Cubes')
def get_sum_of_cubes_in_range(a, b):
    sum = 0
    for i in range(a, b + 1):
        sum += math.pow(i, 3)
    return sum
get_task_result(6, get_sum_of_cubes_in_range(2, 7))
put_empty_line()


#task 7
get_task_description(7, 'Sum Powers Over Range')
def get_sum_of_power_in_range(a, b, power):
    sum = 0
    for i in range(a, b + 1):
        sum += math.pow(i, power)
    return sum
get_task_result(7, get_sum_of_power_in_range(2, 15, 5))
put_empty_line()

#task 8
get_task_description(8, 'Product of range')
def get_product_of_range(a, b, step):
    sum = 1
    for i in range(a, b + 1, step):
        sum *= i
    return sum

get_task_result(8, get_product_of_range(2, 6, 2))
put_empty_line()

#task 9
get_task_description(9, 'Iteration - Sum of the squares of a list of numbers')
def get_squared_sum_in_list(list):
    sum = 0
    for x in list:
        sum += x*x
    return sum
get_task_result(9, get_squared_sum_in_list([1,2,3, 4, 5, 6, 7, 8, 4.5]))
put_empty_line()

#task 10
get_task_description(10, 'Count Evens')
def get_count_of_evens(list):
    count = 0
    for x in list:
        if x%2 == 0:
            count += 1
    return count
list = [1, 2, 33, 54, 25, 676, 57, 18, 9, 11]
get_task_result(10, get_count_of_evens(list))
put_empty_line()

#task11
get_task_description(11, 'Duplicate the elements in a list')
def duplicate_list_elements(list):
    new_list = []
    for x in list:
        new_list.append(x)
        new_list.append(x)
    return new_list

get_task_result(11, duplicate_list_elements([1,2]))
put_empty_line()

#task12
get_task_description(12, 'Symmetric Number Judge')
def symmetric_number_judge(n):
    return str(n) == str(n)[::-1]

get_task_result(12, symmetric_number_judge(345))
put_empty_line()



