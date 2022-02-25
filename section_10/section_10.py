        #Advanced modules
        #collections. Counter
# from  collections import Counter
# number_lst = [1, 1, 1, 4 ,5, 477, 7576, 7]
#
# st = 'hgfdcfvbnmonibuytdx'
#
# c = Counter(st)
# #c.clear()
# print(list(c))
# print(set(c))
# print(dict(c))
# print(sum(c.values()))
# print(c.items())
# #print(Counter(st))

            #collections. defaultdict()
# from  collections import defaultdict
#  my_dict = defaultdict(object) #list, set, lambda, int
# my_dict[1] = 'a'
#
# # my_dict = {1: 'a'}
#
# print(my_dict[1])

            #collections. namedtuple()
# from  collections import namedtuple
#
# # jake = ('Jake', 'Smith', 19, 'male')
# # jim = ('Jim', 'Blom', 23, 'male')
# # jane = ('Jane', 'Mor', 20, 'female')
#
# Person = namedtuple('Person', 'name surname age gender')
# jake = Person(name='Jake', surname='Smith', age=19, gender='male')
# jim = Person(name='Jim', surname='Blom', age=23, gender='male')
# jane = Person(name='Jane', surname='Mor', age=20, gender='female')
# print(jake.age)
# print(jim.gender)
# print(jane.surname)
#
# print(jane)
# jane = jane._replace(surname='Blom')
# print(jane)

            #time
# import time

# print(time.gmtime())
# print(time.localtime())
# print(time.time())
# epoch = time.gmtime()
# print(epoch)
# print('Year: ',  epoch.tm_year)
# print('Month: ',  epoch.tm_mon)
# print('Day: ',  epoch.tm_mday)


# print(time.ctime(time.time()))
#
# loc = time.localtime(time.time())
# print(loc)
# print(time.mktime(loc))
# print(time.asctime(loc))
# print(time.strftime('%X',loc))
# print(time.localtime(1615268760.0))

# time_str = '9 March, 2021'
# str_time = time.strptime(time_str, '%d %B, %Y')
# print(str_time)

# input('Press enter to start: ')
#
# # start_time = time.monotonic()
# start_time = time.perf_counter()
# for i in range(1000000):
#     x = i *i
# # end_time = time.monotonic()
# end_time = time.perf_counter() #предпочтительно использовать perf_counter
# print(end_time - start_time)

# print('UTC time: ' + time.strftime('%Y/%m/%d %H:%M:%S', time.gmtime()))
# print('Local time: ' + time.strftime('%Y/%m/%d %H:%M:%S', time.localtime()))
#
# print(time.altzone/60/60)
# print(time.daylight)
# print(time.localtime())
# print(time.timezone/60/60)
# print(time.tzname)


            #quiz
# import  random
# import time
# q_a = []
# q_a.append(['The epoch is the point where the time starts and is platform independent','F'])
# q_a.append(['For Unix, the epoch is January 1, 1970, 00:00:00 (UTC) ','T'])
# q_a.append(['The term seconds since the epoch refers to the total number of elapsed seconds since the epoch, typically excluding leap seconds.','T'])
# q_a.append(['Function strptime() can parse 4-digit years when given %y format code.','F'])
# q_a.append(['UTC is Coordinated Universal Time ','T'])
# q_a.append(['DST is Daylight Saving Time, an adjustment of the timezone by (usually) two hour during part \
# of the year. DST rules are magic (determined by local law) and can change from year to year. ','F'])
# q_a.append(['The time value as returned by gmtime(), localtime(), and strptime(), \
# and accepted by asctime(), mktime() and strftime(), is a sequence of 9 integers.','T'])
#
# random.shuffle(q_a)
#
# user_score = 0
# start = time.perf_counter()
# for item in q_a:
#     print('True or False: ' + item[0])
#     a = input('Please enter T if it is true and F if it is false: ')
#     if a == item[1]:
#         print('Excellent!')
#         user_score +=1
#     else:
#         print('Not correct:-(  Maybe you will be lucky next time')
# end = time.perf_counter()
# print('Congratulations! Your total scor is: ' + str(user_score) + ', total time is ' + str(end - start) + 'seconds')

        #datetime. pytz package
# import pytz
# import  datetime
#
# k = 'Asia/Krasnoyarsk'
# tz_k = pytz.timezone(k)
# k_time = datetime.datetime.now(tz=tz_k)
# print(k_time)

