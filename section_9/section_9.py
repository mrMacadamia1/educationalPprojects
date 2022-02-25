             #Тестирование
      #Assertions
# assert 2 + 2 == 4
# assert 2 + 2 == 5, '2+2 must eqals 4'

# def divide(a,b):
#     assert b != 0, 'b must not eqals 0'
#     return a/b
# print(divide(2,2))
# print(divide(2, 0))

# def multiply_positive_numbers(a,b):
#     assert a > 0 and b > 0
#     print(a *b)
# multiply_positive_numbers(3,5)
# multiply_positive_numbers(-4,6)

def get_access(password):
    password_list = [111, 2222, 333]
    assert int(password) in password_list
    print('you can make dangerous stuff')

password_1 = input('please input the password')
get_access(password_1)

        #unittest
