               #Object orented programming
# class MyFirstClass:
#     pass
#
# o = MyFirstClass()
# print(type(o))
              #Атрибуты
# class Car:
#     def __init__(self, name):
#         self.name = name
#
# mazda_car = Car(name= 'mazda cx7')
# print(mazda_car.name)

# class BlogPost:
#     def __init__(self, user_name, text, number_of_likes):
#         self.user_name = user_name
#         self.text = text
#         self.number_of_likes = number_of_likes
#
# blog_1 = BlogPost(user_name='MAni', text='Hello people!', number_of_likes=9)
#
# blog_2 = BlogPost(user_name='Dari', text='Goodbye world', number_of_likes= 1)
#
# blog_2.number_of_likes = 10
#
# print(blog_1.number_of_likes)
# print(blog_2.number_of_likes)

           #Методы
# class Car:
#     def __init__(self, name, color, year, is_crashed):
#         self.name = name
#         self.color = color
#         self.year = year
#         self.is_crashed = is_crashed
#
#     def drive(self, city):
#         print(self.name + 'is driving to ' + city)
#
#     def chang(self, new_color):
#         self.color = new_color
#
# opel = Car('Opel Tigra', 'grey', '1999', True)
# opel.drive('London')
# opel.chang('black')
# print(opel.color)

# class Circle:
#     pi = 3.14
#     def __init__(self, radius = 1):
#         self.radius = radius
#         ## self.circumference = 2 * self.pi *self.radius
#     def get_area(self):
#         return self.pi * (self.radius **2)
#     def get_circumference(self):
#         return  2 * self.pi *self.radius
# circle_1 = Circle()
# print(circle_1.get_area())
# print(circle_1.get_circumference())
# # print(circle_1.circumference)
# circle_2 = Circle(5)
# print(circle_2.get_area())
# print(circle_2.get_circumference())
#
# class  BankAccount:
#     def __init__(self,  client_id, client_first_name, client_last_name, balance= 0.0):
#         self.client_id = client_id
#         self.client_first_name = client_first_name
#         self.client_last_name = client_last_name
#         self.balance = balance
#
#     def add(self, amount):
#         self.balance += amount
#
#     def withdraw(self, amount):
#         self.balance -= amount
# account_1 = BankAccount(1256, 'Andy', 'Smith', 300)
# account_2 = BankAccount(93532, 'Jon', 'Black', 50)
#
# account_1.add(12345)
# print(account_1.balance)
# account_2.withdraw(300)
# print(account_2.balance)

             #Метод класса
# class Gamer:
#     active_gamers = 0
#
#     @classmethod
#     def get_active_gemers(cls):
#         return Gamer.active_gamers
#
#     @classmethod
#     def gamer_from_string(cls,data_string):
#         nickname, age, level, points = data_string.split(',')
#         return cls(nickname, age, level, points)
#
#
#     def __init__(self, nickname, age, level, points):
#         self.nickname = nickname
#         self.age = age
#         self.level = level
#         self.points = points
#         Gamer.active_gamers += 1
#
#     def logout(self):
#         Gamer.active_gamers -= 1
#     def get_nickname(self):
#         return self.nickname
#     def get_age(self):
#         return  self.age
#     def get_level(self):
#         return self.level
#     def get_points(self):
#         return self.points
#     def is_adult(self):
#         return self.age >= 18
#     def get_adule_level(self):
#         if self.is_adult():
#             print('go')
#         else:
#             print('stop')
#
# # print(Gamer.active_gamers)
# #
# # gamer_1 = Gamer('hell_boy', 23, 5, 13)
# # print(Gamer.active_gamers)
# # gamer_2 = Gamer('potter', 13, 7, 34)
# # print(Gamer.active_gamers)
# # print(gamer_1.get_age())
# # gamer_1.get_adule_level()
# # print(gamer_2.get_age())
# # gamer_2.get_adule_level()
# #
# # print(Gamer.active_gamers)
# #
# # gamer_1.logout()
# # print(Gamer.active_gamers)
# # print(Gamer.get_active_gemers())
#
# # james = Gamer.gamer_from_string('foo, 32 , 3, 45')
# # jane = Gamer.gamer_from_string('ooooo, 12 , 9, 100')
# # print(james.get_age())
# # print(jane.get_level())
# # print(Gamer.get_active_gemers())
#
# my=dict.fromkeys((1,2,3),('fdf','gdd','ds5dr'))
# print(my)

          #нвследование/полиморфизм
