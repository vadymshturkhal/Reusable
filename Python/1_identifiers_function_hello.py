# Создайте функцию, которая печатает приветствие и имеет один аргумент: name.


def function_for_print_hello(name: str):  # Used Type hint
    print('Hello', name)


if __name__ == '__main__':
    function_for_print_hello('Mark')
