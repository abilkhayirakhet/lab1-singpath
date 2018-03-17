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