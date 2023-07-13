import tkinter
import tkinter.messagebox
import tkinter.filedialog
from tkinter import Label

import mysql.connector as pz

conn = pz.connect(host='localhost', database='Pizza', user='root', password='********')
cursor = conn.cursor()


def submit():
    conn = pz.connect(host='localhost', database='Pizza', user='root', password='root')
    c = conn.cursor()
    c.execute("INSERT INTO client (name, address, telephone) VALUES (%s, %s, %s)", (nameEnter.get(), addressEnter.get(), telephoneEnter.get()))

    records = c.fetchall()
    print(records)

    print_records = ''
    for record in records:
        print_records += str(record[0]) + " " + str(record[1]) + "\n"

    conn.commit()
    conn.close()


def query():
    conn = pz.connect(host='localhost', database='Pizza', user='root', password='Gloire1963')
    c = conn.cursor()
    c.execute("SELECT * FROM client")
    records = c.fetchall()
    print(records)

    print_records = ''
    for record in records:
        print_records += str(record[0]) + " " + str(record[1]) + "\n"


def delete():
    conn = pz.connect(host='localhost', database='Pizza', user='root', password='Gloire1963')
    c = conn.cursor()
    c.execute("DELETE FROM client")

    conn.commit()
    conn.close()


mainapp = tkinter.Tk()
mainapp.title("Speedy Pizza")
mainapp.geometry("300x320+300+150")

fontLabel = 'arial 13 bold'
fontEnter = 'arial 11 bold'

name = tkinter.Label(mainapp, text="Name :", font=fontLabel, fg='white', bg='#FF7800')
address = tkinter.Label(mainapp, text="Address :", font=fontLabel, fg='white', bg='#FF7800')
telephone = tkinter.Label(mainapp, text="Telephone :", font=fontLabel, fg='white', bg='#FF7800')
food = tkinter.Label(mainapp, text="Food :", font=fontLabel, fg='white', bg='#FF7800')
info = tkinter.Label(mainapp, text="Registration ", font=fontLabel, fg='#FF7800', bg='white')

nameEnter = tkinter.Entry(mainapp, font=fontEnter)
addressEnter = tkinter.Entry(mainapp, font=fontEnter)
telephoneEnter = tkinter.Entry(mainapp, font=fontEnter)
foodEnter = tkinter.Entry(mainapp, font=fontEnter)

info.grid(row=0, column=0, columnspan=2)
name.grid(row=1, column=0, sticky=tkinter.E, padx=5, pady=5)
address.grid(row=2, column=0, sticky=tkinter.E, padx=5, pady=5)
telephone.grid(row=3, column=0, sticky=tkinter.E, padx=5, pady=5)
food.grid(row=4, column=0, sticky=tkinter.E, padx=5, pady=5)

nameEnter.grid(row=1, column=1, padx=5, pady=5)
addressEnter.grid(row=2, column=1, padx=5, pady=5)
telephoneEnter.grid(row=3, column=1, padx=5, pady=5)
foodEnter.grid(row=4, column=1, padx=5, pady=5)

submit_btn = tkinter.Button(mainapp, text="add", command=submit, width=10, fg='#FF7800', bg='white')
query_btn = tkinter.Button(mainapp, text="show", command=query, width=10, fg='#FF7800', bg='white')
delete_bt3 = tkinter.Button(mainapp, text="delete", command=delete, width=10, fg='#FF7800', bg='white')

submit_btn.grid(row=5, column=0, pady=5)
query_btn.grid(row=6, column=0, pady=5, sticky=tkinter.E)
delete_bt3.grid(row=7, column=0, pady=5, sticky=tkinter.E)

conn.commit()
conn.close()
mainapp.mainloop()
