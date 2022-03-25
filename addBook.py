from tkinter import *
def btnAddBook():
    #Создание окна
    root1 = Tk()
    root1.title('Library Manager')
    root1.minsize(width=400, height=600)
    root1.geometry("600x500")

    #Создание надписи
    headFrame2 = Frame(root1, bg='#0417a4',bd=5)
    headFrame2.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)
    headLabel2 = Label(headFrame2, text="Добавление книги", bg='white', fg='#0417a4', font=("Arial Black", 15))
    headLabel2.place(relx=0, rely=0, relwidth=1, relheight=1)


    labelFrame = Frame(root1, bg='black')
    labelFrame.place(relx=0.1, rely=0.35, relwidth=0.8, relheight=0.5)
    #ID книги
    lb1 = Label(labelFrame, text="ID книги : ", bg='black', fg="white", font=("Arial Black", 10))
    lb1.place(relx=0.05, rely=0.2, relheight=0.08)

    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.24, rely=0.2, relwidth=0.6, relheight=0.07)
    #Название книги
    lb2 = Label(labelFrame, text="Название : ", bg='black', fg='white', font=("Arial Black", 10))
    lb2.place(relx=0.05, rely=0.35, relheight=0.08)

    bookInfo2 = Entry(labelFrame)
    bookInfo2.place(relx=0.24, rely=0.35, relwidth=0.6, relheight=0.07)
    #Автор
    lb3 = Label(labelFrame, text="Автор : ", bg='black', fg='white',font=("Arial Black", 10))
    lb3.place(relx=0.05, rely=0.5, relheight=0.08)

    bookInfo3 = Entry(labelFrame)
    bookInfo3.place(relx=0.18, rely=0.5, relwidth=0.6, relheight=0.07)
    #Статус книги
    lb4 = Label(labelFrame, text="Статус (в/н) : ", bg='black', fg='white', font=("Arial Black", 10))
    lb4.place(relx=0.03, rely=0.65, relheight=0.08)

    bookInfo4 = Entry(labelFrame)
    bookInfo4.place(relx=0.24, rely=0.65, relwidth=0.6, relheight=0.07)
    #Кнопка "Подтвердить"
    submitBtn = Button(root1, text="Подтвердить", bg='#0417a4', fg='white',font=("Arial Black", 10))
    submitBtn.place(relx=0.12, rely=0.85, relwidth=0.18, relheight=0.08)

    #Кнопка "Выйти"
    quitBtn = Button(root1, text="Выйти", bg="#ff6666", fg='white', font=("Arial Black", 10), )
    quitBtn.place(relx=0.7, rely=0.85, relwidth=0.18, relheight=0.08)
