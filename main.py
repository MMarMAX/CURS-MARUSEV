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

 url = 'https://api.exchangerate-api.com/v4/latest/USD'


class App(tk.Tk):
 def __init__(self, converter):
  tk.Tk.__init__(self)
  self.title = "Converter"
  self.converter = converter
  self.intro = Label(self, text="Конвертер валют", fg='blue', borderwidth=3, font=('Times New Roman', 16))
  self.date = Label(self, text=f"1 индийская рупия = {self.converter.convert('IND','USD',1)} USD \n Дата:{self.converter.data['date']}",
                    relief=tkinter.GROOVE, borderwidth=5)
  self.intro.place(x=125, y=10)
  self.date.place(x=125, y=50)

  #Создание полей для ввода валют
  valid = (self.register(self.restrictNumberOnly), '%d', '%P')
  self.amount_field = Entry(self, bd=3, justify=tk.CENTER, validate='key', validatecommand=valid)
  self.converted_amount_field = Label(self, text='', fg='black', bg='white',justify=tk.CENTER, width=16, borderwidth=3)

  #Значения по умолчанию
  self.from_currency_value = StringVar(self)
  self.from_currency_value.set('RUB')
  self.to_currency_value = StringVar(self)
  self.to_currency_value.set('USD')

  font=('Times New Roman', 12, 'bold')
  self.option_add('*TCombobox*Listbox.font', font)
  self.from_currency_dropdown = ttk.Combobox(self, textvariable=self.from_currency_value,
                                             values=list(self.converter.currencies.keys()), font=font,
                                             state='readonly', width=12, justify=tk.CENTER)
  self.to_currency_dropdown = ttk.Combobox(self, textvariable=self.to_currency_value,
                                           values=list(self.converter.currencies.keys()), font=font,
                                           state='readonly', width=12, justify=tk.CENTER)

  #Размещение элементов
  self.from_currency_dropdown.place(x=30, y=120)
  self.amount_field.place(x=36, y=150)
  self.to_currency_dropdown.place(x=340, y=120)
  self.converted_amount_field.place(x=346, y=150)


  self.convert_button = Button(self, text="Конвертировать", fg="black",
                               command=self.perform, font=('Times New Roman, 12'))
  self.convert_button.place(x=225, y=135)
 def perform(self):
  amount = float(self.amount_field.get())
  from_curr = self.from_currency_value.get()
  to_curr = self.to_currency_value.get()


  converted_amount = self.converter.convert(from_curr, to_curr, amount)
  converted_amount = round(converted_amount, 2)
  self.converted_amount_field.config(text=str(converted_amount))

  def restrictNumberOnly(self, action, string):
        regex = re.compile(r"[0-9,]*?(\.)?[0-9,]*$")
        result = regex.match(string)
        return (string == "" or (string.count('.') <= 1 and result is not None))



if __name__ == '__main__':
   url = 'https://api.exchangerate-api.com/v4/latest/USD'
   converter = CurrencyConverter(url)

   App(converter)
   mainloop()




















