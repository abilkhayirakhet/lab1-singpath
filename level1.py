# SingPath's level_1 task
# Implementer: Abilkhayir Akhet

# Функция для того чтобы печатать переданную строку в bold
def write_bold(input_string):
    bold = "\033[1m"
    boldReset = "\033[0;0m"
    return bold + input_string + boldReset


# Метод который выводит в консоль описание задания
def get_task_description(index, label):
    print(str(index) + ' task\'s label: ' + label)


def get_task_result(index, result):
    print('Result of task' + str(index) + ': ' + write_bold(str(result)))


def put_empty_line():
    print("\n")


# task 1
get_task_description(1, 'Welcome task')
get_task_result(1, 'Here I don\'t have to type any code')
put_empty_line()

# task 2
get_task_description(2, 'Your First Program')
greeting = 'Hello World'
get_task_result(2, greeting)
put_empty_line()

# task 3
get_task_description(3, 'Starter Code')
bob = 'Thanks for the help'
get_task_result(3, bob)
put_empty_line()

# task 5
get_task_description(5, 'Still more variables')
name = 4.27
pigs = 'can fly'
get_task_result(5, str(name) + ' ' + str(pigs))
put_empty_line()

# task 6
get_task_description(6, 'Variables')
age = 7
get_task_result(6, age)
put_empty_line()

# task 7
get_task_description(7, 'Another Variable')
spam = 'anxious'
get_task_result(7, spam)
put_empty_line()

# task 8
get_task_description(8, 'More Fun with Variables')
alphabet = 'abcdefghijklmnopqrstuvwxyz'
pi       = 3.14159265
get_task_result(8, alphabet + ' ' + str(pi))
put_empty_line()

# task 9
get_task_description(9, 'Wizard')
wizard = 'Oz'
get_task_result(9, wizard)

