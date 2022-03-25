from tkinter import *
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

    lb = Label(labelFrame, text="ID книги : ", bg='black', fg='white', font=("Arial Black", 10))
    lb.place(relx=0.05, rely=0.5)

    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3, rely=0.5, relwidth=0.62)

    submitBtn = Button(root2, text="Подтвердить", bg="#003366", fg='white',font=('Arial Black',10))
    submitBtn.place(relx=0.12, rely=0.85, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root2, text="Выйти", bg='#ff6666', fg='white', font=("Arial Black", 10),command=root2.destroy)
    quitBtn.place(relx=0.7, rely=0.85, relwidth=0.18, relheight=0.08)
