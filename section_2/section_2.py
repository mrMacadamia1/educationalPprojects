          #создание функции
# def print_greeting():
#     '''
#     Print 'Hello!' text
#     :return: None
#     '''
#     print('Hello!')
# print_greeting()
# help(print_greeting)

# def print_greeting_whith_name(name = 'name'):
#     '''
#         :param name:
#     :return:
#     '''
#     print('Hello ' + name + '!')
# print_greeting_whith_name('Andrey')
# print_greeting_whith_name()

# def sum_of_two_numbers(a = 0, b = 0):
#     return a + b
# x = sum_of_two_numbers(578, 98.5)
# print(x)

# def is_hello(text):
#     if 'hello' in text.lower():
#         return True
#     else:
#         return False
# print(is_hello('HELLO loos'))


# def is_string(string, text):
#     return string in text
# print(is_string('a', 'The apple')) #содержит букву 'а' в тексте

# def greeting_depends_on_gender(name, gender):
#     if gender == 'male':
#         print('Hello ' + name + '! You look great!')
#         return gender
#     elif gender == 'female':
#         print('Hello ' + name + '! You are so nise!')
#         return gender
#     else:
#         print('Hello ' + name + '! I\'ve never seem the creature like you!')
#         return gender
# returned_value = greeting_depends_on_gender('Jack', 'male')
# returned_value = greeting_depends_on_gender('Jane', 'female')
# returned_value = greeting_depends_on_gender('Ja', 'cmale')

# def cat_voice():
#     return 'Meow!'
#
#
# def dog_voice():
#     return 'Woof!'
# print(cat_voice())
# print(cat_voice())
# print(dog_voice())
# print(dog_voice())
#
# def get_voice(voice):
#     return str(voice) + '!'
# print(get_voice('jo'))

#           # With List Comprehension
# def get_odd_number_list(a, b): #функция
#     number_list = list(range(a, b + 1))
#     odd_number_list = [number for number in number_list if number % 2 != 0]
#     return odd_number_list
# x = get_odd_number_list(1, 76)
# print(x)
#
#
#            # Without List Comprehension
# def get_odd_number_list(a, b):
#     number_list = list(range(a, b + 1))
#     odd_number_list = []
#     for number in number_list:
#         if number % 2 > 0:
#             odd_number_list.append(number)
#     return odd_number_list
# print(get_odd_number_list(1, 76))

            # *args abd **kwards
# def ten_percent_of_product(x, y):
#     return (x * y) * 0.1
# print(ten_percent_of_product(10,20))

# def ten_percent_of_product(*args):
#     product = 1
#     for number in args:
#         product = product * number
#     return product * 0.1
# print(ten_percent_of_product(10,20, 4, 7, 2))

# def percent_of_product(percent, *args):
#     product = 1
#     for number in args:
#         product = product * number
#     return product / 100 * percent
# print(percent_of_product(90, 10, 20, 4, 7, 2))

# def func_with_kwargs(**kwargs):
#     if 'name' in kwargs:
#         print('Hello! Nice to meet you, {}'.format(kwargs['name']))
#     else:
#         print('Hello! What is your name?')
# func_with_kwargs(gender='male', age=24, name='Jack')
# func_with_kwargs(gender='male', age=24)

# def func_with_kwargs(greeting, **kwargs):
#               if 'name' in kwargs:
#                   print('{}! Nice to meet you, {}'.format(greeting, kwargs['name']))
#               else:
#                   print('{}! What is your name?'.format(greeting))
# func_with_kwargs('Hi', gender='male', age=24, name='Jack')

# def args_and_kwargs(*args, **kwargs):
#     print('I would like {} {}'.format(args[0], kwargs['food']))
# args_and_kwargs('one', 2, drink='coffee', food = 'bulochka')

# def is_cat_here(*args):
#     if 'cat' in args:
#         return True
#     else:
#         return False
# print(is_cat_here('cat', 'CAT', 'dog', 'men' ))
#
# def is_item_here(item, *args):
#     if item in args:
#         return True
#     else:
#         return False
# print(is_item_here(4, 323, 657, 7586, 435657, 4))

# def your_favorite_color(my_color, **kwargs):
#     if 'color' in kwargs:
#         print('My favorite color is {}, but {} is also pretty good!'.format(my_color, kwargs['color']))
#     else:
#         print('My favorite color is' + my_color + ', what is your favorite color?')
# your_favorite_color('indigo', color='black', car='bmw')

# def is_cat_here(*args):
#     args_in_lower_case = [str(argument).lower() for argument in list(args)]
#     if 'cat' in args_in_lower_case:
#         return True
#     else:
#         return False
# print(is_cat_here( 'CAT', 'dog', 'men' ))

       #лямбда выражения
# def sum_of_two_numbers(x):
#     return x + x
#
# number_list = [1, 2, 3, 4, 5, 6, 7]
# result = map(sum_of_two_numbers, number_list)
# print(result)
# for item in result:
#     print(item)
#
# for item in map(sum_of_two_numbers, number_list):
#     print(item)
#
# print(list(map(sum_of_two_numbers, number_list)))

# def is_a_in_string(string):
#     if 'a' in string:
#         print('yes')
#     else:
#         print('no')
# string_list = ['hi', 'was', 'name', 'he']
# print(list(map(is_a_in_string, string_list)))

# def is_number_odd(number):
#     return number % 2 == 1
# number_list = [1, 2, 3, 4, 5, 6, 7]
# print(list(filter(is_number_odd,number_list)))
# for number in filter(is_number_odd,number_list):
#     print(number)


# number_list = [1, 2, 3, 4, 5, 6, 7]
# print(list(map(lambda number: number ** 3,number_list)))
# string_list = ['hi', 'was', 'name', 'he']
# print(list(map(lambda string: string[-1], string_list)))

           #область видимости переменных









# def average(x, y):
#     m = (x + y) / 2
#     return m
# a = int(input('a = '))
# b = int(input('b = '))
# av = average(a, b)
# print(round(av, 2))

# from random import randint
# s_num = randint(1, 10)
# us_num = -1
# try_num = 1
# while s_num != us_num:
#     print('%d try: '% try_num, end='')
#     us_num = int(input())
#     if us_num < s_num:
#         print('too less')
#     elif us_num > s_num:
#         print('Too mach')
#     else:
#         print('you guessed it!')
#     try_num += 1

# import  datetime
# print(datetime.date.today())
import  random
print(dir(random))
help(random.randint)


