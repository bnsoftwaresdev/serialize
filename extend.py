#!usr/bin/env python
# -*- coding: utf-8 -*-
import MySQLdb
import pymysql
import yaml

# from tkinter import *
from tkinter import messagebox, StringVar

try:
    import Tkinter
except:
    import tkinter as Tkinter
from Tkinter import*
import ttk
import random
import time
import webbrowser
import ttk
from PIL import ImageTk, Image
import threading
import Queue
import time
from ttk import Combobox
import time
#from Tkinter import MessageBox
import tkMessageBox
from Tkinter import Tk, Frame, Menu, Button

from Tkinter import LEFT, TOP, X, FLAT, RAISED


w1 = Tkinter.Tk()
w1.title('My Contacts')

s = ttk.Style()
s.theme_names()
('aqua', 'aqua cocoa', 'X11', 'step', 'clam', 'alt', 'default', 'classic', 'motif', 'plastique', 'CDE', 'windows')
s.theme_use('clam')

w1.geometry('950x700-30+10')
w1.minsize("950", "680")
w1.maxsize("950", "700")
w1.config(background='#E4E4E4')
style = ttk.Style()
style.configure('Mini.TButton',
                    background='#0066CC',
                    foreground='white',
                    highlightthickness='60',
                    length='2',
                    width='3',
                    font=('DejaVu Sans Mono', 8, 'bold'))
style.map('Mini.TButton',
              foreground=[('disabled', 'yellow'),
                          ('pressed', 'white'),
                          ('active', 'white')],
              background=[('disabled', '#0066CC'),
                          ('pressed', '!focus', 'green'),
                          ('active', 'blue')],
              highlightcolor=[('focus', 'white'),
                              ('!focus', 'blue')],
              relief=[('pressed', 'flat'),
                      ('!pressed', 'flat')])
overrelief = [('pressed', 'flat'),
                  ('!pressed', 'flat')]

style = ttk.Style()
style.configure('Minis.TButton',
                    background='red',
                    foreground='white',
                    highlightthickness='60',
                    width='3',
                    font=('DejaVu Sans Mono', 8, 'bold'))
style.map('Minis.TButton',
              foreground=[('disabled', 'yellow'),
                          ('pressed', 'white'),
                          ('active', 'white')],
              background=[('disabled', '#0066CC'),
                          ('pressed', '!focus', 'green'),
                          ('active', '#ff3333')],
              highlightcolor=[('focus', 'grey'),
                              ('!focus', 'blue')],
              relief=[('pressed', 'flat'),
                      ('!pressed', 'flat')])
overrelief = [('pressed', 'groove'),
                  ('!pressed', 'ridge')]

ento = StringVar()
ento1 = StringVar()
lona = StringVar()
lon = StringVar()
selected_item = StringVar()

fun = "ode.yaml"
hold = "hose.yaml"
fam = "pan.yaml"
nav = "challo.yaml"
portsy = "sed.yaml"
olo = "nei.yaml"
atkui = "bors.yaml"
biug = "chae.yaml"
#=========================We start our functions here===================================================================
def clear():
    ento.set('')
    ento1.set('')


def add_all():
    data = Toplevel(height="300", width="730", relief="flat")
    data.geometry("540x180-410+280")
    data.minsize("540", "180")
    data.maxsize("540", "180")
    data.title("Add Data")
    data.config(background="lavender")

    ent = StringVar()
    ent1 = StringVar()
    ento1 = StringVar()
    ento11 = StringVar()

    lab = ttk.Label(data, text="Name (Input the new Name): ", font=('', 12, ''), background="lavender")
    lab.grid(row=0, column=0, padx=5, pady=5)

    lab1 = ttk.Label(data, text="Telephone (Input the new Telephone #): ", font=('', 12, ''), background="lavender")
    lab1.grid(row=1, column=0, padx=5, pady=5)

    lab2 = ttk.Label(data, text="City (Input the City name): ", font=('', 12, ''), background="lavender")
    lab2.grid(row=2, column=0, padx=5, pady=5)

    lab3 = ttk.Label(data, text="Address (Input the new Address): ", font=('', 12, ''), background="lavender")
    lab3.grid(row=3, column=0, padx=5, pady=5)

    ento = StringVar()
    ento1 = StringVar()
    ent1 = StringVar()
    ento11 = StringVar()

    def add_up():
        hala = (ento11.get() + "", ento1.get() + "", ento1.get() + "", ento.get() + "")
        #
        tree.insert('', 'end', values=hala)
        # tree serialization
        with open(fun, "w") as f:
            yaml.dump(hala, f)

    ento = ttk.Entry(data, width=20, font=('arial', 12, ''))
    ento.grid(row=0, column=1)

    ento1 = ttk.Entry(data, width=20, font=('arial', 12, ''))
    ento1.grid(row=1, column=1)

    ento1 = ttk.Entry(data, width=20, font=('arial', 12, ''))
    ento1.grid(row=2, column=1)

    ento11 = ttk.Entry(data, width=20, font=('arial', 12, ''))
    ento11.grid(row=3, column=1)

    seph = ttk.Separator(data, orient='horizontal')
    # sep.pack(side = BOTTOM)e
    seph.grid(row=4, column=0, sticky='n,w,e,s', columnspan=2, ipadx=200, ipady=1, padx=5, pady=5)

    btn = ttk.Button(data, text="OK", style='Wild.TButton', command=add_up)
    btn.grid(row=5, column=0, sticky='E', padx=5, pady=1)

    btn1 = ttk.Button(data, text="Cancel", command=data.destroy)
    btn1.grid(row=5, column=1, sticky='W', padx=5, pady=1)


def sub_all():
    datum = Toplevel(height="300", width="630", relief="flat")
    datum.geometry("540x180-410+280")
    datum.minsize("490", "180")
    datum.maxsize("490", "180")
    datum.title("Edit Data")
    datum.config(background="lavender")

    ent = StringVar()
    ent1 = StringVar()
    ento1 = StringVar()
    ento11 = StringVar()

    lab = ttk.Label(datum, text="Name (Edit this Name): ", font=('', 12, ''), background="lavender")
    lab.grid(row=0, column=0, padx=5, pady=5)

    lab1 = ttk.Label(datum, text="Telephone (Edit this Telephone #): ", font=('', 12, ''), background="lavender")
    lab1.grid(row=1, column=0, padx=5, pady=5)

    lab2 = ttk.Label(datum, text="City (Edit this City name): ", font=('', 12, ''), background="lavender")
    lab2.grid(row=2, column=0, padx=5, pady=5)

    lab3 = ttk.Label(datum, text="Address (Edit this Address): ", font=('', 12, ''), background="lavender")
    lab3.grid(row=3, column=0, padx=5, pady=5)

    ento = StringVar()
    ento1 = StringVar()
    ent1 = StringVar()
    ento11 = StringVar()

    def add_up():
        hala = (ento11.get() + "", ento1.get() + "", ento1.get() + "", ento.get() + "")
        #
        tree.insert('', 'end', values=hala)
        # tree serialization
        with open(fun, "w") as f:
            yaml.dump(hala, f)

    ento = ttk.Entry(datum, width=20, font=('arial', 12, ''))
    ento.grid(row=0, column=1)

    ento1 = ttk.Entry(datum, width=20, font=('arial', 12, ''))
    ento1.grid(row=1, column=1)

    ento1 = ttk.Entry(datum, width=20, font=('arial', 12, ''))
    ento1.grid(row=2, column=1)

    ento11 = ttk.Entry(datum, width=20, font=('arial', 12, ''))
    ento11.grid(row=3, column=1)

    seph = ttk.Separator(datum, orient='horizontal')
    # sep.pack(side = BOTTOM)e
    seph.grid(row=4, column=0, sticky='n,w,e,s', columnspan=2, ipadx=200, ipady=1, padx=5, pady=5)

    btn = ttk.Button(datum, text="OK", style='Wild.TButton', command=add_up)
    btn.grid(row=5, column=0, sticky='E', padx=5, pady=1)

    btn1 = ttk.Button(datum, text="Cancel", command=datum.destroy)
    btn1.grid(row=5, column=1, sticky='W', padx=5, pady=1)


def iexits():
        go = Toplevel(height="400", width="500", relief="flat")
        go.geometry("465x125-450+300")
#        go.minsize("485", "160")
#        go.maxsize("485", "160")
        go.title("Delete")
        go.resizable(0,0)
        go.config(background = "#E4E4E4")
#        go.overrideredirect(True)
        go.attributes("-toolwindow", 1)

        ento = StringVar()
        ento1 = StringVar()
        ent1 = StringVar()
        ento11 = StringVar()

        lb = ttk.Label(go, text="""Are you sure you want to permanetly delete this item?""", font=('Helvetica', 12, 'bold'), background = "#E4E4E4")
        lb.grid(row=0, column=0,  columnspan=2,sticky='w')

        lb = ttk.Label(go, text="""
        Items deleted would not be recovereable.""", font=('Helvetica', 12, ''), background = "#E4E4E4")
        lb.grid(row=1, column=0,  columnspan=3,sticky='w', padx=5, pady=5)

        def del_tree():
            selected_item =tree.selection()[0]
            tree.delete(selected_item)
            lost = (ento11.get() + "", ento1.get() + "", ento1.get() + "", ento.get() + "")
            # tree serialization
            with open(fun, "w") as f:
                yaml.dump(lost, f)
            #tree.insert('', 'end', text="Item", values=0)
            tkMessageBox.showinfo("Delete Item", "You have succesfully deleted the entries.")
            go.destroy()

        bn = ttk.Button(go, text="Cancel", command=go.destroy)
        bn.grid(row=2, column=0, pady=5, ipadx = 90, ipady = 10)

        bn1 = ttk.Button(go, text="Delete", style='Minis.TButton', command=del_tree)
        bn1.grid(row=2, column=1,  pady=5, ipadx = 90, ipady = 10)


#=======================================================================================================================
lbl1 = ttk.Label(w1, text="Configure Entries", font=('DejaVu Sans Mono', 12, 'bold'), background = '#E4E4E4')
lbl1.grid(row=0, column=0, columnspan=2, sticky='W')

#bn = Button(w1, text='More', command=my_data,bg = "#0066CC", fg = "white", activeforeground = "white", activebackground = "#0066CC", overrelief = "flat", relief = "flat",font = ('DejaVu Sans Mono',10, 'bold'), width = 10,)
#bn.grid(row=0, column=0, padx=5, pady=5, )

lbl = ttk.Label(w1, text="""My Contacts would allow storing, editing and deleting of new entries here.""", font=('DejaVu Sans Mono', 11, ''), background = '#E4E4E4')
lbl.grid(row=1, column=0, columnspan = 5,sticky='w')

# We focus on oma to now dump the inputs
# Tree serialization
with open(fun, "r") as f:
    dany= yaml.load(f)


tree = ttk.Treeview(w1, columns=(3,2,1, 0), displaycolumns=(0, 1,2,3), height=2, selectmode='browse',
                     show='headings')
tree.heading('#0', text='Itemo')
tree.heading('#1', text='Name')
tree.heading('#2', text='City')
tree.heading('#3', text='Telephone')
tree.heading('#4', text='Address')
tree.insert('','end', text = "Item", values=dany)
tree.grid(row=2, column=0, ipadx=1, pady=5, sticky='w')
i = 0
b2 = ttk.Button(w1, text='+', command=add_all, style = "Mini.TButton")
b2.grid(row=2, column=1, rowspan = 1,padx=5, pady=5, )
b3 = ttk.Button(w1, text='...', command=sub_all, style = "Mini.TButton")
b3.grid(row=2, column=2,  padx=5, pady=5, )
b4 = ttk.Button(w1, text='-', command=iexits, style = "Minis.TButton")
b4.grid(row=2, column=4, padx=5, pady=5, )

#===================================This is the second file we serialize================================================
def add_all1():
    try:
        data = Toplevel(height="300", width="730", relief="flat")
        data.geometry("540x180-410+280")
        data.minsize("540", "180")
        data.maxsize("540", "180")
        data.title("Add Data")
        data.config(background="lavender")

        ento = StringVar()
        ento1 = StringVar()
        ent1 = StringVar()
        ento11 = StringVar()

        lab = ttk.Label(data, text="Name (Input the new Name): ", font=('', 12, ''), background="lavender")
        lab.grid(row=0, column=0, padx=5, pady=5)

        lab1 = ttk.Label(data, text="Telephone (Input the new Telephone #): ", font=('', 12, ''), background="lavender")
        lab1.grid(row=1, column=0, padx=5, pady=5)

        lab2 = ttk.Label(data, text="City (Input the City name): ", font=('', 12, ''), background="lavender")
        lab2.grid(row=2, column=0, padx=5, pady=5)

        lab3 = ttk.Label(data, text="Address (Input the new Address): ", font=('', 12, ''), background="lavender")
        lab3.grid(row=3, column=0, padx=5, pady=5)



        def add_up():
            # i = 0
            hala1 = (ento11.get() + "", ento1.get() + "", ento1.get() + "", ento.get() + "")
            tree1.insert('', 'end', values=hala1)

            # tree serialization
            with open(hold, "w") as f:
                yaml.dump(hala1, f)

            tkMessageBox.showinfo("Add New Item", "You have succesfully added new entries.")
            # i + 1

        ento = ttk.Entry(data, width=20, font=('arial', 12, ''))
        ento.grid(row=0, column=1)

        ento1 = ttk.Entry(data, width=20, font=('arial', 12, ''))
        ento1.grid(row=1, column=1)

        ento1 = ttk.Entry(data, width=20, font=('arial', 12, ''))
        ento1.grid(row=2, column=1)

        ento11 = ttk.Entry(data, width=20, font=('arial', 12, ''))
        ento11.grid(row=3, column=1)

        seph = ttk.Separator(data, orient='horizontal')
        # sep.pack(side = BOTTOM)e
        seph.grid(row=4, column=0, sticky='n,w,e,s', columnspan=2, ipadx=200, ipady=1, padx=5, pady=5)

        btn = ttk.Button(data, text="OK", style='Wild.TButton', command=add_up)
        btn.grid(row=5, column=0, sticky='E', padx=5, pady=1)

        btn1 = ttk.Button(data, text="Cancel", command=data.destroy)
        btn1.grid(row=5, column=1, sticky='W', padx=5, pady=1)

    except:
        tkMessageBox.showerror("Add New Item", "Add new Item failed. Please check input.")
    finally:
        clear()


def sub_all1():
    try:
        datum = Toplevel(height="200", width="770", relief="flat")
        datum.geometry("540x180-410+280")
        datum.minsize("490", "180")
        datum.maxsize("490", "180")
        datum.title("Edit Data")
        datum.config(background="lavender")

        ento = StringVar()
        ento1 = StringVar()
        ent1 = StringVar()
        ento11 = StringVar()

        lab = ttk.Label(datum, text="Name (Edit this Name): ", font=('', 12, ''), background="lavender")
        lab.grid(row=0, column=0, padx=5, pady=5)

        lab1 = ttk.Label(datum, text="Telephone (Edit this Telephone #): ", font=('', 12, ''), background="lavender")
        lab1.grid(row=1, column=0, padx=5, pady=5)

        lab2 = ttk.Label(datum, text="City (Edit this City name): ", font=('', 12, ''), background="lavender")
        lab2.grid(row=2, column=0, padx=5, pady=5)

        lab3 = ttk.Label(datum, text="Address (Edit this Address): ", font=('', 12, ''), background="lavender")
        lab3.grid(row=3, column=0, padx=5, pady=5)
        ento = StringVar()
        ento1 = StringVar()

        def add_up():
            hala1 = (ento11.get() + "", ento1.get() + "", ento1.get() + "", ento.get() + "")
            tree1.insert('', 'end', values=hala1)

            # tree serialization
            with open(hold, "w") as f:
                yaml.dump(hala1, f)
            tkMessageBox.showinfo("Edit Item", "You have succesfully edited the entries.")
            # i + 1

        ento = ttk.Entry(datum, width=20, font=('arial', 12, ''))
        ento.grid(row=0, column=1)

        ento1 = ttk.Entry(datum, width=20, font=('arial', 12, ''))
        ento1.grid(row=1, column=1)

        ento1 = ttk.Entry(datum, width=20, font=('arial', 12, ''))
        ento1.grid(row=2, column=1)

        ento11 = ttk.Entry(datum, width=20, font=('arial', 12, ''))
        ento11.grid(row=3, column=1)

        seph = ttk.Separator(datum, orient='horizontal')
        # sep.pack(side = BOTTOM)e
        seph.grid(row=4, column=0, sticky='n,w,e,s', columnspan=2, ipadx=200, ipady=1, padx=5, pady=5)

        btn = ttk.Button(datum, text="OK", style='Wild.TButton', command=add_up)
        btn.grid(row=5, column=0, sticky='E', padx=5, pady=1)

        btn1 = ttk.Button(datum, text="Cancel", command=datum.destroy)
        btn1.grid(row=5, column=1, sticky='W', padx=5, pady=1)

    except:
        tkMessageBox.showerror("Add New Item", "Add new Item failed. Please check input.")
    finally:
        clear()

def iexits1():
        go = Toplevel(height="400", width="500", relief="flat")
        go.geometry("465x125-450+300")
#        go.minsize("485", "160")
#        go.maxsize("485", "160")
        go.title("Delete")
        go.resizable(0,0)
        go.config(background = "#E4E4E4")
