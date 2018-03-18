# SingPath's level_7 task
# Implementer: Abilkhayir Akhet

'''
В 7 уровне решил не все подряд делать, а выборочно, так как выполнение определенных тасков
включает в себе выполнение более ранних тасков
'''

from commonmethods import get_task_description
from commonmethods import get_task_result
from commonmethods import put_empty_line
from commonmethods import get_level_number

get_level_number(7)
put_empty_line()

#task1
get_task_description(1, 'Lists')
def create_list():
    list = [0, 1, [2, 4], 4]
    return list
get_task_result(1, create_list())
put_empty_line()

#task2
get_task_description(2, 'List Head')
def get_head_of_list(list):
    return list[0]
get_task_result(2, get_head_of_list([1, 6, 23]))
put_empty_line()

#task3
get_task_description(3, 'List Head & Tail')
def head_and_tail(list):
	return [list[0],list[len(list)-1]]
get_task_result(3, head_and_tail(['home', 2, 345, [2, 4]]))
put_empty_line()

#task4
get_task_description(4, 'List Contains')
def list_contains(l):
	return list(set(l))
get_task_result(4, list_contains([1,2, 33, 3,3,44]))
put_empty_line()

#task 5
get_task_description(5, 'Parse String')
def parse_string(s):
	return s.split()
get_task_result(5, parse_string('The London is a capital of Great Britain'))
put_empty_line()

#task 6
get_task_description(6, 'Sorting a list')
def sort_list(list):
	return sorted(list) == list
get_task_result(6, sort_list([1,2,3,4,5,6]))
get_task_result(6, sort_list(['b', 'c', 'a']))
put_empty_line()

#task 7
get_task_description(7, 'Centered Average')
def centered_average(l):
	max = l[0]
	min = l[0]
	sum = 0
	for item in l:
		if item > max:
			max = item
		if item < min:
			min = item
		sum += item

	return (sum - max - min) / (len(l) - 2)
get_task_result(7, centered_average([1, 22, 37, 44, 120]))

#task 8
get_task_description(8, 'Frequency')
def get_frequency(l,n):
	count = 0
	for item in l:
		if item == n:
			count+=1
	return count
get_task_result(8, get_frequency([3, 1, 11, 5, 2, 3, 4], 1))

#task9
get_task_description(9, 'Deep Sort')
def deepsort(lists):
	res = []
	for list in lists:
		res+=set(list)
	return sorted(set(res),key = lambda item: len(str(item)))
get_task_result(9, deepsort([['aa','cc','ab'],[22,4,2]]))
put_empty_line()
