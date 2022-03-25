from tkinter import *
from addBook import btnAddBook
from deleteBook import btnDeleteBook
from viewBooks import btnViewBook

def btnIssueBook():
    root4 = Tk()
    root4.title("Library Manager")
    root4.minsize(width=400, height=600)
    root4.geometry("600x500")
    headFrame5=Frame(root4, bg='#4d00db',bd=5)
    headFrame5.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)
    headLabel=Label(headFrame5, text='Выдать книгу студенту', bg='white', fg='#4d00db',font=("Arial Black", 15))
    headLabel.place(relx=0, rely=0, relwidth=1, relheight=1)
    labelFrame=Frame(root4, bg='black')
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)
    #ID
    lb1 = Label(labelFrame, text="ID книги : ", bg="black", fg='white',font=("Arial Black",10))
    lb1.place(relx=0.05, rely=0.2)

    inf1 = Entry(labelFrame)
    inf1.place(relx=0.25, rely=0.2,relwidth=0.62)
    #Имя студента
    lb2 = Label(labelFrame, text="Выдана студенту : ", bg='black', fg='white', font=("Arial Black", 10))
    lb2.place(relx=0.05, rely=0.4)

    inf2 = Entry(labelFrame)
    inf2.place(relx=0.35, rely=0.4, relwidth=0.62)
    submitBtn = Button(root4, text="Выдать книгу студенту", bg='#4d00db', fg='white',font=("Arial Black",10))
    submitBtn.place(relx=0.12, rely=0.83, relwidth=0.3, relheight=0.08)





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
              fg='#1890ec', font=("Arial Black", 13),command=btnIssueBook)

btn4.place(relx=0.29, rely=0.69, relwidth=0.43, relheight=0.1)

btn5=Button(root, text="Возврат книги", bg='white',
            fg='#1890ec', font=("Arial Black",13))

btn5.place(relx=0.29, rely=0.79, relwidth=0.43,relheight=0.1)
root.mainloop()

