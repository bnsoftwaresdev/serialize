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
import threading
import Queue
import time
from ttk import Combobox
import time
import Tix
from Tkinter import*
import random
import time
import webbrowser
import ttk
from PIL import ImageTk, Image
#from Tkinter import MessageBox
import tkMessageBox
from Tkinter import Tk, Frame, Menu, Button

from Tkinter import LEFT, TOP, X, FLAT, RAISED


w1 = Tkinter.Tk()
w1.title('Product List')

s = ttk.Style()
s.theme_names()
('aqua', 'aqua cocoa', 'X11', 'step', 'clam', 'alt', 'default', 'classic', 'motif', 'plastique', 'CDE', 'windows')
s.theme_use('clam')

w1.geometry('1250x300-50+10')
w1.minsize("1200", "680")
w1.maxsize("1150", "700")
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
ents = StringVar()
lona = StringVar()
lon = StringVar()
selected_item = StringVar()

rollman = "roll.yaml"
tripo = "loll.yaml"
oma = "name.yaml"
umaga = "age.yaml"
cena = "name1.yaml"
van = "age1.yaml"
king = "roll1.yaml"
yon = "man.yaml"
josh = "eman.yaml"
wrest = "chilo.yaml"
hum = "moane.yaml"
taker = "loane.yaml"
undr = "hus.yaml"
mena = "wif.yaml"
ania = "fud.yaml"
portsy = "sed.yaml"
olo = "nei.yaml"
atkui = "bors.yaml"
biug = "chae.yaml"

# This is the extension button
l1 = "jan.yaml"
l2 = "feb.yaml"
l3 = "mar.yaml"
l4 = "apr.yaml"
l5 = "may.yaml"
l6 = "jun.yaml"
l7 = "jul.yaml"
l8 = "aug.yaml"
l9 = "sep.yaml"
l10 = "oct.yaml"
l11 = "nov.yaml"
l12 = "dec.yaml"
l13 = "jan1.yaml"
l14 = "feb1.yaml"
l15 = "mar1.yaml"
l16 = "apr1.yaml"
#=========================We start our functions here===================================================================
def clear():
    ento.set('')
    ents.set('')


def add_all():
    try:
        data = Toplevel(height="300", width="730", relief="flat")
        data.geometry("450x150-410+280")
        data.minsize("440", "120")
        data.maxsize("440", "120")
        data.title("Add Data")
        data.config(background="lavender")

        ent = StringVar()
        ent1 = StringVar()

        lab = ttk.Label(data, text="Item (Input the new Item): ", font=('', 12, ''), background="lavender")
        lab.grid(row=0, column=0, padx=5, pady=5)

        lab1 = ttk.Label(data, text="Price (Input the new Price): ", font=('', 12, ''), background="lavender")
        lab1.grid(row=1, column=0, padx=5, pady=5)



        def add_up():
            # i = 0
            hala = (ents.get() + "GHC", ento.get() + "KG", ents.get() + "GHC", ento.get() + "KG")
            #hal = ()
            tree.insert('', 'end', values=hala)

            # tree serialization
            with open(oma, "w") as f:
                yaml.dump(hala, f)

            tkMessageBox.showinfo("Add New Item", "You have succesfully added new entries.")
            # i + 1

        ento = ttk.Entry(data, width=20, font=('arial', 12, ''))
        ento.grid(row=0, column=1)

        ents = ttk.Entry(data, width=20, font=('arial', 12, ''))
        ents.grid(row=1, column=1)

        seph = ttk.Separator(data, orient='horizontal')
        # sep.pack(side = BOTTOM)e
        seph.grid(row=2, column=0, sticky='n,w,e,s', columnspan=2, ipadx=200, ipady=1, padx=5, pady=5)

        btn = ttk.Button(data, text="OK", style='Wild.TButton', command=add_up)
        btn.grid(row=3, column=0, sticky='E', padx=5, pady=1)

        btn1 = ttk.Button(data, text="Cancel", command=data.destroy)
        btn1.grid(row=3, column=1, sticky='W', padx=5, pady=1)

    except:
        tkMessageBox.showerror("Add New Item", "Add new Item failed. Please check input.")
    finally:
        clear()


def sub_all():
    try:
        datum = Toplevel(height="200", width="770", relief="flat")
        datum.geometry("460x150-410+280")
        datum.minsize("450", "120")
        datum.maxsize("450", "120")
        datum.title("Edit Data")
        datum.config(background="lavender")

        ent = StringVar()
        ent1 = StringVar()

        lab = ttk.Label(datum, text="Item (Edit the selected Item): ", font=('', 12, ''), background="lavender")
        lab.grid(row=0, column=0, padx=5, pady=5)

        lab1 = ttk.Label(datum, text="Price (Edit the price): ", font=('', 12, ''), background="lavender")
        lab1.grid(row=1, column=0, padx=5, pady=5)

        ento = StringVar()
        ents = StringVar()

        def add_up():
            hala = (ents.get() + "GHC", ento.get() + "KG")
            tree.insert('', 'end', values=hala)

            # tree serialization
            with open(oma, "w") as f:
                yaml.dump(hala, f)
            tkMessageBox.showinfo("Edit Item", "You have succesfully edited the entries.")
            # i + 1

        ento = ttk.Entry(datum, width=20, font=('arial', 12, ''))
        ento.grid(row=0, column=1)

        ents = ttk.Entry(datum, width=20, font=('arial', 12, ''))
        ents.grid(row=1, column=1)

        seph = ttk.Separator(datum, orient='horizontal')
        # sep.pack(side = BOTTOM)e
        seph.grid(row=2, column=0, sticky='n,w,e,s', columnspan=2, ipadx=200, ipady=1, padx=5, pady=5)

        btn = ttk.Button(datum, text="OK", style='Wild.TButton', command=add_up)
        btn.grid(row=3, column=0, sticky='E', padx=5, pady=1)

        btn1 = ttk.Button(datum, text="Cancel", command=datum.destroy)
        btn1.grid(row=3, column=1, sticky='W', padx=5, pady=1)

    except:
        tkMessageBox.showerror("Add New Item", "Add new Item failed. Please check input.")
    finally:
        clear()

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

        lb = ttk.Label(go, text="""Are you sure you want to permanetly delete this item?""", font=('Helvetica', 12, 'bold'), background = "#E4E4E4")
        lb.grid(row=0, column=0,  columnspan=2,sticky='w')

        lb = ttk.Label(go, text="""
        Items deleted would not be recovereable.""", font=('Helvetica', 12, ''), background = "#E4E4E4")
        lb.grid(row=1, column=0,  columnspan=3,sticky='w', padx=5, pady=5)

        def del_tree():
            selected_item =tree.selection()[0]
            tree.delete(selected_item)
            lost = (ents.get() + "", ento.get() + "")
            # tree serialization
            with open(oma, "w") as f:
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

lbl = ttk.Label(w1, text="""Product List would allow storing, editing and deleting of new entries here.""", font=('DejaVu Sans Mono', 11, ''), background = '#E4E4E4')
lbl.grid(row=1, column=0, columnspan = 5,sticky='w')

# We focus on oma to now dump the inputs
# Tree serialization
with open(oma, "r") as f:
    dany= yaml.load(f)


tree = ttk.Treeview(w1, columns=(1, 0), displaycolumns=(0, 1,), height=2, selectmode='browse',
                     show='headings')
tree.heading('#0', text='Itemo')
tree.heading('#1', text='Item')
tree.heading('#2', text='Price')
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
        data.geometry("450x150-410+280")
        data.minsize("440", "120")
        data.maxsize("440", "120")
        data.title("Add Data")
        data.config(background="lavender")

        ent = StringVar()
        ent1 = StringVar()

        lab = ttk.Label(data, text="Item (Input the new Item): ", font=('', 12, ''), background="lavender")
        lab.grid(row=0, column=0, padx=5, pady=5)

        lab1 = ttk.Label(data, text="Price (Input the new Price): ", font=('', 12, ''), background="lavender")
        lab1.grid(row=1, column=0, padx=5, pady=5)



        def add_up():
            # i = 0
            hala1 = (ents.get() + "GHC", ento.get() + "KG")
            tree1.insert('', 'end', values=hala1)

            # tree serialization
            with open(tripo, "w") as f:
                yaml.dump(hala1, f)

            tkMessageBox.showinfo("Add New Item", "You have succesfully added new entries.")
            # i + 1

        ento = ttk.Entry(data, width=20, font=('arial', 12, ''))
        ento.grid(row=0, column=1)

        ents = ttk.Entry(data, width=20, font=('arial', 12, ''))
        ents.grid(row=1, column=1)

        seph = ttk.Separator(data, orient='horizontal')
        # sep.pack(side = BOTTOM)e
        seph.grid(row=2, column=0, sticky='n,w,e,s', columnspan=2, ipadx=200, ipady=1, padx=5, pady=5)

        btn = ttk.Button(data, text="OK", style='Wild.TButton', command=add_up)
        btn.grid(row=3, column=0, sticky='E', padx=5, pady=1)

        btn1 = ttk.Button(data, text="Cancel", command=data.destroy)
        btn1.grid(row=3, column=1, sticky='W', padx=5, pady=1)

    except:
        tkMessageBox.showerror("Add New Item", "Add new Item failed. Please check input.")
    finally:
        clear()


def sub_all1():
    try:
        datum = Toplevel(height="200", width="770", relief="flat")
        datum.geometry("460x150-410+280")
        datum.minsize("450", "120")
        datum.maxsize("450", "120")
        datum.title("Edit Data")
        datum.config(background="lavender")

        ent = StringVar()
        ent1 = StringVar()

        lab = ttk.Label(datum, text="Item (Edit the selected Item): ", font=('', 12, ''), background="lavender")
        lab.grid(row=0, column=0, padx=5, pady=5)

        lab1 = ttk.Label(datum, text="Price (Edit the price): ", font=('', 12, ''), background="lavender")
        lab1.grid(row=1, column=0, padx=5, pady=5)

        ento = StringVar()
        ents = StringVar()

        def add_up():
            hala1 = (ents.get() + "GHC", ento.get() + "KG")
            tree1.insert('', 'end', values=hala1)

            # tree serialization
            with open(tripo, "w") as f:
                yaml.dump(hala1, f)
            tkMessageBox.showinfo("Edit Item", "You have succesfully edited the entries.")
            # i + 1

        ento = ttk.Entry(datum, width=20, font=('arial', 12, ''))
        ento.grid(row=0, column=1)

        ents = ttk.Entry(datum, width=20, font=('arial', 12, ''))
        ents.grid(row=1, column=1)

        seph = ttk.Separator(datum, orient='horizontal')
        # sep.pack(side = BOTTOM)e
        seph.grid(row=2, column=0, sticky='n,w,e,s', columnspan=2, ipadx=200, ipady=1, padx=5, pady=5)

        btn = ttk.Button(datum, text="OK", style='Wild.TButton', command=add_up)
        btn.grid(row=3, column=0, sticky='E', padx=5, pady=1)

        btn1 = ttk.Button(datum, text="Cancel", command=datum.destroy)
        btn1.grid(row=3, column=1, sticky='W', padx=5, pady=1)

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

        lb = ttk.Label(go, text="""Are you sure you want to permanetly delete this item?""", font=('Helvetica', 12, 'bold'), background = "#E4E4E4")
        lb.grid(row=0, column=0,  columnspan=2,sticky='w')

        lb = ttk.Label(go, text="""
        Items deleted would not be recovereable.""", font=('Helvetica', 12, ''), background = "#E4E4E4")
        lb.grid(row=1, column=0,  columnspan=3,sticky='w', padx=5, pady=5)

        def del_tree():
            selected_item =tree1.selection()[0]
            tree1.delete(selected_item)
            lost1 = (ents.get() + "", ento.get() + "")
            # tree serialization
            with open(tripo, "w") as f:
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
with open(tripo, "r") as f:
    dany1= yaml.load(f)
tree1 = ttk.Treeview(w1, columns=(1, 0), displaycolumns=(0, 1,), height=2, selectmode='browse',
                     show='headings')
tree1.heading('#0', text='Itemo')
tree1.heading('#1', text='Item')
tree1.heading('#2', text='Price')
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
        data.geometry("450x150-410+280")
        data.minsize("440", "120")
        data.maxsize("440", "120")
        data.title("Add Data")
        data.config(background="lavender")

        ent = StringVar()
        ent1 = StringVar()

        lab = ttk.Label(data, text="Item (Input the new Item): ", font=('', 12, ''), background="lavender")
        lab.grid(row=0, column=0, padx=5, pady=5)

        lab1 = ttk.Label(data, text="Price (Input the new Price): ", font=('', 12, ''), background="lavender")
        lab1.grid(row=1, column=0, padx=5, pady=5)



        def add_up():
            # i = 0
            hala2 = (ents.get() + "GHC", ento.get() + "KG")
            tree2.insert('', 'end', values=hala2)

            # tree serialization
            with open(rollman, "w") as f:
                yaml.dump(hala2, f)

            tkMessageBox.showinfo("Add New Item", "You have succesfully added new entries.")
            # i + 1

        ento = ttk.Entry(data, width=20, font=('arial', 12, ''))
        ento.grid(row=0, column=1)

        ents = ttk.Entry(data, width=20, font=('arial', 12, ''))
        ents.grid(row=1, column=1)

        seph = ttk.Separator(data, orient='horizontal')
        # sep.pack(side = BOTTOM)e
        seph.grid(row=2, column=0, sticky='n,w,e,s', columnspan=2, ipadx=200, ipady=1, padx=5, pady=5)

        btn = ttk.Button(data, text="OK", style='Wild.TButton', command=add_up)
        btn.grid(row=3, column=0, sticky='E', padx=5, pady=1)

        btn1 = ttk.Button(data, text="Cancel", command=data.destroy)
        btn1.grid(row=3, column=1, sticky='W', padx=5, pady=1)

    except:
        tkMessageBox.showerror("Add New Item", "Add new Item failed. Please check input.")
    finally:
        clear()


def sub_all2():
    try:
        datum = Toplevel(height="200", width="770", relief="flat")
        datum.geometry("460x150-410+280")
        datum.minsize("450", "120")
        datum.maxsize("450", "120")
        datum.title("Edit Data")
        datum.config(background="lavender")

        ent = StringVar()
        ent1 = StringVar()

        lab = ttk.Label(datum, text="Item (Edit the selected Item): ", font=('', 12, ''), background="lavender")
        lab.grid(row=0, column=0, padx=5, pady=5)

        lab1 = ttk.Label(datum, text="Price (Edit the price): ", font=('', 12, ''), background="lavender")
        lab1.grid(row=1, column=0, padx=5, pady=5)

        ento = StringVar()
        ents = StringVar()

        def add_up():
            hala2 = (ents.get() + "GHC", ento.get() + "KG")
            tree2.insert('', 'end', values=hala2)

            # tree serialization
            with open(rollman, "w") as f:
                yaml.dump(hala2, f)
            tkMessageBox.showinfo("Edit Item", "You have succesfully edited the entries.")
            # i + 1

        ento = ttk.Entry(datum, width=20, font=('arial', 12, ''))
        ento.grid(row=0, column=1)

        ents = ttk.Entry(datum, width=20, font=('arial', 12, ''))
        ents.grid(row=1, column=1)

        seph = ttk.Separator(datum, orient='horizontal')
        # sep.pack(side = BOTTOM)e
        seph.grid(row=2, column=0, sticky='n,w,e,s', columnspan=2, ipadx=200, ipady=1, padx=5, pady=5)

        btn = ttk.Button(datum, text="OK", style='Wild.TButton', command=add_up)
        btn.grid(row=3, column=0, sticky='E', padx=5, pady=1)

        btn1 = ttk.Button(datum, text="Cancel", command=datum.destroy)
        btn1.grid(row=3, column=1, sticky='W', padx=5, pady=1)

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

        lb = ttk.Label(go, text="""Are you sure you want to permanetly delete this item?""", font=('Helvetica', 12, 'bold'), background = "#E4E4E4")
        lb.grid(row=0, column=0,  columnspan=2,sticky='w')

        lb = ttk.Label(go, text="""
        Items deleted would not be recovereable.""", font=('Helvetica', 12, ''), background = "#E4E4E4")
        lb.grid(row=1, column=0,  columnspan=3,sticky='w', padx=5, pady=5)

        def del_tree():
            selected_item =tree2.selection()[0]
            tree2.delete(selected_item)
            lost2 = (ents.get() + "", ento.get() + "")
            # tree serialization
            with open(rollman, "w") as f:
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
with open(rollman, "r") as f:
    dany2= yaml.load(f)

tree2 = ttk.Treeview(w1, columns=(1, 0), displaycolumns=(0, 1,), height=2, selectmode='browse',
                     show='headings')
tree2.heading('#0', text='Itemo')
tree2.heading('#1', text='Item')
tree2.heading('#2', text='Price')
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
        data.geometry("450x150-410+280")
        data.minsize("440", "120")
        data.maxsize("440", "120")
        data.title("Add Data")
        data.config(background="lavender")

        ent = StringVar()
        ent1 = StringVar()

        lab = ttk.Label(data, text="Item (Input the new Item): ", font=('', 12, ''), background="lavender")
        lab.grid(row=0, column=0, padx=5, pady=5)

        lab1 = ttk.Label(data, text="Price (Input the new Price): ", font=('', 12, ''), background="lavender")
        lab1.grid(row=1, column=0, padx=5, pady=5)



        def add_up():
            # i = 0
            hala3 = (ents.get() + "GHC", ento.get() + "KG")
            tree3.insert('', 'end', values=hala3)

            # tree serialization
            with open(oma, "w") as f:
                yaml.dump(hala3, f)

            tkMessageBox.showinfo("Add New Item", "You have succesfully added new entries.")
            # i + 1

        ento = ttk.Entry(data, width=20, font=('arial', 12, ''))
        ento.grid(row=0, column=1)

        ents = ttk.Entry(data, width=20, font=('arial', 12, ''))
        ents.grid(row=1, column=1)

        seph = ttk.Separator(data, orient='horizontal')
        # sep.pack(side = BOTTOM)e
        seph.grid(row=2, column=0, sticky='n,w,e,s', columnspan=2, ipadx=200, ipady=1, padx=5, pady=5)

        btn = ttk.Button(data, text="OK", style='Wild.TButton', command=add_up)
        btn.grid(row=3, column=0, sticky='E', padx=5, pady=1)

        btn1 = ttk.Button(data, text="Cancel", command=data.destroy)
        btn1.grid(row=3, column=1, sticky='W', padx=5, pady=1)

    except:
        tkMessageBox.showerror("Add New Item", "Add new Item failed. Please check input.")
    finally:
        clear()


def sub_all3():
    try:
        datum = Toplevel(height="200", width="770", relief="flat")
        datum.geometry("460x150-410+280")
        datum.minsize("450", "120")
        datum.maxsize("450", "120")
        datum.title("Edit Data")
        datum.config(background="lavender")

        ent = StringVar()
        ent1 = StringVar()

        lab = ttk.Label(datum, text="Item (Edit the selected Item): ", font=('', 12, ''), background="lavender")
        lab.grid(row=0, column=0, padx=5, pady=5)

        lab1 = ttk.Label(datum, text="Price (Edit the price): ", font=('', 12, ''), background="lavender")
        lab1.grid(row=1, column=0, padx=5, pady=5)

        ento = StringVar()
        ents = StringVar()

        def add_up():
            hala3 = (ents.get() + "GHC", ento.get() + "KG")
            tree3.insert('', 'end', values=hala3)

            # tree serialization
            with open(oma, "w") as f:
                yaml.dump(hala3, f)
            tkMessageBox.showinfo("Edit Item", "You have succesfully edited the entries.")
            # i + 1

        ento = ttk.Entry(datum, width=20, font=('arial', 12, ''))
        ento.grid(row=0, column=1)

        ents = ttk.Entry(datum, width=20, font=('arial', 12, ''))
        ents.grid(row=1, column=1)

        seph = ttk.Separator(datum, orient='horizontal')
        # sep.pack(side = BOTTOM)e
        seph.grid(row=2, column=0, sticky='n,w,e,s', columnspan=2, ipadx=200, ipady=1, padx=5, pady=5)

        btn = ttk.Button(datum, text="OK", style='Wild.TButton', command=add_up)
        btn.grid(row=3, column=0, sticky='E', padx=5, pady=1)

        btn1 = ttk.Button(datum, text="Cancel", command=datum.destroy)
        btn1.grid(row=3, column=1, sticky='W', padx=5, pady=1)

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

        lb = ttk.Label(go, text="""Are you sure you want to permanetly delete this item?""", font=('Helvetica', 12, 'bold'), background = "#E4E4E4")
        lb.grid(row=0, column=0,  columnspan=2,sticky='w')

        lb = ttk.Label(go, text="""
        Items deleted would not be recovereable.""", font=('Helvetica', 12, ''), background = "#E4E4E4")
        lb.grid(row=1, column=0,  columnspan=3,sticky='w', padx=5, pady=5)

        def del_tree():
            selected_item =tree3.selection()[0]
            tree3.delete(selected_item)
            lost3 = (ents.get() + "", ento.get() + "")
            # tree serialization
            with open(oma, "w") as f:
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
with open(oma, "r") as f:
    dany3= yaml.load(f)
tree3 = ttk.Treeview(w1, columns=(1, 0), displaycolumns=(0, 1,), height=2, selectmode='browse',
                     show='headings')
tree3.heading('#0', text='Itemo')
tree3.heading('#1', text='Item')
tree3.heading('#2', text='Price')
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
        data.geometry("450x150-410+280")
        data.minsize("440", "120")
        data.maxsize("440", "120")
        data.title("Add Data")
        data.config(background="lavender")

        ent = StringVar()
        ent1 = StringVar()

        lab = ttk.Label(data, text="Item (Input the new Item): ", font=('', 12, ''), background="lavender")
        lab.grid(row=0, column=0, padx=5, pady=5)

        lab1 = ttk.Label(data, text="Price (Input the new Price): ", font=('', 12, ''), background="lavender")
        lab1.grid(row=1, column=0, padx=5, pady=5)



        def add_up():
            # i = 0
            hala4 = (ents.get() + "GHC", ento.get() + "KG")
            tree4.insert('', 'end', values=hala4)

            # tree serialization
            with open(umaga, "w") as f:
                yaml.dump(hala4, f)

            tkMessageBox.showinfo("Add New Item", "You have succesfully added new entries.")
            # i + 1

        ento = ttk.Entry(data, width=20, font=('arial', 12, ''))
        ento.grid(row=0, column=1)

        ents = ttk.Entry(data, width=20, font=('arial', 12, ''))
        ents.grid(row=1, column=1)

        seph = ttk.Separator(data, orient='horizontal')
        # sep.pack(side = BOTTOM)e
        seph.grid(row=2, column=0, sticky='n,w,e,s', columnspan=2, ipadx=200, ipady=1, padx=5, pady=5)

        btn = ttk.Button(data, text="OK", style='Wild.TButton', command=add_up)
        btn.grid(row=3, column=0, sticky='E', padx=5, pady=1)

        btn1 = ttk.Button(data, text="Cancel", command=data.destroy)
        btn1.grid(row=3, column=1, sticky='W', padx=5, pady=1)

    except:
        tkMessageBox.showerror("Add New Item", "Add new Item failed. Please check input.")
    finally:
        clear()


