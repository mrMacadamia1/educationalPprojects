                    #GUI Graphical User InterFace
            #GUI
from tkinter import *
from tkinter import font

root_window = Tk()
root_window.geometry('500x500')
root_window.title('Welcome')

hello_lable = Label(root_window, text='Welcome to Tkinter!', font=('arial', 20, 'bold'), fg='green', bg='white', relief='solid') #solid, flat, raised, sunken,ridge,groove
hello_lable.pack()
# hello_lable.place(x=, y=) #расположения текста


version_lable = Label(root_window, text='version 8.6')
version_lable.pack()


go_button = Button(root_window, text='Go!', font=('arial', 20, 'bold'), fg='black', bg='green', relief=RAISED)
go_button.pack()
# print(font.families()) #типы шрифтов
print(TkVersion)

root_window.mainloop()