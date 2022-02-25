from tkinter import *

root = Tk()
root.geometry('500x300+100+100')

# red_lable = Label(root, text='RED', bg='red', fg='white')
# red_lable.place(x=150, y=250, width=200)
# yellow_lable = Label(root, text='YELLOW', bg='yellow', fg='black')
# yellow_lable.place(x=175, y=130, width=150, height=40)
# green_lable = Label(root, text='GREEN', bg='green', fg='white')
# green_lable.place(x=100, y=135, heigh=30)

# red_lable_rel_height = Label(root, text='RED relheight=0.3', bg='red', fg='white')
# red_lable_rel_height.place(relheight=0.3)
# yellow_lable_rel_width = Label(root, text='YELLOW relwidth=0.7', bg='yellow', fg='black')
# yellow_lable_rel_width.place(relwidth=0.7)
# green_lable_rel_x = Label(root, text='GREEN relx=0.2', bg='green', fg='white')
# green_lable_rel_x.place(relx=0.2)
# green_lable_rel_y = Label(root, text='GREEN rely=0.4', bg='green', fg='white')
# green_lable_rel_y.place(rely=0.4)

label = Label(root, text='some text', bg='green', fg='white')
label.place(width=400, height=100, x=50, y=100)
button = Button(root, text='some button')
button.place(in_=label, relx=0.5, rely=0.5, anchor=CENTER)


root.mainloop()