def sub_all4():
    try:
        datum = Toplevel(height="200", width="770", relief="flat")
        datum.geometry("460x150-410+280")
        datum.minsize("450", "120")
        datum.maxsize("450", "120")
        datum.title("Edit Data")
        datum.config(background="lavender")

        ent = StringVar()
        ent1 = StringVar()

        lab = ttk.Label(datum, text="Item (Edit the selected Item): ", font=('', 12, ''), background="lavender")
        lab.grid(row=0, column=0, padx=5, pady=5)

        lab1 = ttk.Label(datum, text="Price (Edit the price): ", font=('', 12, ''), background="lavender")
        lab1.grid(row=1, column=0, padx=5, pady=5)

        ento = StringVar()
        ents = StringVar()

        def add_up():
            hala4 = (ents.get() + "GHC", ento.get() + "KG")
            tree4.insert('', 'end', values=hala4)

            # tree serialization
            with open(umaga, "w") as f:
                yaml.dump(hala4, f)
            tkMessageBox.showinfo("Edit Item", "You have succesfully edited the entries.")
            # i + 1

        ento = ttk.Entry(datum, width=20, font=('arial', 12, ''))
        ento.grid(row=0, column=1)

        ents = ttk.Entry(datum, width=20, font=('arial', 12, ''))
        ents.grid(row=1, column=1)

        seph = ttk.Separator(datum, orient='horizontal')
        # sep.pack(side = BOTTOM)e
        seph.grid(row=2, column=0, sticky='n,w,e,s', columnspan=2, ipadx=200, ipady=1, padx=5, pady=5)

        btn = ttk.Button(datum, text="OK", style='Wild.TButton', command=add_up)
        btn.grid(row=3, column=0, sticky='E', padx=5, pady=1)

        btn1 = ttk.Button(datum, text="Cancel", command=datum.destroy)
        btn1.grid(row=3, column=1, sticky='W', padx=5, pady=1)

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

        lb = ttk.Label(go, text="""Are you sure you want to permanetly delete this item?""", font=('Helvetica', 12, 'bold'), background = "#E4E4E4")
        lb.grid(row=0, column=0,  columnspan=2,sticky='w')

        lb = ttk.Label(go, text="""
        Items deleted would not be recovereable.""", font=('Helvetica', 12, ''), background = "#E4E4E4")
        lb.grid(row=1, column=0,  columnspan=3,sticky='w', padx=5, pady=5)

        def del_tree():
            selected_item =tree4.selection()[0]
            tree4.delete(selected_item)
            lost4 = (ents.get() + "", ento.get() + "")
            # tree serialization
            with open(umaga, "w") as f:
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
with open(umaga, "r") as f:
    dany4= yaml.load(f)

tree4 = ttk.Treeview(w1, columns=(1, 0), displaycolumns=(0, 1,), height=2, selectmode='browse',
                     show='headings')
tree4.heading('#0', text='Itemo')
tree4.heading('#1', text='Item')
tree4.heading('#2', text='Price')
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
        data.geometry("450x150-410+280")
        data.minsize("440", "120")
        data.maxsize("440", "120")
        data.title("Add Data")
        data.config(background="lavender")

        ent = StringVar()
        ent1 = StringVar()

        lab = ttk.Label(data, text="Item (Input the new Item): ", font=('', 12, ''), background="lavender")
        lab.grid(row=0, column=0, padx=5, pady=5)

        lab1 = ttk.Label(data, text="Price (Input the new Price): ", font=('', 12, ''), background="lavender")
        lab1.grid(row=1, column=0, padx=5, pady=5)



        def add_up():
            # i = 0
            hala5 = (ents.get() + "GHC", ento.get() + "KG")
            tree5.insert('', 'end', values=hala5)

            # tree serialization
            with open(cena, "w") as f:
                yaml.dump(hala5, f)

            tkMessageBox.showinfo("Add New Item", "You have succesfully added new entries.")
            # i + 1

        ento = ttk.Entry(data, width=20, font=('arial', 12, ''))
        ento.grid(row=0, column=1)

        ents = ttk.Entry(data, width=20, font=('arial', 12, ''))
        ents.grid(row=1, column=1)

        seph = ttk.Separator(data, orient='horizontal')
        # sep.pack(side = BOTTOM)e
        seph.grid(row=2, column=0, sticky='n,w,e,s', columnspan=2, ipadx=200, ipady=1, padx=5, pady=5)

        btn = ttk.Button(data, text="OK", style='Wild.TButton', command=add_up)
        btn.grid(row=3, column=0, sticky='E', padx=5, pady=1)

        btn1 = ttk.Button(data, text="Cancel", command=data.destroy)
        btn1.grid(row=3, column=1, sticky='W', padx=5, pady=1)

    except:
        tkMessageBox.showerror("Add New Item", "Add new Item failed. Please check input.")
    finally:
        clear()


def sub_all5():
    try:
        datum = Toplevel(height="200", width="770", relief="flat")
        datum.geometry("460x150-410+280")
        datum.minsize("450", "120")
        datum.maxsize("450", "120")
        datum.title("Edit Data")
        datum.config(background="lavender")

        ent = StringVar()
        ent1 = StringVar()

        lab = ttk.Label(datum, text="Item (Edit the selected Item): ", font=('', 12, ''), background="lavender")
        lab.grid(row=0, column=0, padx=5, pady=5)

        lab1 = ttk.Label(datum, text="Price (Edit the price): ", font=('', 12, ''), background="lavender")
        lab1.grid(row=1, column=0, padx=5, pady=5)

        ento = StringVar()
        ents = StringVar()

        def add_up():
            hala5 = (ents.get() + "GHC", ento.get() + "KG")
            tree5.insert('', 'end', values=hala5)

            # tree serialization
            with open(cena, "w") as f:
                yaml.dump(hala5, f)
            tkMessageBox.showinfo("Edit Item", "You have succesfully edited the entries.")
            # i + 1

        ento = ttk.Entry(datum, width=20, font=('arial', 12, ''))
        ento.grid(row=0, column=1)

        ents = ttk.Entry(datum, width=20, font=('arial', 12, ''))
        ents.grid(row=1, column=1)

        seph = ttk.Separator(datum, orient='horizontal')
        # sep.pack(side = BOTTOM)e
        seph.grid(row=2, column=0, sticky='n,w,e,s', columnspan=2, ipadx=200, ipady=1, padx=5, pady=5)

        btn = ttk.Button(datum, text="OK", style='Wild.TButton', command=add_up)
        btn.grid(row=3, column=0, sticky='E', padx=5, pady=1)

        btn1 = ttk.Button(datum, text="Cancel", command=datum.destroy)
        btn1.grid(row=3, column=1, sticky='W', padx=5, pady=1)

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

        lb = ttk.Label(go, text="""Are you sure you want to permanetly delete this item?""", font=('Helvetica', 12, 'bold'), background = "#E4E4E4")
        lb.grid(row=0, column=0,  columnspan=2,sticky='w')

        lb = ttk.Label(go, text="""
        Items deleted would not be recovereable.""", font=('Helvetica', 12, ''), background = "#E4E4E4")
        lb.grid(row=1, column=0,  columnspan=3,sticky='w', padx=5, pady=5)

        def del_tree():
            selected_item =tree5.selection()[0]
            tree5.delete(selected_item)
            lost5 = (ents.get() + "", ento.get() + "")
            # tree serialization
            with open(cena, "w") as f:
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
with open(cena, "r") as f:
    dany5= yaml.load(f)

tree5 = ttk.Treeview(w1, columns=(1, 0), displaycolumns=(0, 1,), height=2, selectmode='browse',
                     show='headings')
tree5.heading('#0', text='Itemo')
tree5.heading('#1', text='Item')
tree5.heading('#2', text='Price')
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
        data.geometry("450x150-410+280")
        data.minsize("440", "120")
        data.maxsize("440", "120")
        data.title("Add Data")
        data.config(background="lavender")

        ent = StringVar()
        ent1 = StringVar()

        lab = ttk.Label(data, text="Item (Input the new Item): ", font=('', 12, ''), background="lavender")
        lab.grid(row=0, column=0, padx=5, pady=5)

        lab1 = ttk.Label(data, text="Price (Input the new Price): ", font=('', 12, ''), background="lavender")
        lab1.grid(row=1, column=0, padx=5, pady=5)



        def add_up():
            # i = 0
            hala6 = (ents.get() + "GHC", ento.get() + "KG")
            tree6.insert('', 'end', values=hala6)

            # tree serialization
            with open(van, "w") as f:
                yaml.dump(hala6, f)

            tkMessageBox.showinfo("Add New Item", "You have succesfully added new entries.")
            # i + 1

        ento = ttk.Entry(data, width=20, font=('arial', 12, ''))
        ento.grid(row=0, column=1)

        ents = ttk.Entry(data, width=20, font=('arial', 12, ''))
        ents.grid(row=1, column=1)

        seph = ttk.Separator(data, orient='horizontal')
        # sep.pack(side = BOTTOM)e
        seph.grid(row=2, column=0, sticky='n,w,e,s', columnspan=2, ipadx=200, ipady=1, padx=5, pady=5)

        btn = ttk.Button(data, text="OK", style='Wild.TButton', command=add_up)
        btn.grid(row=3, column=0, sticky='E', padx=5, pady=1)

        btn1 = ttk.Button(data, text="Cancel", command=data.destroy)
        btn1.grid(row=3, column=1, sticky='W', padx=5, pady=1)

    except:
        tkMessageBox.showerror("Add New Item", "Add new Item failed. Please check input.")
    finally:
        clear()


def sub_all6():
    try:
        datum = Toplevel(height="200", width="770", relief="flat")
        datum.geometry("460x150-410+280")
        datum.minsize("450", "120")
        datum.maxsize("450", "120")
        datum.title("Edit Data")
        datum.config(background="lavender")

        ent = StringVar()
        ent1 = StringVar()

        lab = ttk.Label(datum, text="Item (Edit the selected Item): ", font=('', 12, ''), background="lavender")
        lab.grid(row=0, column=0, padx=5, pady=5)

        lab1 = ttk.Label(datum, text="Price (Edit the price): ", font=('', 12, ''), background="lavender")
        lab1.grid(row=1, column=0, padx=5, pady=5)

        ento = StringVar()
        ents = StringVar()

        def add_up():
            hala6 = (ents.get() + "GHC", ento.get() + "KG")
            tree6.insert('', 'end', values=hala6)

            # tree serialization
            with open(van, "w") as f:
                yaml.dump(hala6, f)
            tkMessageBox.showinfo("Edit Item", "You have succesfully edited the entries.")
            # i + 1

        ento = ttk.Entry(datum, width=20, font=('arial', 12, ''))
        ento.grid(row=0, column=1)

        ents = ttk.Entry(datum, width=20, font=('arial', 12, ''))
        ents.grid(row=1, column=1)

        seph = ttk.Separator(datum, orient='horizontal')
        # sep.pack(side = BOTTOM)e
        seph.grid(row=2, column=0, sticky='n,w,e,s', columnspan=2, ipadx=200, ipady=1, padx=5, pady=5)

        btn = ttk.Button(datum, text="OK", style='Wild.TButton', command=add_up)
        btn.grid(row=3, column=0, sticky='E', padx=5, pady=1)

        btn1 = ttk.Button(datum, text="Cancel", command=datum.destroy)
        btn1.grid(row=3, column=1, sticky='W', padx=5, pady=1)

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

        lb = ttk.Label(go, text="""Are you sure you want to permanetly delete this item?""", font=('Helvetica', 12, 'bold'), background = "#E4E4E4")
        lb.grid(row=0, column=0,  columnspan=2,sticky='w')

        lb = ttk.Label(go, text="""
        Items deleted would not be recovereable.""", font=('Helvetica', 12, ''), background = "#E4E4E4")
        lb.grid(row=1, column=0,  columnspan=3,sticky='w', padx=5, pady=5)

        def del_tree():
            selected_item =tree6.selection()[0]
            tree6.delete(selected_item)
            lost6 = (ents.get() + "", ento.get() + "")
            # tree serialization
            with open(van, "w") as f:
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
with open(van, "r") as f:
    dany6= yaml.load(f)
tree6 = ttk.Treeview(w1, columns=(1, 0), displaycolumns=(0, 1,), height=2, selectmode='browse',
                     show='headings')
tree6.heading('#0', text='Itemo')
tree6.heading('#1', text='Item')
tree6.heading('#2', text='Price')
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
        data.geometry("450x150-410+280")
        data.minsize("440", "120")
        data.maxsize("440", "120")
        data.title("Add Data")
        data.config(background="lavender")

        ent = StringVar()
        ent1 = StringVar()

        lab = ttk.Label(data, text="Item (Input the new Item): ", font=('', 12, ''), background="lavender")
        lab.grid(row=0, column=0, padx=5, pady=5)

        lab1 = ttk.Label(data, text="Price (Input the new Price): ", font=('', 12, ''), background="lavender")
        lab1.grid(row=1, column=0, padx=5, pady=5)



        def add_up():
            # i = 0
            hala7 = (ents.get() + "GHC", ento.get() + "KG")
            tree7.insert('', 'end', values=hala7)

            # tree serialization
            with open(king, "w") as f:
                yaml.dump(hala7, f)

            tkMessageBox.showinfo("Add New Item", "You have succesfully added new entries.")
            # i + 1

        ento = ttk.Entry(data, width=20, font=('arial', 12, ''))
        ento.grid(row=0, column=1)

        ents = ttk.Entry(data, width=20, font=('arial', 12, ''))
        ents.grid(row=1, column=1)

        seph = ttk.Separator(data, orient='horizontal')
        # sep.pack(side = BOTTOM)e
        seph.grid(row=2, column=0, sticky='n,w,e,s', columnspan=2, ipadx=200, ipady=1, padx=5, pady=5)

        btn = ttk.Button(data, text="OK", style='Wild.TButton', command=add_up)
        btn.grid(row=3, column=0, sticky='E', padx=5, pady=1)

        btn1 = ttk.Button(data, text="Cancel", command=data.destroy)
        btn1.grid(row=3, column=1, sticky='W', padx=5, pady=1)

    except:
        tkMessageBox.showerror("Add New Item", "Add new Item failed. Please check input.")
    finally:
        clear()


def sub_all7():
    try:
        datum = Toplevel(height="200", width="770", relief="flat")
        datum.geometry("460x150-410+280")
        datum.minsize("450", "120")
        datum.maxsize("450", "120")
        datum.title("Edit Data")
        datum.config(background="lavender")

        ent = StringVar()
        ent1 = StringVar()

        lab = ttk.Label(datum, text="Item (Edit the selected Item): ", font=('', 12, ''), background="lavender")
        lab.grid(row=0, column=0, padx=5, pady=5)

        lab1 = ttk.Label(datum, text="Price (Edit the price): ", font=('', 12, ''), background="lavender")
        lab1.grid(row=1, column=0, padx=5, pady=5)

        ento = StringVar()
        ents = StringVar()

        def add_up():
            hala7 = (ents.get() + "GHC", ento.get() + "KG")
            tree7.insert('', 'end', values=hala7)

            # tree serialization
            with open(king, "w") as f:
                yaml.dump(hala7, f)
            tkMessageBox.showinfo("Edit Item", "You have succesfully edited the entries.")
            # i + 1

        ento = ttk.Entry(datum, width=20, font=('arial', 12, ''))
        ento.grid(row=0, column=1)

        ents = ttk.Entry(datum, width=20, font=('arial', 12, ''))
        ents.grid(row=1, column=1)

        seph = ttk.Separator(datum, orient='horizontal')
        # sep.pack(side = BOTTOM)e
        seph.grid(row=2, column=0, sticky='n,w,e,s', columnspan=2, ipadx=200, ipady=1, padx=5, pady=5)

        btn = ttk.Button(datum, text="OK", style='Wild.TButton', command=add_up)
        btn.grid(row=3, column=0, sticky='E', padx=5, pady=1)

        btn1 = ttk.Button(datum, text="Cancel", command=datum.destroy)
        btn1.grid(row=3, column=1, sticky='W', padx=5, pady=1)

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

        lb = ttk.Label(go, text="""Are you sure you want to permanetly delete this item?""", font=('Helvetica', 12, 'bold'), background = "#E4E4E4")
        lb.grid(row=0, column=0,  columnspan=2,sticky='w')

        lb = ttk.Label(go, text="""
        Items deleted would not be recovereable.""", font=('Helvetica', 12, ''), background = "#E4E4E4")
        lb.grid(row=1, column=0,  columnspan=3,sticky='w', padx=5, pady=5)

        def del_tree():
            selected_item =tree7.selection()[0]
            tree7.delete(selected_item)
            lost7 = (ents.get() + "", ento.get() + "")
            # tree serialization
            with open(king, "w") as f:
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
with open(king, "r") as f:
    dany7= yaml.load(f)

tree7 = ttk.Treeview(w1, columns=(1, 0), displaycolumns=(0, 1,), height=2, selectmode='browse',
                     show='headings')
tree7.heading('#0', text='Itemo')
tree7.heading('#1', text='Item')
tree7.heading('#2', text='Price')
tree7.insert('','end', text = "Item", values=dany7)
tree7.grid(row=9, column=0, padx=1, pady=5, sticky='w')
i = 0
b23 = ttk.Button(w1, text='+', command=add_all7, style = "Mini.TButton")
b23.grid(row=9, column=1, rowspan = 1,padx=5, pady=5, )
b24 = ttk.Button(w1, text='...', command=sub_all7, style = "Mini.TButton")
b24.grid(row=9, column=2,  padx=5, pady=5, )
b25 = ttk.Button(w1, text='-', command=iexits7, style = "Minis.TButton")
b25.grid(row=9, column=4, padx=5, pady=5, )

lb2 = ttk.Label(w1, text="""      Tips: In order to see changes take effect, please restart apllication. Thank you.""", font=('DejaVu Sans Mono', 11, ''), background = '#E4E4E4')
lb2.grid(row=1, column=6, columnspan = 9,sticky='e')

# We do more here. The serialization of our tree view widgets===========================================================
def add_all8():
    try:
        data = Toplevel(height="300", width="730", relief="flat")
        data.geometry("450x150-410+280")
        data.minsize("440", "120")
        data.maxsize("440", "120")
        data.title("Add Data")
        data.config(background="lavender")

        ent = StringVar()
        ent1 = StringVar()

        lab = ttk.Label(data, text="Item (Input the new Item): ", font=('', 12, ''), background="lavender")
        lab.grid(row=0, column=0, padx=5, pady=5)

        lab1 = ttk.Label(data, text="Price (Input the new Price): ", font=('', 12, ''), background="lavender")
        lab1.grid(row=1, column=0, padx=5, pady=5)



        def add_up():
            # i = 0
            hala8= (ents.get() + "GHC", ento.get() + "KG")
            tree8.insert('', 'end', values=hala8)

            # tree serialization
            with open(yon, "w") as f:
                yaml.dump(hala8, f)

            tkMessageBox.showinfo("Add New Item", "You have succesfully added new entries.")
            # i + 1

        ento = ttk.Entry(data, width=20, font=('arial', 12, ''))
        ento.grid(row=0, column=1)

        ents = ttk.Entry(data, width=20, font=('arial', 12, ''))
        ents.grid(row=1, column=1)

        seph = ttk.Separator(data, orient='horizontal')
        # sep.pack(side = BOTTOM)e
        seph.grid(row=2, column=0, sticky='n,w,e,s', columnspan=2, ipadx=200, ipady=1, padx=5, pady=5)

        btn = ttk.Button(data, text="OK", style='Wild.TButton', command=add_up)
        btn.grid(row=3, column=0, sticky='E', padx=5, pady=1)

        btn1 = ttk.Button(data, text="Cancel", command=data.destroy)
        btn1.grid(row=3, column=1, sticky='W', padx=5, pady=1)

    except:
        tkMessageBox.showerror("Add New Item", "Add new Item failed. Please check input.")
    finally:
        clear()


def sub_all8():
    try:
        datum = Toplevel(height="200", width="770", relief="flat")
        datum.geometry("460x150-410+280")
        datum.minsize("450", "120")
        datum.maxsize("450", "120")
        datum.title("Edit Data")
        datum.config(background="lavender")

        ent = StringVar()
        ent1 = StringVar()

        lab = ttk.Label(datum, text="Item (Edit the selected Item): ", font=('', 12, ''), background="lavender")
        lab.grid(row=0, column=0, padx=5, pady=5)

        lab1 = ttk.Label(datum, text="Price (Edit the price): ", font=('', 12, ''), background="lavender")
        lab1.grid(row=1, column=0, padx=5, pady=5)

        ento = StringVar()
        ents = StringVar()

        def add_up():
            hala8 = (ents.get() + "GHC", ento.get() + "KG")
            tree8.insert('', 'end', values=hala8)

            # tree serialization
            with open(yon, "w") as f:
                yaml.dump(hala8, f)
            tkMessageBox.showinfo("Edit Item", "You have succesfully edited the entries.")
            # i + 1

        ento = ttk.Entry(datum, width=20, font=('arial', 12, ''))
        ento.grid(row=0, column=1)

        ents = ttk.Entry(datum, width=20, font=('arial', 12, ''))
        ents.grid(row=1, column=1)

        seph = ttk.Separator(datum, orient='horizontal')
        # sep.pack(side = BOTTOM)e
        seph.grid(row=2, column=0, sticky='n,w,e,s', columnspan=2, ipadx=200, ipady=1, padx=5, pady=5)

        btn = ttk.Button(datum, text="OK", style='Wild.TButton', command=add_up)
        btn.grid(row=3, column=0, sticky='E', padx=5, pady=1)

        btn1 = ttk.Button(datum, text="Cancel", command=datum.destroy)
        btn1.grid(row=3, column=1, sticky='W', padx=5, pady=1)

    except:
        tkMessageBox.showerror("Add New Item", "Add new Item failed. Please check input.")
    finally:
        clear()

def iexits8():
        go = Toplevel(height="400", width="500", relief="flat")
        go.geometry("465x125-450+300")
#        go.minsize("485", "160")
#        go.maxsize("485", "160")
        go.title("Delete")
        go.resizable(0,0)
        go.config(background = "#E4E4E4")
#        go.overrideredirect(True)
        go.attributes("-toolwindow", 1)

        lb = ttk.Label(go, text="""Are you sure you want to permanetly delete this item?""", font=('Helvetica', 12, 'bold'), background = "#E4E4E4")
        lb.grid(row=0, column=0,  columnspan=2,sticky='w')

        lb = ttk.Label(go, text="""
        Items deleted would not be recovereable.""", font=('Helvetica', 12, ''), background = "#E4E4E4")
        lb.grid(row=1, column=0,  columnspan=3,sticky='w', padx=5, pady=5)

        def del_tree():
            selected_item =tree8.selection()[0]
            tree8.delete(selected_item)
            lost8 = (ents.get() + "", ento.get() + "")
            # tree serialization
            with open(yon, "w") as f:
               yaml.dump(lost8, f)
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
with open(yon, "r") as f:
    dany8= yaml.load(f)

tree8 = ttk.Treeview(w1, columns=(1, 0), displaycolumns=(0, 1,), height=2, selectmode='browse',
                     show='headings')
tree8.heading('#0', text='Itemo')
tree8.heading('#1', text='Item')
tree8.heading('#2', text='Price')
tree8.insert('','end', text = "Item", values=dany8)
tree8.grid(row=2, column=7, columnspan=1, padx=40, pady=5, sticky='n,e,s,w')
i = 0
b26 = ttk.Button(w1, text='+', command=add_all8, style = "Mini.TButton")
b26.grid(row=2, column=8,  padx=5, pady=5,sticky='w')
b27 = ttk.Button(w1, text='...', command=sub_all8, style = "Mini.TButton")
b27.grid(row=2, column=9, padx=5, pady=5,sticky='w')
b28 = ttk.Button(w1, text='-', command=iexits8, style = "Minis.TButton")
b28.grid(row=2, column=10, padx=5, pady=5,sticky='w')

# Lets move on with what we're doing. Serializing into our yaml file====================================================
def add_all9():
    try:
        data = Toplevel(height="300", width="730", relief="flat")
        data.geometry("450x150-410+280")
        data.minsize("440", "120")
        data.maxsize("440", "120")
        data.title("Add Data")
        data.config(background="lavender")

        ent = StringVar()
        ent1 = StringVar()

        lab = ttk.Label(data, text="Item (Input the new Item): ", font=('', 12, ''), background="lavender")
        lab.grid(row=0, column=0, padx=5, pady=5)

        lab1 = ttk.Label(data, text="Price (Input the new Price): ", font=('', 12, ''), background="lavender")
        lab1.grid(row=1, column=0, padx=5, pady=5)



        def add_up():
            # i = 0
            hala9 = (ents.get() + "GHC", ento.get() + "KG")
            tree9.insert('', 'end', values=hala9)

            # tree serialization
            with open(josh, "w") as f:
                yaml.dump(hala9, f)

            tkMessageBox.showinfo("Add New Item", "You have succesfully added new entries.")
            # i + 1

        ento = ttk.Entry(data, width=20, font=('arial', 12, ''))
        ento.grid(row=0, column=1)

        ents = ttk.Entry(data, width=20, font=('arial', 12, ''))
        ents.grid(row=1, column=1)

        seph = ttk.Separator(data, orient='horizontal')
        # sep.pack(side = BOTTOM)e
        seph.grid(row=2, column=0, sticky='n,w,e,s', columnspan=2, ipadx=200, ipady=1, padx=5, pady=5)

        btn = ttk.Button(data, text="OK", style='Wild.TButton', command=add_up)
        btn.grid(row=3, column=0, sticky='E', padx=5, pady=1)

        btn1 = ttk.Button(data, text="Cancel", command=data.destroy)
        btn1.grid(row=3, column=1, sticky='W', padx=5, pady=1)

    except:
        tkMessageBox.showerror("Add New Item", "Add new Item failed. Please check input.")
    finally:
        clear()