# class Car:
#     wheels_number = 4
#     def __init__(self, name, color, year, is_crashed):
#         self.name = name
#         self.color = color
#         self.year = year
#         self.is_crashed = is_crashed
#         print('Car is created')
#     def drive(self, city):
#         print(self.name + 'is driving to ' + city)
#
#     def chang(self, new_color):
#         self.color = new_color
#         print('Color is changed to ' + new_color)
# class Truck(Car):
#     wheels_number = 6
#     def __init__(self, name, color, year, is_crashed):
#         Car.__init__(self, name, color, year, is_crashed)
#         print('Truck is created')
#     def drive(self, city):
#         print('Truck ' + self.name + 'is driving to ' + city)
#     def load_cargo(self, weight):
#         print('the cargo is loaded. Weight is ' + str(weight) + 'kg')
# man_truck = Truck('Man', 'white', 2015, False)
#
# man_truck.drive('New York')
# print(man_truck.wheels_number)
# man_truck.chang('red')
# man_truck.load_cargo(2000)

# class GameCharacter:
#     def __init__(self, name, health, level):
#         self.name = name
#         self.health = health
#         self.level = level
#     def speak(self):
#         print('Hi, my name is ' + self.name)
#
#
# class Villain(GameCharacter):
#     def __init__(self, name, health, level):
#         GameCharacter.__init__(self, name, health, level)
#     def speak(self):
#         print('Hi, my name is ' + self.name + ' and I will kill you')
#     def kill(self, other):
#         other.health = 0
#         print("Bang-bang, now you're dead")
#
# gamer_1 = GameCharacter('BiBo', 100, 5)
# gamer_2 = Villain('Hell boy', 2000, 45)
#
# gamer_1.speak()
# gamer_2.speak()
# print(gamer_1.health)
# gamer_2.kill(gamer_1)
# print(gamer_1.health)

         #множественное наследование
# class Swimmable:
#     def __init__(self, name):
#         print('Method init() of Swimmable')
#         self.name = name
#     def greeting(self):
#         print(f'Hello! My name is {self.name} and i can swim')
#
# class Walkable:
#     def __init__(self, name):
#         print('Method init() of Walkable')
#         self.name = name
#     def greeting(self):
#         print(f'Hello! My name is {self.name} and i can walk')
#
# class Flayable:
#     def __init__(self, name):
#         print('Method init() of Flayable')
#         self.name = name
#     def greeting(self):
#         print(f'Hello! My name is {self.name} and i can flay')
#
# class GameCharacter(Flayable,Swimmable,Walkable):
#     def __init__(self, name):
#         print('Method init() of GameCharacter')
#         self.name = name
#         Swimmable.__init__(self, name)
#         Walkable.__init__(self, name)
#         Flayable.__init__(self,name)
#
#     def greeting(self):
#         print(f'Hello! My name is {self.name}')
#
#
# james = GameCharacter('James')
# james.greeting()
#
# # print(isinstance(james, Walkable))
# # print(isinstance(james, Swimmable))
# # print(isinstance(james, Flayable))
# # print(isinstance(james, GameCharacter))
# # print(isinstance(james, object))

# class A:
#     def some_metod(self):
#         print('Method of class A')
# class B(A):
#     def some_metod(self):
#         print('Method of class B')
# class C(A):
#     def some_metod(self):
#         print('Method of class C')
# class D(B,C):
#     pass
#     # def some_metod(self):
#     #     print('Method of class D')
#
# print(D.__mro__)
# print(D.mro())
# help(D)
# som_object = D()
# som_object.some_metod()


# class Chain:
#     def __init__(self, number_of_items):
#         self.number_of_items = number_of_items
#     def __str__(self):
#         return 'Chain with ' + str(self.number_of_items) + ' items'
#     def __len__(self):
#         return self.number_of_items
#
# ch_1 = Chain(15)
# ch_2 = Chain(654)
#
# print(ch_1)
# print(ch_2)
#
# print(len(ch_1))
# print(len(ch_2))

