from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def update(rows):
    for i in rows:
        trv.insert("", 'end', values=i)
        
def getrow(event):
    rowid = trv.identify_row(event.y)
    item = trv.item(trv.focus())
    print(item['values'][0])
    print(item['values'][1])
    print(item['values'][2])
    print(item['values'][3])

def select(event=None):
    trv.selection_toggle(trv.focus())
    selected = trv.selection()
    print("\n".join([str(trv.item(i)['values']) for i in selected]))



root = Tk()

wrapper1 = LabelFrame(root, text="Customer List")
wrapper2 = LabelFrame(root, text="Search")
wrapper3 = LabelFrame(root, text="Customer Data")

wrapper1.pack(fill="both", expand="yes", padx=20, pady=10)
wrapper2.pack(fill="both", expand="yes", padx=20, pady=10)
wrapper3.pack(fill="both", expand="yes", padx=20, pady=10)

trv = ttk.Treeview(wrapper1, columns=(1, 2, 3, 4), show="headings", height="6", selectmode="none")
trv.pack()

trv.heading(1, text="Customer ID")
trv.heading(2, text="First Name")
trv.heading(3, text="Last Name")
trv.heading(4, text="Age")

# trv.bind('<<TreeviewSelect>>', getrow)
trv.bind("<ButtonRelease-1>", select)

data = [[
    1,
    'Lucas',
    'Carvalho',
    28
],
[
    2,
    'Pedro',
    'Souza',
    32
]
]

update(data)


root.title('Testando TK')
root.geometry("800x500")
root.mainloop()

