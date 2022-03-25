from tkinter import *
from addBook import btnAddBook
def btnDeleteBook():
    root2 = Tk()
    root2.title("Library Manager")
    root2.minsize(width=400, height=600)
    root2.geometry("600x500")

    headFrame3 = Frame(root2, bg="#003366", bd=5)
    headFrame3.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)
    headLabel3 = Label(headFrame3, text="Удалить книгу", bg='white', fg='#003366', font=('Arial Black',15))
    headLabel3.place(relx=0,rely=0, relwidth=1, relheight=1)
    labelFrame = Frame(root2, bg='black')
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

    lb = Label(labelFrame, text="ID книги : ", bg='black', fg='white',font=("Arial Black", 10))
    lb.place(relx=0.05, rely=0.5)

    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3, rely=0.5, relwidth=0.62)

    submitBtn = Button(root2, text="Подтвердить", bg="#003366", fg='white',font=('Arial Black',10))
    submitBtn.place(relx=0.12, rely=0.85, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root2, text="Выйти", bg='#ff6666', fg='white', font=("Arial Black", 10))
    quitBtn.place(relx=0.7, rely=0.85, relwidth=0.18, relheight=0.08)







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
              bg='white', fg='#1890ec', font=("Arial Black", 13))

btn3.place(relx=0.29, rely=0.59, relwidth=0.43, relheight=0.1)

btn4 = Button(root, text="Выдать книгу студенту", bg='white',
              fg='#1890ec', font=("Arial Black", 13))

btn4.place(relx=0.29, rely=0.69, relwidth=0.43, relheight=0.1)

btn5=Button(root, text="Возврат книги", bg='white',
            fg='#1890ec', font=("Arial Black",13))

btn5.place(relx=0.29, rely=0.79, relwidth=0.43,relheight=0.1)
root.mainloop()

