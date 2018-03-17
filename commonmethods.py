# Функция для того чтобы печатать переданную строку в bold
import random

def write_bold(input_string):
    bold = "\033[1m"
    boldReset = "\033[0;0m"
    return bold + input_string + boldReset


# Метод который выводит в консоль описание задания
def get_task_description(index, label):
    print(str(index) + ' task\'s label: ' + label)


def get_task_result(index, result):
    print('Result of task' + str(index) + ': ' + write_bold(str(result)))

def get_level_number(int):
    print('Tasks from level: ' + write_bold(str(int)))


def put_empty_line():
    #print('--------------------------------------------------')
    print('--------------------------------------------------')
    print("\n")


def get_rand_word():
    words = [
        'people',
        'history',
        'way',
        'art',
        'world',
        'information',
        'map',
        'two',
        'family',
        'government',
        'health',
        'system',
        'computer',
        'meat',
        'year',
        'thanks',
        'music',
        'person',
        'reading',
        'method',
        'data',
        'food',
        'understanding',
        'theory',
        'law',
        'bird',
        'literature',
        'problem',
        'software',
        'control',
        'knowledge',
        'power',
        'ability',
    ]

    word = random.choice(words)

    return word