#        go.overrideredirect(True)
        go.attributes("-toolwindow", 1)

        ento = StringVar()
        ento1 = StringVar()
        ent1 = StringVar()
        ento11 = StringVar()

        lb = ttk.Label(go, text="""Are you sure you want to permanetly delete this item?""", font=('Helvetica', 12, 'bold'), background = "#E4E4E4")
        lb.grid(row=0, column=0,  columnspan=2,sticky='w')

        lb = ttk.Label(go, text="""
        Items deleted would not be recovereable.""", font=('Helvetica', 12, ''), background = "#E4E4E4")
        lb.grid(row=1, column=0,  columnspan=3,sticky='w', padx=5, pady=5)

        def del_tree():
            selected_item =tree1.selection()[0]
            tree1.delete(selected_item)
            lost1 = (ento11.get() + "", ento1.get() + "", ento1.get() + "", ento.get() + "")
            # tree serialization
            with open(hold, "w") as f:
               yaml.dump(lost1, f)
            #tree1.insert('', 'end', text="Item", values=0)
            tkMessageBox.showinfo("Delete Item", "You have succesfully deleted the entries.")
            go.destroy()

        bn = ttk.Button(go, text="Cancel", command=go.destroy)
        bn.grid(row=2, column=0, pady=5, ipadx = 90, ipady = 10)

        bn1 = ttk.Button(go, text="Delete", style='Minis.TButton', command=del_tree)
        bn1.grid(row=2, column=1,  pady=5, ipadx = 90, ipady = 10)


#=======================================================================================================================
# We focus on tripo to now dump the inputs
# Tree serialization
with open(hold, "r") as f:
    dany1= yaml.load(f)
tree1 = ttk.Treeview(w1, columns=(3,2,1, 0), displaycolumns=(0, 1,2,3), height=2, selectmode='browse',
                     show='headings')
tree1.heading('#0', text='Itemo')
tree1.heading('#1', text='Name')
tree1.heading('#2', text='City')
tree1.heading('#3', text='Telephone')
tree1.heading('#4', text='Address')
tree1.insert('','end', text = "Item", values=dany1)
tree1.grid(row=3, column=0, padx=1, pady=5, sticky='w')
i = 0
b5 = ttk.Button(w1, text='+', command=add_all1, style = "Mini.TButton")
b5.grid(row=3, column=1, rowspan = 1,padx=5, pady=5, )
b6 = ttk.Button(w1, text='...', command=sub_all1, style = "Mini.TButton")
b6.grid(row=3, column=2,  padx=5, pady=5, )
b7 = ttk.Button(w1, text='-', command=iexits1, style = "Minis.TButton")
b7.grid(row=3, column=4, padx=5, pady=5, )

#=====================We handle another serialization context here======================================================
def add_all2():
    try:
        data = Toplevel(height="300", width="730", relief="flat")
        data.geometry("540x180-410+280")
        data.minsize("540", "180")
        data.maxsize("540", "180")
        data.title("Add Data")
        data.config(background="lavender")

        ento = StringVar()
        ento1 = StringVar()
        ent1 = StringVar()
        ento11 = StringVar()

        lab = ttk.Label(data, text="Name (Input the new Name): ", font=('', 12, ''), background="lavender")
        lab.grid(row=0, column=0, padx=5, pady=5)

        lab1 = ttk.Label(data, text="Telephone (Input the new Telephone #): ", font=('', 12, ''), background="lavender")
        lab1.grid(row=1, column=0, padx=5, pady=5)

        lab2 = ttk.Label(data, text="City (Input the City name): ", font=('', 12, ''), background="lavender")
        lab2.grid(row=2, column=0, padx=5, pady=5)

        lab3 = ttk.Label(data, text="Address (Input the new Address): ", font=('', 12, ''), background="lavender")
        lab3.grid(row=3, column=0, padx=5, pady=5)

        def add_up():
            # i = 0
            hala2 = (ento11.get() + "", ento1.get() + "", ento1.get() + "", ento.get() + "")
            tree2.insert('', 'end', values=hala2)

            # tree serialization
            with open(fam, "w") as f:
                yaml.dump(hala2, f)

            tkMessageBox.showinfo("Add New Item", "You have succesfully added new entries.")
            # i + 1

        ento = ttk.Entry(data, width=20, font=('arial', 12, ''))
        ento.grid(row=0, column=1)

        ento1 = ttk.Entry(data, width=20, font=('arial', 12, ''))
        ento1.grid(row=1, column=1)

        ento1 = ttk.Entry(data, width=20, font=('arial', 12, ''))
        ento1.grid(row=2, column=1)

        ento11 = ttk.Entry(data, width=20, font=('arial', 12, ''))
        ento11.grid(row=3, column=1)
        seph = ttk.Separator(data, orient='horizontal')
        # sep.pack(side = BOTTOM)e
        seph.grid(row=4, column=0, sticky='n,w,e,s', columnspan=2, ipadx=200, ipady=1, padx=5, pady=5)

        btn = ttk.Button(data, text="OK", style='Wild.TButton', command=add_up)
        btn.grid(row=5, column=0, sticky='E', padx=5, pady=1)

        btn1 = ttk.Button(data, text="Cancel", command=data.destroy)
        btn1.grid(row=5, column=1, sticky='W', padx=5, pady=1)

    except:
        tkMessageBox.showerror("Add New Item", "Add new Item failed. Please check input.")
    finally:
        clear()


def sub_all2():
    try:
        datum = Toplevel(height="200", width="770", relief="flat")
        datum.geometry("540x180-410+280")
        datum.minsize("490", "180")
        datum.maxsize("490", "180")
        datum.title("Edit Data")
        datum.config(background="lavender")

        ento = StringVar()
        ento1 = StringVar()
        ent1 = StringVar()
        ento11 = StringVar()

        lab = ttk.Label(datum, text="Name (Edit this Name): ", font=('', 12, ''), background="lavender")
        lab.grid(row=0, column=0, padx=5, pady=5)

        lab1 = ttk.Label(datum, text="Telephone (Edit this Telephone #): ", font=('', 12, ''), background="lavender")
        lab1.grid(row=1, column=0, padx=5, pady=5)

        lab2 = ttk.Label(datum, text="City (Edit this City name): ", font=('', 12, ''), background="lavender")
        lab2.grid(row=2, column=0, padx=5, pady=5)

        lab3 = ttk.Label(datum, text="Address (Edit this Address): ", font=('', 12, ''), background="lavender")
        lab3.grid(row=3, column=0, padx=5, pady=5)

        ento = StringVar()
        ento1 = StringVar()

        def add_up():
            hala2 = (ento11.get() + "", ento1.get() + "", ento1.get() + "", ento.get() + "")
            tree2.insert('', 'end', values=hala2)

            # tree serialization
            with open(fam, "w") as f:
                yaml.dump(hala2, f)
            tkMessageBox.showinfo("Edit Item", "You have succesfully edited the entries.")
            # i + 1

        ento = ttk.Entry(datum, width=20, font=('arial', 12, ''))
        ento.grid(row=0, column=1)

        ento1 = ttk.Entry(datum, width=20, font=('arial', 12, ''))
        ento1.grid(row=1, column=1)

        ento1 = ttk.Entry(datum, width=20, font=('arial', 12, ''))
        ento1.grid(row=2, column=1)

        ento11 = ttk.Entry(datum, width=20, font=('arial', 12, ''))
        ento11.grid(row=3, column=1)

        seph = ttk.Separator(datum, orient='horizontal')
        # sep.pack(side = BOTTOM)e
        seph.grid(row=4, column=0, sticky='n,w,e,s', columnspan=2, ipadx=200, ipady=1, padx=5, pady=5)

        btn = ttk.Button(datum, text="OK", style='Wild.TButton', command=add_up)
        btn.grid(row=5, column=0, sticky='E', padx=5, pady=1)

        btn1 = ttk.Button(datum, text="Cancel", command=datum.destroy)
        btn1.grid(row=5, column=1, sticky='W', padx=5, pady=1)


    except:
        tkMessageBox.showerror("Add New Item", "Add new Item failed. Please check input.")
    finally:
        clear()

def iexits2():
        go = Toplevel(height="400", width="500", relief="flat")
        go.geometry("465x125-450+300")
#        go.minsize("485", "160")
#        go.maxsize("485", "160")
        go.title("Delete")
        go.resizable(0,0)
        go.config(background = "#E4E4E4")
#        go.overrideredirect(True)
        go.attributes("-toolwindow", 1)

        ento = StringVar()
        ento1 = StringVar()
        ent1 = StringVar()
        ento11 = StringVar()

        lb = ttk.Label(go, text="""Are you sure you want to permanetly delete this item?""", font=('Helvetica', 12, 'bold'), background = "#E4E4E4")
        lb.grid(row=0, column=0,  columnspan=2,sticky='w')

        lb = ttk.Label(go, text="""
        Items deleted would not be recovereable.""", font=('Helvetica', 12, ''), background = "#E4E4E4")
        lb.grid(row=1, column=0,  columnspan=3,sticky='w', padx=5, pady=5)

        def del_tree():
            selected_item =tree2.selection()[0]
            tree2.delete(selected_item)
            lost2 = (ento1.get() + "", ento.get() + "")
            # tree serialization
            with open(fam, "w") as f:
               yaml.dump(lost2, f)
            #tree1.insert('', 'end', text="Item", values=0)
            tkMessageBox.showinfo("Delete Item", "You have succesfully deleted the entries.")
            go.destroy()

        bn = ttk.Button(go, text="Cancel", command=go.destroy)
        bn.grid(row=2, column=0, pady=5, ipadx = 90, ipady = 10)

        bn1 = ttk.Button(go, text="Delete", style='Minis.TButton', command=del_tree)
        bn1.grid(row=2, column=1,  pady=5, ipadx = 90, ipady = 10)

#=======================================================================================================================
# We focus on rollman to now dump the inputs
# Tree serialization
with open(fam, "r") as f:
    dany2= yaml.load(f)

tree2 = ttk.Treeview(w1, columns=(3,2,1, 0), displaycolumns=(0, 1,2,3), height=2, selectmode='browse',
                     show='headings')
tree2.heading('#0', text='Itemo')
tree2.heading('#1', text='Name')
tree2.heading('#2', text='City')
tree2.heading('#3', text='Telephone')
tree2.heading('#4', text='Address')
tree2.insert('','end', text = "Item", values=dany2)
tree2.grid(row=4, column=0, padx=1, pady=5, sticky='w')
i = 0
b8 = ttk.Button(w1, text='+', command=add_all2, style = "Mini.TButton")
b8.grid(row=4, column=1, rowspan = 1,padx=5, pady=5, )
b9 = ttk.Button(w1, text='...', command=sub_all2, style = "Mini.TButton")
b9.grid(row=4, column=2,  padx=5, pady=5, )
b10 = ttk.Button(w1, text='-', command=iexits2, style = "Minis.TButton")
b10.grid(row=4, column=4, padx=5, pady=5, )

#=====================We handle another serialization context here. Its the fourth file=================================
def add_all3():
    try:
        data = Toplevel(height="300", width="730", relief="flat")
        data.geometry("540x180-410+280")
        data.minsize("540", "180")
        data.maxsize("540", "180")
        data.title("Add Data")
        data.config(background="lavender")

        ento = StringVar()
        ento1 = StringVar()
        ent1 = StringVar()
        ento11 = StringVar()

        lab = ttk.Label(data, text="Name (Input the new Name): ", font=('', 12, ''), background="lavender")
        lab.grid(row=0, column=0, padx=5, pady=5)

        lab1 = ttk.Label(data, text="Telephone (Input the new Telephone #): ", font=('', 12, ''), background="lavender")
        lab1.grid(row=1, column=0, padx=5, pady=5)

        lab2 = ttk.Label(data, text="City (Input the City name): ", font=('', 12, ''), background="lavender")
        lab2.grid(row=2, column=0, padx=5, pady=5)

        lab3 = ttk.Label(data, text="Address (Input the new Address): ", font=('', 12, ''), background="lavender")
        lab3.grid(row=3, column=0, padx=5, pady=5)



        def add_up():
            # i = 0
            hala3 = (ento11.get() + "", ento1.get() + "", ento1.get() + "", ento.get() + "")
            tree3.insert('', 'end', values=hala3)

            # tree serialization
            with open(nav, "w") as f:
                yaml.dump(hala3, f)

            tkMessageBox.showinfo("Add New Item", "You have succesfully added new entries.")
            # i + 1

        ento = ttk.Entry(data, width=20, font=('arial', 12, ''))
        ento.grid(row=0, column=1)

        ento1 = ttk.Entry(data, width=20, font=('arial', 12, ''))
        ento1.grid(row=1, column=1)

        ento1 = ttk.Entry(data, width=20, font=('arial', 12, ''))
        ento1.grid(row=2, column=1)

        ento11 = ttk.Entry(data, width=20, font=('arial', 12, ''))
        ento11.grid(row=3, column=1)

        seph = ttk.Separator(data, orient='horizontal')
        # sep.pack(side = BOTTOM)e
        seph.grid(row=4, column=0, sticky='n,w,e,s', columnspan=2, ipadx=200, ipady=1, padx=5, pady=5)

        btn = ttk.Button(data, text="OK", style='Wild.TButton', command=add_up)
        btn.grid(row=5, column=0, sticky='E', padx=5, pady=1)

        btn1 = ttk.Button(data, text="Cancel", command=data.destroy)
        btn1.grid(row=5, column=1, sticky='W', padx=5, pady=1)

    except:
        tkMessageBox.showerror("Add New Item", "Add new Item failed. Please check input.")
    finally:
        clear()


def sub_all3():
    try:
        datum = Toplevel(height="200", width="770", relief="flat")
        datum.geometry("540x180-410+280")
        datum.minsize("490", "180")
        datum.maxsize("490", "180")
        datum.title("Edit Data")
        datum.config(background="lavender")

        ento = StringVar()
        ento1 = StringVar()
        ent1 = StringVar()
        ento11 = StringVar()

        lab = ttk.Label(datum, text="Name (Edit this Name): ", font=('', 12, ''), background="lavender")
        lab.grid(row=0, column=0, padx=5, pady=5)

        lab1 = ttk.Label(datum, text="Telephone (Edit this Telephone #): ", font=('', 12, ''), background="lavender")
        lab1.grid(row=1, column=0, padx=5, pady=5)

        lab2 = ttk.Label(datum, text="City (Edit this City name): ", font=('', 12, ''), background="lavender")
        lab2.grid(row=2, column=0, padx=5, pady=5)

        lab3 = ttk.Label(datum, text="Address (Edit this Address): ", font=('', 12, ''), background="lavender")
        lab3.grid(row=3, column=0, padx=5, pady=5)

        ento = StringVar()
        ento1 = StringVar()

        def add_up():
            hala3 = (ento11.get() + "", ento1.get() + "", ento1.get() + "", ento.get() + "")
            tree3.insert('', 'end', values=hala3)

            # tree serialization
            with open(nav, "w") as f:
                yaml.dump(hala3, f)
            tkMessageBox.showinfo("Edit Item", "You have succesfully edited the entries.")
            # i + 1

        ento = ttk.Entry(datum, width=20, font=('arial', 12, ''))
        ento.grid(row=0, column=1)

        ento1 = ttk.Entry(datum, width=20, font=('arial', 12, ''))
        ento1.grid(row=1, column=1)

        ento1 = ttk.Entry(datum, width=20, font=('arial', 12, ''))
        ento1.grid(row=2, column=1)

        ento11 = ttk.Entry(datum, width=20, font=('arial', 12, ''))
        ento11.grid(row=3, column=1)

        seph = ttk.Separator(datum, orient='horizontal')
        # sep.pack(side = BOTTOM)e
        seph.grid(row=4, column=0, sticky='n,w,e,s', columnspan=2, ipadx=200, ipady=1, padx=5, pady=5)

        btn = ttk.Button(datum, text="OK", style='Wild.TButton', command=add_up)
        btn.grid(row=5, column=0, sticky='E', padx=5, pady=1)

        btn1 = ttk.Button(datum, text="Cancel", command=datum.destroy)
        btn1.grid(row=5, column=1, sticky='W', padx=5, pady=1)
    except:
        tkMessageBox.showerror("Add New Item", "Add new Item failed. Please check input.")
    finally:
        clear()

def iexits3():
        go = Toplevel(height="400", width="500", relief="flat")
        go.geometry("465x125-450+300")
#        go.minsize("485", "160")
#        go.maxsize("485", "160")
        go.title("Delete")
        go.resizable(0,0)
        go.config(background = "#E4E4E4")
#        go.overrideredirect(True)
        go.attributes("-toolwindow", 1)

        ento = StringVar()
        ento1 = StringVar()
        ent1 = StringVar()
        ento11 = StringVar()

        lb = ttk.Label(go, text="""Are you sure you want to permanetly delete this item?""", font=('Helvetica', 12, 'bold'), background = "#E4E4E4")
        lb.grid(row=0, column=0,  columnspan=2,sticky='w')

        lb = ttk.Label(go, text="""
        Items deleted would not be recovereable.""", font=('Helvetica', 12, ''), background = "#E4E4E4")
        lb.grid(row=1, column=0,  columnspan=3,sticky='w', padx=5, pady=5)

        def del_tree():
            selected_item =tree3.selection()[0]
            tree3.delete(selected_item)
            lost3 = (ento11.get() + "", ento1.get() + "", ento1.get() + "", ento.get() + "")
            # tree serialization
            with open(nav, "w") as f:
               yaml.dump(lost3, f)
            #tree1.insert('', 'end', text="Item", values=0)
            tkMessageBox.showinfo("Delete Item", "You have succesfully deleted the entries.")
            go.destroy()

        bn = ttk.Button(go, text="Cancel", command=go.destroy)
        bn.grid(row=2, column=0, pady=5, ipadx = 90, ipady = 10)

        bn1 = ttk.Button(go, text="Delete", style='Minis.TButton', command=del_tree)
        bn1.grid(row=2, column=1,  pady=5, ipadx = 90, ipady = 10)

#=======================================================================================================================
# We focus on rollman to now dump the inputs
# Tree serialization
with open(nav, "r") as f:
    dany3= yaml.load(f)
tree3 = ttk.Treeview(w1, columns=(3,2,1, 0), displaycolumns=(0, 1,2,3), height=2, selectmode='browse',
                     show='headings')
