import tkinter

import requests
from tkinter import *
import tkinter as tk
from tkinter import ttk




class CurrencyConverter():
 def __init__(self, url):
  self.data = requests.get(url).json()
  self.currencies = self.data['rates']
 def convert(self, from_currency, to_currency,amount):
  initial_amount = amount
  if from_currency != 'USD':
    amount = amount/self.currencies[from_currency]
  amount = round(amount * self.currencies[to_currency], 4)
  return amount




class App(tk.Tk):
 def __init__(self, converter):
  tk.Tk.__init__(self)
  self.title = "Converter"
  self.geometry('600x400')
  self.converter = converter
  self.intro = Label(self, text="Конвертер валют", fg='blue', borderwidth=3, font=('Arial Black', 18),relief=tkinter.GROOVE)
  self.currency = Label(self, text=f"1 доллар = {self.converter.convert('USD','RUB',1)} рублей \n "f"1 евро = {self.converter.convert('EUR','RUB',1)} рублей"
                    , fg='blue', font=("Arial Black", 15), borderwidth=5)
  self.date = Label(self,text=f"Дата:{self.converter.data['date']}", fg='red',font=('Arial Black',12))
  self.intro.place(x=200, y=10)
  self.currency.place(x=180, y=50)
  self.date.place(x=440, y=370)

  #Создание полей для ввода валют
  valid = (self.register(self.restrictNumberOnly), '%d', '%P')
  self.amount_field = Entry(self, bd=3, justify=tk.CENTER, validate='key', validatecommand=valid,font=('Times New Roman', 12))
  self.converted_amount_field = Label(self, text='', fg='black', bg='white',justify=tk.CENTER, width=16, borderwidth=3, font=('Times New Roman',12))

  #Значения по умолчанию
  self.from_currency_value = StringVar(self)
  self.from_currency_value.set('USD')
  self.to_currency_value = StringVar(self)
  self.to_currency_value.set('RUB')
  #Выпадающие списки с валютой
  font=('Times New Roman', 12, 'bold')
  self.option_add('*TCombobox*Listbox.font', font)
  self.from_currency_dropdown = ttk.Combobox(self, textvariable=self.from_currency_value,
                                             values=list(self.converter.currencies.keys()), font=font,
                                             state='readonly', width=12, justify=tk.CENTER)
  self.to_currency_dropdown = ttk.Combobox(self, textvariable=self.to_currency_value,
                                           values=list(self.converter.currencies.keys()), font=font,
                                           state='readonly', width=12, justify=tk.CENTER)

  #Размещение элементов
  self.from_currency_dropdown.place(x=100, y=150)
  self.amount_field.place(x=80, y=190)
  self.to_currency_dropdown.place(x=400, y=150)
  self.converted_amount_field.place(x=400, y=190)

  #Кнопка
  self.convert_button = Button(self, text="Конвертировать", fg="black",bg='blue' ,command=self.perform)
  self.convert_button.config(font=("Times New Roman", 11))
  self.convert_button.place(x=265, y=235)
 #Функция конвертирования
 def perform(self):
  amount = float(self.amount_field.get())
  from_curr = self.from_currency_value.get()
  to_curr = self.to_currency_value.get()


  converted_amount = self.converter.convert(from_curr, to_curr, amount)
  converted_amount = round(converted_amount, 2)
  self.converted_amount_field.config(text=str(converted_amount))
  #Ограничение
 def restrictNumberOnly(self, action, string):
        regex = re.compile(r"[0-9,]*?(\.)?[0-9,]*$")
        result = regex.match(string)
        return (string == "" or (string.count('.') <= 1 and result is not None))



if __name__ == '__main__':
   url = 'https://api.exchangerate-api.com/v4/latest/USD'
   converter = CurrencyConverter(url)

   App(converter)
   mainloop()




