def sub_all9():
    try:
        datum = Toplevel(height="200", width="770", relief="flat")
        datum.geometry("460x150-410+280")
        datum.minsize("450", "120")
        datum.maxsize("450", "120")
        datum.title("Edit Data")
        datum.config(background="lavender")

        ent = StringVar()
        ent1 = StringVar()

        lab = ttk.Label(datum, text="Item (Edit the selected Item): ", font=('', 12, ''), background="lavender")
        lab.grid(row=0, column=0, padx=5, pady=5)

        lab1 = ttk.Label(datum, text="Price (Edit the price): ", font=('', 12, ''), background="lavender")
        lab1.grid(row=1, column=0, padx=5, pady=5)

        ento = StringVar()
        ents = StringVar()

        def add_up():
            hala9 = (ents.get() + "GHC", ento.get() + "KG")
            tree9.insert('', 'end', values=hala9)

            # tree serialization
            with open(josh, "w") as f:
                yaml.dump(hala9, f)
            tkMessageBox.showinfo("Edit Item", "You have succesfully edited the entries.")
            # i + 1

        ento = ttk.Entry(datum, width=20, font=('arial', 12, ''))
        ento.grid(row=0, column=1)

        ents = ttk.Entry(datum, width=20, font=('arial', 12, ''))
        ents.grid(row=1, column=1)

        seph = ttk.Separator(datum, orient='horizontal')
        # sep.pack(side = BOTTOM)e
        seph.grid(row=2, column=0, sticky='n,w,e,s', columnspan=2, ipadx=200, ipady=1, padx=5, pady=5)

        btn = ttk.Button(datum, text="OK", style='Wild.TButton', command=add_up)
        btn.grid(row=3, column=0, sticky='E', padx=5, pady=1)

        btn1 = ttk.Button(datum, text="Cancel", command=datum.destroy)
        btn1.grid(row=3, column=1, sticky='W', padx=5, pady=1)

    except:
        tkMessageBox.showerror("Add New Item", "Add new Item failed. Please check input.")
    finally:
        clear()

def iexits9():
        go = Toplevel(height="400", width="500", relief="flat")
        go.geometry("465x125-450+300")
#        go.minsize("485", "160")
#        go.maxsize("485", "160")
        go.title("Delete")
        go.resizable(0,0)
        go.config(background = "#E4E4E4")
#        go.overrideredirect(True)
        go.attributes("-toolwindow", 1)

        lb = ttk.Label(go, text="""Are you sure you want to permanetly delete this item?""", font=('Helvetica', 12, 'bold'), background = "#E4E4E4")
        lb.grid(row=0, column=0,  columnspan=2,sticky='w')

        lb = ttk.Label(go, text="""
        Items deleted would not be recovereable.""", font=('Helvetica', 12, ''), background = "#E4E4E4")
        lb.grid(row=1, column=0,  columnspan=3,sticky='w', padx=5, pady=5)

        def del_tree():
            selected_item =tree9.selection()[0]
            tree9.delete(selected_item)
            lost9 = (ents.get() + "", ento.get() + "")
            # tree serialization
            with open(josh, "w") as f:
               yaml.dump(lost9, f)
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
with open(josh, "r") as f:
    dany9= yaml.load(f)

tree9 = ttk.Treeview(w1, columns=(1, 0), displaycolumns=(0, 1,), height=2, selectmode='browse',
                     show='headings')
tree9.heading('#0', text='Itemo')
tree9.heading('#1', text='Item')
tree9.heading('#2', text='Price')
tree9.insert('','end', text = "Item", values=dany9)
tree9.grid(row=3, column=7, columnspan=1, padx=40, pady=5, sticky='n,e,s,w')
i = 0
b29 = ttk.Button(w1, text='+', command=add_all9, style = "Mini.TButton")
b29.grid(row=3, column=8,  padx=5, pady=5,sticky='w')
b30 = ttk.Button(w1, text='...', command=sub_all9, style = "Mini.TButton")
b30.grid(row=3, column=9, padx=5, pady=5,sticky='w')
b31 = ttk.Button(w1, text='-', command=iexits9, style = "Minis.TButton")
b31.grid(row=3, column=10, padx=5, pady=5,sticky='w')

#=========================Game on Boys==================================================================================
def add_all10():
    try:
        data = Toplevel(height="300", width="730", relief="flat")
        data.geometry("450x150-410+280")
        data.minsize("440", "120")
        data.maxsize("440", "120")
        data.title("Add Data")
        data.config(background="lavender")

        ent = StringVar()
        ent1 = StringVar()

        lab = ttk.Label(data, text="Item (Input the new Item): ", font=('', 12, ''), background="lavender")
        lab.grid(row=0, column=0, padx=5, pady=5)

        lab1 = ttk.Label(data, text="Price (Input the new Price): ", font=('', 12, ''), background="lavender")
        lab1.grid(row=1, column=0, padx=5, pady=5)



        def add_up():
            # i = 0
            hala10 = (ents.get() + "GHC", ento.get() + "KG")
            tree10.insert('', 'end', values=hala10)

            # tree serialization
            with open(wrest, "w") as f:
                yaml.dump(hala10, f)

            tkMessageBox.showinfo("Add New Item", "You have succesfully added new entries.")
            # i + 1

        ento = ttk.Entry(data, width=20, font=('arial', 12, ''))
        ento.grid(row=0, column=1)

        ents = ttk.Entry(data, width=20, font=('arial', 12, ''))
        ents.grid(row=1, column=1)

        seph = ttk.Separator(data, orient='horizontal')
        # sep.pack(side = BOTTOM)e
        seph.grid(row=2, column=0, sticky='n,w,e,s', columnspan=2, ipadx=200, ipady=1, padx=5, pady=5)

        btn = ttk.Button(data, text="OK", style='Wild.TButton', command=add_up)
        btn.grid(row=3, column=0, sticky='E', padx=5, pady=1)

        btn1 = ttk.Button(data, text="Cancel", command=data.destroy)
        btn1.grid(row=3, column=1, sticky='W', padx=5, pady=1)

    except:
        tkMessageBox.showerror("Add New Item", "Add new Item failed. Please check input.")
    finally:
        clear()


def sub_all10():
    try:
        datum = Toplevel(height="200", width="770", relief="flat")
        datum.geometry("460x150-410+280")
        datum.minsize("450", "120")
        datum.maxsize("450", "120")
        datum.title("Edit Data")
        datum.config(background="lavender")

        ent = StringVar()
        ent1 = StringVar()

        lab = ttk.Label(datum, text="Item (Edit the selected Item): ", font=('', 12, ''), background="lavender")
        lab.grid(row=0, column=0, padx=5, pady=5)

        lab1 = ttk.Label(datum, text="Price (Edit the price): ", font=('', 12, ''), background="lavender")
        lab1.grid(row=1, column=0, padx=5, pady=5)

        ento = StringVar()
        ents = StringVar()

        def add_up():
            hala10 = (ents.get() + "GHC", ento.get() + "KG")
            tree10.insert('', 'end', values=hala10)

            # tree serialization
            with open(wrest, "w") as f:
                yaml.dump(hala10, f)
            tkMessageBox.showinfo("Edit Item", "You have succesfully edited the entries.")
            # i + 1

        ento = ttk.Entry(datum, width=20, font=('arial', 12, ''))
        ento.grid(row=0, column=1)

        ents = ttk.Entry(datum, width=20, font=('arial', 12, ''))
        ents.grid(row=1, column=1)

        seph = ttk.Separator(datum, orient='horizontal')
        # sep.pack(side = BOTTOM)e
        seph.grid(row=2, column=0, sticky='n,w,e,s', columnspan=2, ipadx=200, ipady=1, padx=5, pady=5)

        btn = ttk.Button(datum, text="OK", style='Wild.TButton', command=add_up)
        btn.grid(row=3, column=0, sticky='E', padx=5, pady=1)

        btn1 = ttk.Button(datum, text="Cancel", command=datum.destroy)
        btn1.grid(row=3, column=1, sticky='W', padx=5, pady=1)

    except:
        tkMessageBox.showerror("Add New Item", "Add new Item failed. Please check input.")
    finally:
        clear()

def iexits10():
        go = Toplevel(height="400", width="500", relief="flat")
        go.geometry("465x125-450+300")
#        go.minsize("485", "160")
#        go.maxsize("485", "160")
        go.title("Delete")
        go.resizable(0,0)
        go.config(background = "#E4E4E4")
#        go.overrideredirect(True)
        go.attributes("-toolwindow", 1)

        lb = ttk.Label(go, text="""Are you sure you want to permanetly delete this item?""", font=('Helvetica', 12, 'bold'), background = "#E4E4E4")
        lb.grid(row=0, column=0,  columnspan=2,sticky='w')

        lb = ttk.Label(go, text="""
        Items deleted would not be recovereable.""", font=('Helvetica', 12, ''), background = "#E4E4E4")
        lb.grid(row=1, column=0,  columnspan=3,sticky='w', padx=5, pady=5)

        def del_tree():
            selected_item =tree10.selection()[0]
            tree10.delete(selected_item)
            lost10 = (ents.get() + "", ento.get() + "")
            # tree serialization
            with open(wrest, "w") as f:
               yaml.dump(lost10, f)
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
with open(wrest, "r") as f:
    dany10= yaml.load(f)

tree10 = ttk.Treeview(w1, columns=(1, 0), displaycolumns=(0, 1,), height=2, selectmode='browse',
                     show='headings')
tree10.heading('#0', text='Itemo')
tree10.heading('#1', text='Item')
tree10.heading('#2', text='Price')
tree10.insert('','end', text = "Item", values=dany10)
tree10.grid(row=4, column=7, columnspan=1, padx=40, pady=5, sticky='n,e,s,w')
i = 0
b32 = ttk.Button(w1, text='+', command=add_all10, style = "Mini.TButton")
b32.grid(row=4, column=8,  padx=5, pady=5,sticky='w')
b33 = ttk.Button(w1, text='...', command=sub_all10, style = "Mini.TButton")
b33.grid(row=4, column=9, padx=5, pady=5,sticky='w')
b34 = ttk.Button(w1, text='-', command=iexits10, style = "Minis.TButton")
b34.grid(row=4, column=10, padx=5, pady=5,sticky='w')

#=======================================================================================================================
def add_all11():
    try:
        data = Toplevel(height="300", width="730", relief="flat")
        data.geometry("450x150-410+280")
        data.minsize("440", "120")
        data.maxsize("440", "120")
        data.title("Add Data")
        data.config(background="lavender")

        ent = StringVar()
        ent1 = StringVar()

        lab = ttk.Label(data, text="Item (Input the new Item): ", font=('', 12, ''), background="lavender")
        lab.grid(row=0, column=0, padx=5, pady=5)

        lab1 = ttk.Label(data, text="Price (Input the new Price): ", font=('', 12, ''), background="lavender")
        lab1.grid(row=1, column=0, padx=5, pady=5)



        def add_up():
            # i = 0
            hala11 = (ents.get() + "GHC", ento.get() + "KG")
            tree11.insert('', 'end', values=hala11)

            # tree serialization
            with open(hum, "w") as f:
                yaml.dump(hala11, f)

            tkMessageBox.showinfo("Add New Item", "You have succesfully added new entries.")
            # i + 1

        ento = ttk.Entry(data, width=20, font=('arial', 12, ''))
        ento.grid(row=0, column=1)

        ents = ttk.Entry(data, width=20, font=('arial', 12, ''))
        ents.grid(row=1, column=1)

        seph = ttk.Separator(data, orient='horizontal')
        # sep.pack(side = BOTTOM)e
        seph.grid(row=2, column=0, sticky='n,w,e,s', columnspan=2, ipadx=200, ipady=1, padx=5, pady=5)

        btn = ttk.Button(data, text="OK", style='Wild.TButton', command=add_up)
        btn.grid(row=3, column=0, sticky='E', padx=5, pady=1)

        btn1 = ttk.Button(data, text="Cancel", command=data.destroy)
        btn1.grid(row=3, column=1, sticky='W', padx=5, pady=1)

    except:
        tkMessageBox.showerror("Add New Item", "Add new Item failed. Please check input.")
    finally:
        clear()


def sub_all11():
    try:
        datum = Toplevel(height="200", width="770", relief="flat")
        datum.geometry("460x150-410+280")
        datum.minsize("450", "120")
        datum.maxsize("450", "120")
        datum.title("Edit Data")
        datum.config(background="lavender")

        ent = StringVar()
        ent1 = StringVar()

        lab = ttk.Label(datum, text="Item (Edit the selected Item): ", font=('', 12, ''), background="lavender")
        lab.grid(row=0, column=0, padx=5, pady=5)

        lab1 = ttk.Label(datum, text="Price (Edit the price): ", font=('', 12, ''), background="lavender")
        lab1.grid(row=1, column=0, padx=5, pady=5)

        ento = StringVar()
        ents = StringVar()

        def add_up():
            hala11 = (ents.get() + "GHC", ento.get() + "KG")
            tree11.insert('', 'end', values=hala11)

            # tree serialization
            with open(hum, "w") as f:
                yaml.dump(hala11, f)
            tkMessageBox.showinfo("Edit Item", "You have succesfully edited the entries.")
            # i + 1

        ento = ttk.Entry(datum, width=20, font=('arial', 12, ''))
        ento.grid(row=0, column=1)

        ents = ttk.Entry(datum, width=20, font=('arial', 12, ''))
        ents.grid(row=1, column=1)

        seph = ttk.Separator(datum, orient='horizontal')
        # sep.pack(side = BOTTOM)e
        seph.grid(row=2, column=0, sticky='n,w,e,s', columnspan=2, ipadx=200, ipady=1, padx=5, pady=5)

        btn = ttk.Button(datum, text="OK", style='Wild.TButton', command=add_up)
        btn.grid(row=3, column=0, sticky='E', padx=5, pady=1)

        btn1 = ttk.Button(datum, text="Cancel", command=datum.destroy)
        btn1.grid(row=3, column=1, sticky='W', padx=5, pady=1)

    except:
        tkMessageBox.showerror("Add New Item", "Add new Item failed. Please check input.")
    finally:
        clear()

def iexits11():
        go = Toplevel(height="400", width="500", relief="flat")
        go.geometry("465x125-450+300")
#        go.minsize("485", "160")
#        go.maxsize("485", "160")
        go.title("Delete")
        go.resizable(0,0)
        go.config(background = "#E4E4E4")
#        go.overrideredirect(True)
        go.attributes("-toolwindow", 1)

        lb = ttk.Label(go, text="""Are you sure you want to permanetly delete this item?""", font=('Helvetica', 12, 'bold'), background = "#E4E4E4")
        lb.grid(row=0, column=0,  columnspan=2,sticky='w')

        lb = ttk.Label(go, text="""
        Items deleted would not be recovereable.""", font=('Helvetica', 12, ''), background = "#E4E4E4")
        lb.grid(row=1, column=0,  columnspan=3,sticky='w', padx=5, pady=5)

        def del_tree():
            selected_item =tree11.selection()[0]
            tree11.delete(selected_item)
            lost11 = (ents.get() + "", ento.get() + "")
            # tree serialization
            with open(hum, "w") as f:
               yaml.dump(lost11, f)
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
with open(hum, "r") as f:
    dany11= yaml.load(f)

tree11 = ttk.Treeview(w1, columns=(1, 0), displaycolumns=(0, 1,), height=2, selectmode='browse',
                     show='headings')
tree11.heading('#0', text='Itemo')
tree11.heading('#1', text='Item')
tree11.heading('#2', text='Price')
tree11.insert('','end', text = "Item", values=dany11)
tree11.grid(row=5, column=7, columnspan=1, padx=40, pady=5, sticky='n,e,s,w')
i = 0
b35 = ttk.Button(w1, text='+', command=add_all11, style = "Mini.TButton")
b35.grid(row=5, column=8,  padx=5, pady=5,sticky='w')
b36 = ttk.Button(w1, text='...', command=sub_all11, style = "Mini.TButton")
b36.grid(row=5, column=9, padx=5, pady=5,sticky='w')
b37 = ttk.Button(w1, text='-', command=iexits11, style = "Minis.TButton")
b37.grid(row=5, column=10, padx=5, pady=5,sticky='w')

#=========================We move on Dawn===============================================================================
def add_all12():
    try:
        data = Toplevel(height="300", width="730", relief="flat")
        data.geometry("450x150-410+280")
        data.minsize("440", "120")
        data.maxsize("440", "120")
        data.title("Add Data")
        data.config(background="lavender")

        ent = StringVar()
        ent1 = StringVar()

        lab = ttk.Label(data, text="Item (Input the new Item): ", font=('', 12, ''), background="lavender")
        lab.grid(row=0, column=0, padx=5, pady=5)

        lab1 = ttk.Label(data, text="Price (Input the new Price): ", font=('', 12, ''), background="lavender")
        lab1.grid(row=1, column=0, padx=5, pady=5)



        def add_up():
            # i = 0
            hala12 = (ents.get() + "GHC", ento.get() + "KG")
            tree12.insert('', 'end', values=hala12)

            # tree serialization
            with open(taker, "w") as f:
                yaml.dump(hala12, f)

            tkMessageBox.showinfo("Add New Item", "You have succesfully added new entries.")
            # i + 1

        ento = ttk.Entry(data, width=20, font=('arial', 12, ''))
        ento.grid(row=0, column=1)

        ents = ttk.Entry(data, width=20, font=('arial', 12, ''))
        ents.grid(row=1, column=1)

        seph = ttk.Separator(data, orient='horizontal')
        # sep.pack(side = BOTTOM)e
        seph.grid(row=2, column=0, sticky='n,w,e,s', columnspan=2, ipadx=200, ipady=1, padx=5, pady=5)

        btn = ttk.Button(data, text="OK", style='Wild.TButton', command=add_up)
        btn.grid(row=3, column=0, sticky='E', padx=5, pady=1)

        btn1 = ttk.Button(data, text="Cancel", command=data.destroy)
        btn1.grid(row=3, column=1, sticky='W', padx=5, pady=1)

    except:
        tkMessageBox.showerror("Add New Item", "Add new Item failed. Please check input.")
    finally:
        clear()


def sub_all12():
    try:
        datum = Toplevel(height="200", width="770", relief="flat")
        datum.geometry("460x150-410+280")
        datum.minsize("450", "120")
        datum.maxsize("450", "120")
        datum.title("Edit Data")
        datum.config(background="lavender")

        ent = StringVar()
        ent1 = StringVar()

        lab = ttk.Label(datum, text="Item (Edit the selected Item): ", font=('', 12, ''), background="lavender")
        lab.grid(row=0, column=0, padx=5, pady=5)

        lab1 = ttk.Label(datum, text="Price (Edit the price): ", font=('', 12, ''), background="lavender")
        lab1.grid(row=1, column=0, padx=5, pady=5)

        ento = StringVar()
        ents = StringVar()

        def add_up():
            hala12 = (ents.get() + "GHC", ento.get() + "KG")
            tree12.insert('', 'end', values=hala12)

            # tree serialization
            with open(taker, "w") as f:
                yaml.dump(hala12, f)
            tkMessageBox.showinfo("Edit Item", "You have succesfully edited the entries.")
            # i + 1

        ento = ttk.Entry(datum, width=20, font=('arial', 12, ''))
        ento.grid(row=0, column=1)

        ents = ttk.Entry(datum, width=20, font=('arial', 12, ''))
        ents.grid(row=1, column=1)

        seph = ttk.Separator(datum, orient='horizontal')
        # sep.pack(side = BOTTOM)e
        seph.grid(row=2, column=0, sticky='n,w,e,s', columnspan=2, ipadx=200, ipady=1, padx=5, pady=5)

        btn = ttk.Button(datum, text="OK", style='Wild.TButton', command=add_up)
        btn.grid(row=3, column=0, sticky='E', padx=5, pady=1)

        btn1 = ttk.Button(datum, text="Cancel", command=datum.destroy)
        btn1.grid(row=3, column=1, sticky='W', padx=5, pady=1)

    except:
        tkMessageBox.showerror("Add New Item", "Add new Item failed. Please check input.")
    finally:
        clear()

def iexits12():
        go = Toplevel(height="400", width="500", relief="flat")
        go.geometry("465x125-450+300")
#        go.minsize("485", "160")
#        go.maxsize("485", "160")
        go.title("Delete")
        go.resizable(0,0)
        go.config(background = "#E4E4E4")
#        go.overrideredirect(True)
        go.attributes("-toolwindow", 1)

        lb = ttk.Label(go, text="""Are you sure you want to permanetly delete this item?""", font=('Helvetica', 12, 'bold'), background = "#E4E4E4")
        lb.grid(row=0, column=0,  columnspan=2,sticky='w')

        lb = ttk.Label(go, text="""
        Items deleted would not be recovereable.""", font=('Helvetica', 12, ''), background = "#E4E4E4")
        lb.grid(row=1, column=0,  columnspan=3,sticky='w', padx=5, pady=5)

        def del_tree():
            selected_item =tree12.selection()[0]
            tree12.delete(selected_item)
            lost12 = (ents.get() + "", ento.get() + "")
            # tree serialization
            with open(taker, "w") as f:
               yaml.dump(lost12, f)
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
with open(taker, "r") as f:
    dany12= yaml.load(f)

tree12 = ttk.Treeview(w1, columns=(1, 0), displaycolumns=(0, 1,), height=2, selectmode='browse',
                     show='headings')
tree12.heading('#0', text='Itemo')
tree12.heading('#1', text='Item')
tree12.heading('#2', text='Price')
tree12.insert('','end', text = "Item", values=dany12)
tree12.grid(row=6, column=7, columnspan=1, padx=40, pady=5, sticky='n,e,s,w')
i = 0
b38 = ttk.Button(w1, text='+', command=add_all12, style = "Mini.TButton")
b38.grid(row=6, column=8,  padx=5, pady=5,sticky='w')
b39 = ttk.Button(w1, text='...', command=sub_all12, style = "Mini.TButton")
b39.grid(row=6, column=9, padx=5, pady=5,sticky='w')
b40 = ttk.Button(w1, text='-', command=iexits12, style = "Minis.TButton")
b40.grid(row=6, column=10, padx=5, pady=5,sticky='w')

#========================================We are on moving forward=======================================================
def add_all13():
    try:
        data = Toplevel(height="300", width="730", relief="flat")
        data.geometry("450x150-410+280")
        data.minsize("440", "120")
        data.maxsize("440", "120")
        data.title("Add Data")
        data.config(background="lavender")

        ent = StringVar()
        ent1 = StringVar()

        lab = ttk.Label(data, text="Item (Input the new Item): ", font=('', 12, ''), background="lavender")
        lab.grid(row=0, column=0, padx=5, pady=5)

        lab1 = ttk.Label(data, text="Price (Input the new Price): ", font=('', 12, ''), background="lavender")
        lab1.grid(row=1, column=0, padx=5, pady=5)



        def add_up():
            # i = 0
            hala13 = (ents.get() + "GHC", ento.get() + "KG")
            tree13.insert('', 'end', values=hala13)

            # tree serialization
            with open(undr, "w") as f:
                yaml.dump(hala13, f)

            tkMessageBox.showinfo("Add New Item", "You have succesfully added new entries.")
            # i + 1

        ento = ttk.Entry(data, width=20, font=('arial', 12, ''))
        ento.grid(row=0, column=1)

        ents = ttk.Entry(data, width=20, font=('arial', 12, ''))
        ents.grid(row=1, column=1)

        seph = ttk.Separator(data, orient='horizontal')
        # sep.pack(side = BOTTOM)e
        seph.grid(row=2, column=0, sticky='n,w,e,s', columnspan=2, ipadx=200, ipady=1, padx=5, pady=5)

        btn = ttk.Button(data, text="OK", style='Wild.TButton', command=add_up)
        btn.grid(row=3, column=0, sticky='E', padx=5, pady=1)

        btn1 = ttk.Button(data, text="Cancel", command=data.destroy)
        btn1.grid(row=3, column=1, sticky='W', padx=5, pady=1)

    except:
        tkMessageBox.showerror("Add New Item", "Add new Item failed. Please check input.")
    finally:
        clear()