tree3.heading('#0', text='Itemo')
tree3.heading('#1', text='Name')
tree3.heading('#2', text='City')
tree3.heading('#3', text='Telephone')
tree3.heading('#4', text='Address')
tree3.insert('','end', text = "Item", values=dany3)
tree3.grid(row=5, column=0, padx=1, pady=5, sticky='w')
i = 0
b11 = ttk.Button(w1, text='+', command=add_all3, style = "Mini.TButton")
b11.grid(row=5, column=1, rowspan = 1,padx=5, pady=5, )
b12 = ttk.Button(w1, text='...', command=sub_all3, style = "Mini.TButton")
b12.grid(row=5, column=2,  padx=5, pady=5, )
b13 = ttk.Button(w1, text='-', command=iexits3, style = "Minis.TButton")
b13.grid(row=5, column=4, padx=5, pady=5, )

# We handle another tree view serialization=============================================================================
#=====================We handle another serialization context here. Its the fourth file=================================
def add_all4():
    try:
        data = Toplevel(height="300", width="730", relief="flat")
        data.geometry("540x180-410+280")
        data.minsize("540", "180")
        data.maxsize("540", "180")
        data.title("Add Data")
        data.config(background="lavender")

        ento = StringVar()
        ento1 = StringVar()
        ent1 = StringVar()
        ento11 = StringVar()

        lab = ttk.Label(data, text="Name (Input the new Name): ", font=('', 12, ''), background="lavender")
        lab.grid(row=0, column=0, padx=5, pady=5)

        lab1 = ttk.Label(data, text="Telephone (Input the new Telephone #): ", font=('', 12, ''), background="lavender")
        lab1.grid(row=1, column=0, padx=5, pady=5)

        lab2 = ttk.Label(data, text="City (Input the City name): ", font=('', 12, ''), background="lavender")
        lab2.grid(row=2, column=0, padx=5, pady=5)

        lab3 = ttk.Label(data, text="Address (Input the new Address): ", font=('', 12, ''), background="lavender")
        lab3.grid(row=3, column=0, padx=5, pady=5)

        def add_up():
            # i = 0
            hala4 = (ento11.get() + "", ento1.get() + "", ento1.get() + "", ento.get() + "")
            tree4.insert('', 'end', values=hala4)

            # tree serialization
            with open(portsy, "w") as f:
                yaml.dump(hala4, f)

            tkMessageBox.showinfo("Add New Item", "You have succesfully added new entries.")
            # i + 1

        ento = ttk.Entry(data, width=20, font=('arial', 12, ''))
        ento.grid(row=0, column=1)

        ento1 = ttk.Entry(data, width=20, font=('arial', 12, ''))
        ento1.grid(row=1, column=1)

        ento1 = ttk.Entry(data, width=20, font=('arial', 12, ''))
        ento1.grid(row=2, column=1)

        ento11 = ttk.Entry(data, width=20, font=('arial', 12, ''))
        ento11.grid(row=3, column=1)

        seph = ttk.Separator(data, orient='horizontal')
        # sep.pack(side = BOTTOM)e
        seph.grid(row=4, column=0, sticky='n,w,e,s', columnspan=2, ipadx=200, ipady=1, padx=5, pady=5)

        btn = ttk.Button(data, text="OK", style='Wild.TButton', command=add_up)
        btn.grid(row=5, column=0, sticky='E', padx=5, pady=1)

        btn1 = ttk.Button(data, text="Cancel", command=data.destroy)
        btn1.grid(row=5, column=1, sticky='W', padx=5, pady=1)

    except:
        tkMessageBox.showerror("Add New Item", "Add new Item failed. Please check input.")
    finally:
        clear()


def sub_all4():
    try:
        datum = Toplevel(height="200", width="770", relief="flat")
        datum.geometry("540x180-410+280")
        datum.minsize("490", "180")
        datum.maxsize("490", "180")
        datum.title("Edit Data")
        datum.config(background="lavender")

        ento = StringVar()
        ento1 = StringVar()
        ent1 = StringVar()
        ento11 = StringVar()

        lab = ttk.Label(datum, text="Name (Edit this Name): ", font=('', 12, ''), background="lavender")
        lab.grid(row=0, column=0, padx=5, pady=5)

        lab1 = ttk.Label(datum, text="Telephone (Edit this Telephone #): ", font=('', 12, ''), background="lavender")
        lab1.grid(row=1, column=0, padx=5, pady=5)

        lab2 = ttk.Label(datum, text="City (Edit this City name): ", font=('', 12, ''), background="lavender")
        lab2.grid(row=2, column=0, padx=5, pady=5)

        lab3 = ttk.Label(datum, text="Address (Edit this Address): ", font=('', 12, ''), background="lavender")
        lab3.grid(row=3, column=0, padx=5, pady=5)

        ento = StringVar()
        ento1 = StringVar()

        def add_up():
            hala4 = (ento11.get() + "", ento1.get() + "", ento1.get() + "", ento.get() + "")
            tree4.insert('', 'end', values=hala4)

            # tree serialization
            with open(portsy, "w") as f:
                yaml.dump(hala4, f)
            tkMessageBox.showinfo("Edit Item", "You have succesfully edited the entries.")
            # i + 1

        ento = ttk.Entry(datum, width=20, font=('arial', 12, ''))
        ento.grid(row=0, column=1)

        ento1 = ttk.Entry(datum, width=20, font=('arial', 12, ''))
        ento1.grid(row=1, column=1)

        ento1 = ttk.Entry(datum, width=20, font=('arial', 12, ''))
        ento1.grid(row=2, column=1)

        ento11 = ttk.Entry(datum, width=20, font=('arial', 12, ''))
        ento11.grid(row=3, column=1)

        seph = ttk.Separator(datum, orient='horizontal')
        # sep.pack(side = BOTTOM)e
        seph.grid(row=4, column=0, sticky='n,w,e,s', columnspan=2, ipadx=200, ipady=1, padx=5, pady=5)

        btn = ttk.Button(datum, text="OK", style='Wild.TButton', command=add_up)
        btn.grid(row=5, column=0, sticky='E', padx=5, pady=1)

        btn1 = ttk.Button(datum, text="Cancel", command=datum.destroy)
        btn1.grid(row=5, column=1, sticky='W', padx=5, pady=1)


    except:
        tkMessageBox.showerror("Add New Item", "Add new Item failed. Please check input.")
    finally:
        clear()

def iexits4():
        go = Toplevel(height="400", width="500", relief="flat")
        go.geometry("465x125-450+300")
#        go.minsize("485", "160")
#        go.maxsize("485", "160")
        go.title("Delete")
        go.resizable(0,0)
        go.config(background = "#E4E4E4")
#        go.overrideredirect(True)
        go.attributes("-toolwindow", 1)

        ento = StringVar()
        ento1 = StringVar()
        ento1 = StringVar()
        ento11 = StringVar()

        lb = ttk.Label(go, text="""Are you sure you want to permanetly delete this item?""", font=('Helvetica', 12, 'bold'), background = "#E4E4E4")
        lb.grid(row=0, column=0,  columnspan=2,sticky='w')

        lb = ttk.Label(go, text="""
        Items deleted would not be recovereable.""", font=('Helvetica', 12, ''), background = "#E4E4E4")
        lb.grid(row=1, column=0,  columnspan=3,sticky='w', padx=5, pady=5)

        def del_tree():
            selected_item =tree4.selection()[0]
            tree4.delete(selected_item)
            lost4 = (ento11.get() + "", ento1.get() + "", ento1.get() + "", ento.get() + "")
            # tree serialization
            with open(portsy, "w") as f:
               yaml.dump(lost4, f)
            #tree1.insert('', 'end', text="Item", values=0)
            tkMessageBox.showinfo("Delete Item", "You have succesfully deleted the entries.")
            go.destroy()

        bn = ttk.Button(go, text="Cancel", command=go.destroy)
        bn.grid(row=2, column=0, pady=5, ipadx = 90, ipady = 10)

        bn1 = ttk.Button(go, text="Delete", style='Minis.TButton', command=del_tree)
        bn1.grid(row=2, column=1,  pady=5, ipadx = 90, ipady = 10)

#=======================================================================================================================
# We focus on rollman to now dump the inputs
# Tree serialization
with open(portsy, "r") as f:
    dany4= yaml.load(f)

tree4 = ttk.Treeview(w1, columns=(3,2,1, 0), displaycolumns=(0, 1,2,3), height=2, selectmode='browse',
                     show='headings')
tree4.heading('#0', text='Itemo')
tree4.heading('#1', text='Name')
tree4.heading('#2', text='City')
tree4.heading('#3', text='Telephone')
tree4.heading('#4', text='Address')
tree4.insert('','end', text = "Item", values=dany4)
tree4.grid(row=6, column=0, padx=1, pady=5, sticky='w')
i = 0
b14 = ttk.Button(w1, text='+', command=add_all4, style = "Mini.TButton")
b14.grid(row=6, column=1, rowspan = 1,padx=5, pady=5, )
b15 = ttk.Button(w1, text='...', command=sub_all4, style = "Mini.TButton")
b15.grid(row=6, column=2,  padx=5, pady=5, )
b16 = ttk.Button(w1, text='-', command=iexits4, style = "Minis.TButton")
b16.grid(row=6, column=4, padx=5, pady=5, )

# Game on Dawn, we continue with our mashalling in yaml format==========================================================
#=====================We handle another serialization context here. Its the fourth file=================================
def add_all5():
    try:
        data = Toplevel(height="300", width="730", relief="flat")
        data.geometry("540x180-410+280")
        data.minsize("540", "180")
        data.maxsize("540", "180")
        data.title("Add Data")
        data.config(background="lavender")

        ento = StringVar()
        ento1 = StringVar()
        ent1 = StringVar()
        ento11 = StringVar()

        lab = ttk.Label(data, text="Name (Input the new Name): ", font=('', 12, ''), background="lavender")
        lab.grid(row=0, column=0, padx=5, pady=5)

        lab1 = ttk.Label(data, text="Telephone (Input the new Telephone #): ", font=('', 12, ''), background="lavender")
        lab1.grid(row=1, column=0, padx=5, pady=5)

        lab2 = ttk.Label(data, text="City (Input the City name): ", font=('', 12, ''), background="lavender")
        lab2.grid(row=2, column=0, padx=5, pady=5)

        lab3 = ttk.Label(data, text="Address (Input the new Address): ", font=('', 12, ''), background="lavender")
        lab3.grid(row=3, column=0, padx=5, pady=5)



        def add_up():
            # i = 0
            hala5 = (ento11.get() + "", ento1.get() + "", ento1.get() + "", ento.get() + "")
            tree5.insert('', 'end', values=hala5)

            # tree serialization
            with open(olo, "w") as f:
                yaml.dump(hala5, f)

            tkMessageBox.showinfo("Add New Item", "You have succesfully added new entries.")
            # i + 1

        ento = ttk.Entry(data, width=20, font=('arial', 12, ''))
        ento.grid(row=0, column=1)

        ento1 = ttk.Entry(data, width=20, font=('arial', 12, ''))
        ento1.grid(row=1, column=1)

        ento1 = ttk.Entry(data, width=20, font=('arial', 12, ''))
        ento1.grid(row=2, column=1)

        ento11 = ttk.Entry(data, width=20, font=('arial', 12, ''))
        ento11.grid(row=3, column=1)

        seph = ttk.Separator(data, orient='horizontal')
        # sep.pack(side = BOTTOM)e
        seph.grid(row=4, column=0, sticky='n,w,e,s', columnspan=2, ipadx=200, ipady=1, padx=5, pady=5)

        btn = ttk.Button(data, text="OK", style='Wild.TButton', command=add_up)
        btn.grid(row=5, column=0, sticky='E', padx=5, pady=1)

        btn1 = ttk.Button(data, text="Cancel", command=data.destroy)
        btn1.grid(row=5, column=1, sticky='W', padx=5, pady=1)

    except:
        tkMessageBox.showerror("Add New Item", "Add new Item failed. Please check input.")
    finally:
        clear()


def sub_all5():
    try:
        datum = Toplevel(height="200", width="770", relief="flat")
        datum.geometry("540x180-410+280")
        datum.minsize("490", "180")
        datum.maxsize("490", "180")
        datum.title("Edit Data")
        datum.config(background="lavender")

        ento = StringVar()
        ento1 = StringVar()
        ent1 = StringVar()
        ento11 = StringVar()

        lab = ttk.Label(datum, text="Name (Edit this Name): ", font=('', 12, ''), background="lavender")
        lab.grid(row=0, column=0, padx=5, pady=5)

        lab1 = ttk.Label(datum, text="Telephone (Edit this Telephone #): ", font=('', 12, ''), background="lavender")
        lab1.grid(row=1, column=0, padx=5, pady=5)

        lab2 = ttk.Label(datum, text="City (Edit this City name): ", font=('', 12, ''), background="lavender")
        lab2.grid(row=2, column=0, padx=5, pady=5)

        lab3 = ttk.Label(datum, text="Address (Edit this Address): ", font=('', 12, ''), background="lavender")
        lab3.grid(row=3, column=0, padx=5, pady=5)

        def add_up():
            hala5 = (ento11.get() + "", ento1.get() + "", ento1.get() + "", ento.get() + "")
            tree5.insert('', 'end', values=hala5)

            # tree serialization
            with open(olo, "w") as f:
                yaml.dump(hala5, f)
            tkMessageBox.showinfo("Edit Item", "You have succesfully edited the entries.")
            # i + 1

        ento = ttk.Entry(datum, width=20, font=('arial', 12, ''))
        ento.grid(row=0, column=1)

        ento1 = ttk.Entry(datum, width=20, font=('arial', 12, ''))
        ento1.grid(row=1, column=1)

        ento1 = ttk.Entry(datum, width=20, font=('arial', 12, ''))
        ento1.grid(row=2, column=1)

        ento11 = ttk.Entry(datum, width=20, font=('arial', 12, ''))
        ento11.grid(row=3, column=1)

        seph = ttk.Separator(datum, orient='horizontal')
        # sep.pack(side = BOTTOM)e
        seph.grid(row=4, column=0, sticky='n,w,e,s', columnspan=2, ipadx=200, ipady=1, padx=5, pady=5)

        btn = ttk.Button(datum, text="OK", style='Wild.TButton', command=add_up)
        btn.grid(row=5, column=0, sticky='E', padx=5, pady=1)

        btn1 = ttk.Button(datum, text="Cancel", command=datum.destroy)
        btn1.grid(row=5, column=1, sticky='W', padx=5, pady=1)

    except:
        tkMessageBox.showerror("Add New Item", "Add new Item failed. Please check input.")
    finally:
        clear()

def iexits5():
        go = Toplevel(height="400", width="500", relief="flat")
        go.geometry("465x125-450+300")
#        go.minsize("485", "160")
#        go.maxsize("485", "160")
        go.title("Delete")
        go.resizable(0,0)
        go.config(background = "#E4E4E4")
#        go.overrideredirect(True)
        go.attributes("-toolwindow", 1)

        ento = StringVar()
        ento1 = StringVar()
        ento1 = StringVar()
        ento11 = StringVar()

        lb = ttk.Label(go, text="""Are you sure you want to permanetly delete this item?""", font=('Helvetica', 12, 'bold'), background = "#E4E4E4")
        lb.grid(row=0, column=0,  columnspan=2,sticky='w')

        lb = ttk.Label(go, text="""
        Items deleted would not be recovereable.""", font=('Helvetica', 12, ''), background = "#E4E4E4")
        lb.grid(row=1, column=0,  columnspan=3,sticky='w', padx=5, pady=5)

        def del_tree():
            selected_item =tree5.selection()[0]
            tree5.delete(selected_item)
            lost5 = (ento11.get() + "", ento1.get() + "", ento1.get() + "", ento.get() + "")
            # tree serialization
            with open(olo, "w") as f:
               yaml.dump(lost5, f)
            #tree1.insert('', 'end', text="Item", values=0)
            tkMessageBox.showinfo("Delete Item", "You have succesfully deleted the entries.")
            go.destroy()

        bn = ttk.Button(go, text="Cancel", command=go.destroy)
        bn.grid(row=2, column=0, pady=5, ipadx = 90, ipady = 10)

        bn1 = ttk.Button(go, text="Delete", style='Minis.TButton', command=del_tree)
        bn1.grid(row=2, column=1,  pady=5, ipadx = 90, ipady = 10)

#=======================================================================================================================
# We focus on rollman to now dump the inputs
# Tree serialization
with open(olo, "r") as f:
    dany5= yaml.load(f)

tree5 = ttk.Treeview(w1, columns=(3,2,1, 0), displaycolumns=(0, 1,2,3), height=2, selectmode='browse',
                     show='headings')
tree5.heading('#0', text='Itemo')
tree5.heading('#1', text='Name')
tree5.heading('#2', text='City')
tree5.heading('#3', text='Telephone')
tree5.heading('#4', text='Address')
tree5.insert('','end', text = "Item", values=dany5)
tree5.grid(row=7, column=0, padx=1, pady=5, sticky='w')
i = 0
b17 = ttk.Button(w1, text='+', command=add_all5, style = "Mini.TButton")
b17.grid(row=7, column=1, rowspan = 1,padx=5, pady=5, )
b18 = ttk.Button(w1, text='...', command=sub_all5, style = "Mini.TButton")
b18.grid(row=7, column=2,  padx=5, pady=5, )
b19 = ttk.Button(w1, text='-', command=iexits5, style = "Minis.TButton")
b19.grid(row=7, column=4, padx=5, pady=5, )

