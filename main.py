import requests
from tkinter import *
import tkinter as tk
from tkinter import ttk




class CurrencyConverter():
 def __init__(self,url):
  self.data = requests.get(url).json()
  self.currencies = self.data['rates']
 def convert(self,from_currency, to_currency,amount):
  initial_amount = amount
  if from_currency != 'USD':
    amount = amount/self.currencies[from_currency]
  amount = round(amount * self.currencies[to_currency], 4)
  return amount

url='https://api.exchangerate-api.com/v4/latest/USD'
converter= CurrencyConverter(url)
print(converter.convert('USD','RUB',100))













root=Tk()
root.title = 'Converter'
root.geometry("500x200")
  #Labels

intro = Label(root,text='Конвертер валют',fg='blue',relief=tk.RAISED, borderwidth=3)
intro.config(font = ('Times New Roman',15,'bold'))
date = Label(root,text='1 USD = 82.5 RUB \n Date:14.04.2022 ', relief=tk.GROOVE,borderwidth=5)
intro.place(x=50,y=5)
date.place(x=170, y=50)