def sub_all13():
    try:
        datum = Toplevel(height="200", width="770", relief="flat")
        datum.geometry("460x150-410+280")
        datum.minsize("450", "120")
        datum.maxsize("450", "120")
        datum.title("Edit Data")
        datum.config(background="lavender")

        ent = StringVar()
        ent1 = StringVar()

        lab = ttk.Label(datum, text="Item (Edit the selected Item): ", font=('', 12, ''), background="lavender")
        lab.grid(row=0, column=0, padx=5, pady=5)

        lab1 = ttk.Label(datum, text="Price (Edit the price): ", font=('', 12, ''), background="lavender")
        lab1.grid(row=1, column=0, padx=5, pady=5)

        ento = StringVar()
        ents = StringVar()

        def add_up():
            hala13 = (ents.get() + "GHC", ento.get() + "KG")
            tree13.insert('', 'end', values=hala13)

            # tree serialization
            with open(undr, "w") as f:
                yaml.dump(hala13, f)
            tkMessageBox.showinfo("Edit Item", "You have succesfully edited the entries.")
            # i + 1

        ento = ttk.Entry(datum, width=20, font=('arial', 12, ''))
        ento.grid(row=0, column=1)

        ents = ttk.Entry(datum, width=20, font=('arial', 12, ''))
        ents.grid(row=1, column=1)

        seph = ttk.Separator(datum, orient='horizontal')
        # sep.pack(side = BOTTOM)e
        seph.grid(row=2, column=0, sticky='n,w,e,s', columnspan=2, ipadx=200, ipady=1, padx=5, pady=5)

        btn = ttk.Button(datum, text="OK", style='Wild.TButton', command=add_up)
        btn.grid(row=3, column=0, sticky='E', padx=5, pady=1)

        btn1 = ttk.Button(datum, text="Cancel", command=datum.destroy)
        btn1.grid(row=3, column=1, sticky='W', padx=5, pady=1)

    except:
        tkMessageBox.showerror("Add New Item", "Add new Item failed. Please check input.")
    finally:
        clear()

def iexits13():
        go = Toplevel(height="400", width="500", relief="flat")
        go.geometry("465x125-450+300")
#        go.minsize("485", "160")
#        go.maxsize("485", "160")
        go.title("Delete")
        go.resizable(0,0)
        go.config(background = "#E4E4E4")
#        go.overrideredirect(True)
        go.attributes("-toolwindow", 1)

        lb = ttk.Label(go, text="""Are you sure you want to permanetly delete this item?""", font=('Helvetica', 12, 'bold'), background = "#E4E4E4")
        lb.grid(row=0, column=0,  columnspan=2,sticky='w')

        lb = ttk.Label(go, text="""
        Items deleted would not be recovereable.""", font=('Helvetica', 12, ''), background = "#E4E4E4")
        lb.grid(row=1, column=0,  columnspan=3,sticky='w', padx=5, pady=5)

        def del_tree():
            selected_item =tree13.selection()[0]
            tree13.delete(selected_item)
            lost13 = (ents.get() + "", ento.get() + "")
            # tree serialization
            with open(undr, "w") as f:
               yaml.dump(lost13, f)
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
with open(undr, "r") as f:
    dany13= yaml.load(f)

tree13 = ttk.Treeview(w1, columns=(1, 0), displaycolumns=(0, 1,), height=2, selectmode='browse',
                     show='headings')
tree13.heading('#0', text='Itemo')
tree13.heading('#1', text='Item')
tree13.heading('#2', text='Price')
tree13.insert('','end', text = "Item", values=dany13)
tree13.grid(row=7, column=7, columnspan=1, padx=40, pady=5, sticky='n,e,s,w')
i = 0
b41 = ttk.Button(w1, text='+', command=add_all13, style = "Mini.TButton")
b41.grid(row=7, column=8,  padx=5, pady=5,sticky='w')
b42 = ttk.Button(w1, text='...', command=sub_all13, style = "Mini.TButton")
b42.grid(row=7, column=9, padx=5, pady=5,sticky='w')
b43 = ttk.Button(w1, text='-', command=iexits13, style = "Minis.TButton")
b43.grid(row=7, column=10, padx=5, pady=5,sticky='w')

#========================================We are on moving forward=======================================================
def add_all14():
    try:
        data = Toplevel(height="300", width="730", relief="flat")
        data.geometry("450x150-410+280")
        data.minsize("440", "120")
        data.maxsize("440", "120")
        data.title("Add Data")
        data.config(background="lavender")

        ent = StringVar()
        ent1 = StringVar()

        lab = ttk.Label(data, text="Item (Input the new Item): ", font=('', 12, ''), background="lavender")
        lab.grid(row=0, column=0, padx=5, pady=5)

        lab1 = ttk.Label(data, text="Price (Input the new Price): ", font=('', 12, ''), background="lavender")
        lab1.grid(row=1, column=0, padx=5, pady=5)



        def add_up():
            # i = 0
            hala14 = (ents.get() + "GHC", ento.get() + "KG")
            tree14.insert('', 'end', values=hala14)

            # tree serialization
            with open(mena, "w") as f:
                yaml.dump(hala14, f)

            tkMessageBox.showinfo("Add New Item", "You have succesfully added new entries.")
            # i + 1

        ento = ttk.Entry(data, width=20, font=('arial', 12, ''))
        ento.grid(row=0, column=1)

        ents = ttk.Entry(data, width=20, font=('arial', 12, ''))
        ents.grid(row=1, column=1)

        seph = ttk.Separator(data, orient='horizontal')
        # sep.pack(side = BOTTOM)e
        seph.grid(row=2, column=0, sticky='n,w,e,s', columnspan=2, ipadx=200, ipady=1, padx=5, pady=5)

        btn = ttk.Button(data, text="OK", style='Wild.TButton', command=add_up)
        btn.grid(row=3, column=0, sticky='E', padx=5, pady=1)

        btn1 = ttk.Button(data, text="Cancel", command=data.destroy)
        btn1.grid(row=3, column=1, sticky='W', padx=5, pady=1)

    except:
        tkMessageBox.showerror("Add New Item", "Add new Item failed. Please check input.")
    finally:
        clear()


def sub_all14():
    try:
        datum = Toplevel(height="200", width="770", relief="flat")
        datum.geometry("460x150-410+280")
        datum.minsize("450", "120")
        datum.maxsize("450", "120")
        datum.title("Edit Data")
        datum.config(background="lavender")

        ent = StringVar()
        ent1 = StringVar()

        lab = ttk.Label(datum, text="Item (Edit the selected Item): ", font=('', 12, ''), background="lavender")
        lab.grid(row=0, column=0, padx=5, pady=5)

        lab1 = ttk.Label(datum, text="Price (Edit the price): ", font=('', 12, ''), background="lavender")
        lab1.grid(row=1, column=0, padx=5, pady=5)

        ento = StringVar()
        ents = StringVar()

        def add_up():
            hala14 = (ents.get() + "GHC", ento.get() + "KG")
            tree14.insert('', 'end', values=hala14)

            # tree serialization
            with open(mena, "w") as f:
                yaml.dump(hala14, f)
            tkMessageBox.showinfo("Edit Item", "You have succesfully edited the entries.")
            # i + 1

        ento = ttk.Entry(datum, width=20, font=('arial', 12, ''))
        ento.grid(row=0, column=1)

        ents = ttk.Entry(datum, width=20, font=('arial', 12, ''))
        ents.grid(row=1, column=1)

        seph = ttk.Separator(datum, orient='horizontal')
        # sep.pack(side = BOTTOM)e
        seph.grid(row=2, column=0, sticky='n,w,e,s', columnspan=2, ipadx=200, ipady=1, padx=5, pady=5)

        btn = ttk.Button(datum, text="OK", style='Wild.TButton', command=add_up)
        btn.grid(row=3, column=0, sticky='E', padx=5, pady=1)

        btn1 = ttk.Button(datum, text="Cancel", command=datum.destroy)
        btn1.grid(row=3, column=1, sticky='W', padx=5, pady=1)

    except:
        tkMessageBox.showerror("Add New Item", "Add new Item failed. Please check input.")
    finally:
        clear()

def iexits14():
        go = Toplevel(height="400", width="500", relief="flat")
        go.geometry("465x125-450+300")
#        go.minsize("485", "160")
#        go.maxsize("485", "160")
        go.title("Delete")
        go.resizable(0,0)
        go.config(background = "#E4E4E4")
#        go.overrideredirect(True)
        go.attributes("-toolwindow", 1)

        lb = ttk.Label(go, text="""Are you sure you want to permanetly delete this item?""", font=('Helvetica', 12, 'bold'), background = "#E4E4E4")
        lb.grid(row=0, column=0,  columnspan=2,sticky='w')

        lb = ttk.Label(go, text="""
        Items deleted would not be recovereable.""", font=('Helvetica', 12, ''), background = "#E4E4E4")
        lb.grid(row=1, column=0,  columnspan=3,sticky='w', padx=5, pady=5)

        def del_tree():
            selected_item =tree14.selection()[0]
            tree14.delete(selected_item)
            lost14 = (ents.get() + "", ento.get() + "")
            # tree serialization
            with open(mena, "w") as f:
               yaml.dump(lost14, f)
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
with open(mena, "r") as f:
    dany14= yaml.load(f)

tree14 = ttk.Treeview(w1, columns=(1, 0), displaycolumns=(0, 1,), height=2, selectmode='browse',
                     show='headings')
tree14.heading('#0', text='Itemo')
tree14.heading('#1', text='Item')
tree14.heading('#2', text='Price')
tree14.insert('','end', text = "Item", values=dany14)
tree14.grid(row=8, column=7, columnspan=1, padx=40, pady=5, sticky='n,e,s,w')
i = 0
b44 = ttk.Button(w1, text='+', command=add_all14, style = "Mini.TButton")
b44.grid(row=8, column=8,  padx=5, pady=5,sticky='w')
b45 = ttk.Button(w1, text='...', command=sub_all14, style = "Mini.TButton")
b45.grid(row=8, column=9, padx=5, pady=5,sticky='w')
b46 = ttk.Button(w1, text='-', command=iexits14, style = "Minis.TButton")
b46.grid(row=8, column=10, padx=5, pady=5,sticky='w')

#========================================We are on moving forward=======================================================
def add_all15():
    try:
        data = Toplevel(height="300", width="730", relief="flat")
        data.geometry("450x150-410+280")
        data.minsize("440", "120")
        data.maxsize("440", "120")
        data.title("Add Data")
        data.config(background="lavender")

        ent = StringVar()
        ent1 = StringVar()

        lab = ttk.Label(data, text="Item (Input the new Item): ", font=('', 12, ''), background="lavender")
        lab.grid(row=0, column=0, padx=5, pady=5)

        lab1 = ttk.Label(data, text="Price (Input the new Price): ", font=('', 12, ''), background="lavender")
        lab1.grid(row=1, column=0, padx=5, pady=5)



        def add_up():
            # i = 0
            hala15 = (ents.get() + "GHC", ento.get() + "KG")
            tree15.insert('', 'end', values=hala15)

            # tree serialization
            with open(ania, "w") as f:
                yaml.dump(hala15, f)

            tkMessageBox.showinfo("Add New Item", "You have succesfully added new entries.")
            # i + 1

        ento = ttk.Entry(data, width=20, font=('arial', 12, ''))
        ento.grid(row=0, column=1)

        ents = ttk.Entry(data, width=20, font=('arial', 12, ''))
        ents.grid(row=1, column=1)

        seph = ttk.Separator(data, orient='horizontal')
        # sep.pack(side = BOTTOM)e
        seph.grid(row=2, column=0, sticky='n,w,e,s', columnspan=2, ipadx=200, ipady=1, padx=5, pady=5)

        btn = ttk.Button(data, text="OK", style='Wild.TButton', command=add_up)
        btn.grid(row=3, column=0, sticky='E', padx=5, pady=1)

        btn1 = ttk.Button(data, text="Cancel", command=data.destroy)
        btn1.grid(row=3, column=1, sticky='W', padx=5, pady=1)

    except:
        tkMessageBox.showerror("Add New Item", "Add new Item failed. Please check input.")
    finally:
        clear()


def sub_all15():
    try:
        datum = Toplevel(height="200", width="770", relief="flat")
        datum.geometry("460x150-410+280")
        datum.minsize("450", "120")
        datum.maxsize("450", "120")
        datum.title("Edit Data")
        datum.config(background="lavender")

        ent = StringVar()
        ent1 = StringVar()

        lab = ttk.Label(datum, text="Item (Edit the selected Item): ", font=('', 12, ''), background="lavender")
        lab.grid(row=0, column=0, padx=5, pady=5)

        lab1 = ttk.Label(datum, text="Price (Edit the price): ", font=('', 12, ''), background="lavender")
        lab1.grid(row=1, column=0, padx=5, pady=5)

        ento = StringVar()
        ents = StringVar()

        def add_up():
            hala15 = (ents.get() + "GHC", ento.get() + "KG")
            tree15.insert('', 'end', values=hala15)

            # tree serialization
            with open(ania, "w") as f:
                yaml.dump(hala15, f)
            tkMessageBox.showinfo("Edit Item", "You have succesfully edited the entries.")
            # i + 1

        ento = ttk.Entry(datum, width=20, font=('arial', 12, ''))
        ento.grid(row=0, column=1)

        ents = ttk.Entry(datum, width=20, font=('arial', 12, ''))
        ents.grid(row=1, column=1)

        seph = ttk.Separator(datum, orient='horizontal')
        # sep.pack(side = BOTTOM)e
        seph.grid(row=2, column=0, sticky='n,w,e,s', columnspan=2, ipadx=200, ipady=1, padx=5, pady=5)

        btn = ttk.Button(datum, text="OK", style='Wild.TButton', command=add_up)
        btn.grid(row=3, column=0, sticky='E', padx=5, pady=1)

        btn1 = ttk.Button(datum, text="Cancel", command=datum.destroy)
        btn1.grid(row=3, column=1, sticky='W', padx=5, pady=1)

    except:
        tkMessageBox.showerror("Add New Item", "Add new Item failed. Please check input.")
    finally:
        clear()

def iexits15():
        go = Toplevel(height="400", width="500", relief="flat")
        go.geometry("465x125-450+300")
#        go.minsize("485", "160")
#        go.maxsize("485", "160")
        go.title("Delete")
        go.resizable(0,0)
        go.config(background = "#E4E4E4")
#        go.overrideredirect(True)
        go.attributes("-toolwindow", 1)

        lb = ttk.Label(go, text="""Are you sure you want to permanetly delete this item?""", font=('Helvetica', 12, 'bold'), background = "#E4E4E4")
        lb.grid(row=0, column=0,  columnspan=2,sticky='w')

        lb = ttk.Label(go, text="""
        Items deleted would not be recovereable.""", font=('Helvetica', 12, ''), background = "#E4E4E4")
        lb.grid(row=1, column=0,  columnspan=3,sticky='w', padx=5, pady=5)

        def del_tree():
            selected_item =tree15.selection()[0]
            tree15.delete(selected_item)
            lost15 = (ents.get() + "", ento.get() + "")
            # tree serialization
            with open(ania, "w") as f:
               yaml.dump(lost15, f)
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
with open(ania, "r") as f:
    dany15= yaml.load(f)

tree15 = ttk.Treeview(w1, columns=(1, 0), displaycolumns=(0, 1,), height=2, selectmode='browse',
                     show='headings')
tree15.heading('#0', text='Itemo')
tree15.heading('#1', text='Item')
tree15.heading('#2', text='Price')
tree15.insert('','end', text = "Item", values=dany15)
tree15.grid(row=9, column=7, columnspan=1, padx=40, pady=5, sticky='n,e,s,w')
i = 0
b47 = ttk.Button(w1, text='+', command=add_all15, style = "Mini.TButton")
b47.grid(row=9, column=8,  padx=5, pady=5,sticky='w')
b48 = ttk.Button(w1, text='...', command=sub_all15, style = "Mini.TButton")
b48.grid(row=9, column=9, padx=5, pady=5,sticky='w')
b49 = ttk.Button(w1, text='-', command=iexits15, style = "Minis.TButton")
b49.grid(row=9, column=10, padx=5, pady=5,sticky='w')