# We continue our mashalling in .yaml So good I have to say.============================================================
#=====================We handle another serialization context here. Its the fourth file=================================
def add_all6():
    try:
        data = Toplevel(height="300", width="730", relief="flat")
        data.geometry("540x180-410+280")
        data.minsize("540", "180")
        data.maxsize("540", "180")
        data.title("Add Data")
        data.config(background="lavender")

        ento = StringVar()
        ento1 = StringVar()
        ent1 = StringVar()
        ento11 = StringVar()

        lab = ttk.Label(data, text="Name (Input the new Name): ", font=('', 12, ''), background="lavender")
        lab.grid(row=0, column=0, padx=5, pady=5)

        lab1 = ttk.Label(data, text="Telephone (Input the new Telephone #): ", font=('', 12, ''), background="lavender")
        lab1.grid(row=1, column=0, padx=5, pady=5)

        lab2 = ttk.Label(data, text="City (Input the City name): ", font=('', 12, ''), background="lavender")
        lab2.grid(row=2, column=0, padx=5, pady=5)

        lab3 = ttk.Label(data, text="Address (Input the new Address): ", font=('', 12, ''), background="lavender")
        lab3.grid(row=3, column=0, padx=5, pady=5)


        def add_up():
            # i = 0
            hala6 = (ento11.get() + "", ento1.get() + "", ento1.get() + "", ento.get() + "")
            tree6.insert('', 'end', values=hala6)

            # tree serialization
            with open(atkui, "w") as f:
                yaml.dump(hala6, f)

            tkMessageBox.showinfo("Add New Item", "You have succesfully added new entries.")
            # i + 1

        ento = ttk.Entry(data, width=20, font=('arial', 12, ''))
        ento.grid(row=0, column=1)

        ento1 = ttk.Entry(data, width=20, font=('arial', 12, ''))
        ento1.grid(row=1, column=1)

        ento1 = ttk.Entry(data, width=20, font=('arial', 12, ''))
        ento1.grid(row=2, column=1)

        ento11 = ttk.Entry(data, width=20, font=('arial', 12, ''))
        ento11.grid(row=3, column=1)

        seph = ttk.Separator(data, orient='horizontal')
        # sep.pack(side = BOTTOM)e
        seph.grid(row=4, column=0, sticky='n,w,e,s', columnspan=2, ipadx=200, ipady=1, padx=5, pady=5)

        btn = ttk.Button(data, text="OK", style='Wild.TButton', command=add_up)
        btn.grid(row=5, column=0, sticky='E', padx=5, pady=1)

        btn1 = ttk.Button(data, text="Cancel", command=data.destroy)
        btn1.grid(row=5, column=1, sticky='W', padx=5, pady=1)


    except:
        tkMessageBox.showerror("Add New Item", "Add new Item failed. Please check input.")
    finally:
        clear()


def sub_all6():
    try:
        datum = Toplevel(height="200", width="770", relief="flat")
        datum.geometry("540x180-410+280")
        datum.minsize("490", "180")
        datum.maxsize("490", "180")
        datum.title("Edit Data")
        datum.config(background="lavender")

        ento = StringVar()
        ento1 = StringVar()
        ent1 = StringVar()
        ento11 = StringVar()

        lab = ttk.Label(datum, text="Name (Edit this Name): ", font=('', 12, ''), background="lavender")
        lab.grid(row=0, column=0, padx=5, pady=5)

        lab1 = ttk.Label(datum, text="Telephone (Edit this Telephone #): ", font=('', 12, ''), background="lavender")
        lab1.grid(row=1, column=0, padx=5, pady=5)

        lab2 = ttk.Label(datum, text="City (Edit this City name): ", font=('', 12, ''), background="lavender")
        lab2.grid(row=2, column=0, padx=5, pady=5)

        lab3 = ttk.Label(datum, text="Address (Edit this Address): ", font=('', 12, ''), background="lavender")
        lab3.grid(row=3, column=0, padx=5, pady=5)

        ento = StringVar()
        ento1 = StringVar()

        def add_up():
            hala6 = (ento11.get() + "", ento1.get() + "", ento1.get() + "", ento.get() + "")
            tree6.insert('', 'end', values=hala6)

            # tree serialization
            with open(atkui, "w") as f:
                yaml.dump(hala6, f)
            tkMessageBox.showinfo("Edit Item", "You have succesfully edited the entries.")
            # i + 1

        ento = ttk.Entry(datum, width=20, font=('arial', 12, ''))
        ento.grid(row=0, column=1)

        ento1 = ttk.Entry(datum, width=20, font=('arial', 12, ''))
        ento1.grid(row=1, column=1)

        ento1 = ttk.Entry(datum, width=20, font=('arial', 12, ''))
        ento1.grid(row=2, column=1)

        ento11 = ttk.Entry(datum, width=20, font=('arial', 12, ''))
        ento11.grid(row=3, column=1)

        seph = ttk.Separator(datum, orient='horizontal')
        # sep.pack(side = BOTTOM)e
        seph.grid(row=4, column=0, sticky='n,w,e,s', columnspan=2, ipadx=200, ipady=1, padx=5, pady=5)

        btn = ttk.Button(datum, text="OK", style='Wild.TButton', command=add_up)
        btn.grid(row=5, column=0, sticky='E', padx=5, pady=1)

        btn1 = ttk.Button(datum, text="Cancel", command=datum.destroy)
        btn1.grid(row=5, column=1, sticky='W', padx=5, pady=1)


    except:
        tkMessageBox.showerror("Add New Item", "Add new Item failed. Please check input.")
    finally:
        clear()

def iexits6():
        go = Toplevel(height="400", width="500", relief="flat")
        go.geometry("465x125-450+300")
#        go.minsize("485", "160")
#        go.maxsize("485", "160")
        go.title("Delete")
        go.resizable(0,0)
        go.config(background = "#E4E4E4")
#        go.overrideredirect(True)
        go.attributes("-toolwindow", 1)

        ento = StringVar()
        ento1 = StringVar()
        ento1 = StringVar()
        ento11 = StringVar()

        lb = ttk.Label(go, text="""Are you sure you want to permanetly delete this item?""", font=('Helvetica', 12, 'bold'), background = "#E4E4E4")
        lb.grid(row=0, column=0,  columnspan=2,sticky='w')

        lb = ttk.Label(go, text="""
        Items deleted would not be recovereable.""", font=('Helvetica', 12, ''), background = "#E4E4E4")
        lb.grid(row=1, column=0,  columnspan=3,sticky='w', padx=5, pady=5)

        def del_tree():
            selected_item =tree6.selection()[0]
            tree6.delete(selected_item)
            lost6 = (ento11.get() + "", ento1.get() + "", ento1.get() + "", ento.get() + "")
            # tree serialization
            with open(atkui, "w") as f:
               yaml.dump(lost6, f)
            #tree1.insert('', 'end', text="Item", values=0)
            tkMessageBox.showinfo("Delete Item", "You have succesfully deleted the entries.")
            go.destroy()

        bn = ttk.Button(go, text="Cancel", command=go.destroy)
        bn.grid(row=2, column=0, pady=5, ipadx = 90, ipady = 10)

        bn1 = ttk.Button(go, text="Delete", style='Minis.TButton', command=del_tree)
        bn1.grid(row=2, column=1,  pady=5, ipadx = 90, ipady = 10)

#=======================================================================================================================
# We focus on rollman to now dump the inputs
# Tree serialization
with open(atkui, "r") as f:
    dany6= yaml.load(f)
tree6 = ttk.Treeview(w1, columns=(3,2,1, 0), displaycolumns=(0, 1,2,3), height=2, selectmode='browse',
                     show='headings')
tree6.heading('#0', text='Itemo')
tree6.heading('#1', text='Name')
tree6.heading('#2', text='City')
tree6.heading('#3', text='Telephone')
tree6.heading('#4', text='Address')
tree6.insert('','end', text = "Item", values=dany6)
tree6.grid(row=8, column=0, padx=1, pady=5, sticky='w')
i = 0
b20 = ttk.Button(w1, text='+', command=add_all6, style = "Mini.TButton")
b20.grid(row=8, column=1, rowspan = 1,padx=5, pady=5, )
b21 = ttk.Button(w1, text='...', command=sub_all6, style = "Mini.TButton")
b21.grid(row=8, column=2,  padx=5, pady=5, )
b22 = ttk.Button(w1, text='-', command=iexits6, style = "Minis.TButton")
b22.grid(row=8, column=4, padx=5, pady=5, )

#==========Game on Chief.===============================================================================================
#=====================We handle another serialization context here. Its the fourth file=================================
def add_all7():
    try:
        data = Toplevel(height="300", width="730", relief="flat")
        data.geometry("540x180-410+280")
        data.minsize("540", "180")
        data.maxsize("540", "180")
        data.title("Add Data")
        data.config(background="lavender")

        ento = StringVar()
        ento1 = StringVar()
        ent1 = StringVar()
        ento11 = StringVar()

        lab = ttk.Label(data, text="Name (Input the new Name): ", font=('', 12, ''), background="lavender")
        lab.grid(row=0, column=0, padx=5, pady=5)

        lab1 = ttk.Label(data, text="Telephone (Input the new Telephone #): ", font=('', 12, ''), background="lavender")
        lab1.grid(row=1, column=0, padx=5, pady=5)

        lab2 = ttk.Label(data, text="City (Input the City name): ", font=('', 12, ''), background="lavender")
        lab2.grid(row=2, column=0, padx=5, pady=5)

        lab3 = ttk.Label(data, text="Address (Input the new Address): ", font=('', 12, ''), background="lavender")
        lab3.grid(row=3, column=0, padx=5, pady=5)


        def add_up():
            # i = 0
            hala7 = (ento11.get() + "", ento1.get() + "", ento1.get() + "", ento.get() + "")
            tree7.insert('', 'end', values=hala7)

            # tree serialization
            with open(biug, "w") as f:
                yaml.dump(hala7, f)

            tkMessageBox.showinfo("Add New Item", "You have succesfully added new entries.")
            # i + 1

        ento = ttk.Entry(data, width=20, font=('arial', 12, ''))
        ento.grid(row=0, column=1)

        ento1 = ttk.Entry(data, width=20, font=('arial', 12, ''))
        ento1.grid(row=1, column=1)

        ento1 = ttk.Entry(data, width=20, font=('arial', 12, ''))
        ento1.grid(row=2, column=1)

        ento11 = ttk.Entry(data, width=20, font=('arial', 12, ''))
        ento11.grid(row=3, column=1)

        seph = ttk.Separator(data, orient='horizontal')
        # sep.pack(side = BOTTOM)e
        seph.grid(row=4, column=0, sticky='n,w,e,s', columnspan=2, ipadx=200, ipady=1, padx=5, pady=5)

        btn = ttk.Button(data, text="OK", style='Wild.TButton', command=add_up)
        btn.grid(row=5, column=0, sticky='E', padx=5, pady=1)

        btn1 = ttk.Button(data, text="Cancel", command=data.destroy)
        btn1.grid(row=5, column=1, sticky='W', padx=5, pady=1)


    except:
        tkMessageBox.showerror("Add New Item", "Add new Item failed. Please check input.")
    finally:
        clear()


def sub_all7():
    try:
        datum = Toplevel(height="200", width="770", relief="flat")
        datum.geometry("540x180-410+280")
        datum.minsize("490", "180")
        datum.maxsize("490", "180")
        datum.title("Edit Data")
        datum.config(background="lavender")

        ento = StringVar()
        ento1 = StringVar()
        ent1 = StringVar()
        ento11 = StringVar()

        lab = ttk.Label(datum, text="Name (Edit this Name): ", font=('', 12, ''), background="lavender")
        lab.grid(row=0, column=0, padx=5, pady=5)

        lab1 = ttk.Label(datum, text="Telephone (Edit this Telephone #): ", font=('', 12, ''), background="lavender")
        lab1.grid(row=1, column=0, padx=5, pady=5)

        lab2 = ttk.Label(datum, text="City (Edit this City name): ", font=('', 12, ''), background="lavender")
        lab2.grid(row=2, column=0, padx=5, pady=5)

        lab3 = ttk.Label(datum, text="Address (Edit this Address): ", font=('', 12, ''), background="lavender")
        lab3.grid(row=3, column=0, padx=5, pady=5)

        ento = StringVar()
        ento1 = StringVar()

        def add_up():
            hala7 = (ento11.get() + "", ento1.get() + "", ento1.get() + "", ento.get() + "")
            tree7.insert('', 'end', values=hala7)

            # tree serialization
            with open(biug, "w") as f:
                yaml.dump(hala7, f)
            tkMessageBox.showinfo("Edit Item", "You have succesfully edited the entries.")
            # i + 1

        ento = ttk.Entry(datum, width=20, font=('arial', 12, ''))
        ento.grid(row=0, column=1)

        ento1 = ttk.Entry(datum, width=20, font=('arial', 12, ''))
        ento1.grid(row=1, column=1)

        ento1 = ttk.Entry(datum, width=20, font=('arial', 12, ''))
        ento1.grid(row=2, column=1)

        ento11 = ttk.Entry(datum, width=20, font=('arial', 12, ''))
        ento11.grid(row=3, column=1)

        seph = ttk.Separator(datum, orient='horizontal')
        # sep.pack(side = BOTTOM)e
        seph.grid(row=4, column=0, sticky='n,w,e,s', columnspan=2, ipadx=200, ipady=1, padx=5, pady=5)

        btn = ttk.Button(datum, text="OK", style='Wild.TButton', command=add_up)
        btn.grid(row=5, column=0, sticky='E', padx=5, pady=1)

        btn1 = ttk.Button(datum, text="Cancel", command=datum.destroy)
        btn1.grid(row=5, column=1, sticky='W', padx=5, pady=1)
    except:
        tkMessageBox.showerror("Add New Item", "Add new Item failed. Please check input.")
    finally:
        clear()

def iexits7():
        go = Toplevel(height="400", width="500", relief="flat")
        go.geometry("465x125-450+300")
#        go.minsize("485", "160")
#        go.maxsize("485", "160")
        go.title("Delete")
        go.resizable(0,0)
        go.config(background = "#E4E4E4")
#        go.overrideredirect(True)
        go.attributes("-toolwindow", 1)

        ento1 = StringVar()
        ento1 = StringVar()
        ento = StringVar()
        ento11 = StringVar()

        lb = ttk.Label(go, text="""Are you sure you want to permanetly delete this item?""", font=('Helvetica', 12, 'bold'), background = "#E4E4E4")
        lb.grid(row=0, column=0,  columnspan=2,sticky='w')

        lb = ttk.Label(go, text="""
        Items deleted would not be recovereable.""", font=('Helvetica', 12, ''), background = "#E4E4E4")
        lb.grid(row=1, column=0,  columnspan=3,sticky='w', padx=5, pady=5)

        def del_tree():
            selected_item =tree7.selection()[0]
            tree7.delete(selected_item)
            lost7 = (ento11.get() + "", ento1.get() + "", ento1.get() + "", ento.get() + "")
            # tree serialization
            with open(biug, "w") as f:
               yaml.dump(lost7, f)
            #tree1.insert('', 'end', text="Item", values=0)
            tkMessageBox.showinfo("Delete Item", "You have succesfully deleted the entries.")
            go.destroy()

        bn = ttk.Button(go, text="Cancel", command=go.destroy)
        bn.grid(row=2, column=0, pady=5, ipadx = 90, ipady = 10)

        bn1 = ttk.Button(go, text="Delete", style='Minis.TButton', command=del_tree)
        bn1.grid(row=2, column=1,  pady=5, ipadx = 90, ipady = 10)

#=======================================================================================================================
# We focus on rollman to now dump the inputs
# Tree serialization
with open(biug, "r") as f:
    dany7= yaml.load(f)

tree7 = ttk.Treeview(w1, columns=(3,2,1, 0), displaycolumns=(0, 1,2,3), height=2, selectmode='browse',
                     show='headings')
tree7.heading('#0', text='Itemo')
tree7.heading('#1', text='Name')
tree7.heading('#2', text='City')
tree7.heading('#3', text='Telephone')
tree7.heading('#4', text='Address')
tree7.insert('','end', text = "Item", values=dany7)
tree7.grid(row=9, column=0, padx=1, pady=5, sticky='w')
i = 0
b23 = ttk.Button(w1, text='+', command=add_all7, style = "Mini.TButton")
b23.grid(row=9, column=1, rowspan = 1,padx=5, pady=5, )
b24 = ttk.Button(w1, text='...', command=sub_all7, style = "Mini.TButton")
b24.grid(row=9, column=2,  padx=5, pady=5, )
b25 = ttk.Button(w1, text='-', command=iexits7, style = "Minis.TButton")
b25.grid(row=9, column=4, padx=5, pady=5, )

#lb2 = ttk.Label(w1, text="""      Tips: In order to see changes take effect, please restart apllication. Thank you.""", font=('DejaVu Sans Mono', 11, ''), background = '#E4E4E4')
#lb2.grid(row=1, column=6, columnspan = 9,sticky='e')
la = "acc.yaml"
la1 = "kum.yaml"
la2 = "kof.yaml"
la3 = "tak.yaml"
la4 = "nor.yaml"
la5 = "ash.yaml"
la6 = "upe.yaml"
la7 = "upw.yaml"
la8 = "cen.yaml"
la9 = "eas.yaml"

