# SingPath's level_6 task
# Implementer: Abilkhayir Akhet

'''
В 6 уровне решил не все подряд делать, а выборочно, так как выполнение определенных тасков
включает в себе выполнение более ранних тасков
'''

from commonmethods import get_task_description
from commonmethods import get_task_result
from commonmethods import put_empty_line
from commonmethods import get_level_number

get_level_number(6)
put_empty_line()

#task1
get_task_description(1, 'Strings')
def get_nth_char_in_string(string, index):
    return string[index]

get_task_result(1, get_nth_char_in_string('success', 4))
put_empty_line()

#task2
get_task_description(2, 'Hello')
def get_greeting(name):
    return 'Hello ' + name + '!'
get_task_result(2, get_greeting('Abilkhayir'))
put_empty_line()

#task3
get_task_description(3, 'String Slice')
def get_string_middle(string):
    string_length = len(string)
    return string[1:string_length-1]
get_task_result(3, get_string_middle('opportunity'))
put_empty_line()

#task4
get_task_description(4, 'String Search')
def search_char_in_string(string, char):
    return string.find(char)

get_task_result(4, search_char_in_string('great', 'a'))
put_empty_line()


#task5
get_task_description(5, 'Search Upgrade')
def search_string_in_string(str1, str2):
    return str1.find(str2)
get_task_result(5, search_string_in_string('This is a great example of success', 'exam'))

#task6
get_task_description(6, 'Upper Case')
def to_upper(string):
    return string.upper()
get_task_result(6, to_upper('school'))
put_empty_line()

#task7
get_task_description(7, 'Strip Last 3')
def takof_part_of_string(string):
    return string[:-3]
get_task_result(7, takof_part_of_string('Learning'))
put_empty_line()

#task8
get_task_description(8, 'Change Case')
def swap_up_and_low_cases(string):
    return string.swapcase()
get_task_result(8, swap_up_and_low_cases('doNotLikeThatInPythonCamelCaseIsNotWelcome'))
put_empty_line()

#task9
get_task_description(9, 'String Reversal')
def reverse_string(string):
    return string[::-1]
get_task_result(9, reverse_string('Python'))
put_empty_line()


#task10
get_task_description(10, 'Comparing Strings')
def in_both(s1,s2):
	return ''.join(sorted(set(s1.lower()).intersection(set(s2.lower()))))

get_task_result(10, in_both("apple","pie"))
put_empty_line()


#task 11
get_task_description(11, 'Concatenate strings')
def concatenate(list, delimeter=' '):
    return delimeter.join(list)
get_task_result(11, concatenate('good'))
put_empty_line()

#task 12
get_task_description(12, 'Find xyz')
def is_there_xyz(s):
	i = s.find("xyz")
	if i == 0:
		return True
	if i > 0 and s[i-1] != '.':
		return True
	if i > 0 and s[i-1] == '.' and i+3 <len(s) and s[i+3] == '.':
		return True
	return False

get_task_result(12, is_there_xyz('.xyz.xyz2xyz'))

#task 13
get_task_description(13, 'Half String')
def half(s,is_front = True):
	if is_front:
		return s[0:int(len(s)/2)]
	return s[int(len(s)/2):len(s)]
get_task_result(13, half('jira', False))
get_task_result(13, half('jira', True))
put_empty_line()

#task14
get_task_description(14, 'Email Checker')
def has_space(string):
    return ' ' in string

def has_email_sign(string):
    return '@' in string

def is_email(string):
    if not has_space(string) and has_email_sign(string):
        return True
    return False
get_task_result(14, is_email('email@cheaker'))
put_empty_line()





