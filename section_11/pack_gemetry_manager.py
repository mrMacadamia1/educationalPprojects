#если нужно установить виджет внутри рамки, то  есть виджет внутри виджета
#если нужно расположить виджеты один под другим
#если нужно расположить элементы рядом друг с другом

from tkinter import *

main_window = Tk()
main_window.geometry('800x600+50+50')

# my_lable = Label(main_window, text='My Text', bg='green', fg='white')
# my_lable.pack(fill=X)



red_lable = Label(main_window, text='RED', bg='red', fg='white')
red_lable.pack(fill=BOTH, expand =1, padx=10)
yellow_lable = Label(main_window, text='YELLOW', bg='yellow', fg='black')
yellow_lable.pack(fill=BOTH, expand =1, padx=30, pady=20)
green_lable = Label(main_window, text='GREEN', bg='green', fg='white')
green_lable.pack(fill=BOTH, expand=1,padx=50)



# list_box = Listbox(main_window)
# list_box.pack()
# for i in range(20):
#     list_box.insert(END, str(i))





main_window.mainloop()