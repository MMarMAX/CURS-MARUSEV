from tkinter import *
from addBook import btnAddBook
from deleteBook import btnDeleteBook
from viewBooks import btnViewBook







root = Tk()
root.title("Library Manager")
root.minsize(width=400, height=600)
root.geometry("600x500")
headFrame1 = Frame(root, bg="#1890ec", bd=5)
headFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)
headLabel = Label(headFrame1, text="Добро пожаловать в \n Менеджер библиотеки",
                  bg='white', fg='#1890ec', font=("Arial Black", 16))
headLabel.place(relx=0, rely=0, relwidth=1, relheight=1 )

btn1 = Button(root, text="Добавить книгу", bg='white', fg='#1890ec',
              font=("Arial Black", 13), command=btnAddBook)

btn1.place(relx=0.29, rely=0.39, relwidth=0.43, relheight=0.1)

btn2 = Button(root, text="Удалить книгу", bg='white',
              fg='#1890ec', font=("Arial Black", 13), command=btnDeleteBook)

btn2.place(relx=0.29, rely=0.49,relwidth=0.43, relheight=0.1)

btn3 = Button(root, text="Просмотреть книги \n в библиотеке",
              bg='white', fg='#1890ec', font=("Arial Black", 13), command=btnViewBook)

btn3.place(relx=0.29, rely=0.59, relwidth=0.43, relheight=0.1)

btn4 = Button(root, text="Выдать книгу студенту", bg='white',
              fg='#1890ec', font=("Arial Black", 13))

btn4.place(relx=0.29, rely=0.69, relwidth=0.43, relheight=0.1)

btn5=Button(root, text="Возврат книги", bg='white',
            fg='#1890ec', font=("Arial Black",13))

btn5.place(relx=0.29, rely=0.79, relwidth=0.43,relheight=0.1)
root.mainloop()