# ====================We continue with an extensive data type instead===================================================
def my_data():
    my_datum = Toplevel()
    my_datum.title("More Entries")
    my_datum.geometry('950x700-290+10')
    my_datum.minsize("950", "680")
    my_datum.maxsize("950", "700")
    my_datum.config(background="#E4E4E4")

    s = ttk.Style()
    s.theme_names()
    ('aqua', 'step', 'clam', 'alt', 'default', 'classic', 'gtk+ style', 'motif', 'plastique', 'CDE', 'windows')
    s.theme_use('clam')

    style = ttk.Style()
    style.configure('Mini.TButton',
                    background='#0066CC',
                    foreground='white',
                    highlightthickness='60',
                    length='2',
                    width='3',
                    font=('DejaVu Sans Mono', 8, 'bold'))
    style.map('Mini.TButton',
              foreground=[('disabled', 'yellow'),
                          ('pressed', 'white'),
                          ('active', 'white')],
              background=[('disabled', '#0066CC'),
                          ('pressed', '!focus', 'green'),
                          ('active', 'blue')],
              highlightcolor=[('focus', 'white'),
                              ('!focus', 'blue')],
              relief=[('pressed', 'flat'),
                      ('!pressed', 'flat')])
    overrelief = [('pressed', 'flat'),
                  ('!pressed', 'flat')]

    style = ttk.Style()
    style.configure('Minis.TButton',
                    background='red',
                    foreground='white',
                    highlightthickness='60',
                    width='3',
                    font=('DejaVu Sans Mono', 8, 'bold'))
    style.map('Minis.TButton',
              foreground=[('disabled', 'yellow'),
                          ('pressed', 'white'),
                          ('active', 'white')],
              background=[('disabled', '#0066CC'),
                          ('pressed', '!focus', 'green'),
                          ('active', '#ff3333')],
              highlightcolor=[('focus', 'grey'),
                              ('!focus', 'blue')],
              relief=[('pressed', 'flat'),
                      ('!pressed', 'flat')])
    overrelief = [('pressed', 'groove'),
                  ('!pressed', 'ridge')]

    ento = StringVar()
    ento1 = StringVar()
    lona = StringVar()
    lon = StringVar()
    selected_item = StringVar()

    fun = "ode.yaml"
    hold = "hose.yaml"
    fam = "pan.yaml"
    nav = "challo.yaml"
    portsy = "sed.yaml"
    olo = "nei.yaml"
    atkui = "bors.yaml"
    biug = "chae.yaml"

    def clear():
        ento.set('')
        ento1.set('')

    def add_all():
        data = Toplevel(height="300", width="730", relief="flat")
        data.geometry("540x180-410+280")
        data.minsize("540", "180")
        data.maxsize("540", "180")
        data.title("Add Data")
        data.config(background="lavender")

        ent = StringVar()
        ent1 = StringVar()
        ento1 = StringVar()
        ento11 = StringVar()

        lab = ttk.Label(data, text="Name (Input the new Name): ", font=('', 12, ''), background="lavender")
        lab.grid(row=0, column=0, padx=5, pady=5)

        lab1 = ttk.Label(data, text="Telephone (Input the new Telephone #): ", font=('', 12, ''), background="lavender")
        lab1.grid(row=1, column=0, padx=5, pady=5)

        lab2 = ttk.Label(data, text="City (Input the City name): ", font=('', 12, ''), background="lavender")
        lab2.grid(row=2, column=0, padx=5, pady=5)

        lab3 = ttk.Label(data, text="Address (Input the new Address): ", font=('', 12, ''), background="lavender")
        lab3.grid(row=3, column=0, padx=5, pady=5)

        ento = StringVar()
        ento1 = StringVar()
        ent1 = StringVar()
        ento11 = StringVar()

        def add_up():
            hala = (ento.get() + "", ento1.get() + "", ent1.get() + "", ento11.get() + "")
            #
            tree.insert('', 'end', values=hala)
            # tree serialization
            with open(la, "w") as f:
                yaml.dump(hala, f)

        ento = ttk.Entry(data, width=20, font=('arial', 12, ''))
        ento.grid(row=0, column=1)

        ento1 = ttk.Entry(data, width=20, font=('arial', 12, ''))
        ento1.grid(row=1, column=1)

        ento1 = ttk.Entry(data, width=20, font=('arial', 12, ''))
        ento1.grid(row=2, column=1)

        ento11 = ttk.Entry(data, width=20, font=('arial', 12, ''))
        ento11.grid(row=3, column=1)

        seph = ttk.Separator(data, orient='horizontal')
        # sep.pack(side = BOTTOM)e
        seph.grid(row=4, column=0, sticky='n,w,e,s', columnspan=2, ipadx=200, ipady=1, padx=5, pady=5)

        btn = ttk.Button(data, text="OK", style='Wild.TButton', command=add_up)
        btn.grid(row=5, column=0, sticky='E', padx=5, pady=1)

        btn1 = ttk.Button(data, text="Cancel", command=data.destroy)
        btn1.grid(row=5, column=1, sticky='W', padx=5, pady=1)

    def sub_all():
        datum = Toplevel(height="300", width="630", relief="flat")
        datum.geometry("540x180-410+280")
        datum.minsize("490", "180")
        datum.maxsize("490", "180")
        datum.title("Edit Data")
        datum.config(background="lavender")

        ent = StringVar()
        ent1 = StringVar()
        ento1 = StringVar()
        ento11 = StringVar()

        lab = ttk.Label(datum, text="Name (Edit this Name): ", font=('', 12, ''), background="lavender")
        lab.grid(row=0, column=0, padx=5, pady=5)

        lab1 = ttk.Label(datum, text="Telephone (Edit this Telephone #): ", font=('', 12, ''), background="lavender")
        lab1.grid(row=1, column=0, padx=5, pady=5)

        lab2 = ttk.Label(datum, text="City (Edit this City name): ", font=('', 12, ''), background="lavender")
        lab2.grid(row=2, column=0, padx=5, pady=5)

        lab3 = ttk.Label(datum, text="Address (Edit this Address): ", font=('', 12, ''), background="lavender")
        lab3.grid(row=3, column=0, padx=5, pady=5)

        ento = StringVar()
        ento1 = StringVar()
        ent1 = StringVar()
        ento11 = StringVar()

        def add_up():
            hala = (ento11.get() + "", ento1.get() + "", ento1.get() + "", ento.get() + "")
            #
            tree.insert('', 'end', values=hala)
            # tree serialization
            with open(la, "w") as f:
                yaml.dump(hala, f)

        ento = ttk.Entry(datum, width=20, font=('arial', 12, ''))
        ento.grid(row=0, column=1)

        ento1 = ttk.Entry(datum, width=20, font=('arial', 12, ''))
        ento1.grid(row=1, column=1)

        ento1 = ttk.Entry(datum, width=20, font=('arial', 12, ''))
        ento1.grid(row=2, column=1)

        ento11 = ttk.Entry(datum, width=20, font=('arial', 12, ''))
        ento11.grid(row=3, column=1)

        seph = ttk.Separator(datum, orient='horizontal')
        # sep.pack(side = BOTTOM)e
        seph.grid(row=4, column=0, sticky='n,w,e,s', columnspan=2, ipadx=200, ipady=1, padx=5, pady=5)

        btn = ttk.Button(datum, text="OK", style='Wild.TButton', command=add_up)
        btn.grid(row=5, column=0, sticky='E', padx=5, pady=1)

        btn1 = ttk.Button(datum, text="Cancel", command=datum.destroy)
        btn1.grid(row=5, column=1, sticky='W', padx=5, pady=1)

    def iexits():
        go = Toplevel(height="400", width="500", relief="flat")
        go.geometry("465x125-450+300")
        #        go.minsize("485", "160")
        #        go.maxsize("485", "160")
        go.title("Delete")
        go.resizable(0, 0)
        go.config(background="#E4E4E4")
        #        go.overrideredirect(True)
        go.attributes("-toolwindow", 1)

        ento = StringVar()
        ento1 = StringVar()
        ento1 = StringVar()
        ento11 = StringVar()

        lb = ttk.Label(go, text="""Are you sure you want to permanetly delete this item?""",
                       font=('Helvetica', 12, 'bold'), background="#E4E4E4")
        lb.grid(row=0, column=0, columnspan=2, sticky='w')

        lb = ttk.Label(go, text="""
            Items deleted would not be recovereable.""", font=('Helvetica', 12, ''), background="#E4E4E4")
        lb.grid(row=1, column=0, columnspan=3, sticky='w', padx=5, pady=5)

        def del_tree():
            selected_item = tree.selection()[0]
            tree.delete(selected_item)
            lost = (ento11.get() + "", ento1.get() + "", ento1.get() + "", ento.get() + "")
            # tree serialization
            with open(la, "w") as f:
                yaml.dump(lost, f)
            # tree.insert('', 'end', text="Item", values=0)
            #tkMessageBox.showinfo("Delete Item", "You have succesfully deleted the entries.")
            go.destroy()

        bn = ttk.Button(go, text="Cancel", command=go.destroy)
        bn.grid(row=2, column=0, pady=5, ipadx=90, ipady=10)

        bn1 = ttk.Button(go, text="Delete", style='Minis.TButton', command=del_tree)
        bn1.grid(row=2, column=1, pady=5, ipadx=90, ipady=10)

    # =======================================================================================================================
    lbl1 = ttk.Label(my_datum, text="Configure Entries", font=('DejaVu Sans Mono', 12, 'bold'), background='#E4E4E4')
    lbl1.grid(row=0, column=0, columnspan=2, sticky='W')

    #bn = Button(my_datum, text='More', command=my_data, bg="#0066CC", fg="white", activeforeground="white",
    #            activebackground="#0066CC", overrelief="flat", relief="flat", font=('DejaVu Sans Mono', 10, 'bold'),
    #            width=10, )
    #bn.grid(row=0, column=0, padx=5, pady=5, )

    lbl = ttk.Label(my_datum, text="""Management System would allow storing, editing and deleting of new entries here.""",
                    font=('DejaVu Sans Mono', 11, ''), background='#E4E4E4')
    lbl.grid(row=1, column=0, columnspan=5, sticky='w')

    # We focus on oma to now dump the inputs
    # Tree serialization
    with open(la, "r") as f:
        dany = yaml.load(f)

    tree = ttk.Treeview(my_datum, columns=(3, 2, 1, 0), displaycolumns=(0, 1, 2, 3), height=2, selectmode='browse',
                        show='headings')
    tree.heading('#0', text='Itemo')
    tree.heading('#1', text='Name')
    tree.heading('#2', text='City')
    tree.heading('#3', text='Telephone')
    tree.heading('#4', text='Address')
    tree.insert('', 'end', text="Item", values=dany)
    tree.grid(row=2, column=0, ipadx=1, pady=5, sticky='w')
    i = 0
    b2 = ttk.Button(my_datum, text='+', command=add_all, style="Mini.TButton")
    b2.grid(row=2, column=1, rowspan=1, padx=5, pady=5, )
    b3 = ttk.Button(my_datum, text='...', command=sub_all, style="Mini.TButton")
    b3.grid(row=2, column=2, padx=5, pady=5, )
    b4 = ttk.Button(my_datum, text='-', command=iexits, style="Minis.TButton")
    b4.grid(row=2, column=4, padx=5, pady=5, )

    # ===================================This is the second file we serialize================================================
    def add_all1():
        try:
            data = Toplevel(height="300", width="730", relief="flat")
            data.geometry("540x180-410+280")
            data.minsize("540", "180")
            data.maxsize("540", "180")
            data.title("Add Data")
            data.config(background="lavender")

            ento = StringVar()
            ento1 = StringVar()
            ent1 = StringVar()
            ento11 = StringVar()

            lab = ttk.Label(data, text="Name (Input the new Name): ", font=('', 12, ''), background="lavender")
            lab.grid(row=0, column=0, padx=5, pady=5)

            lab1 = ttk.Label(data, text="Telephone (Input the new Telephone #): ", font=('', 12, ''),
                             background="lavender")
            lab1.grid(row=1, column=0, padx=5, pady=5)

            lab2 = ttk.Label(data, text="City (Input the City name): ", font=('', 12, ''), background="lavender")
            lab2.grid(row=2, column=0, padx=5, pady=5)

            lab3 = ttk.Label(data, text="Address (Input the new Address): ", font=('', 12, ''), background="lavender")
            lab3.grid(row=3, column=0, padx=5, pady=5)

            def add_up():
                # i = 0
                hala1 = (ento11.get() + "", ento1.get() + "", ento1.get() + "", ento.get() + "")
                tree1.insert('', 'end', values=hala1)

                # tree serialization
                with open(la1, "w") as f:
                    yaml.dump(hala1, f)

                #tkMessageBox.showinfo("Add New Item", "You have succesfully added new entries.")
                # i + 1

            ento = ttk.Entry(data, width=20, font=('arial', 12, ''))
            ento.grid(row=0, column=1)

            ento1 = ttk.Entry(data, width=20, font=('arial', 12, ''))
            ento1.grid(row=1, column=1)

            ento1 = ttk.Entry(data, width=20, font=('arial', 12, ''))
            ento1.grid(row=2, column=1)

            ento11 = ttk.Entry(data, width=20, font=('arial', 12, ''))
            ento11.grid(row=3, column=1)

            seph = ttk.Separator(data, orient='horizontal')
            # sep.pack(side = BOTTOM)e
            seph.grid(row=4, column=0, sticky='n,w,e,s', columnspan=2, ipadx=200, ipady=1, padx=5, pady=5)

            btn = ttk.Button(data, text="OK", style='Wild.TButton', command=add_up)
            btn.grid(row=5, column=0, sticky='E', padx=5, pady=1)

            btn1 = ttk.Button(data, text="Cancel", command=data.destroy)
            btn1.grid(row=5, column=1, sticky='W', padx=5, pady=1)

        except:
            tkMessageBox.showerror("Add New Item", "Add new Item failed. Please check input.")
        finally:
            clear()

    def sub_all1():
        try:
            datum = Toplevel(height="200", width="770", relief="flat")
            datum.geometry("540x180-410+280")
            datum.minsize("490", "180")
            datum.maxsize("490", "180")
            datum.title("Edit Data")
            datum.config(background="lavender")

            ento = StringVar()
            ento1 = StringVar()
            ent1 = StringVar()
            ento11 = StringVar()

            lab = ttk.Label(datum, text="Name (Edit this Name): ", font=('', 12, ''), background="lavender")
            lab.grid(row=0, column=0, padx=5, pady=5)

            lab1 = ttk.Label(datum, text="Telephone (Edit this Telephone #): ", font=('', 12, ''),
                             background="lavender")
            lab1.grid(row=1, column=0, padx=5, pady=5)

            lab2 = ttk.Label(datum, text="City (Edit this City name): ", font=('', 12, ''), background="lavender")
            lab2.grid(row=2, column=0, padx=5, pady=5)

            lab3 = ttk.Label(datum, text="Address (Edit this Address): ", font=('', 12, ''), background="lavender")
            lab3.grid(row=3, column=0, padx=5, pady=5)
            ento = StringVar()
            ento1 = StringVar()

            def add_up():
                hala1 = (ento11.get() + "", ento1.get() + "", ento1.get() + "", ento.get() + "")
                tree1.insert('', 'end', values=hala1)

                # tree serialization
                with open(la1, "w") as f:
                    yaml.dump(hala1, f)
                #tkMessageBox.showinfo("Edit Item", "You have succesfully edited the entries.")
                # i + 1

            ento = ttk.Entry(datum, width=20, font=('arial', 12, ''))
            ento.grid(row=0, column=1)

            ento1 = ttk.Entry(datum, width=20, font=('arial', 12, ''))
            ento1.grid(row=1, column=1)

            ento1 = ttk.Entry(datum, width=20, font=('arial', 12, ''))
            ento1.grid(row=2, column=1)

            ento11 = ttk.Entry(datum, width=20, font=('arial', 12, ''))
            ento11.grid(row=3, column=1)

            seph = ttk.Separator(datum, orient='horizontal')
            # sep.pack(side = BOTTOM)e
            seph.grid(row=4, column=0, sticky='n,w,e,s', columnspan=2, ipadx=200, ipady=1, padx=5, pady=5)

            btn = ttk.Button(datum, text="OK", style='Wild.TButton', command=add_up)
            btn.grid(row=5, column=0, sticky='E', padx=5, pady=1)

            btn1 = ttk.Button(datum, text="Cancel", command=datum.destroy)
            btn1.grid(row=5, column=1, sticky='W', padx=5, pady=1)

        except:
            tkMessageBox.showerror("Add New Item", "Add new Item failed. Please check input.")
        finally:
            clear()

    def iexits1():
        go = Toplevel(height="400", width="500", relief="flat")
        go.geometry("465x125-450+300")
        #        go.minsize("485", "160")
        #        go.maxsize("485", "160")
        go.title("Delete")
        go.resizable(0, 0)
        go.config(background="#E4E4E4")
        #        go.overrideredirect(True)
        go.attributes("-toolwindow", 1)

        ento = StringVar()
        ento1 = StringVar()
        ento1 = StringVar()
        ento11 = StringVar()

        lb = ttk.Label(go, text="""Are you sure you want to permanetly delete this item?""",
                       font=('Helvetica', 12, 'bold'), background="#E4E4E4")
        lb.grid(row=0, column=0, columnspan=2, sticky='w')

        lb = ttk.Label(go, text="""
            Items deleted would not be recovereable.""", font=('Helvetica', 12, ''), background="#E4E4E4")
        lb.grid(row=1, column=0, columnspan=3, sticky='w', padx=5, pady=5)

        def del_tree():
            selected_item = tree1.selection()[0]
            tree1.delete(selected_item)
            lost1 = (ento11.get() + "", ento1.get() + "", ento1.get() + "", ento.get() + "")
            # tree serialization
            with open(la1, "w") as f:
                yaml.dump(lost1, f)
            # tree1.insert('', 'end', text="Item", values=0)
            #tkMessageBox.showinfo("Delete Item", "You have succesfully deleted the entries.")
            go.destroy()

        bn = ttk.Button(go, text="Cancel", command=go.destroy)
        bn.grid(row=2, column=0, pady=5, ipadx=90, ipady=10)

        bn1 = ttk.Button(go, text="Delete", style='Minis.TButton', command=del_tree)
        bn1.grid(row=2, column=1, pady=5, ipadx=90, ipady=10)

    # =======================================================================================================================
    # We focus on tripo to now dump the inputs
    # Tree serialization
    with open(la1, "r") as f:
        dany1 = yaml.load(f)
    tree1 = ttk.Treeview(my_datum, columns=(3, 2, 1, 0), displaycolumns=(0, 1, 2, 3), height=2, selectmode='browse',
                         show='headings')
    tree1.heading('#0', text='Itemo')
    tree1.heading('#1', text='Name')
    tree1.heading('#2', text='City')
    tree1.heading('#3', text='Telephone')
    tree1.heading('#4', text='Address')
    tree1.insert('', 'end', text="Item", values=dany1)
    tree1.grid(row=3, column=0, padx=1, pady=5, sticky='w')
    i = 0
    b5 = ttk.Button(my_datum, text='+', command=add_all1, style="Mini.TButton")
    b5.grid(row=3, column=1, rowspan=1, padx=5, pady=5, )
    b6 = ttk.Button(my_datum, text='...', command=sub_all1, style="Mini.TButton")
    b6.grid(row=3, column=2, padx=5, pady=5, )
    b7 = ttk.Button(my_datum, text='-', command=iexits1, style="Minis.TButton")
    b7.grid(row=3, column=4, padx=5, pady=5, )

    # =====================We handle another serialization context here======================================================
    def add_all2():
        try:
            data = Toplevel(height="300", width="730", relief="flat")
            data.geometry("540x180-410+280")
            data.minsize("540", "180")
            data.maxsize("540", "180")
            data.title("Add Data")
            data.config(background="lavender")

            ento = StringVar()
            ento1 = StringVar()
            ent1 = StringVar()
            ento11 = StringVar()

            lab = ttk.Label(data, text="Name (Input the new Name): ", font=('', 12, ''), background="lavender")
            lab.grid(row=0, column=0, padx=5, pady=5)

            lab1 = ttk.Label(data, text="Telephone (Input the new Telephone #): ", font=('', 12, ''),
                             background="lavender")
            lab1.grid(row=1, column=0, padx=5, pady=5)

            lab2 = ttk.Label(data, text="City (Input the City name): ", font=('', 12, ''), background="lavender")
            lab2.grid(row=2, column=0, padx=5, pady=5)

            lab3 = ttk.Label(data, text="Address (Input the new Address): ", font=('', 12, ''), background="lavender")
            lab3.grid(row=3, column=0, padx=5, pady=5)

            def add_up():
                # i = 0
                hala2 = (ento11.get() + "", ento1.get() + "", ento1.get() + "", ento.get() + "")
                tree2.insert('', 'end', values=hala2)

                # tree serialization
                with open(la2, "w") as f:
                    yaml.dump(hala2, f)

                #tkMessageBox.showinfo("Add New Item", "You have succesfully added new entries.")
                # i + 1

            ento = ttk.Entry(data, width=20, font=('arial', 12, ''))
            ento.grid(row=0, column=1)

            ento1 = ttk.Entry(data, width=20, font=('arial', 12, ''))
            ento1.grid(row=1, column=1)

            ento1 = ttk.Entry(data, width=20, font=('arial', 12, ''))
            ento1.grid(row=2, column=1)

            ento11 = ttk.Entry(data, width=20, font=('arial', 12, ''))
            ento11.grid(row=3, column=1)
            seph = ttk.Separator(data, orient='horizontal')
            # sep.pack(side = BOTTOM)e
            seph.grid(row=4, column=0, sticky='n,w,e,s', columnspan=2, ipadx=200, ipady=1, padx=5, pady=5)

            btn = ttk.Button(data, text="OK", style='Wild.TButton', command=add_up)
            btn.grid(row=5, column=0, sticky='E', padx=5, pady=1)

            btn1 = ttk.Button(data, text="Cancel", command=data.destroy)
            btn1.grid(row=5, column=1, sticky='W', padx=5, pady=1)

        except:
            tkMessageBox.showerror("Add New Item", "Add new Item failed. Please check input.")
        finally:
            clear()

    def sub_all2():
        try:
            datum = Toplevel(height="200", width="770", relief="flat")
            datum.geometry("540x180-410+280")
            datum.minsize("490", "180")
            datum.maxsize("490", "180")
            datum.title("Edit Data")
            datum.config(background="lavender")

            ento = StringVar()
            ento1 = StringVar()
            ent1 = StringVar()
            ento11 = StringVar()

            lab = ttk.Label(datum, text="Name (Edit this Name): ", font=('', 12, ''), background="lavender")
            lab.grid(row=0, column=0, padx=5, pady=5)

            lab1 = ttk.Label(datum, text="Telephone (Edit this Telephone #): ", font=('', 12, ''),
                             background="lavender")
            lab1.grid(row=1, column=0, padx=5, pady=5)

            lab2 = ttk.Label(datum, text="City (Edit this City name): ", font=('', 12, ''), background="lavender")
            lab2.grid(row=2, column=0, padx=5, pady=5)

            lab3 = ttk.Label(datum, text="Address (Edit this Address): ", font=('', 12, ''), background="lavender")
            lab3.grid(row=3, column=0, padx=5, pady=5)

            ento = StringVar()
            ento1 = StringVar()

            def add_up():
                hala2 = (ento11.get() + "", ento1.get() + "", ento1.get() + "", ento.get() + "")
                tree2.insert('', 'end', values=hala2)

                # tree serialization
                with open(la2, "w") as f:
                    yaml.dump(hala2, f)
                #tkMessageBox.showinfo("Edit Item", "You have succesfully edited the entries.")
                # i + 1

            ento = ttk.Entry(datum, width=20, font=('arial', 12, ''))
            ento.grid(row=0, column=1)

            ento1 = ttk.Entry(datum, width=20, font=('arial', 12, ''))
            ento1.grid(row=1, column=1)

            ento1 = ttk.Entry(datum, width=20, font=('arial', 12, ''))
            ento1.grid(row=2, column=1)

            ento11 = ttk.Entry(datum, width=20, font=('arial', 12, ''))
            ento11.grid(row=3, column=1)

            seph = ttk.Separator(datum, orient='horizontal')
            # sep.pack(side = BOTTOM)e
            seph.grid(row=4, column=0, sticky='n,w,e,s', columnspan=2, ipadx=200, ipady=1, padx=5, pady=5)

            btn = ttk.Button(datum, text="OK", style='Wild.TButton', command=add_up)
            btn.grid(row=5, column=0, sticky='E', padx=5, pady=1)

            btn1 = ttk.Button(datum, text="Cancel", command=datum.destroy)
            btn1.grid(row=5, column=1, sticky='W', padx=5, pady=1)


        except:
            tkMessageBox.showerror("Add New Item", "Add new Item failed. Please check input.")
        finally:
            clear()

    def iexits2():
        go = Toplevel(height="400", width="500", relief="flat")
        go.geometry("465x125-450+300")
        #        go.minsize("485", "160")
        #        go.maxsize("485", "160")
        go.title("Delete")
        go.resizable(0, 0)
        go.config(background="#E4E4E4")
        #        go.overrideredirect(True)
        go.attributes("-toolwindow", 1)

        ento = StringVar()
        ento1 = StringVar()
        ent1 = StringVar()
        ento11 = StringVar()

        lb = ttk.Label(go, text="""Are you sure you want to permanetly delete this item?""",
                       font=('Helvetica', 12, 'bold'), background="#E4E4E4")
        lb.grid(row=0, column=0, columnspan=2, sticky='w')

        lb = ttk.Label(go, text="""
            Items deleted would not be recovereable.""", font=('Helvetica', 12, ''), background="#E4E4E4")
        lb.grid(row=1, column=0, columnspan=3, sticky='w', padx=5, pady=5)

        def del_tree():
            selected_item = tree2.selection()[0]
            tree2.delete(selected_item)
            lost2 = (ento1.get() + "", ento.get() + "")
            # tree serialization
            with open(la2, "w") as f:
                yaml.dump(lost2, f)
            # tree1.insert('', 'end', text="Item", values=0)
            #tkMessageBox.showinfo("Delete Item", "You have succesfully deleted the entries.")
            go.destroy()

        bn = ttk.Button(go, text="Cancel", command=go.destroy)
        bn.grid(row=2, column=0, pady=5, ipadx=90, ipady=10)

        bn1 = ttk.Button(go, text="Delete", style='Minis.TButton', command=del_tree)
        bn1.grid(row=2, column=1, pady=5, ipadx=90, ipady=10)

    # =======================================================================================================================
    # We focus on rollman to now dump the inputs
    # Tree serialization
    with open(fam, "r") as f:
        dany2 = yaml.load(f)

    tree2 = ttk.Treeview(my_datum, columns=(3, 2, 1, 0), displaycolumns=(0, 1, 2, 3), height=2, selectmode='browse',
                         show='headings')
    tree2.heading('#0', text='Itemo')
    tree2.heading('#1', text='Name')
    tree2.heading('#2', text='City')
    tree2.heading('#3', text='Telephone')
    tree2.heading('#4', text='Address')
    tree2.insert('', 'end', text="Item", values=dany2)
    tree2.grid(row=4, column=0, padx=1, pady=5, sticky='w')
    i = 0
    b8 = ttk.Button(my_datum, text='+', command=add_all2, style="Mini.TButton")
    b8.grid(row=4, column=1, rowspan=1, padx=5, pady=5, )
    b9 = ttk.Button(my_datum, text='...', command=sub_all2, style="Mini.TButton")
    b9.grid(row=4, column=2, padx=5, pady=5, )
    b10 = ttk.Button(my_datum, text='-', command=iexits2, style="Minis.TButton")
    b10.grid(row=4, column=4, padx=5, pady=5, )

    # =====================We handle another serialization context here. Its the fourth file=================================
    def add_all3():
        try:
            data = Toplevel(height="300", width="730", relief="flat")
            data.geometry("540x180-410+280")
            data.minsize("540", "180")
            data.maxsize("540", "180")
            data.title("Add Data")
            data.config(background="lavender")

            ento = StringVar()
            ento1 = StringVar()
            ent1 = StringVar()
            ento11 = StringVar()

            lab = ttk.Label(data, text="Name (Input the new Name): ", font=('', 12, ''), background="lavender")
            lab.grid(row=0, column=0, padx=5, pady=5)

            lab1 = ttk.Label(data, text="Telephone (Input the new Telephone #): ", font=('', 12, ''),
                             background="lavender")
            lab1.grid(row=1, column=0, padx=5, pady=5)

            lab2 = ttk.Label(data, text="City (Input the City name): ", font=('', 12, ''), background="lavender")
            lab2.grid(row=2, column=0, padx=5, pady=5)

            lab3 = ttk.Label(data, text="Address (Input the new Address): ", font=('', 12, ''), background="lavender")
            lab3.grid(row=3, column=0, padx=5, pady=5)

            def add_up():
                # i = 0
                hala3 = (ento11.get() + "", ento1.get() + "", ento1.get() + "", ento.get() + "")
                tree3.insert('', 'end', values=hala3)

                # tree serialization
                with open(la3, "w") as f:
                    yaml.dump(hala3, f)

                #tkMessageBox.showinfo("Add New Item", "You have succesfully added new entries.")
                # i + 1

            ento = ttk.Entry(data, width=20, font=('arial', 12, ''))
            ento.grid(row=0, column=1)

            ento1 = ttk.Entry(data, width=20, font=('arial', 12, ''))
            ento1.grid(row=1, column=1)

            ento1 = ttk.Entry(data, width=20, font=('arial', 12, ''))
            ento1.grid(row=2, column=1)

            ento11 = ttk.Entry(data, width=20, font=('arial', 12, ''))
            ento11.grid(row=3, column=1)

            seph = ttk.Separator(data, orient='horizontal')
            # sep.pack(side = BOTTOM)e
            seph.grid(row=4, column=0, sticky='n,w,e,s', columnspan=2, ipadx=200, ipady=1, padx=5, pady=5)

            btn = ttk.Button(data, text="OK", style='Wild.TButton', command=add_up)
            btn.grid(row=5, column=0, sticky='E', padx=5, pady=1)

            btn1 = ttk.Button(data, text="Cancel", command=data.destroy)
            btn1.grid(row=5, column=1, sticky='W', padx=5, pady=1)

        except:
            tkMessageBox.showerror("Add New Item", "Add new Item failed. Please check input.")
        finally:
            clear()

    def sub_all3():
        try:
            datum = Toplevel(height="200", width="770", relief="flat")
            datum.geometry("540x180-410+280")
            datum.minsize("490", "180")
            datum.maxsize("490", "180")
            datum.title("Edit Data")
            datum.config(background="lavender")

            ento = StringVar()
            ento1 = StringVar()
            ent1 = StringVar()
            ento11 = StringVar()

            lab = ttk.Label(datum, text="Name (Edit this Name): ", font=('', 12, ''), background="lavender")
            lab.grid(row=0, column=0, padx=5, pady=5)

            lab1 = ttk.Label(datum, text="Telephone (Edit this Telephone #): ", font=('', 12, ''),
                             background="lavender")
            lab1.grid(row=1, column=0, padx=5, pady=5)

            lab2 = ttk.Label(datum, text="City (Edit this City name): ", font=('', 12, ''), background="lavender")
            lab2.grid(row=2, column=0, padx=5, pady=5)

            lab3 = ttk.Label(datum, text="Address (Edit this Address): ", font=('', 12, ''), background="lavender")
            lab3.grid(row=3, column=0, padx=5, pady=5)

            ento = StringVar()
            ento1 = StringVar()

            def add_up():
                hala3 = (ento11.get() + "", ento1.get() + "", ento1.get() + "", ento.get() + "")
                tree3.insert('', 'end', values=hala3)

                # tree serialization
                with open(la3, "w") as f:
                    yaml.dump(hala3, f)
                #tkMessageBox.showinfo("Edit Item", "You have succesfully edited the entries.")
                # i + 1

            ento = ttk.Entry(datum, width=20, font=('arial', 12, ''))
            ento.grid(row=0, column=1)

            ento1 = ttk.Entry(datum, width=20, font=('arial', 12, ''))
            ento1.grid(row=1, column=1)

            ento1 = ttk.Entry(datum, width=20, font=('arial', 12, ''))
            ento1.grid(row=2, column=1)

            ento11 = ttk.Entry(datum, width=20, font=('arial', 12, ''))
            ento11.grid(row=3, column=1)

            seph = ttk.Separator(datum, orient='horizontal')
            # sep.pack(side = BOTTOM)e
            seph.grid(row=4, column=0, sticky='n,w,e,s', columnspan=2, ipadx=200, ipady=1, padx=5, pady=5)

            btn = ttk.Button(datum, text="OK", style='Wild.TButton', command=add_up)
            btn.grid(row=5, column=0, sticky='E', padx=5, pady=1)

            btn1 = ttk.Button(datum, text="Cancel", command=datum.destroy)
            btn1.grid(row=5, column=1, sticky='W', padx=5, pady=1)
        except:
            tkMessageBox.showerror("Add New Item", "Add new Item failed. Please check input.")
        finally:
            clear()

    def iexits3():
        go = Toplevel(height="400", width="500", relief="flat")
        go.geometry("465x125-450+300")
        #        go.minsize("485", "160")
        #        go.maxsize("485", "160")
        go.title("Delete")
        go.resizable(0, 0)
        go.config(background="#E4E4E4")
        #        go.overrideredirect(True)
        go.attributes("-toolwindow", 1)

        ento = StringVar()
        ento1 = StringVar()
        ento1 = StringVar()
        ento11 = StringVar()

        lb = ttk.Label(go, text="""Are you sure you want to permanetly delete this item?""",
                       font=('Helvetica', 12, 'bold'), background="#E4E4E4")
        lb.grid(row=0, column=0, columnspan=2, sticky='w')

        lb = ttk.Label(go, text="""
            Items deleted would not be recovereable.""", font=('Helvetica', 12, ''), background="#E4E4E4")
        lb.grid(row=1, column=0, columnspan=3, sticky='w', padx=5, pady=5)

        def del_tree():
            selected_item = tree3.selection()[0]
            tree3.delete(selected_item)
            lost3 = (ento11.get() + "", ento1.get() + "", ento1.get() + "", ento.get() + "")
            # tree serialization
            with open(la3, "w") as f:
                yaml.dump(lost3, f)
            # tree1.insert('', 'end', text="Item", values=0)
            #tkMessageBox.showinfo("Delete Item", "You have succesfully deleted the entries.")
            go.destroy()

        bn = ttk.Button(go, text="Cancel", command=go.destroy)
        bn.grid(row=2, column=0, pady=5, ipadx=90, ipady=10)

        bn1 = ttk.Button(go, text="Delete", style='Minis.TButton', command=del_tree)
        bn1.grid(row=2, column=1, pady=5, ipadx=90, ipady=10)

    # =======================================================================================================================
    # We focus on rollman to now dump the inputs
    # Tree serialization
    with open(la3, "r") as f:
        dany3 = yaml.load(f)
    tree3 = ttk.Treeview(my_datum, columns=(3, 2, 1, 0), displaycolumns=(0, 1, 2, 3), height=2, selectmode='browse',
                         show='headings')
    tree3.heading('#0', text='Itemo')
    tree3.heading('#1', text='Name')
    tree3.heading('#2', text='City')
    tree3.heading('#3', text='Telephone')
    tree3.heading('#4', text='Address')
    tree3.insert('', 'end', text="Item", values=dany3)
    tree3.grid(row=5, column=0, padx=1, pady=5, sticky='w')
    i = 0
    b11 = ttk.Button(my_datum, text='+', command=add_all3, style="Mini.TButton")
    b11.grid(row=5, column=1, rowspan=1, padx=5, pady=5, )
    b12 = ttk.Button(my_datum, text='...', command=sub_all3, style="Mini.TButton")
    b12.grid(row=5, column=2, padx=5, pady=5, )
    b13 = ttk.Button(my_datum, text='-', command=iexits3, style="Minis.TButton")
    b13.grid(row=5, column=4, padx=5, pady=5, )

    # We handle another tree view serialization=============================================================================
    # =====================We handle another serialization context here. Its the fourth file=================================
    def add_all4():
        try:
            data = Toplevel(height="300", width="730", relief="flat")
            data.geometry("540x180-410+280")
            data.minsize("540", "180")
            data.maxsize("540", "180")
            data.title("Add Data")
            data.config(background="lavender")

            ento = StringVar()
            ento1 = StringVar()
            ent1 = StringVar()
            ento11 = StringVar()

            lab = ttk.Label(data, text="Name (Input the new Name): ", font=('', 12, ''), background="lavender")
            lab.grid(row=0, column=0, padx=5, pady=5)

            lab1 = ttk.Label(data, text="Telephone (Input the new Telephone #): ", font=('', 12, ''),
                             background="lavender")
            lab1.grid(row=1, column=0, padx=5, pady=5)

            lab2 = ttk.Label(data, text="City (Input the City name): ", font=('', 12, ''), background="lavender")
            lab2.grid(row=2, column=0, padx=5, pady=5)

            lab3 = ttk.Label(data, text="Address (Input the new Address): ", font=('', 12, ''), background="lavender")
            lab3.grid(row=3, column=0, padx=5, pady=5)

            def add_up():
                # i = 0
                hala4 = (ento11.get() + "", ento1.get() + "", ento1.get() + "", ento.get() + "")
                tree4.insert('', 'end', values=hala4)

                # tree serialization
                with open(la4, "w") as f:
                    yaml.dump(hala4, f)

                #tkMessageBox.showinfo("Add New Item", "You have succesfully added new entries.")
                # i + 1

            ento = ttk.Entry(data, width=20, font=('arial', 12, ''))
            ento.grid(row=0, column=1)

            ento1 = ttk.Entry(data, width=20, font=('arial', 12, ''))
            ento1.grid(row=1, column=1)

            ento1 = ttk.Entry(data, width=20, font=('arial', 12, ''))
            ento1.grid(row=2, column=1)

            ento11 = ttk.Entry(data, width=20, font=('arial', 12, ''))
            ento11.grid(row=3, column=1)

            seph = ttk.Separator(data, orient='horizontal')
            # sep.pack(side = BOTTOM)e
            seph.grid(row=4, column=0, sticky='n,w,e,s', columnspan=2, ipadx=200, ipady=1, padx=5, pady=5)

            btn = ttk.Button(data, text="OK", style='Wild.TButton', command=add_up)
            btn.grid(row=5, column=0, sticky='E', padx=5, pady=1)

            btn1 = ttk.Button(data, text="Cancel", command=data.destroy)
            btn1.grid(row=5, column=1, sticky='W', padx=5, pady=1)

        except:
            tkMessageBox.showerror("Add New Item", "Add new Item failed. Please check input.")
        finally:
            clear()

    def sub_all4():
        try:
            datum = Toplevel(height="200", width="770", relief="flat")
            datum.geometry("540x180-410+280")
            datum.minsize("490", "180")
            datum.maxsize("490", "180")
            datum.title("Edit Data")
            datum.config(background="lavender")

            ento = StringVar()
            ento1 = StringVar()
            ent1 = StringVar()
            ento11 = StringVar()

            lab = ttk.Label(datum, text="Name (Edit this Name): ", font=('', 12, ''), background="lavender")
            lab.grid(row=0, column=0, padx=5, pady=5)

            lab1 = ttk.Label(datum, text="Telephone (Edit this Telephone #): ", font=('', 12, ''),
                             background="lavender")
            lab1.grid(row=1, column=0, padx=5, pady=5)

            lab2 = ttk.Label(datum, text="City (Edit this City name): ", font=('', 12, ''), background="lavender")
            lab2.grid(row=2, column=0, padx=5, pady=5)

            lab3 = ttk.Label(datum, text="Address (Edit this Address): ", font=('', 12, ''), background="lavender")
            lab3.grid(row=3, column=0, padx=5, pady=5)

            ento = StringVar()
            ento1 = StringVar()

            def add_up():
                hala4 = (ento11.get() + "", ento1.get() + "", ento1.get() + "", ento.get() + "")
                tree4.insert('', 'end', values=hala4)

                # tree serialization
                with open(la4, "w") as f:
                    yaml.dump(hala4, f)
                #tkMessageBox.showinfo("Edit Item", "You have succesfully edited the entries.")
                # i + 1

            ento = ttk.Entry(datum, width=20, font=('arial', 12, ''))
            ento.grid(row=0, column=1)

            ento1 = ttk.Entry(datum, width=20, font=('arial', 12, ''))
            ento1.grid(row=1, column=1)

            ento1 = ttk.Entry(datum, width=20, font=('arial', 12, ''))
            ento1.grid(row=2, column=1)

            ento11 = ttk.Entry(datum, width=20, font=('arial', 12, ''))
            ento11.grid(row=3, column=1)

            seph = ttk.Separator(datum, orient='horizontal')
            # sep.pack(side = BOTTOM)e
            seph.grid(row=4, column=0, sticky='n,w,e,s', columnspan=2, ipadx=200, ipady=1, padx=5, pady=5)

            btn = ttk.Button(datum, text="OK", style='Wild.TButton', command=add_up)
            btn.grid(row=5, column=0, sticky='E', padx=5, pady=1)

            btn1 = ttk.Button(datum, text="Cancel", command=datum.destroy)
            btn1.grid(row=5, column=1, sticky='W', padx=5, pady=1)


        except:
            tkMessageBox.showerror("Add New Item", "Add new Item failed. Please check input.")
        finally:
            clear()

    def iexits4():
        go = Toplevel(height="400", width="500", relief="flat")
        go.geometry("465x125-450+300")
        #        go.minsize("485", "160")
        #        go.maxsize("485", "160")
        go.title("Delete")
        go.resizable(0, 0)
        go.config(background="#E4E4E4")
        #        go.overrideredirect(True)
        go.attributes("-toolwindow", 1)

        ento = StringVar()
        ento1 = StringVar()
        ento1 = StringVar()
        ento11 = StringVar()

        lb = ttk.Label(go, text="""Are you sure you want to permanetly delete this item?""",
                       font=('Helvetica', 12, 'bold'), background="#E4E4E4")
        lb.grid(row=0, column=0, columnspan=2, sticky='w')

        lb = ttk.Label(go, text="""
            Items deleted would not be recovereable.""", font=('Helvetica', 12, ''), background="#E4E4E4")
        lb.grid(row=1, column=0, columnspan=3, sticky='w', padx=5, pady=5)

        def del_tree():
            selected_item = tree4.selection()[0]
            tree4.delete(selected_item)
            lost4 = (ento11.get() + "", ento1.get() + "", ento1.get() + "", ento.get() + "")
            # tree serialization
            with open(la4, "w") as f:
                yaml.dump(lost4, f)
            # tree1.insert('', 'end', text="Item", values=0)
            #tkMessageBox.showinfo("Delete Item", "You have succesfully deleted the entries.")
            go.destroy()

        bn = ttk.Button(go, text="Cancel", command=go.destroy)
        bn.grid(row=2, column=0, pady=5, ipadx=90, ipady=10)

        bn1 = ttk.Button(go, text="Delete", style='Minis.TButton', command=del_tree)
        bn1.grid(row=2, column=1, pady=5, ipadx=90, ipady=10)

    # =======================================================================================================================
    # We focus on rollman to now dump the inputs
    # Tree serialization
    with open(la4, "r") as f:
        dany4 = yaml.load(f)

    tree4 = ttk.Treeview(my_datum, columns=(3, 2, 1, 0), displaycolumns=(0, 1, 2, 3), height=2, selectmode='browse',
                         show='headings')
    tree4.heading('#0', text='Itemo')
    tree4.heading('#1', text='Name')
    tree4.heading('#2', text='City')
    tree4.heading('#3', text='Telephone')
    tree4.heading('#4', text='Address')
    tree4.insert('', 'end', text="Item", values=dany4)
    tree4.grid(row=6, column=0, padx=1, pady=5, sticky='w')
    i = 0
    b14 = ttk.Button(my_datum, text='+', command=add_all4, style="Mini.TButton")
    b14.grid(row=6, column=1, rowspan=1, padx=5, pady=5, )
    b15 = ttk.Button(my_datum, text='...', command=sub_all4, style="Mini.TButton")
    b15.grid(row=6, column=2, padx=5, pady=5, )
    b16 = ttk.Button(my_datum, text='-', command=iexits4, style="Minis.TButton")
    b16.grid(row=6, column=4, padx=5, pady=5, )

    # Game on Dawn, we continue with our mashalling in yaml format==========================================================
    # =====================We handle another serialization context here. Its the fourth file=================================
    def add_all5():
        try:
            data = Toplevel(height="300", width="730", relief="flat")
            data.geometry("540x180-410+280")
            data.minsize("540", "180")
            data.maxsize("540", "180")
            data.title("Add Data")
            data.config(background="lavender")

            ento = StringVar()
            ento1 = StringVar()
            ent1 = StringVar()
            ento11 = StringVar()

            lab = ttk.Label(data, text="Name (Input the new Name): ", font=('', 12, ''), background="lavender")
            lab.grid(row=0, column=0, padx=5, pady=5)

            lab1 = ttk.Label(data, text="Telephone (Input the new Telephone #): ", font=('', 12, ''),
                             background="lavender")
            lab1.grid(row=1, column=0, padx=5, pady=5)

            lab2 = ttk.Label(data, text="City (Input the City name): ", font=('', 12, ''), background="lavender")
            lab2.grid(row=2, column=0, padx=5, pady=5)

            lab3 = ttk.Label(data, text="Address (Input the new Address): ", font=('', 12, ''), background="lavender")
            lab3.grid(row=3, column=0, padx=5, pady=5)

            def add_up():
                # i = 0
                hala5 = (ento11.get() + "", ento1.get() + "", ento1.get() + "", ento.get() + "")
                tree5.insert('', 'end', values=hala5)

                # tree serialization
                with open(la5, "w") as f:
                    yaml.dump(hala5, f)

                #tkMessageBox.showinfo("Add New Item", "You have succesfully added new entries.")
                # i + 1

            ento = ttk.Entry(data, width=20, font=('arial', 12, ''))
            ento.grid(row=0, column=1)

            ento1 = ttk.Entry(data, width=20, font=('arial', 12, ''))
            ento1.grid(row=1, column=1)

            ento1 = ttk.Entry(data, width=20, font=('arial', 12, ''))
            ento1.grid(row=2, column=1)

            ento11 = ttk.Entry(data, width=20, font=('arial', 12, ''))
            ento11.grid(row=3, column=1)

            seph = ttk.Separator(data, orient='horizontal')
            # sep.pack(side = BOTTOM)e
            seph.grid(row=4, column=0, sticky='n,w,e,s', columnspan=2, ipadx=200, ipady=1, padx=5, pady=5)

            btn = ttk.Button(data, text="OK", style='Wild.TButton', command=add_up)
            btn.grid(row=5, column=0, sticky='E', padx=5, pady=1)

            btn1 = ttk.Button(data, text="Cancel", command=data.destroy)
            btn1.grid(row=5, column=1, sticky='W', padx=5, pady=1)

        except:
            tkMessageBox.showerror("Add New Item", "Add new Item failed. Please check input.")
        finally:
            clear()

    def sub_all5():
        try:
            datum = Toplevel(height="200", width="770", relief="flat")
            datum.geometry("540x180-410+280")
            datum.minsize("490", "180")
            datum.maxsize("490", "180")
            datum.title("Edit Data")
            datum.config(background="lavender")

            ento = StringVar()
            ento1 = StringVar()
            ent1 = StringVar()
            ento11 = StringVar()

            lab = ttk.Label(datum, text="Name (Edit this Name): ", font=('', 12, ''), background="lavender")
            lab.grid(row=0, column=0, padx=5, pady=5)

            lab1 = ttk.Label(datum, text="Telephone (Edit this Telephone #): ", font=('', 12, ''),
                             background="lavender")
            lab1.grid(row=1, column=0, padx=5, pady=5)

            lab2 = ttk.Label(datum, text="City (Edit this City name): ", font=('', 12, ''), background="lavender")
            lab2.grid(row=2, column=0, padx=5, pady=5)

            lab3 = ttk.Label(datum, text="Address (Edit this Address): ", font=('', 12, ''), background="lavender")
            lab3.grid(row=3, column=0, padx=5, pady=5)

            def add_up():
                hala5 = (ento11.get() + "", ento1.get() + "", ento1.get() + "", ento.get() + "")
                tree5.insert('', 'end', values=hala5)

                # tree serialization
                with open(la5, "w") as f:
                    yaml.dump(hala5, f)
                #tkMessageBox.showinfo("Edit Item", "You have succesfully edited the entries.")
                # i + 1

            ento = ttk.Entry(datum, width=20, font=('arial', 12, ''))
            ento.grid(row=0, column=1)

            ento1 = ttk.Entry(datum, width=20, font=('arial', 12, ''))
            ento1.grid(row=1, column=1)

            ento1 = ttk.Entry(datum, width=20, font=('arial', 12, ''))
            ento1.grid(row=2, column=1)

            ento11 = ttk.Entry(datum, width=20, font=('arial', 12, ''))
            ento11.grid(row=3, column=1)

            seph = ttk.Separator(datum, orient='horizontal')
            # sep.pack(side = BOTTOM)e
            seph.grid(row=4, column=0, sticky='n,w,e,s', columnspan=2, ipadx=200, ipady=1, padx=5, pady=5)

            btn = ttk.Button(datum, text="OK", style='Wild.TButton', command=add_up)
            btn.grid(row=5, column=0, sticky='E', padx=5, pady=1)

            btn1 = ttk.Button(datum, text="Cancel", command=datum.destroy)
            btn1.grid(row=5, column=1, sticky='W', padx=5, pady=1)

        except:
            tkMessageBox.showerror("Add New Item", "Add new Item failed. Please check input.")
        finally:
            clear()

    def iexits5():
        go = Toplevel(height="400", width="500", relief="flat")
        go.geometry("465x125-450+300")
        #        go.minsize("485", "160")
        #        go.maxsize("485", "160")
        go.title("Delete")
        go.resizable(0, 0)
        go.config(background="#E4E4E4")
        #        go.overrideredirect(True)
        go.attributes("-toolwindow", 1)

        ento = StringVar()
        ento1 = StringVar()
        ento1 = StringVar()
        ento11 = StringVar()

        lb = ttk.Label(go, text="""Are you sure you want to permanetly delete this item?""",
                       font=('Helvetica', 12, 'bold'), background="#E4E4E4")
        lb.grid(row=0, column=0, columnspan=2, sticky='w')

        lb = ttk.Label(go, text="""
            Items deleted would not be recovereable.""", font=('Helvetica', 12, ''), background="#E4E4E4")
        lb.grid(row=1, column=0, columnspan=3, sticky='w', padx=5, pady=5)

        def del_tree():
            selected_item = tree5.selection()[0]
            tree5.delete(selected_item)
            lost5 = (ento11.get() + "", ento1.get() + "", ento1.get() + "", ento.get() + "")
            # tree serialization
            with open(la5, "w") as f:
                yaml.dump(lost5, f)
            # tree1.insert('', 'end', text="Item", values=0)
            #tkMessageBox.showinfo("Delete Item", "You have succesfully deleted the entries.")
            go.destroy()

        bn = ttk.Button(go, text="Cancel", command=go.destroy)
        bn.grid(row=2, column=0, pady=5, ipadx=90, ipady=10)

        bn1 = ttk.Button(go, text="Delete", style='Minis.TButton', command=del_tree)
        bn1.grid(row=2, column=1, pady=5, ipadx=90, ipady=10)

    # =======================================================================================================================
    # We focus on rollman to now dump the inputs
    # Tree serialization
    with open(la5, "r") as f:
        dany5 = yaml.load(f)

    tree5 = ttk.Treeview(my_datum, columns=(3, 2, 1, 0), displaycolumns=(0, 1, 2, 3), height=2, selectmode='browse',
                         show='headings')
    tree5.heading('#0', text='Itemo')
    tree5.heading('#1', text='Name')
    tree5.heading('#2', text='City')
    tree5.heading('#3', text='Telephone')
    tree5.heading('#4', text='Address')
    tree5.insert('', 'end', text="Item", values=dany5)
    tree5.grid(row=7, column=0, padx=1, pady=5, sticky='w')
    i = 0
    b17 = ttk.Button(my_datum, text='+', command=add_all5, style="Mini.TButton")
    b17.grid(row=7, column=1, rowspan=1, padx=5, pady=5, )
    b18 = ttk.Button(my_datum, text='...', command=sub_all5, style="Mini.TButton")
    b18.grid(row=7, column=2, padx=5, pady=5, )
    b19 = ttk.Button(my_datum, text='-', command=iexits5, style="Minis.TButton")
    b19.grid(row=7, column=4, padx=5, pady=5, )

    # We continue our mashalling in .yaml So good I have to say.============================================================
    # =====================We handle another serialization context here. Its the fourth file=================================
    def add_all6():
        try:
            data = Toplevel(height="300", width="730", relief="flat")
            data.geometry("540x180-410+280")
            data.minsize("540", "180")
            data.maxsize("540", "180")
            data.title("Add Data")
            data.config(background="lavender")

            ento = StringVar()
            ento1 = StringVar()
            ent1 = StringVar()
            ento11 = StringVar()

            lab = ttk.Label(data, text="Name (Input the new Name): ", font=('', 12, ''), background="lavender")
            lab.grid(row=0, column=0, padx=5, pady=5)

            lab1 = ttk.Label(data, text="Telephone (Input the new Telephone #): ", font=('', 12, ''),
                             background="lavender")
            lab1.grid(row=1, column=0, padx=5, pady=5)

            lab2 = ttk.Label(data, text="City (Input the City name): ", font=('', 12, ''), background="lavender")
            lab2.grid(row=2, column=0, padx=5, pady=5)

            lab3 = ttk.Label(data, text="Address (Input the new Address): ", font=('', 12, ''), background="lavender")
            lab3.grid(row=3, column=0, padx=5, pady=5)

            def add_up():
                # i = 0
                hala6 = (ento11.get() + "", ento1.get() + "", ento1.get() + "", ento.get() + "")
                tree6.insert('', 'end', values=hala6)

                # tree serialization
                with open(la6, "w") as f:
                    yaml.dump(hala6, f)

                #tkMessageBox.showinfo("Add New Item", "You have succesfully added new entries.")
                # i + 1

            ento = ttk.Entry(data, width=20, font=('arial', 12, ''))
            ento.grid(row=0, column=1)

            ento1 = ttk.Entry(data, width=20, font=('arial', 12, ''))
            ento1.grid(row=1, column=1)

            ento1 = ttk.Entry(data, width=20, font=('arial', 12, ''))
            ento1.grid(row=2, column=1)

            ento11 = ttk.Entry(data, width=20, font=('arial', 12, ''))
            ento11.grid(row=3, column=1)

            seph = ttk.Separator(data, orient='horizontal')
            # sep.pack(side = BOTTOM)e
            seph.grid(row=4, column=0, sticky='n,w,e,s', columnspan=2, ipadx=200, ipady=1, padx=5, pady=5)

            btn = ttk.Button(data, text="OK", style='Wild.TButton', command=add_up)
            btn.grid(row=5, column=0, sticky='E', padx=5, pady=1)

            btn1 = ttk.Button(data, text="Cancel", command=data.destroy)
            btn1.grid(row=5, column=1, sticky='W', padx=5, pady=1)


        except:
            tkMessageBox.showerror("Add New Item", "Add new Item failed. Please check input.")
        finally:
            clear()

    def sub_all6():
        try:
            datum = Toplevel(height="200", width="770", relief="flat")
            datum.geometry("540x180-410+280")
            datum.minsize("490", "180")
            datum.maxsize("490", "180")
            datum.title("Edit Data")
            datum.config(background="lavender")

            ento = StringVar()
            ento1 = StringVar()
            ent1 = StringVar()
            ento11 = StringVar()

            lab = ttk.Label(datum, text="Name (Edit this Name): ", font=('', 12, ''), background="lavender")
            lab.grid(row=0, column=0, padx=5, pady=5)

            lab1 = ttk.Label(datum, text="Telephone (Edit this Telephone #): ", font=('', 12, ''),
                             background="lavender")
            lab1.grid(row=1, column=0, padx=5, pady=5)

            lab2 = ttk.Label(datum, text="City (Edit this City name): ", font=('', 12, ''), background="lavender")
            lab2.grid(row=2, column=0, padx=5, pady=5)

            lab3 = ttk.Label(datum, text="Address (Edit this Address): ", font=('', 12, ''), background="lavender")
            lab3.grid(row=3, column=0, padx=5, pady=5)

            ento = StringVar()
            ento1 = StringVar()

            def add_up():
                hala6 = (ento11.get() + "", ento1.get() + "", ento1.get() + "", ento.get() + "")
                tree6.insert('', 'end', values=hala6)

                # tree serialization
                with open(la6, "w") as f:
                    yaml.dump(hala6, f)
                #tkMessageBox.showinfo("Edit Item", "You have succesfully edited the entries.")
                # i + 1

            ento = ttk.Entry(datum, width=20, font=('arial', 12, ''))
            ento.grid(row=0, column=1)

            ento1 = ttk.Entry(datum, width=20, font=('arial', 12, ''))
            ento1.grid(row=1, column=1)

            ento1 = ttk.Entry(datum, width=20, font=('arial', 12, ''))
            ento1.grid(row=2, column=1)

            ento11 = ttk.Entry(datum, width=20, font=('arial', 12, ''))
            ento11.grid(row=3, column=1)

            seph = ttk.Separator(datum, orient='horizontal')
            # sep.pack(side = BOTTOM)e
            seph.grid(row=4, column=0, sticky='n,w,e,s', columnspan=2, ipadx=200, ipady=1, padx=5, pady=5)

            btn = ttk.Button(datum, text="OK", style='Wild.TButton', command=add_up)
            btn.grid(row=5, column=0, sticky='E', padx=5, pady=1)

            btn1 = ttk.Button(datum, text="Cancel", command=datum.destroy)
            btn1.grid(row=5, column=1, sticky='W', padx=5, pady=1)


        except:
            tkMessageBox.showerror("Add New Item", "Add new Item failed. Please check input.")
        finally:
            clear()

    def iexits6():
        go = Toplevel(height="400", width="500", relief="flat")
        go.geometry("465x125-450+300")
        #        go.minsize("485", "160")
        #        go.maxsize("485", "160")
        go.title("Delete")
        go.resizable(0, 0)
        go.config(background="#E4E4E4")
        #        go.overrideredirect(True)
        go.attributes("-toolwindow", 1)

        ento = StringVar()
        ento1 = StringVar()
        ento1 = StringVar()
        ento11 = StringVar()

        lb = ttk.Label(go, text="""Are you sure you want to permanetly delete this item?""",
                       font=('Helvetica', 12, 'bold'), background="#E4E4E4")
        lb.grid(row=0, column=0, columnspan=2, sticky='w')

        lb = ttk.Label(go, text="""
            Items deleted would not be recovereable.""", font=('Helvetica', 12, ''), background="#E4E4E4")
        lb.grid(row=1, column=0, columnspan=3, sticky='w', padx=5, pady=5)

        def del_tree():
            selected_item = tree6.selection()[0]
            tree6.delete(selected_item)
            lost6 = (ento11.get() + "", ento1.get() + "", ento1.get() + "", ento.get() + "")
            # tree serialization
            with open(la6, "w") as f:
                yaml.dump(lost6, f)
            # tree1.insert('', 'end', text="Item", values=0)
            #tkMessageBox.showinfo("Delete Item", "You have succesfully deleted the entries.")
            go.destroy()

        bn = ttk.Button(go, text="Cancel", command=go.destroy)
        bn.grid(row=2, column=0, pady=5, ipadx=90, ipady=10)

        bn1 = ttk.Button(go, text="Delete", style='Minis.TButton', command=del_tree)
        bn1.grid(row=2, column=1, pady=5, ipadx=90, ipady=10)

    # =======================================================================================================================
    # We focus on rollman to now dump the inputs
    # Tree serialization
    with open(la6, "r") as f:
        dany6 = yaml.load(f)
    tree6 = ttk.Treeview(my_datum, columns=(3, 2, 1, 0), displaycolumns=(0, 1, 2, 3), height=2, selectmode='browse',
                         show='headings')
    tree6.heading('#0', text='Itemo')
    tree6.heading('#1', text='Name')
    tree6.heading('#2', text='City')
    tree6.heading('#3', text='Telephone')
    tree6.heading('#4', text='Address')
    tree6.insert('', 'end', text="Item", values=dany6)
    tree6.grid(row=8, column=0, padx=1, pady=5, sticky='w')
    i = 0
    b20 = ttk.Button(my_datum, text='+', command=add_all6, style="Mini.TButton")
    b20.grid(row=8, column=1, rowspan=1, padx=5, pady=5, )
    b21 = ttk.Button(my_datum, text='...', command=sub_all6, style="Mini.TButton")
    b21.grid(row=8, column=2, padx=5, pady=5, )
    b22 = ttk.Button(my_datum, text='-', command=iexits6, style="Minis.TButton")
    b22.grid(row=8, column=4, padx=5, pady=5, )

    # ==========Game on Chief.===============================================================================================
    # =====================We handle another serialization context here. Its the fourth file=================================
    def add_all7():
        try:
            data = Toplevel(height="300", width="730", relief="flat")
            data.geometry("540x180-410+280")
            data.minsize("540", "180")
            data.maxsize("540", "180")
            data.title("Add Data")
            data.config(background="lavender")

            ento = StringVar()
            ento1 = StringVar()
            ent1 = StringVar()
            ento11 = StringVar()

            lab = ttk.Label(data, text="Name (Input the new Name): ", font=('', 12, ''), background="lavender")
            lab.grid(row=0, column=0, padx=5, pady=5)

            lab1 = ttk.Label(data, text="Telephone (Input the new Telephone #): ", font=('', 12, ''),
                             background="lavender")
            lab1.grid(row=1, column=0, padx=5, pady=5)

            lab2 = ttk.Label(data, text="City (Input the City name): ", font=('', 12, ''), background="lavender")
            lab2.grid(row=2, column=0, padx=5, pady=5)

            lab3 = ttk.Label(data, text="Address (Input the new Address): ", font=('', 12, ''), background="lavender")
            lab3.grid(row=3, column=0, padx=5, pady=5)

            def add_up():
                # i = 0
                hala7 = (ento11.get() + "", ento1.get() + "", ento1.get() + "", ento.get() + "")
                tree7.insert('', 'end', values=hala7)

                # tree serialization
                with open(la7, "w") as f:
                    yaml.dump(hala7, f)

                #tkMessageBox.showinfo("Add New Item", "You have succesfully added new entries.")
                # i + 1

            ento = ttk.Entry(data, width=20, font=('arial', 12, ''))
            ento.grid(row=0, column=1)

            ento1 = ttk.Entry(data, width=20, font=('arial', 12, ''))
            ento1.grid(row=1, column=1)

            ento1 = ttk.Entry(data, width=20, font=('arial', 12, ''))
            ento1.grid(row=2, column=1)

            ento11 = ttk.Entry(data, width=20, font=('arial', 12, ''))
            ento11.grid(row=3, column=1)

            seph = ttk.Separator(data, orient='horizontal')
            # sep.pack(side = BOTTOM)e
            seph.grid(row=4, column=0, sticky='n,w,e,s', columnspan=2, ipadx=200, ipady=1, padx=5, pady=5)

            btn = ttk.Button(data, text="OK", style='Wild.TButton', command=add_up)
            btn.grid(row=5, column=0, sticky='E', padx=5, pady=1)

            btn1 = ttk.Button(data, text="Cancel", command=data.destroy)
            btn1.grid(row=5, column=1, sticky='W', padx=5, pady=1)


        except:
            tkMessageBox.showerror("Add New Item", "Add new Item failed. Please check input.")
        finally:
            clear()

    def sub_all7():
        try:
            datum = Toplevel(height="200", width="770", relief="flat")
            datum.geometry("540x180-410+280")
            datum.minsize("490", "180")
            datum.maxsize("490", "180")
            datum.title("Edit Data")
            datum.config(background="lavender")

            ento = StringVar()
            ento1 = StringVar()
            ent1 = StringVar()
            ento11 = StringVar()

            lab = ttk.Label(datum, text="Name (Edit this Name): ", font=('', 12, ''), background="lavender")
            lab.grid(row=0, column=0, padx=5, pady=5)

            lab1 = ttk.Label(datum, text="Telephone (Edit this Telephone #): ", font=('', 12, ''),
                             background="lavender")
            lab1.grid(row=1, column=0, padx=5, pady=5)

            lab2 = ttk.Label(datum, text="City (Edit this City name): ", font=('', 12, ''), background="lavender")
            lab2.grid(row=2, column=0, padx=5, pady=5)

            lab3 = ttk.Label(datum, text="Address (Edit this Address): ", font=('', 12, ''), background="lavender")
            lab3.grid(row=3, column=0, padx=5, pady=5)

            ento = StringVar()
            ento1 = StringVar()

            def add_up():
                hala7 = (ento11.get() + "", ento1.get() + "", ento1.get() + "", ento.get() + "")
                tree7.insert('', 'end', values=hala7)

                # tree serialization
                with open(la7, "w") as f:
                    yaml.dump(hala7, f)
                #tkMessageBox.showinfo("Edit Item", "You have succesfully edited the entries.")
                # i + 1

            ento = ttk.Entry(datum, width=20, font=('arial', 12, ''))
            ento.grid(row=0, column=1)

            ento1 = ttk.Entry(datum, width=20, font=('arial', 12, ''))
            ento1.grid(row=1, column=1)

            ento1 = ttk.Entry(datum, width=20, font=('arial', 12, ''))
            ento1.grid(row=2, column=1)

            ento11 = ttk.Entry(datum, width=20, font=('arial', 12, ''))
            ento11.grid(row=3, column=1)

            seph = ttk.Separator(datum, orient='horizontal')
            # sep.pack(side = BOTTOM)e
            seph.grid(row=4, column=0, sticky='n,w,e,s', columnspan=2, ipadx=200, ipady=1, padx=5, pady=5)

            btn = ttk.Button(datum, text="OK", style='Wild.TButton', command=add_up)
            btn.grid(row=5, column=0, sticky='E', padx=5, pady=1)

            btn1 = ttk.Button(datum, text="Cancel", command=datum.destroy)
            btn1.grid(row=5, column=1, sticky='W', padx=5, pady=1)
        except:
            tkMessageBox.showerror("Add New Item", "Add new Item failed. Please check input.")
        finally:
            clear()

    def iexits7():
        go = Toplevel(height="400", width="500", relief="flat")
        go.geometry("465x125-450+300")
        #        go.minsize("485", "160")
        #        go.maxsize("485", "160")
        go.title("Delete")
        go.resizable(0, 0)
        go.config(background="#E4E4E4")
        #        go.overrideredirect(True)
        go.attributes("-toolwindow", 1)

        ento1 = StringVar()
        ento1 = StringVar()
        ento = StringVar()
        ento11 = StringVar()

        lb = ttk.Label(go, text="""Are you sure you want to permanetly delete this item?""",
                       font=('Helvetica', 12, 'bold'), background="#E4E4E4")
        lb.grid(row=0, column=0, columnspan=2, sticky='w')

        lb = ttk.Label(go, text="""
            Items deleted would not be recovereable.""", font=('Helvetica', 12, ''), background="#E4E4E4")
        lb.grid(row=1, column=0, columnspan=3, sticky='w', padx=5, pady=5)

        def del_tree():
            selected_item = tree7.selection()[0]
            tree7.delete(selected_item)
            lost7 = (ento11.get() + "", ento1.get() + "", ento1.get() + "", ento.get() + "")
            # tree serialization
            with open(la7, "w") as f:
                yaml.dump(lost7, f)
            # tree1.insert('', 'end', text="Item", values=0)
            #tkMessageBox.showinfo("Delete Item", "You have succesfully deleted the entries.")
            go.destroy()

        bn = ttk.Button(go, text="Cancel", command=go.destroy)
        bn.grid(row=2, column=0, pady=5, ipadx=90, ipady=10)

        bn1 = ttk.Button(go, text="Delete", style='Minis.TButton', command=del_tree)
        bn1.grid(row=2, column=1, pady=5, ipadx=90, ipady=10)

    # =======================================================================================================================
    # We focus on rollman to now dump the inputs
    # Tree serialization
    with open(la7, "r") as f:
        dany7 = yaml.load(f)

    tree7 = ttk.Treeview(my_datum, columns=(3, 2, 1, 0), displaycolumns=(0, 1, 2, 3), height=2, selectmode='browse',
                         show='headings')
    tree7.heading('#0', text='Itemo')
    tree7.heading('#1', text='Name')
    tree7.heading('#2', text='City')
    tree7.heading('#3', text='Telephone')
    tree7.heading('#4', text='Address')
    tree7.insert('', 'end', text="Item", values=dany7)
    tree7.grid(row=9, column=0, padx=1, pady=5, sticky='w')
    i = 0
    b23 = ttk.Button(my_datum, text='+', command=add_all7, style="Mini.TButton")
    b23.grid(row=9, column=1, rowspan=1, padx=5, pady=5, )
    b24 = ttk.Button(my_datum, text='...', command=sub_all7, style="Mini.TButton")
    b24.grid(row=9, column=2, padx=5, pady=5, )
    b25 = ttk.Button(my_datum, text='-', command=iexits7, style="Minis.TButton")
    b25.grid(row=9, column=4, padx=5, pady=5, )