#==============We extend the use of More button over here. More database in place guys==================================
#==========So then we bring the More button here down here.=============================================================
def ctr():
    counter = Toplevel()
    counter.title("More Entries")
    counter.geometry('1250x300-160+10')
    counter.minsize("1200", "680")
    counter.maxsize("1150", "700")
    counter.config(background="#E4E4E4")
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

    def add_all():
        try:
            data = Toplevel(height="300", width="730", relief="flat")
            data.geometry("450x150-410+280")
            data.minsize("440", "120")
            data.maxsize("440", "120")
            data.title("Add Data")
            data.config(background="lavender")

            ent = StringVar()
            ent1 = StringVar()

            lab = ttk.Label(data, text="Item (Input the new Item): ", font=('', 12, ''), background="lavender")
            lab.grid(row=0, column=0, padx=5, pady=5)

            lab1 = ttk.Label(data, text="Price (Input the new Price): ", font=('', 12, ''), background="lavender")
            lab1.grid(row=1, column=0, padx=5, pady=5)

            def add_up():
                # i = 0
                hala = (ents.get() + "GHC", ento.get() + "KG")
                # hal = ()
                tree.insert('', 'end', values=hala)

                # tree serialization
                with open(l1, "w") as f:
                    yaml.dump(hala, f)

                ##("Add New Item", "You have succesfully added new entries.")
                # i + 1

            ento = ttk.Entry(data, width=20, font=('arial', 12, ''))
            ento.grid(row=0, column=1)

            ents = ttk.Entry(data, width=20, font=('arial', 12, ''))
            ents.grid(row=1, column=1)

            seph = ttk.Separator(data, orient='horizontal')
            # sep.pack(side = BOTTOM)e
            seph.grid(row=2, column=0, sticky='n,w,e,s', columnspan=2, ipadx=200, ipady=1, padx=5, pady=5)

            btn = ttk.Button(data, text="OK", style='Wild.TButton', command=add_up)
            btn.grid(row=3, column=0, sticky='E', padx=5, pady=1)

            btn1 = ttk.Button(data, text="Cancel", command=data.destroy)
            btn1.grid(row=3, column=1, sticky='W', padx=5, pady=1)

        except:
            tkMessageBox.showerror("Add New Item", "Add new Item failed. Please check input.")
        finally:
            clear()

    def sub_all():
        try:
            datum = Toplevel(height="200", width="770", relief="flat")
            datum.geometry("460x150-410+280")
            datum.minsize("450", "120")
            datum.maxsize("450", "120")
            datum.title("Edit Data")
            datum.config(background="lavender")

            ent = StringVar()
            ent1 = StringVar()

            lab = ttk.Label(datum, text="Item (Edit the selected Item): ", font=('', 12, ''), background="lavender")
            lab.grid(row=0, column=0, padx=5, pady=5)

            lab1 = ttk.Label(datum, text="Price (Edit the price): ", font=('', 12, ''), background="lavender")
            lab1.grid(row=1, column=0, padx=5, pady=5)

            ento = StringVar()
            ents = StringVar()

            def add_up():
                hala = (ents.get() + "GHC", ento.get() + "KG")
                tree.insert('', 'end', values=hala)

                # tree serialization
                with open(l1, "w") as f:
                    yaml.dump(hala, f)
                ##("Edit Item", "You have succesfully edited the entries.")
                # i + 1

            ento = ttk.Entry(datum, width=20, font=('arial', 12, ''))
            ento.grid(row=0, column=1)

            ents = ttk.Entry(datum, width=20, font=('arial', 12, ''))
            ents.grid(row=1, column=1)

            seph = ttk.Separator(datum, orient='horizontal')
            # sep.pack(side = BOTTOM)e
            seph.grid(row=2, column=0, sticky='n,w,e,s', columnspan=2, ipadx=200, ipady=1, padx=5, pady=5)

            btn = ttk.Button(datum, text="OK", style='Wild.TButton', command=add_up)
            btn.grid(row=3, column=0, sticky='E', padx=5, pady=1)

            btn1 = ttk.Button(datum, text="Cancel", command=datum.destroy)
            btn1.grid(row=3, column=1, sticky='W', padx=5, pady=1)

        except:
            tkMessageBox.showerror("Add New Item", "Add new Item failed. Please check input.")
        finally:
            clear()

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

        lb = ttk.Label(go, text="""Are you sure you want to permanetly delete this item?""",
                       font=('Helvetica', 12, 'bold'), background="#E4E4E4")
        lb.grid(row=0, column=0, columnspan=2, sticky='w')

        lb = ttk.Label(go, text="""
            Items deleted would not be recovereable.""", font=('Helvetica', 12, ''), background="#E4E4E4")
        lb.grid(row=1, column=0, columnspan=3, sticky='w', padx=5, pady=5)

        def del_tree():
            selected_item = tree.selection()[0]
            tree.delete(selected_item)
            lost = (ents.get() + "", ento.get() + "")
            # tree serialization
            with open(l1, "w") as f:
                yaml.dump(lost, f)
            # tree.insert('', 'end', text="Item", values=0)
            #("Delete Item", "You have succesfully deleted the entries.")
            go.destroy()

        bn = ttk.Button(go, text="Cancel", command=go.destroy)
        bn.grid(row=2, column=0, pady=5, ipadx=90, ipady=10)

        bn1 = ttk.Button(go, text="Delete", style='Minis.TButton', command=del_tree)
        bn1.grid(row=2, column=1, pady=5, ipadx=90, ipady=10)

    # =======================================================================================================================
    lbl1 = ttk.Label(counter, text="Configure Entries", font=('DejaVu Sans Mono', 12, 'bold'), background='#E4E4E4')
    lbl1.grid(row=0, column=0, columnspan=2, sticky='W')

    #bn = Button(counter, text='More', command=iexits, bg="#0066CC", fg="white", activeforeground="white",
    #            activebackground="#0066CC", overrelief="flat", relief="flat", font=('DejaVu Sans Mono', 10, 'bold'),
    #            width=10, )
    #bn.grid(row=0, column=0, padx=5, pady=5, )

    lbl = ttk.Label(counter, text="""Management System would allow storing, editing and deleting of new entries here.""",
                    font=('DejaVu Sans Mono', 11, ''), background='#E4E4E4')
    lbl.grid(row=1, column=0, columnspan=5, sticky='w')

    # We focus on oma to now dump the inputs
    # Tree serialization
    with open(l1, "r") as f:
        dany = yaml.load(f)

    tree = ttk.Treeview(counter, columns=(1, 0), displaycolumns=(0, 1,), height=2, selectmode='browse',
                        show='headings')
    tree.heading('#0', text='Itemo')
    tree.heading('#1', text='Item')
    tree.heading('#2', text='Price')
    tree.insert('', 'end', text="Item", values=dany)
    tree.grid(row=2, column=0, ipadx=1, pady=5, sticky='w')
    i = 0
    b2 = ttk.Button(counter, text='+', command=add_all, style="Mini.TButton")
    b2.grid(row=2, column=1, rowspan=1, padx=5, pady=5, )
    b3 = ttk.Button(counter, text='...', command=sub_all, style="Mini.TButton")
    b3.grid(row=2, column=2, padx=5, pady=5, )
    b4 = ttk.Button(counter, text='-', command=iexits, style="Minis.TButton")
    b4.grid(row=2, column=4, padx=5, pady=5, )

    # ===================================This is the second file we serialize================================================
    def add_all1():
        try:
            data = Toplevel(height="300", width="730", relief="flat")
            data.geometry("450x150-410+280")
            data.minsize("440", "120")
            data.maxsize("440", "120")
            data.title("Add Data")
            data.config(background="lavender")

            ent = StringVar()
            ent1 = StringVar()

            lab = ttk.Label(data, text="Item (Input the new Item): ", font=('', 12, ''), background="lavender")
            lab.grid(row=0, column=0, padx=5, pady=5)

            lab1 = ttk.Label(data, text="Price (Input the new Price): ", font=('', 12, ''), background="lavender")
            lab1.grid(row=1, column=0, padx=5, pady=5)

            def add_up():
                # i = 0
                hala1 = (ents.get() + "GHC", ento.get() + "KG")
                tree1.insert('', 'end', values=hala1)

                # tree serialization
                with open(l2, "w") as f:
                    yaml.dump(hala1, f)

                #("Add New Item", "You have succesfully added new entries.")
                # i + 1

            ento = ttk.Entry(data, width=20, font=('arial', 12, ''))
            ento.grid(row=0, column=1)

            ents = ttk.Entry(data, width=20, font=('arial', 12, ''))
            ents.grid(row=1, column=1)

            seph = ttk.Separator(data, orient='horizontal')
            # sep.pack(side = BOTTOM)e
            seph.grid(row=2, column=0, sticky='n,w,e,s', columnspan=2, ipadx=200, ipady=1, padx=5, pady=5)

            btn = ttk.Button(data, text="OK", style='Wild.TButton', command=add_up)
            btn.grid(row=3, column=0, sticky='E', padx=5, pady=1)

            btn1 = ttk.Button(data, text="Cancel", command=data.destroy)
            btn1.grid(row=3, column=1, sticky='W', padx=5, pady=1)

        except:
            tkMessageBox.showerror("Add New Item", "Add new Item failed. Please check input.")
        finally:
            clear()

    def sub_all1():
        try:
            datum = Toplevel(height="200", width="770", relief="flat")
            datum.geometry("460x150-410+280")
            datum.minsize("450", "120")
            datum.maxsize("450", "120")
            datum.title("Edit Data")
            datum.config(background="lavender")

            ent = StringVar()
            ent1 = StringVar()

            lab = ttk.Label(datum, text="Item (Edit the selected Item): ", font=('', 12, ''), background="lavender")
            lab.grid(row=0, column=0, padx=5, pady=5)

            lab1 = ttk.Label(datum, text="Price (Edit the price): ", font=('', 12, ''), background="lavender")
            lab1.grid(row=1, column=0, padx=5, pady=5)

            ento = StringVar()
            ents = StringVar()

            def add_up():
                hala1 = (ents.get() + "GHC", ento.get() + "KG")
                tree1.insert('', 'end', values=hala1)

                # tree serialization
                with open(l2, "w") as f:
                    yaml.dump(hala1, f)
                #("Edit Item", "You have succesfully edited the entries.")
                # i + 1

            ento = ttk.Entry(datum, width=20, font=('arial', 12, ''))
            ento.grid(row=0, column=1)

            ents = ttk.Entry(datum, width=20, font=('arial', 12, ''))
            ents.grid(row=1, column=1)

            seph = ttk.Separator(datum, orient='horizontal')
            # sep.pack(side = BOTTOM)e
            seph.grid(row=2, column=0, sticky='n,w,e,s', columnspan=2, ipadx=200, ipady=1, padx=5, pady=5)

            btn = ttk.Button(datum, text="OK", style='Wild.TButton', command=add_up)
            btn.grid(row=3, column=0, sticky='E', padx=5, pady=1)

            btn1 = ttk.Button(datum, text="Cancel", command=datum.destroy)
            btn1.grid(row=3, column=1, sticky='W', padx=5, pady=1)

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

        lb = ttk.Label(go, text="""Are you sure you want to permanetly delete this item?""",
                       font=('Helvetica', 12, 'bold'), background="#E4E4E4")
        lb.grid(row=0, column=0, columnspan=2, sticky='w')

        lb = ttk.Label(go, text="""
            Items deleted would not be recovereable.""", font=('Helvetica', 12, ''), background="#E4E4E4")
        lb.grid(row=1, column=0, columnspan=3, sticky='w', padx=5, pady=5)

        def del_tree():
            selected_item = tree1.selection()[0]
            tree1.delete(selected_item)
            lost1 = (ents.get() + "", ento.get() + "")
            # tree serialization
            with open(l2, "w") as f:
                yaml.dump(lost1, f)
            # tree1.insert('', 'end', text="Item", values=0)
            #("Delete Item", "You have succesfully deleted the entries.")
            go.destroy()

        bn = ttk.Button(go, text="Cancel", command=go.destroy)
        bn.grid(row=2, column=0, pady=5, ipadx=90, ipady=10)

        bn1 = ttk.Button(go, text="Delete", style='Minis.TButton', command=del_tree)
        bn1.grid(row=2, column=1, pady=5, ipadx=90, ipady=10)

    # =======================================================================================================================
    # We focus on tripo to now dump the inputs
    # Tree serialization
    with open(l2, "r") as f:
        dany1 = yaml.load(f)
    tree1 = ttk.Treeview(counter, columns=(1, 0), displaycolumns=(0, 1,), height=2, selectmode='browse',
                         show='headings')
    tree1.heading('#0', text='Itemo')
    tree1.heading('#1', text='Item')
    tree1.heading('#2', text='Price')
    tree1.insert('', 'end', text="Item", values=dany1)
    tree1.grid(row=3, column=0, padx=1, pady=5, sticky='w')
    i = 0
    b5 = ttk.Button(counter, text='+', command=add_all1, style="Mini.TButton")
    b5.grid(row=3, column=1, rowspan=1, padx=5, pady=5, )
    b6 = ttk.Button(counter, text='...', command=sub_all1, style="Mini.TButton")
    b6.grid(row=3, column=2, padx=5, pady=5, )
    b7 = ttk.Button(counter, text='-', command=iexits1, style="Minis.TButton")
    b7.grid(row=3, column=4, padx=5, pady=5, )

    # =====================We handle another serialization context here======================================================
    def add_all2():
        try:
            data = Toplevel(height="300", width="730", relief="flat")
            data.geometry("450x150-410+280")
            data.minsize("440", "120")
            data.maxsize("440", "120")
            data.title("Add Data")
            data.config(background="lavender")

            ent = StringVar()
            ent1 = StringVar()

            lab = ttk.Label(data, text="Item (Input the new Item): ", font=('', 12, ''), background="lavender")
            lab.grid(row=0, column=0, padx=5, pady=5)

            lab1 = ttk.Label(data, text="Price (Input the new Price): ", font=('', 12, ''), background="lavender")
            lab1.grid(row=1, column=0, padx=5, pady=5)

            def add_up():
                # i = 0
                hala2 = (ents.get() + "GHC", ento.get() + "KG")
                tree2.insert('', 'end', values=hala2)

                # tree serialization
                with open(l3, "w") as f:
                    yaml.dump(hala2, f)

                #("Add New Item", "You have succesfully added new entries.")
                # i + 1

            ento = ttk.Entry(data, width=20, font=('arial', 12, ''))
            ento.grid(row=0, column=1)

            ents = ttk.Entry(data, width=20, font=('arial', 12, ''))
            ents.grid(row=1, column=1)

            seph = ttk.Separator(data, orient='horizontal')
            # sep.pack(side = BOTTOM)e
            seph.grid(row=2, column=0, sticky='n,w,e,s', columnspan=2, ipadx=200, ipady=1, padx=5, pady=5)

            btn = ttk.Button(data, text="OK", style='Wild.TButton', command=add_up)
            btn.grid(row=3, column=0, sticky='E', padx=5, pady=1)

            btn1 = ttk.Button(data, text="Cancel", command=data.destroy)
            btn1.grid(row=3, column=1, sticky='W', padx=5, pady=1)

        except:
            tkMessageBox.showerror("Add New Item", "Add new Item failed. Please check input.")
        finally:
            clear()

    def sub_all2():
        try:
            datum = Toplevel(height="200", width="770", relief="flat")
            datum.geometry("460x150-410+280")
            datum.minsize("450", "120")
            datum.maxsize("450", "120")
            datum.title("Edit Data")
            datum.config(background="lavender")

            ent = StringVar()
            ent1 = StringVar()

            lab = ttk.Label(datum, text="Item (Edit the selected Item): ", font=('', 12, ''), background="lavender")
            lab.grid(row=0, column=0, padx=5, pady=5)

            lab1 = ttk.Label(datum, text="Price (Edit the price): ", font=('', 12, ''), background="lavender")
            lab1.grid(row=1, column=0, padx=5, pady=5)

            ento = StringVar()
            ents = StringVar()

            def add_up():
                hala2 = (ents.get() + "GHC", ento.get() + "KG")
                tree2.insert('', 'end', values=hala2)

                # tree serialization
                with open(l3, "w") as f:
                    yaml.dump(hala2, f)
                #("Edit Item", "You have succesfully edited the entries.")
                # i + 1

            ento = ttk.Entry(datum, width=20, font=('arial', 12, ''))
            ento.grid(row=0, column=1)

            ents = ttk.Entry(datum, width=20, font=('arial', 12, ''))
            ents.grid(row=1, column=1)

            seph = ttk.Separator(datum, orient='horizontal')
            # sep.pack(side = BOTTOM)e
            seph.grid(row=2, column=0, sticky='n,w,e,s', columnspan=2, ipadx=200, ipady=1, padx=5, pady=5)

            btn = ttk.Button(datum, text="OK", style='Wild.TButton', command=add_up)
            btn.grid(row=3, column=0, sticky='E', padx=5, pady=1)

            btn1 = ttk.Button(datum, text="Cancel", command=datum.destroy)
            btn1.grid(row=3, column=1, sticky='W', padx=5, pady=1)

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

        lb = ttk.Label(go, text="""Are you sure you want to permanetly delete this item?""",
                       font=('Helvetica', 12, 'bold'), background="#E4E4E4")
        lb.grid(row=0, column=0, columnspan=2, sticky='w')

        lb = ttk.Label(go, text="""
            Items deleted would not be recovereable.""", font=('Helvetica', 12, ''), background="#E4E4E4")
        lb.grid(row=1, column=0, columnspan=3, sticky='w', padx=5, pady=5)

        def del_tree():
            selected_item = tree2.selection()[0]
            tree2.delete(selected_item)
            lost2 = (ents.get() + "", ento.get() + "")
            # tree serialization
            with open(l3, "w") as f:
                yaml.dump(lost2, f)
            # tree1.insert('', 'end', text="Item", values=0)
            #("Delete Item", "You have succesfully deleted the entries.")
            go.destroy()

        bn = ttk.Button(go, text="Cancel", command=go.destroy)
        bn.grid(row=2, column=0, pady=5, ipadx=90, ipady=10)

        bn1 = ttk.Button(go, text="Delete", style='Minis.TButton', command=del_tree)
        bn1.grid(row=2, column=1, pady=5, ipadx=90, ipady=10)

    # =======================================================================================================================
    # We focus on rollman to now dump the inputs
    # Tree serialization
    with open(l3, "r") as f:
        dany2 = yaml.load(f)

    tree2 = ttk.Treeview(counter, columns=(1, 0), displaycolumns=(0, 1,), height=2, selectmode='browse',
                         show='headings')
    tree2.heading('#0', text='Itemo')
    tree2.heading('#1', text='Item')
    tree2.heading('#2', text='Price')
    tree2.insert('', 'end', text="Item", values=dany2)
    tree2.grid(row=4, column=0, padx=1, pady=5, sticky='w')
    i = 0
    b8 = ttk.Button(counter, text='+', command=add_all2, style="Mini.TButton")
    b8.grid(row=4, column=1, rowspan=1, padx=5, pady=5, )
    b9 = ttk.Button(counter, text='...', command=sub_all2, style="Mini.TButton")
    b9.grid(row=4, column=2, padx=5, pady=5, )
    b10 = ttk.Button(counter, text='-', command=iexits2, style="Minis.TButton")
    b10.grid(row=4, column=4, padx=5, pady=5, )

    # =====================We handle another serialization context here. Its the fourth file=================================
    def add_all3():
        try:
            data = Toplevel(height="300", width="730", relief="flat")
            data.geometry("450x150-410+280")
            data.minsize("440", "120")
            data.maxsize("440", "120")
            data.title("Add Data")
            data.config(background="lavender")

            ent = StringVar()
            ent1 = StringVar()

            lab = ttk.Label(data, text="Item (Input the new Item): ", font=('', 12, ''), background="lavender")
            lab.grid(row=0, column=0, padx=5, pady=5)

            lab1 = ttk.Label(data, text="Price (Input the new Price): ", font=('', 12, ''), background="lavender")
            lab1.grid(row=1, column=0, padx=5, pady=5)

            def add_up():
                # i = 0
                hala3 = (ents.get() + "GHC", ento.get() + "KG")
                tree3.insert('', 'end', values=hala3)

                # tree serialization
                with open(l4, "w") as f:
                    yaml.dump(hala3, f)

                #("Add New Item", "You have succesfully added new entries.")
                # i + 1

            ento = ttk.Entry(data, width=20, font=('arial', 12, ''))
            ento.grid(row=0, column=1)

            ents = ttk.Entry(data, width=20, font=('arial', 12, ''))
            ents.grid(row=1, column=1)

            seph = ttk.Separator(data, orient='horizontal')
            # sep.pack(side = BOTTOM)e
            seph.grid(row=2, column=0, sticky='n,w,e,s', columnspan=2, ipadx=200, ipady=1, padx=5, pady=5)

            btn = ttk.Button(data, text="OK", style='Wild.TButton', command=add_up)
            btn.grid(row=3, column=0, sticky='E', padx=5, pady=1)

            btn1 = ttk.Button(data, text="Cancel", command=data.destroy)
            btn1.grid(row=3, column=1, sticky='W', padx=5, pady=1)

        except:
            tkMessageBox.showerror("Add New Item", "Add new Item failed. Please check input.")
        finally:
            clear()

    def sub_all3():
        try:
            datum = Toplevel(height="200", width="770", relief="flat")
            datum.geometry("460x150-410+280")
            datum.minsize("450", "120")
            datum.maxsize("450", "120")
            datum.title("Edit Data")
            datum.config(background="lavender")

            ent = StringVar()
            ent1 = StringVar()

            lab = ttk.Label(datum, text="Item (Edit the selected Item): ", font=('', 12, ''), background="lavender")
            lab.grid(row=0, column=0, padx=5, pady=5)

            lab1 = ttk.Label(datum, text="Price (Edit the price): ", font=('', 12, ''), background="lavender")
            lab1.grid(row=1, column=0, padx=5, pady=5)

            ento = StringVar()
            ents = StringVar()

            def add_up():
                hala3 = (ents.get() + "GHC", ento.get() + "KG")
                tree3.insert('', 'end', values=hala3)

                # tree serialization
                with open(l4, "w") as f:
                    yaml.dump(hala3, f)
                #("Edit Item", "You have succesfully edited the entries.")
                # i + 1

            ento = ttk.Entry(datum, width=20, font=('arial', 12, ''))
            ento.grid(row=0, column=1)

            ents = ttk.Entry(datum, width=20, font=('arial', 12, ''))
            ents.grid(row=1, column=1)

            seph = ttk.Separator(datum, orient='horizontal')
            # sep.pack(side = BOTTOM)e
            seph.grid(row=2, column=0, sticky='n,w,e,s', columnspan=2, ipadx=200, ipady=1, padx=5, pady=5)

            btn = ttk.Button(datum, text="OK", style='Wild.TButton', command=add_up)
            btn.grid(row=3, column=0, sticky='E', padx=5, pady=1)

            btn1 = ttk.Button(datum, text="Cancel", command=datum.destroy)
            btn1.grid(row=3, column=1, sticky='W', padx=5, pady=1)

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

        lb = ttk.Label(go, text="""Are you sure you want to permanetly delete this item?""",
                       font=('Helvetica', 12, 'bold'), background="#E4E4E4")
        lb.grid(row=0, column=0, columnspan=2, sticky='w')

        lb = ttk.Label(go, text="""
            Items deleted would not be recovereable.""", font=('Helvetica', 12, ''), background="#E4E4E4")
        lb.grid(row=1, column=0, columnspan=3, sticky='w', padx=5, pady=5)

        def del_tree():
            selected_item = tree3.selection()[0]
            tree3.delete(selected_item)
            lost3 = (ents.get() + "", ento.get() + "")
            # tree serialization
            with open(l4, "w") as f:
                yaml.dump(lost3, f)
            # tree1.insert('', 'end', text="Item", values=0)
            #("Delete Item", "You have succesfully deleted the entries.")
            go.destroy()

        bn = ttk.Button(go, text="Cancel", command=go.destroy)
        bn.grid(row=2, column=0, pady=5, ipadx=90, ipady=10)

        bn1 = ttk.Button(go, text="Delete", style='Minis.TButton', command=del_tree)
        bn1.grid(row=2, column=1, pady=5, ipadx=90, ipady=10)

    # =======================================================================================================================
    # We focus on rollman to now dump the inputs
    # Tree serialization
    with open(l4, "r") as f:
        dany3 = yaml.load(f)
    tree3 = ttk.Treeview(counter, columns=(1, 0), displaycolumns=(0, 1,), height=2, selectmode='browse',
                         show='headings')
    tree3.heading('#0', text='Itemo')
    tree3.heading('#1', text='Item')
    tree3.heading('#2', text='Price')
    tree3.insert('', 'end', text="Item", values=dany3)
    tree3.grid(row=5, column=0, padx=1, pady=5, sticky='w')
    i = 0
    b11 = ttk.Button(counter, text='+', command=add_all3, style="Mini.TButton")
    b11.grid(row=5, column=1, rowspan=1, padx=5, pady=5, )
    b12 = ttk.Button(counter, text='...', command=sub_all3, style="Mini.TButton")
    b12.grid(row=5, column=2, padx=5, pady=5, )
    b13 = ttk.Button(counter, text='-', command=iexits3, style="Minis.TButton")
    b13.grid(row=5, column=4, padx=5, pady=5, )

    # We handle another tree view serialization=============================================================================
    # =====================We handle another serialization context here. Its the fourth file=================================
    def add_all4():
        try:
            data = Toplevel(height="300", width="730", relief="flat")
            data.geometry("450x150-410+280")
            data.minsize("440", "120")
            data.maxsize("440", "120")
            data.title("Add Data")
            data.config(background="lavender")

            ent = StringVar()
            ent1 = StringVar()

            lab = ttk.Label(data, text="Item (Input the new Item): ", font=('', 12, ''), background="lavender")
            lab.grid(row=0, column=0, padx=5, pady=5)

            lab1 = ttk.Label(data, text="Price (Input the new Price): ", font=('', 12, ''), background="lavender")
            lab1.grid(row=1, column=0, padx=5, pady=5)

            def add_up():
                # i = 0
                hala4 = (ents.get() + "GHC", ento.get() + "KG")
                tree4.insert('', 'end', values=hala4)

                # tree serialization
                with open(l5, "w") as f:
                    yaml.dump(hala4, f)

                #("Add New Item", "You have succesfully added new entries.")
                # i + 1

            ento = ttk.Entry(data, width=20, font=('arial', 12, ''))
            ento.grid(row=0, column=1)

            ents = ttk.Entry(data, width=20, font=('arial', 12, ''))
            ents.grid(row=1, column=1)

            seph = ttk.Separator(data, orient='horizontal')
            # sep.pack(side = BOTTOM)e
            seph.grid(row=2, column=0, sticky='n,w,e,s', columnspan=2, ipadx=200, ipady=1, padx=5, pady=5)

            btn = ttk.Button(data, text="OK", style='Wild.TButton', command=add_up)
            btn.grid(row=3, column=0, sticky='E', padx=5, pady=1)

            btn1 = ttk.Button(data, text="Cancel", command=data.destroy)
            btn1.grid(row=3, column=1, sticky='W', padx=5, pady=1)

        except:
            tkMessageBox.showerror("Add New Item", "Add new Item failed. Please check input.")
        finally:
            clear()

    def sub_all4():
        try:
            datum = Toplevel(height="200", width="770", relief="flat")
            datum.geometry("460x150-410+280")
            datum.minsize("450", "120")
            datum.maxsize("450", "120")
            datum.title("Edit Data")
            datum.config(background="lavender")

            ent = StringVar()
            ent1 = StringVar()

            lab = ttk.Label(datum, text="Item (Edit the selected Item): ", font=('', 12, ''), background="lavender")
            lab.grid(row=0, column=0, padx=5, pady=5)

            lab1 = ttk.Label(datum, text="Price (Edit the price): ", font=('', 12, ''), background="lavender")
            lab1.grid(row=1, column=0, padx=5, pady=5)

            ento = StringVar()
            ents = StringVar()

            def add_up():
                hala4 = (ents.get() + "GHC", ento.get() + "KG")
                tree4.insert('', 'end', values=hala4)

                # tree serialization
                with open(l5, "w") as f:
                    yaml.dump(hala4, f)
                #("Edit Item", "You have succesfully edited the entries.")
                # i + 1

            ento = ttk.Entry(datum, width=20, font=('arial', 12, ''))
            ento.grid(row=0, column=1)

            ents = ttk.Entry(datum, width=20, font=('arial', 12, ''))
            ents.grid(row=1, column=1)

            seph = ttk.Separator(datum, orient='horizontal')
            # sep.pack(side = BOTTOM)e
            seph.grid(row=2, column=0, sticky='n,w,e,s', columnspan=2, ipadx=200, ipady=1, padx=5, pady=5)

            btn = ttk.Button(datum, text="OK", style='Wild.TButton', command=add_up)
            btn.grid(row=3, column=0, sticky='E', padx=5, pady=1)

            btn1 = ttk.Button(datum, text="Cancel", command=datum.destroy)
            btn1.grid(row=3, column=1, sticky='W', padx=5, pady=1)

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

        lb = ttk.Label(go, text="""Are you sure you want to permanetly delete this item?""",
                       font=('Helvetica', 12, 'bold'), background="#E4E4E4")
        lb.grid(row=0, column=0, columnspan=2, sticky='w')

        lb = ttk.Label(go, text="""
            Items deleted would not be recovereable.""", font=('Helvetica', 12, ''), background="#E4E4E4")
        lb.grid(row=1, column=0, columnspan=3, sticky='w', padx=5, pady=5)

        def del_tree():
            selected_item = tree4.selection()[0]
            tree4.delete(selected_item)
            lost4 = (ents.get() + "", ento.get() + "")
            # tree serialization
            with open(l5, "w") as f:
                yaml.dump(lost4, f)
            # tree1.insert('', 'end', text="Item", values=0)
            #("Delete Item", "You have succesfully deleted the entries.")
            go.destroy()

        bn = ttk.Button(go, text="Cancel", command=go.destroy)
        bn.grid(row=2, column=0, pady=5, ipadx=90, ipady=10)

        bn1 = ttk.Button(go, text="Delete", style='Minis.TButton', command=del_tree)
        bn1.grid(row=2, column=1, pady=5, ipadx=90, ipady=10)

    # =======================================================================================================================
    # We focus on rollman to now dump the inputs
    # Tree serialization
    with open(l5, "r") as f:
        dany4 = yaml.load(f)

    tree4 = ttk.Treeview(counter, columns=(1, 0), displaycolumns=(0, 1,), height=2, selectmode='browse',
                         show='headings')
    tree4.heading('#0', text='Itemo')
    tree4.heading('#1', text='Item')
    tree4.heading('#2', text='Price')
    tree4.insert('', 'end', text="Item", values=dany4)
    tree4.grid(row=6, column=0, padx=1, pady=5, sticky='w')
    i = 0
    b14 = ttk.Button(counter, text='+', command=add_all4, style="Mini.TButton")
    b14.grid(row=6, column=1, rowspan=1, padx=5, pady=5, )
    b15 = ttk.Button(counter, text='...', command=sub_all4, style="Mini.TButton")
    b15.grid(row=6, column=2, padx=5, pady=5, )
    b16 = ttk.Button(counter, text='-', command=iexits4, style="Minis.TButton")
    b16.grid(row=6, column=4, padx=5, pady=5, )

    # Game on Dawn, we continue with our mashalling in yaml format==========================================================
    # =====================We handle another serialization context here. Its the fourth file=================================
    def add_all5():
        try:
            data = Toplevel(height="300", width="730", relief="flat")
            data.geometry("450x150-410+280")
            data.minsize("440", "120")
            data.maxsize("440", "120")
            data.title("Add Data")
            data.config(background="lavender")

            ent = StringVar()
            ent1 = StringVar()

            lab = ttk.Label(data, text="Item (Input the new Item): ", font=('', 12, ''), background="lavender")
            lab.grid(row=0, column=0, padx=5, pady=5)

            lab1 = ttk.Label(data, text="Price (Input the new Price): ", font=('', 12, ''), background="lavender")
            lab1.grid(row=1, column=0, padx=5, pady=5)

            def add_up():
                # i = 0
                hala5 = (ents.get() + "GHC", ento.get() + "KG")
                tree5.insert('', 'end', values=hala5)

                # tree serialization
                with open(l6, "w") as f:
                    yaml.dump(hala5, f)

                #("Add New Item", "You have succesfully added new entries.")
                # i + 1

            ento = ttk.Entry(data, width=20, font=('arial', 12, ''))
            ento.grid(row=0, column=1)

            ents = ttk.Entry(data, width=20, font=('arial', 12, ''))
            ents.grid(row=1, column=1)

            seph = ttk.Separator(data, orient='horizontal')
            # sep.pack(side = BOTTOM)e
            seph.grid(row=2, column=0, sticky='n,w,e,s', columnspan=2, ipadx=200, ipady=1, padx=5, pady=5)

            btn = ttk.Button(data, text="OK", style='Wild.TButton', command=add_up)
            btn.grid(row=3, column=0, sticky='E', padx=5, pady=1)

            btn1 = ttk.Button(data, text="Cancel", command=data.destroy)
            btn1.grid(row=3, column=1, sticky='W', padx=5, pady=1)

        except:
            tkMessageBox.showerror("Add New Item", "Add new Item failed. Please check input.")
        finally:
            clear()

    def sub_all5():
        try:
            datum = Toplevel(height="200", width="770", relief="flat")
            datum.geometry("460x150-410+280")
            datum.minsize("450", "120")
            datum.maxsize("450", "120")
            datum.title("Edit Data")
            datum.config(background="lavender")

            ent = StringVar()
            ent1 = StringVar()

            lab = ttk.Label(datum, text="Item (Edit the selected Item): ", font=('', 12, ''), background="lavender")
            lab.grid(row=0, column=0, padx=5, pady=5)

            lab1 = ttk.Label(datum, text="Price (Edit the price): ", font=('', 12, ''), background="lavender")
            lab1.grid(row=1, column=0, padx=5, pady=5)

            ento = StringVar()
            ents = StringVar()

            def add_up():
                hala5 = (ents.get() + "GHC", ento.get() + "KG")
                tree5.insert('', 'end', values=hala5)

                # tree serialization
                with open(l6, "w") as f:
                    yaml.dump(hala5, f)
                #("Edit Item", "You have succesfully edited the entries.")
                # i + 1

            ento = ttk.Entry(datum, width=20, font=('arial', 12, ''))
            ento.grid(row=0, column=1)

            ents = ttk.Entry(datum, width=20, font=('arial', 12, ''))
            ents.grid(row=1, column=1)

            seph = ttk.Separator(datum, orient='horizontal')
            # sep.pack(side = BOTTOM)e
            seph.grid(row=2, column=0, sticky='n,w,e,s', columnspan=2, ipadx=200, ipady=1, padx=5, pady=5)

            btn = ttk.Button(datum, text="OK", style='Wild.TButton', command=add_up)
            btn.grid(row=3, column=0, sticky='E', padx=5, pady=1)

            btn1 = ttk.Button(datum, text="Cancel", command=datum.destroy)
            btn1.grid(row=3, column=1, sticky='W', padx=5, pady=1)

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

        lb = ttk.Label(go, text="""Are you sure you want to permanetly delete this item?""",
                       font=('Helvetica', 12, 'bold'), background="#E4E4E4")
        lb.grid(row=0, column=0, columnspan=2, sticky='w')

        lb = ttk.Label(go, text="""
            Items deleted would not be recovereable.""", font=('Helvetica', 12, ''), background="#E4E4E4")
        lb.grid(row=1, column=0, columnspan=3, sticky='w', padx=5, pady=5)

        def del_tree():
            selected_item = tree5.selection()[0]
            tree5.delete(selected_item)
            lost5 = (ents.get() + "", ento.get() + "")
            # tree serialization
            with open(l6, "w") as f:
                yaml.dump(lost5, f)
            # tree1.insert('', 'end', text="Item", values=0)
            #("Delete Item", "You have succesfully deleted the entries.")
            go.destroy()

        bn = ttk.Button(go, text="Cancel", command=go.destroy)
        bn.grid(row=2, column=0, pady=5, ipadx=90, ipady=10)

        bn1 = ttk.Button(go, text="Delete", style='Minis.TButton', command=del_tree)
        bn1.grid(row=2, column=1, pady=5, ipadx=90, ipady=10)

    # =======================================================================================================================
    # We focus on rollman to now dump the inputs
    # Tree serialization
    with open(l6, "r") as f:
        dany5 = yaml.load(f)

    tree5 = ttk.Treeview(counter, columns=(1, 0), displaycolumns=(0, 1,), height=2, selectmode='browse',
                         show='headings')
    tree5.heading('#0', text='Itemo')
    tree5.heading('#1', text='Item')
    tree5.heading('#2', text='Price')
    tree5.insert('', 'end', text="Item", values=dany5)
    tree5.grid(row=7, column=0, padx=1, pady=5, sticky='w')
    i = 0
    b17 = ttk.Button(counter, text='+', command=add_all5, style="Mini.TButton")
    b17.grid(row=7, column=1, rowspan=1, padx=5, pady=5, )
    b18 = ttk.Button(counter, text='...', command=sub_all5, style="Mini.TButton")
    b18.grid(row=7, column=2, padx=5, pady=5, )
    b19 = ttk.Button(counter, text='-', command=iexits5, style="Minis.TButton")
    b19.grid(row=7, column=4, padx=5, pady=5, )

    # We continue our mashalling in .yaml So good I have to say.============================================================
    # =====================We handle another serialization context here. Its the fourth file=================================
    def add_all6():
        try:
            data = Toplevel(height="300", width="730", relief="flat")
            data.geometry("450x150-410+280")
            data.minsize("440", "120")
            data.maxsize("440", "120")
            data.title("Add Data")
            data.config(background="lavender")

            ent = StringVar()
            ent1 = StringVar()

            lab = ttk.Label(data, text="Item (Input the new Item): ", font=('', 12, ''), background="lavender")
            lab.grid(row=0, column=0, padx=5, pady=5)

            lab1 = ttk.Label(data, text="Price (Input the new Price): ", font=('', 12, ''), background="lavender")
            lab1.grid(row=1, column=0, padx=5, pady=5)

            def add_up():
                # i = 0
                hala6 = (ents.get() + "GHC", ento.get() + "KG")
                tree6.insert('', 'end', values=hala6)

                # tree serialization
                with open(l7, "w") as f:
                    yaml.dump(hala6, f)

                #("Add New Item", "You have succesfully added new entries.")
                # i + 1

            ento = ttk.Entry(data, width=20, font=('arial', 12, ''))
            ento.grid(row=0, column=1)

            ents = ttk.Entry(data, width=20, font=('arial', 12, ''))
            ents.grid(row=1, column=1)

            seph = ttk.Separator(data, orient='horizontal')
            # sep.pack(side = BOTTOM)e
            seph.grid(row=2, column=0, sticky='n,w,e,s', columnspan=2, ipadx=200, ipady=1, padx=5, pady=5)

            btn = ttk.Button(data, text="OK", style='Wild.TButton', command=add_up)
            btn.grid(row=3, column=0, sticky='E', padx=5, pady=1)

            btn1 = ttk.Button(data, text="Cancel", command=data.destroy)
            btn1.grid(row=3, column=1, sticky='W', padx=5, pady=1)

        except:
            tkMessageBox.showerror("Add New Item", "Add new Item failed. Please check input.")
        finally:
            clear()

    def sub_all6():
        try:
            datum = Toplevel(height="200", width="770", relief="flat")
            datum.geometry("460x150-410+280")
            datum.minsize("450", "120")
            datum.maxsize("450", "120")
            datum.title("Edit Data")
            datum.config(background="lavender")

            ent = StringVar()
            ent1 = StringVar()

            lab = ttk.Label(datum, text="Item (Edit the selected Item): ", font=('', 12, ''), background="lavender")
            lab.grid(row=0, column=0, padx=5, pady=5)

            lab1 = ttk.Label(datum, text="Price (Edit the price): ", font=('', 12, ''), background="lavender")
            lab1.grid(row=1, column=0, padx=5, pady=5)

            ento = StringVar()
            ents = StringVar()

            def add_up():
                hala6 = (ents.get() + "GHC", ento.get() + "KG")
                tree6.insert('', 'end', values=hala6)

                # tree serialization
                with open(l7, "w") as f:
                    yaml.dump(hala6, f)
                #("Edit Item", "You have succesfully edited the entries.")
                # i + 1

            ento = ttk.Entry(datum, width=20, font=('arial', 12, ''))
            ento.grid(row=0, column=1)

            ents = ttk.Entry(datum, width=20, font=('arial', 12, ''))
            ents.grid(row=1, column=1)

            seph = ttk.Separator(datum, orient='horizontal')
            # sep.pack(side = BOTTOM)e
            seph.grid(row=2, column=0, sticky='n,w,e,s', columnspan=2, ipadx=200, ipady=1, padx=5, pady=5)

            btn = ttk.Button(datum, text="OK", style='Wild.TButton', command=add_up)
            btn.grid(row=3, column=0, sticky='E', padx=5, pady=1)

            btn1 = ttk.Button(datum, text="Cancel", command=datum.destroy)
            btn1.grid(row=3, column=1, sticky='W', padx=5, pady=1)

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

        lb = ttk.Label(go, text="""Are you sure you want to permanetly delete this item?""",
                       font=('Helvetica', 12, 'bold'), background="#E4E4E4")
        lb.grid(row=0, column=0, columnspan=2, sticky='w')

        lb = ttk.Label(go, text="""
            Items deleted would not be recovereable.""", font=('Helvetica', 12, ''), background="#E4E4E4")
        lb.grid(row=1, column=0, columnspan=3, sticky='w', padx=5, pady=5)

        def del_tree():
            selected_item = tree6.selection()[0]
            tree6.delete(selected_item)
            lost6 = (ents.get() + "", ento.get() + "")
            # tree serialization
            with open(l7, "w") as f:
                yaml.dump(lost6, f)
            # tree1.insert('', 'end', text="Item", values=0)
            #("Delete Item", "You have succesfully deleted the entries.")
            go.destroy()

        bn = ttk.Button(go, text="Cancel", command=go.destroy)
        bn.grid(row=2, column=0, pady=5, ipadx=90, ipady=10)

        bn1 = ttk.Button(go, text="Delete", style='Minis.TButton', command=del_tree)
        bn1.grid(row=2, column=1, pady=5, ipadx=90, ipady=10)

    # =======================================================================================================================
    # We focus on rollman to now dump the inputs
    # Tree serialization
    with open(van, "r") as f:
        dany6 = yaml.load(f)
    tree6 = ttk.Treeview(counter, columns=(1, 0), displaycolumns=(0, 1,), height=2, selectmode='browse',
                         show='headings')
    tree6.heading('#0', text='Itemo')
    tree6.heading('#1', text='Item')
    tree6.heading('#2', text='Price')
    tree6.insert('', 'end', text="Item", values=dany6)
    tree6.grid(row=8, column=0, padx=1, pady=5, sticky='w')
    i = 0
    b20 = ttk.Button(counter, text='+', command=add_all6, style="Mini.TButton")
    b20.grid(row=8, column=1, rowspan=1, padx=5, pady=5, )
    b21 = ttk.Button(counter, text='...', command=sub_all6, style="Mini.TButton")
    b21.grid(row=8, column=2, padx=5, pady=5, )
    b22 = ttk.Button(counter, text='-', command=iexits6, style="Minis.TButton")
    b22.grid(row=8, column=4, padx=5, pady=5, )

    # ==========Game on Chief.===============================================================================================
    # =====================We handle another serialization context here. Its the fourth file=================================
    def add_all7():
        try:
            data = Toplevel(height="300", width="730", relief="flat")
            data.geometry("450x150-410+280")
            data.minsize("440", "120")
            data.maxsize("440", "120")
            data.title("Add Data")
            data.config(background="lavender")

            ent = StringVar()
            ent1 = StringVar()

            lab = ttk.Label(data, text="Item (Input the new Item): ", font=('', 12, ''), background="lavender")
            lab.grid(row=0, column=0, padx=5, pady=5)

            lab1 = ttk.Label(data, text="Price (Input the new Price): ", font=('', 12, ''), background="lavender")
            lab1.grid(row=1, column=0, padx=5, pady=5)

            def add_up():
                # i = 0
                hala7 = (ents.get() + "GHC", ento.get() + "KG")
                tree7.insert('', 'end', values=hala7)

                # tree serialization
                with open(l8, "w") as f:
                    yaml.dump(hala7, f)

                #("Add New Item", "You have succesfully added new entries.")
                # i + 1

            ento = ttk.Entry(data, width=20, font=('arial', 12, ''))
            ento.grid(row=0, column=1)

            ents = ttk.Entry(data, width=20, font=('arial', 12, ''))
            ents.grid(row=1, column=1)

            seph = ttk.Separator(data, orient='horizontal')
            # sep.pack(side = BOTTOM)e
            seph.grid(row=2, column=0, sticky='n,w,e,s', columnspan=2, ipadx=200, ipady=1, padx=5, pady=5)

            btn = ttk.Button(data, text="OK", style='Wild.TButton', command=add_up)
            btn.grid(row=3, column=0, sticky='E', padx=5, pady=1)

            btn1 = ttk.Button(data, text="Cancel", command=data.destroy)
            btn1.grid(row=3, column=1, sticky='W', padx=5, pady=1)

        except:
            tkMessageBox.showerror("Add New Item", "Add new Item failed. Please check input.")
        finally:
            clear()

    def sub_all7():
        try:
            datum = Toplevel(height="200", width="770", relief="flat")
            datum.geometry("460x150-410+280")
            datum.minsize("450", "120")
            datum.maxsize("450", "120")
            datum.title("Edit Data")
            datum.config(background="lavender")

            ent = StringVar()
            ent1 = StringVar()

            lab = ttk.Label(datum, text="Item (Edit the selected Item): ", font=('', 12, ''), background="lavender")
            lab.grid(row=0, column=0, padx=5, pady=5)

            lab1 = ttk.Label(datum, text="Price (Edit the price): ", font=('', 12, ''), background="lavender")
            lab1.grid(row=1, column=0, padx=5, pady=5)

            ento = StringVar()
            ents = StringVar()

            def add_up():
                hala7 = (ents.get() + "GHC", ento.get() + "KG")
                tree7.insert('', 'end', values=hala7)

                # tree serialization
                with open(l8, "w") as f:
                    yaml.dump(hala7, f)
                #("Edit Item", "You have succesfully edited the entries.")
                # i + 1

            ento = ttk.Entry(datum, width=20, font=('arial', 12, ''))
            ento.grid(row=0, column=1)

            ents = ttk.Entry(datum, width=20, font=('arial', 12, ''))
            ents.grid(row=1, column=1)

            seph = ttk.Separator(datum, orient='horizontal')
            # sep.pack(side = BOTTOM)e
            seph.grid(row=2, column=0, sticky='n,w,e,s', columnspan=2, ipadx=200, ipady=1, padx=5, pady=5)

            btn = ttk.Button(datum, text="OK", style='Wild.TButton', command=add_up)
            btn.grid(row=3, column=0, sticky='E', padx=5, pady=1)

            btn1 = ttk.Button(datum, text="Cancel", command=datum.destroy)
            btn1.grid(row=3, column=1, sticky='W', padx=5, pady=1)

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

        lb = ttk.Label(go, text="""Are you sure you want to permanetly delete this item?""",
                       font=('Helvetica', 12, 'bold'), background="#E4E4E4")
        lb.grid(row=0, column=0, columnspan=2, sticky='w')

        lb = ttk.Label(go, text="""
            Items deleted would not be recovereable.""", font=('Helvetica', 12, ''), background="#E4E4E4")
        lb.grid(row=1, column=0, columnspan=3, sticky='w', padx=5, pady=5)

        def del_tree():
            selected_item = tree7.selection()[0]
            tree7.delete(selected_item)
            lost7 = (ents.get() + "", ento.get() + "")
            # tree serialization
            with open(l8, "w") as f:
                yaml.dump(lost7, f)
            # tree1.insert('', 'end', text="Item", values=0)
            #("Delete Item", "You have succesfully deleted the entries.")
            go.destroy()

        bn = ttk.Button(go, text="Cancel", command=go.destroy)
        bn.grid(row=2, column=0, pady=5, ipadx=90, ipady=10)

        bn1 = ttk.Button(go, text="Delete", style='Minis.TButton', command=del_tree)
        bn1.grid(row=2, column=1, pady=5, ipadx=90, ipady=10)

    # =======================================================================================================================
    # We focus on rollman to now dump the inputs
    # Tree serialization
    with open(l8, "r") as f:
        dany7 = yaml.load(f)

    tree7 = ttk.Treeview(counter, columns=(1, 0), displaycolumns=(0, 1,), height=2, selectmode='browse',
                         show='headings')
    tree7.heading('#0', text='Itemo')
    tree7.heading('#1', text='Item')
    tree7.heading('#2', text='Price')
    tree7.insert('', 'end', text="Item", values=dany7)
    tree7.grid(row=9, column=0, padx=1, pady=5, sticky='w')
    i = 0
    b23 = ttk.Button(counter, text='+', command=add_all7, style="Mini.TButton")
    b23.grid(row=9, column=1, rowspan=1, padx=5, pady=5, )
    b24 = ttk.Button(counter, text='...', command=sub_all7, style="Mini.TButton")
    b24.grid(row=9, column=2, padx=5, pady=5, )
    b25 = ttk.Button(counter, text='-', command=iexits7, style="Minis.TButton")
    b25.grid(row=9, column=4, padx=5, pady=5, )

    lb2 = ttk.Label(counter,
                    text="""      Tips: In order to see changes take effect, please restart apllication. Thank you.""",
                    font=('DejaVu Sans Mono', 11, ''), background='#E4E4E4')
    lb2.grid(row=1, column=6, columnspan=9, sticky='e')

    # We do more here. The serialization of our tree view widgets===========================================================
    def add_all8():
        try:
            data = Toplevel(height="300", width="730", relief="flat")
            data.geometry("450x150-410+280")
            data.minsize("440", "120")
            data.maxsize("440", "120")
            data.title("Add Data")
            data.config(background="lavender")

            ent = StringVar()
            ent1 = StringVar()

            lab = ttk.Label(data, text="Item (Input the new Item): ", font=('', 12, ''), background="lavender")
            lab.grid(row=0, column=0, padx=5, pady=5)

            lab1 = ttk.Label(data, text="Price (Input the new Price): ", font=('', 12, ''), background="lavender")
            lab1.grid(row=1, column=0, padx=5, pady=5)

            def add_up():
                # i = 0
                hala8 = (ents.get() + "GHC", ento.get() + "KG")
                tree8.insert('', 'end', values=hala8)

                # tree serialization
                with open(l9, "w") as f:
                    yaml.dump(hala8, f)

                #("Add New Item", "You have succesfully added new entries.")
                # i + 1

            ento = ttk.Entry(data, width=20, font=('arial', 12, ''))
            ento.grid(row=0, column=1)

            ents = ttk.Entry(data, width=20, font=('arial', 12, ''))
            ents.grid(row=1, column=1)

            seph = ttk.Separator(data, orient='horizontal')
            # sep.pack(side = BOTTOM)e
            seph.grid(row=2, column=0, sticky='n,w,e,s', columnspan=2, ipadx=200, ipady=1, padx=5, pady=5)

            btn = ttk.Button(data, text="OK", style='Wild.TButton', command=add_up)
            btn.grid(row=3, column=0, sticky='E', padx=5, pady=1)

            btn1 = ttk.Button(data, text="Cancel", command=data.destroy)
            btn1.grid(row=3, column=1, sticky='W', padx=5, pady=1)

        except:
            tkMessageBox.showerror("Add New Item", "Add new Item failed. Please check input.")
        finally:
            clear()

    def sub_all8():
        try:
            datum = Toplevel(height="200", width="770", relief="flat")
            datum.geometry("460x150-410+280")
            datum.minsize("450", "120")
            datum.maxsize("450", "120")
            datum.title("Edit Data")
            datum.config(background="lavender")

            ent = StringVar()
            ent1 = StringVar()

            lab = ttk.Label(datum, text="Item (Edit the selected Item): ", font=('', 12, ''), background="lavender")
            lab.grid(row=0, column=0, padx=5, pady=5)

            lab1 = ttk.Label(datum, text="Price (Edit the price): ", font=('', 12, ''), background="lavender")
            lab1.grid(row=1, column=0, padx=5, pady=5)

            ento = StringVar()
            ents = StringVar()

            def add_up():
                hala8 = (ents.get() + "GHC", ento.get() + "KG")
                tree8.insert('', 'end', values=hala8)

                # tree serialization
                with open(l9, "w") as f:
                    yaml.dump(hala8, f)
                #("Edit Item", "You have succesfully edited the entries.")
                # i + 1

            ento = ttk.Entry(datum, width=20, font=('arial', 12, ''))
            ento.grid(row=0, column=1)

            ents = ttk.Entry(datum, width=20, font=('arial', 12, ''))
            ents.grid(row=1, column=1)

            seph = ttk.Separator(datum, orient='horizontal')
            # sep.pack(side = BOTTOM)e
            seph.grid(row=2, column=0, sticky='n,w,e,s', columnspan=2, ipadx=200, ipady=1, padx=5, pady=5)

            btn = ttk.Button(datum, text="OK", style='Wild.TButton', command=add_up)
            btn.grid(row=3, column=0, sticky='E', padx=5, pady=1)

            btn1 = ttk.Button(datum, text="Cancel", command=datum.destroy)
            btn1.grid(row=3, column=1, sticky='W', padx=5, pady=1)

        except:
            tkMessageBox.showerror("Add New Item", "Add new Item failed. Please check input.")
        finally:
            clear()

    def iexits8():
        go = Toplevel(height="400", width="500", relief="flat")
        go.geometry("465x125-450+300")
        #        go.minsize("485", "160")
        #        go.maxsize("485", "160")
        go.title("Delete")
        go.resizable(0, 0)
        go.config(background="#E4E4E4")
        #        go.overrideredirect(True)
        go.attributes("-toolwindow", 1)

        lb = ttk.Label(go, text="""Are you sure you want to permanetly delete this item?""",
                       font=('Helvetica', 12, 'bold'), background="#E4E4E4")
        lb.grid(row=0, column=0, columnspan=2, sticky='w')

        lb = ttk.Label(go, text="""
            Items deleted would not be recovereable.""", font=('Helvetica', 12, ''), background="#E4E4E4")
        lb.grid(row=1, column=0, columnspan=3, sticky='w', padx=5, pady=5)

        def del_tree():
            selected_item = tree8.selection()[0]
            tree8.delete(selected_item)
            lost8 = (ents.get() + "", ento.get() + "")
            # tree serialization
            with open(l9, "w") as f:
                yaml.dump(lost8, f)
            # tree1.insert('', 'end', text="Item", values=0)
            #("Delete Item", "You have succesfully deleted the entries.")
            go.destroy()

        bn = ttk.Button(go, text="Cancel", command=go.destroy)
        bn.grid(row=2, column=0, pady=5, ipadx=90, ipady=10)

        bn1 = ttk.Button(go, text="Delete", style='Minis.TButton', command=del_tree)
        bn1.grid(row=2, column=1, pady=5, ipadx=90, ipady=10)

    # =======================================================================================================================
    # We focus on rollman to now dump the inputs
    # Tree serialization
    with open(l9, "r") as f:
        dany8 = yaml.load(f)

    tree8 = ttk.Treeview(counter, columns=(1, 0), displaycolumns=(0, 1,), height=2, selectmode='browse',
                         show='headings')
    tree8.heading('#0', text='Itemo')
    tree8.heading('#1', text='Item')
    tree8.heading('#2', text='Price')
    tree8.insert('', 'end', text="Item", values=dany8)
    tree8.grid(row=2, column=7, columnspan=1, padx=40, pady=5, sticky='n,e,s,w')
    i = 0
    b26 = ttk.Button(counter, text='+', command=add_all8, style="Mini.TButton")
    b26.grid(row=2, column=8, padx=5, pady=5, sticky='w')
    b27 = ttk.Button(counter, text='...', command=sub_all8, style="Mini.TButton")
    b27.grid(row=2, column=9, padx=5, pady=5, sticky='w')
    b28 = ttk.Button(counter, text='-', command=iexits8, style="Minis.TButton")
    b28.grid(row=2, column=10, padx=5, pady=5, sticky='w')

    # Lets move on with what we're doing. Serializing into our yaml file====================================================
    def add_all9():
        try:
            data = Toplevel(height="300", width="730", relief="flat")
            data.geometry("450x150-410+280")
            data.minsize("440", "120")
            data.maxsize("440", "120")
            data.title("Add Data")
            data.config(background="lavender")

            ent = StringVar()
            ent1 = StringVar()

            lab = ttk.Label(data, text="Item (Input the new Item): ", font=('', 12, ''), background="lavender")
            lab.grid(row=0, column=0, padx=5, pady=5)

            lab1 = ttk.Label(data, text="Price (Input the new Price): ", font=('', 12, ''), background="lavender")
            lab1.grid(row=1, column=0, padx=5, pady=5)

            def add_up():
                # i = 0
                hala9 = (ents.get() + "GHC", ento.get() + "KG")
                tree9.insert('', 'end', values=hala9)

                # tree serialization
                with open(l10, "w") as f:
                    yaml.dump(hala9, f)

                #("Add New Item", "You have succesfully added new entries.")
                # i + 1

            ento = ttk.Entry(data, width=20, font=('arial', 12, ''))
            ento.grid(row=0, column=1)

            ents = ttk.Entry(data, width=20, font=('arial', 12, ''))
            ents.grid(row=1, column=1)

            seph = ttk.Separator(data, orient='horizontal')
            # sep.pack(side = BOTTOM)e
            seph.grid(row=2, column=0, sticky='n,w,e,s', columnspan=2, ipadx=200, ipady=1, padx=5, pady=5)

            btn = ttk.Button(data, text="OK", style='Wild.TButton', command=add_up)
            btn.grid(row=3, column=0, sticky='E', padx=5, pady=1)

            btn1 = ttk.Button(data, text="Cancel", command=data.destroy)
            btn1.grid(row=3, column=1, sticky='W', padx=5, pady=1)

        except:
            tkMessageBox.showerror("Add New Item", "Add new Item failed. Please check input.")
        finally:
            clear()

    def sub_all9():
        try:
            datum = Toplevel(height="200", width="770", relief="flat")
            datum.geometry("460x150-410+280")
            datum.minsize("450", "120")
            datum.maxsize("450", "120")
            datum.title("Edit Data")
            datum.config(background="lavender")

            ent = StringVar()
            ent1 = StringVar()

            lab = ttk.Label(datum, text="Item (Edit the selected Item): ", font=('', 12, ''), background="lavender")
            lab.grid(row=0, column=0, padx=5, pady=5)

            lab1 = ttk.Label(datum, text="Price (Edit the price): ", font=('', 12, ''), background="lavender")
            lab1.grid(row=1, column=0, padx=5, pady=5)

            ento = StringVar()
            ents = StringVar()

            def add_up():
                hala9 = (ents.get() + "GHC", ento.get() + "KG")
                tree9.insert('', 'end', values=hala9)

                # tree serialization
                with open(l10, "w") as f:
                    yaml.dump(hala9, f)
                #("Edit Item", "You have succesfully edited the entries.")
                # i + 1

            ento = ttk.Entry(datum, width=20, font=('arial', 12, ''))
            ento.grid(row=0, column=1)

            ents = ttk.Entry(datum, width=20, font=('arial', 12, ''))
            ents.grid(row=1, column=1)

            seph = ttk.Separator(datum, orient='horizontal')
            # sep.pack(side = BOTTOM)e
            seph.grid(row=2, column=0, sticky='n,w,e,s', columnspan=2, ipadx=200, ipady=1, padx=5, pady=5)

            btn = ttk.Button(datum, text="OK", style='Wild.TButton', command=add_up)
            btn.grid(row=3, column=0, sticky='E', padx=5, pady=1)

            btn1 = ttk.Button(datum, text="Cancel", command=datum.destroy)
            btn1.grid(row=3, column=1, sticky='W', padx=5, pady=1)

        except:
            tkMessageBox.showerror("Add New Item", "Add new Item failed. Please check input.")
        finally:
            clear()

    def iexits9():
        go = Toplevel(height="400", width="500", relief="flat")
        go.geometry("465x125-450+300")
        #        go.minsize("485", "160")
        #        go.maxsize("485", "160")
        go.title("Delete")
        go.resizable(0, 0)
        go.config(background="#E4E4E4")
        #        go.overrideredirect(True)
        go.attributes("-toolwindow", 1)

        lb = ttk.Label(go, text="""Are you sure you want to permanetly delete this item?""",
                       font=('Helvetica', 12, 'bold'), background="#E4E4E4")
        lb.grid(row=0, column=0, columnspan=2, sticky='w')

        lb = ttk.Label(go, text="""
            Items deleted would not be recovereable.""", font=('Helvetica', 12, ''), background="#E4E4E4")
        lb.grid(row=1, column=0, columnspan=3, sticky='w', padx=5, pady=5)

        def del_tree():
            selected_item = tree9.selection()[0]
            tree9.delete(selected_item)
            lost9 = (ents.get() + "", ento.get() + "")
            # tree serialization
            with open(l10, "w") as f:
                yaml.dump(lost9, f)
            # tree1.insert('', 'end', text="Item", values=0)
            #("Delete Item", "You have succesfully deleted the entries.")
            go.destroy()

        bn = ttk.Button(go, text="Cancel", command=go.destroy)
        bn.grid(row=2, column=0, pady=5, ipadx=90, ipady=10)

        bn1 = ttk.Button(go, text="Delete", style='Minis.TButton', command=del_tree)
        bn1.grid(row=2, column=1, pady=5, ipadx=90, ipady=10)

    # =======================================================================================================================
    # We focus on rollman to now dump the inputs
    # Tree serialization
    with open(l10, "r") as f:
        dany9 = yaml.load(f)

    tree9 = ttk.Treeview(counter, columns=(1, 0), displaycolumns=(0, 1,), height=2, selectmode='browse',
                         show='headings')
    tree9.heading('#0', text='Itemo')
    tree9.heading('#1', text='Item')
    tree9.heading('#2', text='Price')
    tree9.insert('', 'end', text="Item", values=dany9)
    tree9.grid(row=3, column=7, columnspan=1, padx=40, pady=5, sticky='n,e,s,w')
    i = 0
    b29 = ttk.Button(counter, text='+', command=add_all9, style="Mini.TButton")
    b29.grid(row=3, column=8, padx=5, pady=5, sticky='w')
    b30 = ttk.Button(counter, text='...', command=sub_all9, style="Mini.TButton")
    b30.grid(row=3, column=9, padx=5, pady=5, sticky='w')
    b31 = ttk.Button(counter, text='-', command=iexits9, style="Minis.TButton")
    b31.grid(row=3, column=10, padx=5, pady=5, sticky='w')

    # =========================Game on Boys==================================================================================
    def add_all10():
        try:
            data = Toplevel(height="300", width="730", relief="flat")
            data.geometry("450x150-410+280")
            data.minsize("440", "120")
            data.maxsize("440", "120")
            data.title("Add Data")
            data.config(background="lavender")

            ent = StringVar()
            ent1 = StringVar()

            lab = ttk.Label(data, text="Item (Input the new Item): ", font=('', 12, ''), background="lavender")
            lab.grid(row=0, column=0, padx=5, pady=5)

            lab1 = ttk.Label(data, text="Price (Input the new Price): ", font=('', 12, ''), background="lavender")
            lab1.grid(row=1, column=0, padx=5, pady=5)

            def add_up():
                # i = 0
                hala10 = (ents.get() + "GHC", ento.get() + "KG")
                tree10.insert('', 'end', values=hala10)

                # tree serialization
                with open(l11, "w") as f:
                    yaml.dump(hala10, f)

                #("Add New Item", "You have succesfully added new entries.")
                # i + 1

            ento = ttk.Entry(data, width=20, font=('arial', 12, ''))
            ento.grid(row=0, column=1)

            ents = ttk.Entry(data, width=20, font=('arial', 12, ''))
            ents.grid(row=1, column=1)

            seph = ttk.Separator(data, orient='horizontal')
            # sep.pack(side = BOTTOM)e
            seph.grid(row=2, column=0, sticky='n,w,e,s', columnspan=2, ipadx=200, ipady=1, padx=5, pady=5)

            btn = ttk.Button(data, text="OK", style='Wild.TButton', command=add_up)
            btn.grid(row=3, column=0, sticky='E', padx=5, pady=1)

            btn1 = ttk.Button(data, text="Cancel", command=data.destroy)
            btn1.grid(row=3, column=1, sticky='W', padx=5, pady=1)

        except:
            tkMessageBox.showerror("Add New Item", "Add new Item failed. Please check input.")
        finally:
            clear()

    def sub_all10():
        try:
            datum = Toplevel(height="200", width="770", relief="flat")
            datum.geometry("460x150-410+280")
            datum.minsize("450", "120")
            datum.maxsize("450", "120")
            datum.title("Edit Data")
            datum.config(background="lavender")

            ent = StringVar()
            ent1 = StringVar()

            lab = ttk.Label(datum, text="Item (Edit the selected Item): ", font=('', 12, ''), background="lavender")
            lab.grid(row=0, column=0, padx=5, pady=5)

            lab1 = ttk.Label(datum, text="Price (Edit the price): ", font=('', 12, ''), background="lavender")
            lab1.grid(row=1, column=0, padx=5, pady=5)

            ento = StringVar()
            ents = StringVar()

            def add_up():
                hala10 = (ents.get() + "GHC", ento.get() + "KG")
                tree10.insert('', 'end', values=hala10)

                # tree serialization
                with open(l11, "w") as f:
                    yaml.dump(hala10, f)
                #("Edit Item", "You have succesfully edited the entries.")
                # i + 1

            ento = ttk.Entry(datum, width=20, font=('arial', 12, ''))
            ento.grid(row=0, column=1)

            ents = ttk.Entry(datum, width=20, font=('arial', 12, ''))
            ents.grid(row=1, column=1)

            seph = ttk.Separator(datum, orient='horizontal')
            # sep.pack(side = BOTTOM)e
            seph.grid(row=2, column=0, sticky='n,w,e,s', columnspan=2, ipadx=200, ipady=1, padx=5, pady=5)

            btn = ttk.Button(datum, text="OK", style='Wild.TButton', command=add_up)
            btn.grid(row=3, column=0, sticky='E', padx=5, pady=1)

            btn1 = ttk.Button(datum, text="Cancel", command=datum.destroy)
            btn1.grid(row=3, column=1, sticky='W', padx=5, pady=1)

        except:
            tkMessageBox.showerror("Add New Item", "Add new Item failed. Please check input.")
        finally:
            clear()

    def iexits10():
        go = Toplevel(height="400", width="500", relief="flat")
        go.geometry("465x125-450+300")
        #        go.minsize("485", "160")
        #        go.maxsize("485", "160")
        go.title("Delete")
        go.resizable(0, 0)
        go.config(background="#E4E4E4")
        #        go.overrideredirect(True)
        go.attributes("-toolwindow", 1)

        lb = ttk.Label(go, text="""Are you sure you want to permanetly delete this item?""",
                       font=('Helvetica', 12, 'bold'), background="#E4E4E4")
        lb.grid(row=0, column=0, columnspan=2, sticky='w')

        lb = ttk.Label(go, text="""
            Items deleted would not be recovereable.""", font=('Helvetica', 12, ''), background="#E4E4E4")
        lb.grid(row=1, column=0, columnspan=3, sticky='w', padx=5, pady=5)

        def del_tree():
            selected_item = tree10.selection()[0]
            tree10.delete(selected_item)
            lost10 = (ents.get() + "", ento.get() + "")
            # tree serialization
            with open(l11, "w") as f:
                yaml.dump(lost10, f)
            # tree1.insert('', 'end', text="Item", values=0)
            #("Delete Item", "You have succesfully deleted the entries.")
            go.destroy()

        bn = ttk.Button(go, text="Cancel", command=go.destroy)
        bn.grid(row=2, column=0, pady=5, ipadx=90, ipady=10)

        bn1 = ttk.Button(go, text="Delete", style='Minis.TButton', command=del_tree)
        bn1.grid(row=2, column=1, pady=5, ipadx=90, ipady=10)

    # =======================================================================================================================
    # We focus on rollman to now dump the inputs
    # Tree serialization
    with open(l11, "r") as f:
        dany10 = yaml.load(f)

    tree10 = ttk.Treeview(counter, columns=(1, 0), displaycolumns=(0, 1,), height=2, selectmode='browse',
                          show='headings')
    tree10.heading('#0', text='Itemo')
    tree10.heading('#1', text='Item')
    tree10.heading('#2', text='Price')
    tree10.insert('', 'end', text="Item", values=dany10)
    tree10.grid(row=4, column=7, columnspan=1, padx=40, pady=5, sticky='n,e,s,w')
    i = 0
    b32 = ttk.Button(counter, text='+', command=add_all10, style="Mini.TButton")
    b32.grid(row=4, column=8, padx=5, pady=5, sticky='w')
    b33 = ttk.Button(counter, text='...', command=sub_all10, style="Mini.TButton")
    b33.grid(row=4, column=9, padx=5, pady=5, sticky='w')
    b34 = ttk.Button(counter, text='-', command=iexits10, style="Minis.TButton")
    b34.grid(row=4, column=10, padx=5, pady=5, sticky='w')

    # =======================================================================================================================
    def add_all11():
        try:
            data = Toplevel(height="300", width="730", relief="flat")
            data.geometry("450x150-410+280")
            data.minsize("440", "120")
            data.maxsize("440", "120")
            data.title("Add Data")
            data.config(background="lavender")

            ent = StringVar()
            ent1 = StringVar()

            lab = ttk.Label(data, text="Item (Input the new Item): ", font=('', 12, ''), background="lavender")
            lab.grid(row=0, column=0, padx=5, pady=5)

            lab1 = ttk.Label(data, text="Price (Input the new Price): ", font=('', 12, ''), background="lavender")
            lab1.grid(row=1, column=0, padx=5, pady=5)

            def add_up():
                # i = 0
                hala11 = (ents.get() + "GHC", ento.get() + "KG")
                tree11.insert('', 'end', values=hala11)

                # tree serialization
                with open(l12, "w") as f:
                    yaml.dump(hala11, f)

                #("Add New Item", "You have succesfully added new entries.")
                # i + 1

            ento = ttk.Entry(data, width=20, font=('arial', 12, ''))
            ento.grid(row=0, column=1)

            ents = ttk.Entry(data, width=20, font=('arial', 12, ''))
            ents.grid(row=1, column=1)

            seph = ttk.Separator(data, orient='horizontal')
            # sep.pack(side = BOTTOM)e
            seph.grid(row=2, column=0, sticky='n,w,e,s', columnspan=2, ipadx=200, ipady=1, padx=5, pady=5)

            btn = ttk.Button(data, text="OK", style='Wild.TButton', command=add_up)
            btn.grid(row=3, column=0, sticky='E', padx=5, pady=1)

            btn1 = ttk.Button(data, text="Cancel", command=data.destroy)
            btn1.grid(row=3, column=1, sticky='W', padx=5, pady=1)

        except:
            tkMessageBox.showerror("Add New Item", "Add new Item failed. Please check input.")
        finally:
            clear()

    def sub_all11():
        try:
            datum = Toplevel(height="200", width="770", relief="flat")
            datum.geometry("460x150-410+280")
            datum.minsize("450", "120")
            datum.maxsize("450", "120")
            datum.title("Edit Data")
            datum.config(background="lavender")

            ent = StringVar()
            ent1 = StringVar()

            lab = ttk.Label(datum, text="Item (Edit the selected Item): ", font=('', 12, ''), background="lavender")
            lab.grid(row=0, column=0, padx=5, pady=5)

            lab1 = ttk.Label(datum, text="Price (Edit the price): ", font=('', 12, ''), background="lavender")
            lab1.grid(row=1, column=0, padx=5, pady=5)

            ento = StringVar()
            ents = StringVar()

            def add_up():
                hala11 = (ents.get() + "GHC", ento.get() + "KG")
                tree11.insert('', 'end', values=hala11)

                # tree serialization
                with open(l12, "w") as f:
                    yaml.dump(hala11, f)
                #("Edit Item", "You have succesfully edited the entries.")
                # i + 1

            ento = ttk.Entry(datum, width=20, font=('arial', 12, ''))
            ento.grid(row=0, column=1)

            ents = ttk.Entry(datum, width=20, font=('arial', 12, ''))
            ents.grid(row=1, column=1)

            seph = ttk.Separator(datum, orient='horizontal')
            # sep.pack(side = BOTTOM)e
            seph.grid(row=2, column=0, sticky='n,w,e,s', columnspan=2, ipadx=200, ipady=1, padx=5, pady=5)

            btn = ttk.Button(datum, text="OK", style='Wild.TButton', command=add_up)
            btn.grid(row=3, column=0, sticky='E', padx=5, pady=1)

            btn1 = ttk.Button(datum, text="Cancel", command=datum.destroy)
            btn1.grid(row=3, column=1, sticky='W', padx=5, pady=1)

        except:
            tkMessageBox.showerror("Add New Item", "Add new Item failed. Please check input.")
        finally:
            clear()

    def iexits11():
        go = Toplevel(height="400", width="500", relief="flat")
        go.geometry("465x125-450+300")
        #        go.minsize("485", "160")
        #        go.maxsize("485", "160")
        go.title("Delete")
        go.resizable(0, 0)
        go.config(background="#E4E4E4")
        #        go.overrideredirect(True)
        go.attributes("-toolwindow", 1)

        lb = ttk.Label(go, text="""Are you sure you want to permanetly delete this item?""",
                       font=('Helvetica', 12, 'bold'), background="#E4E4E4")
        lb.grid(row=0, column=0, columnspan=2, sticky='w')

        lb = ttk.Label(go, text="""
            Items deleted would not be recovereable.""", font=('Helvetica', 12, ''), background="#E4E4E4")
        lb.grid(row=1, column=0, columnspan=3, sticky='w', padx=5, pady=5)

        def del_tree():
            selected_item = tree11.selection()[0]
            tree11.delete(selected_item)
            lost11 = (ents.get() + "", ento.get() + "")
            # tree serialization
            with open(l12, "w") as f:
                yaml.dump(lost11, f)
            # tree1.insert('', 'end', text="Item", values=0)
            #("Delete Item", "You have succesfully deleted the entries.")
            go.destroy()

        bn = ttk.Button(go, text="Cancel", command=go.destroy)
        bn.grid(row=2, column=0, pady=5, ipadx=90, ipady=10)

        bn1 = ttk.Button(go, text="Delete", style='Minis.TButton', command=del_tree)
        bn1.grid(row=2, column=1, pady=5, ipadx=90, ipady=10)

    # =======================================================================================================================
    # We focus on rollman to now dump the inputs
    # Tree serialization
    with open(l12, "r") as f:
        dany11 = yaml.load(f)

    tree11 = ttk.Treeview(counter, columns=(1, 0), displaycolumns=(0, 1,), height=2, selectmode='browse',
                          show='headings')
    tree11.heading('#0', text='Itemo')
    tree11.heading('#1', text='Item')
    tree11.heading('#2', text='Price')
    tree11.insert('', 'end', text="Item", values=dany11)
    tree11.grid(row=5, column=7, columnspan=1, padx=40, pady=5, sticky='n,e,s,w')
    i = 0
    b35 = ttk.Button(counter, text='+', command=add_all11, style="Mini.TButton")
    b35.grid(row=5, column=8, padx=5, pady=5, sticky='w')
    b36 = ttk.Button(counter, text='...', command=sub_all11, style="Mini.TButton")
    b36.grid(row=5, column=9, padx=5, pady=5, sticky='w')
    b37 = ttk.Button(counter, text='-', command=iexits11, style="Minis.TButton")
    b37.grid(row=5, column=10, padx=5, pady=5, sticky='w')

    # =========================We move on Dawn===============================================================================
    def add_all12():
        try:
            data = Toplevel(height="300", width="730", relief="flat")
            data.geometry("450x150-410+280")
            data.minsize("440", "120")
            data.maxsize("440", "120")
            data.title("Add Data")
            data.config(background="lavender")

            ent = StringVar()
            ent1 = StringVar()

            lab = ttk.Label(data, text="Item (Input the new Item): ", font=('', 12, ''), background="lavender")
            lab.grid(row=0, column=0, padx=5, pady=5)

            lab1 = ttk.Label(data, text="Price (Input the new Price): ", font=('', 12, ''), background="lavender")
            lab1.grid(row=1, column=0, padx=5, pady=5)

            def add_up():
                # i = 0
                hala12 = (ents.get() + "GHC", ento.get() + "KG")
                tree12.insert('', 'end', values=hala12)

                # tree serialization
                with open(l13, "w") as f:
                    yaml.dump(hala12, f)

                #("Add New Item", "You have succesfully added new entries.")
                # i + 1

            ento = ttk.Entry(data, width=20, font=('arial', 12, ''))
            ento.grid(row=0, column=1)

            ents = ttk.Entry(data, width=20, font=('arial', 12, ''))
            ents.grid(row=1, column=1)

            seph = ttk.Separator(data, orient='horizontal')
            # sep.pack(side = BOTTOM)e
            seph.grid(row=2, column=0, sticky='n,w,e,s', columnspan=2, ipadx=200, ipady=1, padx=5, pady=5)

            btn = ttk.Button(data, text="OK", style='Wild.TButton', command=add_up)
            btn.grid(row=3, column=0, sticky='E', padx=5, pady=1)

            btn1 = ttk.Button(data, text="Cancel", command=data.destroy)
            btn1.grid(row=3, column=1, sticky='W', padx=5, pady=1)

        except:
            tkMessageBox.showerror("Add New Item", "Add new Item failed. Please check input.")
        finally:
            clear()

    def sub_all12():
        try:
            datum = Toplevel(height="200", width="770", relief="flat")
            datum.geometry("460x150-410+280")
            datum.minsize("450", "120")
            datum.maxsize("450", "120")
            datum.title("Edit Data")
            datum.config(background="lavender")

            ent = StringVar()
            ent1 = StringVar()

            lab = ttk.Label(datum, text="Item (Edit the selected Item): ", font=('', 12, ''), background="lavender")
            lab.grid(row=0, column=0, padx=5, pady=5)

            lab1 = ttk.Label(datum, text="Price (Edit the price): ", font=('', 12, ''), background="lavender")
            lab1.grid(row=1, column=0, padx=5, pady=5)

            ento = StringVar()
            ents = StringVar()

            def add_up():
                hala12 = (ents.get() + "GHC", ento.get() + "KG")
                tree12.insert('', 'end', values=hala12)

                # tree serialization
                with open(l13, "w") as f:
                    yaml.dump(hala12, f)
                #("Edit Item", "You have succesfully edited the entries.")
                # i + 1

            ento = ttk.Entry(datum, width=20, font=('arial', 12, ''))
            ento.grid(row=0, column=1)

            ents = ttk.Entry(datum, width=20, font=('arial', 12, ''))
            ents.grid(row=1, column=1)

            seph = ttk.Separator(datum, orient='horizontal')
            # sep.pack(side = BOTTOM)e
            seph.grid(row=2, column=0, sticky='n,w,e,s', columnspan=2, ipadx=200, ipady=1, padx=5, pady=5)

            btn = ttk.Button(datum, text="OK", style='Wild.TButton', command=add_up)
            btn.grid(row=3, column=0, sticky='E', padx=5, pady=1)

            btn1 = ttk.Button(datum, text="Cancel", command=datum.destroy)
            btn1.grid(row=3, column=1, sticky='W', padx=5, pady=1)

        except:
            tkMessageBox.showerror("Add New Item", "Add new Item failed. Please check input.")
        finally:
            clear()

    def iexits12():
        go = Toplevel(height="400", width="500", relief="flat")
        go.geometry("465x125-450+300")
        #        go.minsize("485", "160")
        #        go.maxsize("485", "160")
        go.title("Delete")
        go.resizable(0, 0)
        go.config(background="#E4E4E4")
        #        go.overrideredirect(True)
        go.attributes("-toolwindow", 1)

        lb = ttk.Label(go, text="""Are you sure you want to permanetly delete this item?""",
                       font=('Helvetica', 12, 'bold'), background="#E4E4E4")
        lb.grid(row=0, column=0, columnspan=2, sticky='w')

        lb = ttk.Label(go, text="""
            Items deleted would not be recovereable.""", font=('Helvetica', 12, ''), background="#E4E4E4")
        lb.grid(row=1, column=0, columnspan=3, sticky='w', padx=5, pady=5)

        def del_tree():
            selected_item = tree12.selection()[0]
            tree12.delete(selected_item)
            lost12 = (ents.get() + "", ento.get() + "")
            # tree serialization
            with open(l13, "w") as f:
                yaml.dump(lost12, f)
            # tree1.insert('', 'end', text="Item", values=0)
            #("Delete Item", "You have succesfully deleted the entries.")
            go.destroy()

        bn = ttk.Button(go, text="Cancel", command=go.destroy)
        bn.grid(row=2, column=0, pady=5, ipadx=90, ipady=10)

        bn1 = ttk.Button(go, text="Delete", style='Minis.TButton', command=del_tree)
        bn1.grid(row=2, column=1, pady=5, ipadx=90, ipady=10)

    # =======================================================================================================================
    # We focus on rollman to now dump the inputs
    # Tree serialization
    with open(l13, "r") as f:
        dany12 = yaml.load(f)

    tree12 = ttk.Treeview(counter, columns=(1, 0), displaycolumns=(0, 1,), height=2, selectmode='browse',
                          show='headings')
    tree12.heading('#0', text='Itemo')
    tree12.heading('#1', text='Item')
    tree12.heading('#2', text='Price')
    tree12.insert('', 'end', text="Item", values=dany12)
    tree12.grid(row=6, column=7, columnspan=1, padx=40, pady=5, sticky='n,e,s,w')
    i = 0
    b38 = ttk.Button(counter, text='+', command=add_all12, style="Mini.TButton")
    b38.grid(row=6, column=8, padx=5, pady=5, sticky='w')
    b39 = ttk.Button(counter, text='...', command=sub_all12, style="Mini.TButton")
    b39.grid(row=6, column=9, padx=5, pady=5, sticky='w')
    b40 = ttk.Button(counter, text='-', command=iexits12, style="Minis.TButton")
    b40.grid(row=6, column=10, padx=5, pady=5, sticky='w')

    # ========================================We are on moving forward=======================================================
    def add_all13():
        try:
            data = Toplevel(height="300", width="730", relief="flat")
            data.geometry("450x150-410+280")
            data.minsize("440", "120")
            data.maxsize("440", "120")
            data.title("Add Data")
            data.config(background="lavender")

            ent = StringVar()
            ent1 = StringVar()

            lab = ttk.Label(data, text="Item (Input the new Item): ", font=('', 12, ''), background="lavender")
            lab.grid(row=0, column=0, padx=5, pady=5)

            lab1 = ttk.Label(data, text="Price (Input the new Price): ", font=('', 12, ''), background="lavender")
            lab1.grid(row=1, column=0, padx=5, pady=5)

            def add_up():
                # i = 0
                hala13 = (ents.get() + "GHC", ento.get() + "KG")
                tree13.insert('', 'end', values=hala13)

                # tree serialization
                with open(l14, "w") as f:
                    yaml.dump(hala13, f)

                #("Add New Item", "You have succesfully added new entries.")
                # i + 1

            ento = ttk.Entry(data, width=20, font=('arial', 12, ''))
            ento.grid(row=0, column=1)

            ents = ttk.Entry(data, width=20, font=('arial', 12, ''))
            ents.grid(row=1, column=1)

            seph = ttk.Separator(data, orient='horizontal')
            # sep.pack(side = BOTTOM)e
            seph.grid(row=2, column=0, sticky='n,w,e,s', columnspan=2, ipadx=200, ipady=1, padx=5, pady=5)

            btn = ttk.Button(data, text="OK", style='Wild.TButton', command=add_up)
            btn.grid(row=3, column=0, sticky='E', padx=5, pady=1)

            btn1 = ttk.Button(data, text="Cancel", command=data.destroy)
            btn1.grid(row=3, column=1, sticky='W', padx=5, pady=1)

        except:
            tkMessageBox.showerror("Add New Item", "Add new Item failed. Please check input.")
        finally:
            clear()

    def sub_all13():
        try:
            datum = Toplevel(height="200", width="770", relief="flat")
            datum.geometry("460x150-410+280")
            datum.minsize("450", "120")
            datum.maxsize("450", "120")
            datum.title("Edit Data")
            datum.config(background="lavender")

            ent = StringVar()
            ent1 = StringVar()

            lab = ttk.Label(datum, text="Item (Edit the selected Item): ", font=('', 12, ''), background="lavender")
            lab.grid(row=0, column=0, padx=5, pady=5)

            lab1 = ttk.Label(datum, text="Price (Edit the price): ", font=('', 12, ''), background="lavender")
            lab1.grid(row=1, column=0, padx=5, pady=5)

            ento = StringVar()
            ents = StringVar()

            def add_up():
                hala13 = (ents.get() + "GHC", ento.get() + "KG")
                tree13.insert('', 'end', values=hala13)

                # tree serialization
                with open(l14, "w") as f:
                    yaml.dump(hala13, f)
                #("Edit Item", "You have succesfully edited the entries.")
                # i + 1

            ento = ttk.Entry(datum, width=20, font=('arial', 12, ''))
            ento.grid(row=0, column=1)

            ents = ttk.Entry(datum, width=20, font=('arial', 12, ''))
            ents.grid(row=1, column=1)

            seph = ttk.Separator(datum, orient='horizontal')
            # sep.pack(side = BOTTOM)e
            seph.grid(row=2, column=0, sticky='n,w,e,s', columnspan=2, ipadx=200, ipady=1, padx=5, pady=5)

            btn = ttk.Button(datum, text="OK", style='Wild.TButton', command=add_up)
            btn.grid(row=3, column=0, sticky='E', padx=5, pady=1)

            btn1 = ttk.Button(datum, text="Cancel", command=datum.destroy)
            btn1.grid(row=3, column=1, sticky='W', padx=5, pady=1)

        except:
            tkMessageBox.showerror("Add New Item", "Add new Item failed. Please check input.")
        finally:
            clear()

    def iexits13():
        go = Toplevel(height="400", width="500", relief="flat")
        go.geometry("465x125-450+300")
        #        go.minsize("485", "160")
        #        go.maxsize("485", "160")
        go.title("Delete")
        go.resizable(0, 0)
        go.config(background="#E4E4E4")
        #        go.overrideredirect(True)
        go.attributes("-toolwindow", 1)

        lb = ttk.Label(go, text="""Are you sure you want to permanetly delete this item?""",
                       font=('Helvetica', 12, 'bold'), background="#E4E4E4")
        lb.grid(row=0, column=0, columnspan=2, sticky='w')

        lb = ttk.Label(go, text="""
            Items deleted would not be recovereable.""", font=('Helvetica', 12, ''), background="#E4E4E4")
        lb.grid(row=1, column=0, columnspan=3, sticky='w', padx=5, pady=5)

        def del_tree():
            selected_item = tree13.selection()[0]
            tree13.delete(selected_item)
            lost13 = (ents.get() + "", ento.get() + "")
            # tree serialization
            with open(l14, "w") as f:
                yaml.dump(lost13, f)
            # tree1.insert('', 'end', text="Item", values=0)
            #("Delete Item", "You have succesfully deleted the entries.")
            go.destroy()

        bn = ttk.Button(go, text="Cancel", command=go.destroy)
        bn.grid(row=2, column=0, pady=5, ipadx=90, ipady=10)

        bn1 = ttk.Button(go, text="Delete", style='Minis.TButton', command=del_tree)
        bn1.grid(row=2, column=1, pady=5, ipadx=90, ipady=10)

    # =======================================================================================================================
    # We focus on rollman to now dump the inputs
    # Tree serialization
    with open(l14, "r") as f:
        dany13 = yaml.load(f)

    tree13 = ttk.Treeview(counter, columns=(1, 0), displaycolumns=(0, 1,), height=2, selectmode='browse',
                          show='headings')
    tree13.heading('#0', text='Itemo')
    tree13.heading('#1', text='Item')
    tree13.heading('#2', text='Price')
    tree13.insert('', 'end', text="Item", values=dany13)
    tree13.grid(row=7, column=7, columnspan=1, padx=40, pady=5, sticky='n,e,s,w')
    i = 0
    b41 = ttk.Button(counter, text='+', command=add_all13, style="Mini.TButton")
    b41.grid(row=7, column=8, padx=5, pady=5, sticky='w')
    b42 = ttk.Button(counter, text='...', command=sub_all13, style="Mini.TButton")
    b42.grid(row=7, column=9, padx=5, pady=5, sticky='w')
    b43 = ttk.Button(counter, text='-', command=iexits13, style="Minis.TButton")
    b43.grid(row=7, column=10, padx=5, pady=5, sticky='w')

    # ========================================We are on moving forward=======================================================
    def add_all14():
        try:
            data = Toplevel(height="300", width="730", relief="flat")
            data.geometry("450x150-410+280")
            data.minsize("440", "120")
            data.maxsize("440", "120")
            data.title("Add Data")
            data.config(background="lavender")

            ent = StringVar()
            ent1 = StringVar()

            lab = ttk.Label(data, text="Item (Input the new Item): ", font=('', 12, ''), background="lavender")
            lab.grid(row=0, column=0, padx=5, pady=5)

            lab1 = ttk.Label(data, text="Price (Input the new Price): ", font=('', 12, ''), background="lavender")
            lab1.grid(row=1, column=0, padx=5, pady=5)

            def add_up():
                # i = 0
                hala14 = (ents.get() + "GHC", ento.get() + "KG")
                tree14.insert('', 'end', values=hala14)

                # tree serialization
                with open(l15, "w") as f:
                    yaml.dump(hala14, f)

                #("Add New Item", "You have succesfully added new entries.")
                # i + 1

            ento = ttk.Entry(data, width=20, font=('arial', 12, ''))
            ento.grid(row=0, column=1)

            ents = ttk.Entry(data, width=20, font=('arial', 12, ''))
            ents.grid(row=1, column=1)

            seph = ttk.Separator(data, orient='horizontal')
            # sep.pack(side = BOTTOM)e
            seph.grid(row=2, column=0, sticky='n,w,e,s', columnspan=2, ipadx=200, ipady=1, padx=5, pady=5)

            btn = ttk.Button(data, text="OK", style='Wild.TButton', command=add_up)
            btn.grid(row=3, column=0, sticky='E', padx=5, pady=1)

            btn1 = ttk.Button(data, text="Cancel", command=data.destroy)
            btn1.grid(row=3, column=1, sticky='W', padx=5, pady=1)

        except:
            tkMessageBox.showerror("Add New Item", "Add new Item failed. Please check input.")
        finally:
            clear()

    def sub_all14():
        try:
            datum = Toplevel(height="200", width="770", relief="flat")
            datum.geometry("460x150-410+280")
            datum.minsize("450", "120")
            datum.maxsize("450", "120")
            datum.title("Edit Data")
            datum.config(background="lavender")

            ent = StringVar()
            ent1 = StringVar()

            lab = ttk.Label(datum, text="Item (Edit the selected Item): ", font=('', 12, ''), background="lavender")
            lab.grid(row=0, column=0, padx=5, pady=5)

            lab1 = ttk.Label(datum, text="Price (Edit the price): ", font=('', 12, ''), background="lavender")
            lab1.grid(row=1, column=0, padx=5, pady=5)

            ento = StringVar()
            ents = StringVar()

            def add_up():
                hala14 = (ents.get() + "GHC", ento.get() + "KG")
                tree14.insert('', 'end', values=hala14)

                # tree serialization
                with open(l15, "w") as f:
                    yaml.dump(hala14, f)
                #("Edit Item", "You have succesfully edited the entries.")
                # i + 1

            ento = ttk.Entry(datum, width=20, font=('arial', 12, ''))
            ento.grid(row=0, column=1)

            ents = ttk.Entry(datum, width=20, font=('arial', 12, ''))
            ents.grid(row=1, column=1)

            seph = ttk.Separator(datum, orient='horizontal')
            # sep.pack(side = BOTTOM)e
            seph.grid(row=2, column=0, sticky='n,w,e,s', columnspan=2, ipadx=200, ipady=1, padx=5, pady=5)

            btn = ttk.Button(datum, text="OK", style='Wild.TButton', command=add_up)
            btn.grid(row=3, column=0, sticky='E', padx=5, pady=1)

            btn1 = ttk.Button(datum, text="Cancel", command=datum.destroy)
            btn1.grid(row=3, column=1, sticky='W', padx=5, pady=1)

        except:
            tkMessageBox.showerror("Add New Item", "Add new Item failed. Please check input.")
        finally:
            clear()

    def iexits14():
        go = Toplevel(height="400", width="500", relief="flat")
        go.geometry("465x125-450+300")
        #        go.minsize("485", "160")
        #        go.maxsize("485", "160")
        go.title("Delete")
        go.resizable(0, 0)
        go.config(background="#E4E4E4")
        #        go.overrideredirect(True)
        go.attributes("-toolwindow", 1)

        lb = ttk.Label(go, text="""Are you sure you want to permanetly delete this item?""",
                       font=('Helvetica', 12, 'bold'), background="#E4E4E4")
        lb.grid(row=0, column=0, columnspan=2, sticky='w')

        lb = ttk.Label(go, text="""
            Items deleted would not be recovereable.""", font=('Helvetica', 12, ''), background="#E4E4E4")
        lb.grid(row=1, column=0, columnspan=3, sticky='w', padx=5, pady=5)

        def del_tree():
            selected_item = tree14.selection()[0]
            tree14.delete(selected_item)
            lost14 = (ents.get() + "", ento.get() + "")
            # tree serialization
            with open(l15, "w") as f:
                yaml.dump(lost14, f)
            # tree1.insert('', 'end', text="Item", values=0)
            #("Delete Item", "You have succesfully deleted the entries.")
            go.destroy()

        bn = ttk.Button(go, text="Cancel", command=go.destroy)
        bn.grid(row=2, column=0, pady=5, ipadx=90, ipady=10)

        bn1 = ttk.Button(go, text="Delete", style='Minis.TButton', command=del_tree)
        bn1.grid(row=2, column=1, pady=5, ipadx=90, ipady=10)

    # =======================================================================================================================
    # We focus on rollman to now dump the inputs
    # Tree serialization
    with open(l15, "r") as f:
        dany14 = yaml.load(f)

    tree14 = ttk.Treeview(counter, columns=(1, 0), displaycolumns=(0, 1,), height=2, selectmode='browse',
                          show='headings')
    tree14.heading('#0', text='Itemo')
    tree14.heading('#1', text='Item')
    tree14.heading('#2', text='Price')
    tree14.insert('', 'end', text="Item", values=dany14)
    tree14.grid(row=8, column=7, columnspan=1, padx=40, pady=5, sticky='n,e,s,w')
    i = 0
    b44 = ttk.Button(counter, text='+', command=add_all14, style="Mini.TButton")
    b44.grid(row=8, column=8, padx=5, pady=5, sticky='w')
    b45 = ttk.Button(counter, text='...', command=sub_all14, style="Mini.TButton")
    b45.grid(row=8, column=9, padx=5, pady=5, sticky='w')
    b46 = ttk.Button(counter, text='-', command=iexits14, style="Minis.TButton")
    b46.grid(row=8, column=10, padx=5, pady=5, sticky='w')

    # ========================================We are on moving forward=======================================================
    def add_all15():
        try:
            data = Toplevel(height="300", width="730", relief="flat")
            data.geometry("450x150-410+280")
            data.minsize("440", "120")
            data.maxsize("440", "120")
            data.title("Add Data")
            data.config(background="lavender")

            ent = StringVar()
            ent1 = StringVar()

            lab = ttk.Label(data, text="Item (Input the new Item): ", font=('', 12, ''), background="lavender")
            lab.grid(row=0, column=0, padx=5, pady=5)

            lab1 = ttk.Label(data, text="Price (Input the new Price): ", font=('', 12, ''), background="lavender")
            lab1.grid(row=1, column=0, padx=5, pady=5)

            def add_up():
                # i = 0
                hala15 = (ents.get() + "GHC", ento.get() + "KG")
                tree15.insert('', 'end', values=hala15)

                # tree serialization
                with open(l16, "w") as f:
                    yaml.dump(hala15, f)

                #("Add New Item", "You have succesfully added new entries.")
                # i + 1

            ento = ttk.Entry(data, width=20, font=('arial', 12, ''))
            ento.grid(row=0, column=1)

            ents = ttk.Entry(data, width=20, font=('arial', 12, ''))
            ents.grid(row=1, column=1)

            seph = ttk.Separator(data, orient='horizontal')
            # sep.pack(side = BOTTOM)e
            seph.grid(row=2, column=0, sticky='n,w,e,s', columnspan=2, ipadx=200, ipady=1, padx=5, pady=5)

            btn = ttk.Button(data, text="OK", style='Wild.TButton', command=add_up)
            btn.grid(row=3, column=0, sticky='E', padx=5, pady=1)

            btn1 = ttk.Button(data, text="Cancel", command=data.destroy)
            btn1.grid(row=3, column=1, sticky='W', padx=5, pady=1)

        except:
            tkMessageBox.showerror("Add New Item", "Add new Item failed. Please check input.")
        finally:
            clear()

    def sub_all15():
        try:
            datum = Toplevel(height="200", width="770", relief="flat")
            datum.geometry("460x150-410+280")
            datum.minsize("450", "120")
            datum.maxsize("450", "120")
            datum.title("Edit Data")
            datum.config(background="lavender")

            ent = StringVar()
            ent1 = StringVar()

            lab = ttk.Label(datum, text="Item (Edit the selected Item): ", font=('', 12, ''), background="lavender")
            lab.grid(row=0, column=0, padx=5, pady=5)

            lab1 = ttk.Label(datum, text="Price (Edit the price): ", font=('', 12, ''), background="lavender")
            lab1.grid(row=1, column=0, padx=5, pady=5)

            ento = StringVar()
            ents = StringVar()

            def add_up():
                hala15 = (ents.get() + "GHC", ento.get() + "KG")
                tree15.insert('', 'end', values=hala15)

                # tree serialization
                with open(l16, "w") as f:
                    yaml.dump(hala15, f)
                #("Edit Item", "You have succesfully edited the entries.")
                # i + 1

            ento = ttk.Entry(datum, width=20, font=('arial', 12, ''))
            ento.grid(row=0, column=1)

            ents = ttk.Entry(datum, width=20, font=('arial', 12, ''))
            ents.grid(row=1, column=1)

            seph = ttk.Separator(datum, orient='horizontal')
            # sep.pack(side = BOTTOM)e
            seph.grid(row=2, column=0, sticky='n,w,e,s', columnspan=2, ipadx=200, ipady=1, padx=5, pady=5)

            btn = ttk.Button(datum, text="OK", style='Wild.TButton', command=add_up)
            btn.grid(row=3, column=0, sticky='E', padx=5, pady=1)

            btn1 = ttk.Button(datum, text="Cancel", command=datum.destroy)
            btn1.grid(row=3, column=1, sticky='W', padx=5, pady=1)

        except:
            tkMessageBox.showerror("Add New Item", "Add new Item failed. Please check input.")
        finally:
            clear()

    def iexits15():
        go = Toplevel(height="400", width="500", relief="flat")
        go.geometry("465x125-450+300")
        #        go.minsize("485", "160")
        #        go.maxsize("485", "160")
        go.title("Delete")
        go.resizable(0, 0)
        go.config(background="#E4E4E4")
        #        go.overrideredirect(True)
        go.attributes("-toolwindow", 1)

        lb = ttk.Label(go, text="""Are you sure you want to permanetly delete this item?""",
                       font=('Helvetica', 12, 'bold'), background="#E4E4E4")
        lb.grid(row=0, column=0, columnspan=2, sticky='w')

        lb = ttk.Label(go, text="""
            Items deleted would not be recovereable.""", font=('Helvetica', 12, ''), background="#E4E4E4")
        lb.grid(row=1, column=0, columnspan=3, sticky='w', padx=5, pady=5)

        def del_tree():
            selected_item = tree15.selection()[0]
            tree15.delete(selected_item)
            lost15 = (ents.get() + "", ento.get() + "")
            # tree serialization
            with open(l16, "w") as f:
                yaml.dump(lost15, f)
            # tree1.insert('', 'end', text="Item", values=0)
            #("Delete Item", "You have succesfully deleted the entries.")
            go.destroy()

        bn = ttk.Button(go, text="Cancel", command=go.destroy)
        bn.grid(row=2, column=0, pady=5, ipadx=90, ipady=10)

        bn1 = ttk.Button(go, text="Delete", style='Minis.TButton', command=del_tree)
        bn1.grid(row=2, column=1, pady=5, ipadx=90, ipady=10)

    # =======================================================================================================================
    # We focus on rollman to now dump the inputs
    # Tree serialization
    with open(l16, "r") as f:
        dany15 = yaml.load(f)

    tree15 = ttk.Treeview(counter, columns=(1, 0), displaycolumns=(0, 1,), height=2, selectmode='browse',
                          show='headings')
    tree15.heading('#0', text='Itemo')
    tree15.heading('#1', text='Item')
    tree15.heading('#2', text='Price')
    tree15.insert('', 'end', text="Item", values=dany15)
    tree15.grid(row=9, column=7, columnspan=1, padx=40, pady=5, sticky='n,e,s,w')
    i = 0
    b47 = ttk.Button(counter, text='+', command=add_all15, style="Mini.TButton")
    b47.grid(row=9, column=8, padx=5, pady=5, sticky='w')
    b48 = ttk.Button(counter, text='...', command=sub_all15, style="Mini.TButton")
    b48.grid(row=9, column=9, padx=5, pady=5, sticky='w')
    b49 = ttk.Button(counter, text='-', command=iexits15, style="Minis.TButton")
    b49.grid(row=9, column=10, padx=5, pady=5, sticky='w')

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
    path = "dekp.png"
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
#===========================================================================

bn = Button(w1, text='More', command=ctr,bg = "#0066CC", fg = "white", activeforeground = "white", activebackground = "#0066CC", overrelief = "flat", relief = "flat",font = ('DejaVu Sans Mono',10, 'bold'), width = 10,)
bn.grid(row=0, column=0, padx=5, pady=5, )

bn1 = Button(w1, text='About', command=abt,bg = "#0066CC", fg = "white", activeforeground = "white", activebackground = "#0066CC", overrelief = "flat", relief = "flat",font = ('DejaVu Sans Mono',10, 'bold'), width = 10,)
bn1.grid(row=0, columnspan=5, padx=5, pady=5, )

w1.mainloop()