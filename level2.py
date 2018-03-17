# SingPath's level_2 task
# Implementer: Abilkhayir Akhet

'''
Вр 2 уровне решил не все подряд делать, а выборочно, так как выполнение определенных тасков
включает в себе выполнение более ранних тасков
'''

from commonmethods import get_task_description
from commonmethods import get_task_result
from commonmethods import put_empty_line

# task 5
get_task_description(5, 'Python Math')
a = 1
b = 2
c = a+b
get_task_result(5, c)
put_empty_line()