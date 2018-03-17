# SingPath's level_4 task
# Implementer: Abilkhayir Akhet

'''
В 4 уровне решил не все подряд делать, а выборочно, так как выполнение определенных тасков
включает в себе выполнение более ранних тасков
'''

from commonmethods import get_task_description
from commonmethods import get_task_result
from commonmethods import put_empty_line
from commonmethods import get_level_number

get_level_number(4)
put_empty_line()

# task 1
get_task_description(1, 'Find the quotient')

def quotient(a, b):
    return int(a/b)


get_task_result(1, quotient(9, 3))
put_empty_line()

#task 2
get_task_description(2, 'Find the remainder')

def get_remainder(a, b):
    return int(a%b)

get_task_result(2, get_remainder(5,2))
put_empty_line()

#task 3
get_task_description(3, 'Check for equality')

def isEqual(a, b):
    return a == b

get_task_result(3, isEqual(2, 3))
get_task_result(3, isEqual(3, 3))
put_empty_line()

#task 4
get_task_description(4, 'Sign')

def getSign(numb):
    if numb < 0:
        return -1
    elif numb > 0:
        return 1
    else:
        return 0


get_task_result(4, getSign(-23))
get_task_result(4, getSign(0))
get_task_result(4, getSign(45))
put_empty_line()

#task 5
get_task_description(5, 'Six is great')

def isSixGreat(num1, num2):
    if num1 == 6 or num2 == 6 or num1 + num2 == 6 or num2-num1 == 6 or num1-num2 == 6:
        get_task_result(5, True)
    else:
        get_task_result(5, False)


isSixGreat(1,7)
put_empty_line()

#task 6
get_task_description(6, 'Triangle Test')

def isTriangle(a, b, c):
    if a+b > c and b+c > a and a+c > b:
        return True
    else:
        return False


get_task_result(6, isTriangle(1,2,124))
get_task_result(6, isTriangle(3,4,5))
put_empty_line()