#===========================================================================
def abt():
#    time.sleep(5)
    kn = Toplevel()
    kn.title("About")
#    photo = PhotoImage(file="dek1.png")
    kn.geometry("542x350-330+210")
#    kn.minsize("542", "345")
#    kn.maxsize("542", "345")
#    kn.config(background = "#666666")
    kn.overrideredirect(True)

    def des(event):
        kn.destroy()
#    photo = PhotoImage(file="dek1.png")
    path = "dekc.png"
    img = ImageTk.PhotoImage(Image.open(path))
    abn = Label(kn, image = img)
    abn.image = img
    abn.grid(row = 0, column = 0, ipadx = 1, ipady = 1, sticky = 'n')
    abn.bind("<Button-1>", des)

    def click_link(event):
        webbrowser.open_new(r"https://dvslonline.wordpress.com")

    abn1 = ttk.Button(kn, text = " Website: https://dvslonline.wordpress.com", style = "Mini.TButton", width = 70, cursor = "hand2")
    abn1.grid(row=1, column=0, padx = 1, pady = 1, ipadx = 67)
    abn1.bind("<Button-1>", click_link)

bn = Button(w1, text='More', command=my_data,bg = "#0066CC", fg = "white", activeforeground = "white", activebackground = "#0066CC", overrelief = "flat", relief = "flat",font = ('DejaVu Sans Mono',10, 'bold'), width = 10,)
bn.grid(row=0, column=0, padx=5, pady=5, )

bn1 = Button(w1, text='About', command=abt,bg = "#0066CC", fg = "white", activeforeground = "white", activebackground = "#0066CC", overrelief = "flat", relief = "flat",font = ('DejaVu Sans Mono',10, 'bold'), width = 10,)
bn1.grid(row=0, columnspan=40, padx=5, pady=5, )
w1.mainloop()