# for tz in pytz.all_timezones:
#     print(tz) #список тайм зон
#
# for country in pytz.country_names:
#     print(country, pytz.country_names[country], pytz.country_timezones.get(country))
# print(datetime.datetime.today())
# print(datetime.datetime.now())
# print(datetime.datetime.utcnow())


            #datetime. Класс data
# from datetime import date

# today = date.today()
# print(today)
# print(today.year)
# print(today.month)
# print(today.day)

# date_1 =date(2021,3,10)
# date_2 = date(2020,3,10)
# diff = date_1 - date_2
# print(diff)

# today = date.today()
# print(today)
# my_b = date(2021,3,13)
# diff = my_b-today
# print(diff)

# today = date.today()
#
# week_day = today.weekday()
# week_day = today.isoweekday()
# print(week_day)

# year = input('Введите год: ')
# month = input('Введите месяц: ')
# day = input('Введите день: ')
#
# date_1 = date(int(year), int(month), int(day))
# # print(data_1)
# week_day = date_1.weekday()
# if week_day == 0:
#     print(date_1, 'это понедельник')
# elif week_day == 1:
#     print(date_1, 'это вторник')
# elif week_day == 2:
#     print(date_1, 'это среда')
# elif week_day == 3:
#     print(date_1, 'это четверг')
# elif week_day == 4:
#     print(date_1, 'это пятница')
# elif week_day == 5:
#     print(date_1, 'это суббота')
# elif week_day == 6:
#     print(date_1, 'это воскресенье')

# from datetime import datetime

# today = datetime(2021,3,10)
# today_now = datetime.now()
# print(today)
# print(today_now)
#
# tamp = datetime.timestamp(today)
# print(tamp)
# tamp_now = datetime.timestamp(today_now)
# print(tamp_now)

# today = datetime(2021,3,10)
# print(today)
# tamp = datetime.timestamp(today)
# print(tamp)
# today_ft = datetime.fromtimestamp(tamp)
# print(today_ft)
# today_format = today.strftime('%d %B %Y')
# print(today_format)
# print(today.strftime('%A'))

# today = datetime.today()
# print(today)
# utc_today =today.utcnow()
# print(utc_today)
# print(today.date())
# print(today.time())
# print(today.isocalendar())

            #datetime. timedelta разница между двумя промежутками времени
# from datetime import timedelta, datetime
#
# # year = timedelta(days=365)
# # print(year)
#
# today = datetime.now()
# print(today)
# print('23 days from today will be', (today + timedelta(days=23)))

#
# import pytz, datetime
#
# # for country in pytz.country_names:
# #     print(country, pytz.country_names[country], pytz.country_timezones.get(country))
#
# timezone_dict = {
#     'AD': ('Andorra', 'Europe/Andorra'),
#     'AE': ('United Arab Emirates', 'Asia/Dubai'),
#     'AF': ('Afghanistan', 'Asia/Kabul'),
#     'AG': ('Antigua & Barbuda', 'America/Antigua'),
#     'AI': ('Anguilla', 'America/Anguilla'),
#     'AL': ('Albania', 'Europe/Tirane'),
#     'AM': ('Armenia', 'Asia/Yerevan')
# }
#
# for key in timezone_dict:
#     print(key, timezone_dict[key])
# print('Пожалуйста введите код страны, что бы посмотреть тайм-зону (или нажмите "q" для выхода)')
#
#
# while True:
#     country_code = input()
#     if country_code == 'q':
#         break
#     if country_code in timezone_dict.keys():
#         timezone = pytz.timezone(timezone_dict[country_code][1])
#         print('Local time is {}'.format(datetime.datetime.now(tz=timezone)))
#         print('UTC time is {}'.format(datetime.datetime.utcnow()))

            #Best practices
import datetime, pytz

iso_format_string = '%Y-%m-%dT%H: %M:%S%z'
now_uts = datetime.datetime.now(pytz.timezone('UTC'))
print(now_uts.strftime(iso_format_string))

now_eu = now_uts.astimezone(pytz.timezone('Europe/Kiev'))
print(now_eu.strftime(iso_format_string))

# all_timezones = pytz.all_timezones
# for timezone in all_timezones:
#     print(timezone)

naive_now = datetime.datetime.now()
print(naive_now)
kiev_timezone = pytz.timezone('Europe/Kiev')
local_datetime = kiev_timezone.localize(naive_now)
print(local_datetime)