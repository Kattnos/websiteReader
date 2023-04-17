import requests
import html2text
import tkinter as tk
from tkinter import messagebox

root=tk.Tk()
root.geometry('900x700')

def updateText():
    print('updating text')
    url = inputSelect.get()

    response = requests.get(url)

    html = response.text
    content = html2text.html2text(html)

   # if content.find('<title>') != -1:
    #    title1 = content.partition('<title>')[2]
     #   title = title1.partition('</title>')[0]
    outputField.delete('1.0',tk.END)
    outputField.insert(tk.END,content)
    print(content)


inputField = tk.Frame(root)
inputSelect = tk.Entry(inputField, width=40)
inputSelectText = tk.Label(inputField, text='Select URL', font=('Arial', 11))
confirm = tk.Button(inputField, text='Confirm URL', font=('Arial', 12), command=updateText)
outputField = tk.Text(root, font=('Arial', 12))


confirm.grid(column=1, row=0)
inputSelect.grid(column=0, row=0, padx=5)
inputSelectText.grid(column=0, row=1, columnspan=1)
inputField.pack(pady=5,padx=2)
outputField.pack(pady=20,padx=10)

scroll = tk.Scrollbar(root, orient='vertical', command=outputField.yview)
outputField.config(yscrollcommand=scroll.set)
scroll.pack(side=tk.RIGHT, fill='y')

root.mainloop()