from tkinter import *

root_window=Tk()

red_label = Label(root_window, text='RED', bg='red', fg='white', width=20, height=5)
red_label.grid(row=0, column=0)
yellow_label = Label(root_window, text='YELLOW', bg='yellow', fg='black',width=20, height=5)
yellow_label.grid(row=0, column=1)
green_label = Label(root_window, text='GREEN', bg='green', fg='white',width=20, height=5)
green_label.grid(row=0, column=2)

red_label_1 = Label(root_window, text='RED', bg='red', fg='white', width=20, height=5)
red_label_1.grid(row=1, column=0)
yellow_label_2 = Label(root_window, text='YELLOW', bg='yellow', fg='black',width=20, height=5)
yellow_label_2.grid(row=1, column=1)
green_label_3 = Label(root_window, text='GREEN', bg='green', fg='white',width=20, height=5)
green_label_3.grid(row=1, column=2)

button_1 = Button(root_window, text='Butten_1')
button_1.grid(row=2, column=0)
button_2 = Button(root_window, text='Butten_2')
button_2.grid(row=2, column=1)
button_3 = Button(root_window, text='Butten_3')
button_3.grid(row=2, column=2)



root_window.mainloop()