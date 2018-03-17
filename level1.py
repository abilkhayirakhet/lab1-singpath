# SingPath's level_1 task
# Implementer: Abilkhayir Akhet

# Функция для того чтобы печатать переданную строку в bold
def write_bold(input_string):
    bold = "\033[1m"
    boldReset = "\033[0;0m"
    return bold + input_string + boldReset

# task 1
print('1 task\'s label: "Welcome task"')
print("Result of task 1: Here I don't have to type any code")
print("\n")

# task 2
print('2 task\'s label: "Your First Program"')
greeting = 'Hello World'
print("Result of task 2: "+ write_bold(greeting))
print("\n")

# task 3
print('3 task\'s label: "Starter Code"')
bob = 'Thanks for the help'
print("Result of task 3: "+ write_bold(bob))
print("\n")

# task 5
print('5 task\'s label: "Still more variables"')
name = 4.27
pigs = 'can fly'
print("Result of task 5: "+write_bold(str(name) + ' ' + str(pigs)))
print("\n")

# task 6
print('6 task\'s label: "Variables"')
age = 7
print("Result of task 6: "+write_bold(str(age)))
print("\n")

# task 7
print('7 task\'s label: "Another Variable"')
spam = 'anxious'
print("Result of task 7: "+write_bold(spam))
print("\n")

# task 8
print('8 task\'s label: "More Fun with Variables"')
alphabet = 'abcdefghijklmnopqrstuvwxyz'
pi       = 3.14159265
print("Result of task 8: ")
print(write_bold(alphabet))
print(write_bold(str(pi)))
print("\n")

# task 9
print('9 task\'s label: "Wizard"')
wizard = 'Oz'
print("Result of task 9: " + write_bold(wizard))

