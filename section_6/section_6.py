            #типы ошибок
#try except
# print('some code')
# try:
#     print(number)
# except:
#     print('error')
# print('code after error')

# user_dictionary = {'first_name': 'Jack', 'last_name': 'White', 'age': 24}
# # print(user_dictionary['last_name'])
# #
# # print(user_dictionary.get('last_name'))
#
# def get_dictionary_values(dictionary, key):
#     try:
#
#         return dictionary[key]
#     except KeyError:
#         return None
# print(get_dictionary_values(user_dictionary, 'age'))
# print(get_dictionary_values(user_dictionary, 'a'))
# print(get_dictionary_values(user_dictionary, 'first_name'))

# while True:
#     try:
#         number = int(input('enter som number'))
#         print(number / 2)
#     except:
#         print('error')
#     else:
#         print('elso block')
#         break
#     finally:
#         print('finally block')
# print('code after error handling')

def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError as e:
        print("you can't divide by zero")
        print(e)
    except TypeError as e:
        print('x and y be numbers')
        print(e)
    else:
        print('x hase divided by y')
    finally:
        print('finally block')
print(divide(4,'k'))