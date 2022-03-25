from tkinter import *
def btnViewBook():
    root3 = Tk()
    root3.title("Library Manager")
    root3.minsize(width=400, height=600)
    root3.geometry("600x500")
    headFrame4 = Frame(root3, bg="#34dfdc", bd=5)
    headFrame4.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)
    headLabel = Label(headFrame4, text="Список книг", bg='white', fg='#34dfdc', font=("Arial Black", 15))
    headLabel.place(relx=0, rely=0, relwidth=1, relheight=1)
    labelFrame = Frame(root3, bg='black')
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)
    lb = Label(labelFrame, text="%-10s%-40s%-30s%-20s"%('ID книги', 'Название', 'Автор', 'Статус'), bg='black', fg='white', font=("Arial Black", 8))
    lb.place(relx=0.07, rely=0.1)
    lb1 = Label(labelFrame,
                text='------------------------------------------------------------------------------------------------', bg='black', fg='white')
    lb1.place(relx=0.06, rely=0.2)
    quitBtn = Button(root3, text="Выйти", bg='#ff6666', fg='white', font=('Arial Black', 10),command=root3.destroy)
    quitBtn.place(relx=0.4, rely=0.85, relwidth=0.18, relheight=0.08)
