                #декораторы
        #Higher order function
# def product(n, func):
#     result = 1
#     for number in range(1, n):
#         result *= func(number)
#     return result
#
# def square(x):
#     return x * x
#
# def cube(x):
#     return  x * x * x
#
# print(product(4, square))
# print(product(4, cube))

# def my_function(a, b, func):
#     result = func([a,b])
#     return result
# print(my_function(7, 3, sum))

# from random import choice
# def colorize(thing):
#     def get_color():
#         colors = ('red', 'green', 'yellow')
#         color = choice(colors)
#         return color
#     result = get_color() + ' ' + thing
#     return result
#
# print(colorize('apple'))

# from random import choice
# def make_color():
#     def get_color():
#         colors = ('red', 'green', 'yellow')
#         color = choice(colors)
#         return color
#     return get_color
#
# first_color = make_color()
# print(first_color())

# from random import choice
# def colorize_1(thing):
#     def get_color():
#         colors = ('red', 'green', 'yellow')
#         color = choice(colors)
#         return color + ' ' + thing
#
#     return get_color
#
# # print(colorize_1('apple')())
# colorize_dog = colorize_1('dog')
# print(colorize_dog())
     #@
# def simpl_function():
#     #print('some code before the old cod')
#     print('Simple function cod')
#     #print('some code after the old cod')
#
# simpl_function()

# def decorator_function(original_function):
#     def wrap_function():
#         print('some code before the old cod')
#         original_function()
#         print('some code after the old cod')
#     return wrap_function
#
# # decorated_function = decorator_function(simpl_function)
# # decorated_function()
#
# @decorator_function
# def simpl_function():
#     print('Simple function cod')
# simpl_function()
# def make_compliment(func):
#     def wrapper(*args, **kwargs):
#         print('Nice to meet you!')
#         func(*args, **kwargs)
#         print('you look great!')
#     return wrapper
#
# @make_compliment
# def ask_name():
#     print('what is your name?')
#
# ask_name()
#
# @make_compliment
# def say_name(name):
#     print('My name is ' + name)
#
# say_name('Jack')
# @make_compliment
# def order(food, drink):
#     print(f'Give me {food} and {drink}')
# order('chips', 'kola')

        #@wraps
# from functools import wraps
#
# def print_function(function):
#     '''
#     This is decorator function
#     :param function:
#     :return:
#     '''
#     @wraps(function)
#     def wrapper(*args, **kwargs):
#         print(f'You are using {function.__name__}')
#         print(f'Function documentation {function.__doc__}')
#         return function(*args, **kwargs)
#     return wrapper
# @print_function
# def squares_sum(a,b):
#     '''
#
#     :param a: first number
#     :param b: second number
#     :return: sum of squares
#     '''
#     return a * a + b * b
#
# print(squares_sum(2, 3))
# print(squares_sum.__doc__)
# print(squares_sum.__name__)

# from functools import wraps
# def print_args(f):
#     @wraps(f)
#     def wrapper(*args, **kwargs):
#         print('args:', args)
#         print('kwargs:', kwargs)
#         return f(*args, **kwargs)
#     return wrapper
#
# @print_args
# def func():
#
#     print('Code')
#
# func()


        #тестирование скорости
# from time import time
# from functools import wraps
# start_time = time.time()
# sum([num for num in range(1000000)])
# end_time = time.time() - start_time
#
# start_time = time.time()
# sum(num for num in range(1000000))
# end_time = time.time() - start_time

# def speed_test(func):
#     @wraps(func)
#     def wrapper(*args,**kwargs):
#         start_time = time()
#         result = func(*args,**kwargs)
#         end_time = time()
#         print(f'Time of cod execution {end_time - start_time}')
#         return result
#     return wrapper
#
# @speed_test
# def sum_with_list():
#     return  sum([num for num in range(10000000)])
# @speed_test
# def sum_with_gen():
#     return  sum(num for num in range(10000000))
#
# @speed_test
# def product(reang_v):
#     result = 1
#     for num in range(1, reang_v):
#         result *= num
#     return  result
#
# print(sum_with_list())
# print(sum_with_gen())
# print(product(1000))

# from functools import wraps
# def hello_from_decorator(func):
#     @wraps(func)
#     def wrapper(*args,**kwargs):
#         result = func(*args, **kwargs)
#         return str(result) + ' Hello from decorator!'
#     return wrapper
# @hello_from_decorator
# def slovo():
#     return 'hello'
#
# print(slovo())

    #Проверка вргументов
# from functools import wraps
# def prohibit_kwards(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         if kwargs:
#             raise ValueError('Keyword arguments are prohibited')
#         return func(*args,**kwargs)
#     return wrapper

# def prohibit_int_arguments(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         for val in args:
#             if type(val) == int:
#             raise ValueError('Integer arguments are prohibited')
#         for key, val in kwargs.items():
#             if type(val) == int:
#                 raise ValueError('Integer arguments are prohibited')
#
#         return func(*args,**kwargs)
#     return wrapper
# @prohibit_int_arguments
# def print_hello(name):
#     print(f'Hello {name}')
#
# print_hello('Jack')

# from functools import wraps
# def prohibit_more_than_2_args(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         if len(args) < 3:
#             return func(*args,**kwargs)
#         else:
#             raise ValueError('Function must have less than 3 arguments!')
#
#     return wrapper
#
# @prohibit_more_than_2_args
# def arg_val(a, b, c):
#     return a + b + c
#
# print(arg_val(1, 2))

        #Декораторы с аргументами
# from functools import wraps
# def check_if_first_arg_is(value):
#     def inner_dec(func):
#         @wraps(func)
#         def wrapper(*args,**kwargs):
#             if args and args[0] != value:
#                 print(f'First argument has to be {value}')
#             return func(*args, **kwargs)
#         return wrapper
#     return inner_dec
# @check_if_first_arg_is('red')
# def print_rainbow_colors(*colors):
#     print(colors)
# @check_if_first_arg_is(7)
# def multiply_7(a, b):
#     return a * b
#
#
# print_rainbow_colors('red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet')
# print(multiply_7(9,3))


# from functools import wraps
# def enforce(*types):
#     def inner_dec(func):
#         @wraps(func)
#         def wrapper(*args,**kwargs):
#             new_args = []
#             for a, t in zip(args, types):
#                 new_args.append(t(a))
#             return func(*new_args,**kwargs)
#         return wrapper
#     return inner_dec
# @enforce(str, int)
# def print_text(text,n):
#     for number in range(n):
#         print(text)
#
# print_text('hi', "3")
#
# from functools import wraps
# from time import sleep
# def wait(n):
#     def ogo(func):
#         @wraps(func)
#         def wrapper(*args,**kwargs):
#             sleep(n)
#             print(f'There was a pause {n} seconds before execution {sum_num}')
#             return func(*args,**kwargs)
#         return wrapper
#     return ogo
#
# @wait(3)
# def sum_num(a,b):
#     return a ** b
#
# print(sum_num(4,9))