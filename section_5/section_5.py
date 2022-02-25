             #файловый ввод
             #чтение текста
# lorem_ipsum_text = open('C:/Users/user/Downloads/sample.txt')
# for line in lorem_ipsum_text:
#     print(line, end='')
# lorem_ipsum_text.close()

             #двоичная система
# with open('test_binare', 'bw') as test_file:
#     for number in range(21):
#         test_file.write(bytes([number]))
#
# with open('test_binare', 'br') as test_file:
#     for number in test_file:
#         print(number)


             #pickle
# import pickle

# honda = ('civic', 'grey', '2009', ((1, 'James Brown'),(2, 'Jane White'),(3, 'jake Green')))
#
# with open('honda.pickle', 'wb') as honda_file:
#     pickle.dump(honda, honda_file)

# with open('honda.pickle', 'rb') as honda_retrieved:
#     honda = pickle.load(honda_retrieved)
# print(honda)
# model, color, year, owner_list = honda
# print(model)
# print(color)
# print(year)
# for owner in owner_list:
#     owner_number, owner_name = owner
#     print(owner_number, owner_name)


              #shelve
# import shelve
# with shelve.open('shelve_test') as cars:
#     cars['opel'] = 'Germany'
#     cars['ford'] = 'USA'
#     cars['mazda'] = 'Japan'
#     cars['renault'] = 'France'
#     # print(cars['ford'])
#     # print(cars['renault'])
#     #
#     # cars['kia'] = 'South Korea'
#     #
#     # for key in cars:
#     #     print(key + ':' + cars[key])
#
#     # while True:
#     #     key = input('Plrase enter a car name')
#     #     if key == 'quit':
#     #         break
#     #     contry = cars.get(key, "We don't have a " + key)
#     #     print(contry)
#
#     # while True:
#     #     key = input('Plrase enter a car name')
#     #     if key == 'quit':
#     #         break
#     #     if key in cars:
#     #         country = cars[key]
#     #         print(contry)
#     #     else:
#     #         print("We don't have a " + key)
#     # ordered_keys_list = list(cars.keys())
#     # ordered_keys_list.sort()
#     # for key in ordered_keys_list:
#     #     print(key + ' ' + cars[key])
#     # for key in cars:
#     #     print(key + ' ' + cars[key])
#     for value in cars.values():
#         print(value)
#     print(cars.values)
#     for key in cars.keys():
#         print(key)
#     print(cars.keys)
#     for item in cars.items():
#         print(item)
#     print(cars.items)
import shelve

# monday_schedule = ['Math', 'English language', 'System programming', 'Python']
# tuesday_schedule = ['English language', 'HTML', 'Python', 'Football']
# wednesday_schedule = ['Physics', 'English language', 'Python']
# thursday_schedule = ['Math', 'Chemistry', 'Java']
# friday_schedule = ['Running', 'Math',  'Python']

# with shelve.open ('schedules', writeback=True) as schedules:     #'writeback=' - удобно,но использовать для небольших обновлений, иначе большая нагрузка на процессор
# #     schedules['monday_schedules'] = monday_schedule
# #     schedules['tuesday_schedule'] = tuesday_schedule
# #     schedules['wednesday_schedule'] = wednesday_schedule
# #     schedules['thursday_schedule'] = thursday_schedule
# #     schedules['friday_schedule'] = friday_schedule
#
# #     schedules['thursday_schedule'].append('Swimming')
#
#     # temp_list = schedules['thursday_schedule']
#     # temp_list.append('Swimming')
#     # schedules['thursday_schedule'] = temp_list
#
#     schedules['thursday_schedule'].append('Python')
#     for key in schedules:
#         print(key, schedules[key])
#
