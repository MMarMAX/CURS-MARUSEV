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
converter = CurrencyConverter(url)
print(converter.convert('RUB', 'USD', 10000))



class ConvereterUI:
 def __init__(self, converter):
  Tk.__init__(self)
  self.title = "Converter"
  self.converter = converter
  self.intro = Label(self, text="Конвертер валют", fg='blue', borderwidth=3, font=('Times New Roman', 16))
  self.date = Label(self, text=f"1 индийская рупия = {self.converter.convert('IND','USD',1)} USD \n Date:{self.converter.data['date']}",
                    relief=tkinter.GROOVE, borderwidth=5)
  self.intro.place(x=20, y=10)
  self.date.place(x=170, y=50)





