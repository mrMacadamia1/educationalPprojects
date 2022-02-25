           #интеграторы и генераторы
# number_list = [1,2,3,4,5]
# for number in number_list:
#     print(number)

# def my_for_loop(iterable):
#     iterator = iter(iterable)
#     # print(iterator.__next__())
#     # print(iterator.__next__())
#     # print(next(iterator))
#     while True:
#         try:
#             print(iterator.__next__())
#         except StopIteration:
#             print('iteration is finished')
#             break
# my_for_loop('hello')
       #custom iterable
# for number in range(1, 10):
#     print(number)

# class MyRange:
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end
#         self.current = start
#
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.current < self.end:
#             number = self.current
#             self.current += 1
#             return number
#         raise StopIteration
#
# first_range = MyRange(5,20)
# for number in first_range:
#     print(number)

        #Generator functions
# def my_function(x):
#     return x
# print(my_function(4))

# def count_up_to(x):
#     count = 1
#     while count <= x:
#         yield count
#         count += 1
# # print(count_up_to(4))
# # c = count_up_to(4)
# # print(c.__next__())
# # print(c.__next__())
#
# for number in count_up_to(10):
#     print(number)

# def get_week():
#     week = ["Sunday", "Monday","Tuesday", "Wednesday","Thursday","Friday", "Saturday"]
#     for day in week:
#         yield day
# current_day = get_week()
# print(current_day.__next__())
# print(current_day.__next__())
# print(current_day.__next__())
# print(current_day.__next__())
# print(current_day.__next__())
# print(current_day.__next__())
# print(current_day.__next__())


# def even_odd():
#     count = 1
#     even=  'even'
#     odd= 'odd'
#     while count >=1:
#         if count%2==1:
#             yield even
#         else:
#             yield odd
#         count +=1
#
#
# even_odd_generator = even_odd()
# print(next(even_odd_generator))
# print(next(even_odd_generator))
# print(next(even_odd_generator))
# print(next(even_odd_generator))

    #Infinitr process
# def created_patterns():
#     max_patterns_number = 100
#     patterns = ('first', 'second', 'third', 'forth')
#     i = 0
#     result_list = []
#     while len(result_list)< max_patterns_number:
#         if i >= len(patterns):
#             i = 0
#         result_list.append(patterns[i])
#         i +=1
#     return result_list
#
# print(created_patterns())

# def get_current_pattern():
#     patterns = ('first', 'second', 'third', 'forth')
#     i = 0
#     while True:
#         if i>= len(patterns):
#             i=0
#         yield  patterns[i]
#         i+=1
# current_pattern = get_current_pattern()
# print(next(current_pattern))
# print(next(current_pattern))
# print(next(current_pattern))
# print(next(current_pattern))

# def get_infinite_square_generator():
#     i = 1
#
#     while True:
#
#         yield i*i
#         i+=1
# infinite_square_generator = get_infinite_square_generator()
# print(next(infinite_square_generator))
# print(next(infinite_square_generator))
# print(next(infinite_square_generator))
# print(next(infinite_square_generator))

        #Generator expressions
# def from_range():
#     for number in range(10):
#         yield number
# counter = from_range()
# print(next(counter))

counter1 = (number for number in range(10))
print([number for number in range(10)])
print(next(counter1))
print(next(counter1))