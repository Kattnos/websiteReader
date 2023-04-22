import requests
import html2text
from bs4 import BeautifulSoup
import lxml
import tkinter as tk
from tkinter import messagebox

root=tk.Tk()
root.geometry('900x700')

def updateText():
    print('updating text')
    url = inputSelect.get()

    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'lxml')

    articleTitle = soup.title
    articleText = soup.get_text()
    outputField.delete('1.0', tk.END)
    outputField.insert(tk.END, articleText)

inputField = tk.Frame(root)
inputSelect = tk.Entry(inputField, width=40)
inputSelectText = tk.Label(inputField, text='Select URL', font=('Arial', 11))
confirm = tk.Button(inputField, text='Confirm URL', font=('Arial', 12), command=updateText)
outputFieldFrame = tk.Frame(root)
outputField = tk.Text(outputFieldFrame, font=('Arial', 12))


confirm.grid(column=1, row=0)
inputSelect.grid(column=0, row=0, padx=5)
inputSelectText.grid(column=0, row=1, columnspan=1)
inputField.pack(pady=5,padx=2)
outputFieldFrame.pack(pady=20,padx=10)
outputField.pack(side =tk.LEFT, fill = tk.BOTH)

scroll = tk.Scrollbar(outputFieldFrame, orient='vertical', command=outputField.yview)
outputField.config(yscrollcommand=scroll.set)
scroll.pack(side=tk.RIGHT, fill='y')

root.mainloop()