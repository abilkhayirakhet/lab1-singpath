# SingPath's level_8 task
# Implementer: Abilkhayir Akhet

'''
В 8 уровне решил не все подряд делать, а выборочно, так как выполнение определенных тасков
включает в себе выполнение более ранних тасков
'''

from commonmethods import get_task_description
from commonmethods import get_task_result
from commonmethods import put_empty_line
from commonmethods import get_level_number

get_level_number(8)
put_empty_line()

#task1
get_task_description(1, 'Dictionaries')
dictionary = {"color":"blue",7:"seven",3.14:[3,1,4,6]}
get_task_result(1, dictionary);
put_empty_line()

#task2
get_task_description(2, 'List the keys of a dictionary')
def sort_dictioary_keys(dict):
	return sorted(list(dict.keys()))
get_task_result(2, sort_dictioary_keys({'a':1, 'c':2, 'b':3}))
put_empty_line()

#task3
get_task_description(3, 'Reverse Lookup')
def lookup(dict,val):
    res = []
    for key,value in dict.items():
        if value == val:
            res.append(key)
    return res
get_task_result(3, lookup({'hi':3,8:'32',(5,3):'bye',(4,3,2):[4,3],'':4,73:8,839:234,34:857,'whatsapp':4}, 3))
put_empty_line()

#task4
get_task_description(4, 'Switch Keys and Values')
def switch_dict(d):
	new_dic = {}
	for key,value in d.items():
		new_dic[value] = key
	return new_dic
get_task_result(4, switch_dict({'z':22, 'y':34, 't':97}))
put_empty_line()