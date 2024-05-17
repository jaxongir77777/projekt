from tkinter import *

window = Tk()

window.title('My App')

window.geometry('250x50')

window.configure(background='black')

my_label=Label(window, width=40,
               
height=5, bg='red', text='hello')


def change_text():
        my_label.config(text='Hello!')

my_button=Button(window, text="Pressme!", width=50, command=change_text())

my_button.grid(row=1, column=0)

window.mainloop()   
