import tkinter as tk
from tkinter import messagebox


# osnovni izgled okna
okno = tk.Tk()
okno.title('Pretvornik enot')
okno.geometry('530x280')
okno.resizable(width=False, height=False)
okno.wm_iconbitmap('favicon.ico')

#zacetne spremenljivke
tk.Label(okno, text='Iz enote: ', font='Arial 20 bold').grid(row=1)

var1 = tk.IntVar()
tk.Checkbutton(okno, text="Kilometer", variable=var1, justify='left').grid(row=2, column=0)
var2 = tk.IntVar()
tk.Checkbutton(okno, text="Meter", variable=var2).grid(row=2, column=1)
var3 = tk.IntVar()
tk.Checkbutton(okno, text="Decimeter", variable=var3).grid(row=2, column=2)
var4 = tk.IntVar()
tk.Checkbutton(okno, text="Milja", variable=var4).grid(row=2, column=3)
var5 = tk.IntVar()
tk.Checkbutton(okno, text="Čevelj", variable=var5).grid(row=2, column=4)
var6 = tk.IntVar()
tk.Checkbutton(okno, text="Palec", variable=var6).grid(row=2, column=5)

#napis
tk.Label(okno, text='Vrednost: ', font='Arial 13 bold').grid()

#stevilo, ki ga vnesemo, da ga pretvorimo.
stevilo = tk.IntVar()
stevilo.set('')
tk.Entry(okno, textvariable=stevilo).grid()

#pretvorjene spremenljivke
tk.Label(okno, text='V enoto: ', font='Arial 20 bold').grid()

var10 = tk.IntVar()
tk.Checkbutton(okno, text="Kilometer", variable=var10).grid(row=6, column=0)
var20 = tk.IntVar()
tk.Checkbutton(okno, text="Meter", variable=var20).grid(row=6, column=1)
var30 = tk.IntVar()
tk.Checkbutton(okno, text="Decimeter", variable=var30).grid(row=6, column=2)
var40 = tk.IntVar()
tk.Checkbutton(okno, text="Milja", variable=var40).grid(row=6, column=3)
var50 = tk.IntVar()
tk.Checkbutton(okno, text="Čevelj", variable=var50).grid(row=6, column=4)
var60 = tk.IntVar()
tk.Checkbutton(okno, text="Palec", variable=var60).grid(row=6, column=5)

#ostali gumbi/napisi
tk.Button(okno, text='Pretvori', command=lambda:[preveri(), pretvori_drugo_enoto()], font='Arial 17 bold', fg='green2', bg='grey60').grid(row=8, column=0)

tk.Label(okno, text='Pretvorjeno: ', font='Arial 10 bold').grid(row=9)
tk.Label(okno, text='                                                      ').grid(row=10)

tk.Button(okno, text='Zapri', font='Arial 17 bold', fg='red', bg='grey60', command=okno.quit).grid(row=8, column=5)

#seznama za racunanje:
list1 = [var1, var2, var3, var4, var5, var6]
list2 = [var10, var20, var30, var40, var50, var60]

#funkcija da se klikne samo eno enoto.
def preveri():
    skupaj1 = 0
    for i in list1:
        if i.get() == 1:
            skupaj1 += 1
    if skupaj1 > 1 or skupaj1 == 0:
        return messagebox.showinfo("Opozorilo!", "Izbrati morate ENO vhodno enoto, ki jo želite pretvoriti. Poizkusite ponovno.")
    skupaj2 = 0
    for i in list2:
        if i.get() == 1:
            skupaj2 += 1
    if skupaj2 > 1 or skupaj2 == 0:
        return messagebox.showinfo("Opozorilo!", "Izbrati morate ENO enoto, v katero želite pretvoriti. Poizkusite ponovno.")

#funkcija za racunanje
def pretvori_drugo_enoto():
    for i in list1:
        if i.get() == 1:
            mesto1 = list1.index(i)
    for j in list2:
        if j.get() == 1:
            mesto2 = list2.index(j)
    if mesto1 == 0:
        if mesto2 == 0:
            tk.Label(okno, text='                                                      ').grid(row=10)
            tk.Label(okno, text=round(stevilo.get(), 2)).grid(row=10, column=0)
        if mesto2 == 1:
            tk.Label(okno, text='                                                      ').grid(row=10)
            tk.Label(okno, text=round(stevilo.get() * 1000, 2)).grid(row=10, column=0)
        if mesto2 == 2:
            tk.Label(okno, text='                                                      ').grid(row=10)
            tk.Label(okno, text=round(stevilo.get() * 10000, 2)).grid(row=10, column=0)
        if mesto2 == 3:
            tk.Label(okno, text='                                                      ').grid(row=10)
            tk.Label(okno, text=round(stevilo.get() * 0.621371, 2)).grid(row=10, column=0)
        if mesto2 == 4:
            tk.Label(okno, text='                                                      ').grid(row=10)
            tk.Label(okno, text=round(stevilo.get() * 3280.84, 2)).grid(row=10, column=0)
        if mesto2 == 5:
            tk.Label(okno, text='                                                      ').grid(row=10)
            tk.Label(okno, text=round(stevilo.get() * 39370.1, 2)).grid(row=10, column=0)
    if mesto1 == 1:
        if mesto2 == 0:
            tk.Label(okno, text='                                                      ').grid(row=10)
            tk.Label(okno, text=round(stevilo.get() / 1000, 2)).grid(row=10, column=0)
        if mesto2 == 1:
            tk.Label(okno, text='                                                      ').grid(row=10)
            tk.Label(okno, text=round(stevilo.get(), 2)).grid(row=10, column=0)
        if mesto2 == 2:
            tk.Label(okno, text='                                                      ').grid(row=10)
            tk.Label(okno, text=round(stevilo.get() * 10, 2)).grid(row=10, column=0)
        if mesto2 == 3:
            tk.Label(okno, text='                                                      ').grid(row=10)
            tk.Label(okno, text=round(stevilo.get() * 0.000621371, 2)).grid(row=10, column=0)
        if mesto2 == 4:
            tk.Label(okno, text='                                                      ').grid(row=10)
            tk.Label(okno, text=round(stevilo.get() * 3.28084, 2)).grid(row=10, column=0)
        if mesto2 == 5:
            tk.Label(okno, text='                                                      ').grid(row=10)
            tk.Label(okno, text=round(stevilo.get() * 39.3701, 2)).grid(row=10, column=0)
    if mesto1 == 2:
        if mesto2 == 0:
            tk.Label(okno, text='                                                      ').grid(row=10)
            tk.Label(okno, text=round(stevilo.get() / 10000, 2)).grid(row=10, column=0)
        if mesto2 == 1:
            tk.Label(okno, text='                                                      ').grid(row=10)
            tk.Label(okno, text=round(stevilo.get() / 10, 2)).grid(row=10, column=0)
        if mesto2 == 2:
            tk.Label(okno, text='                                                      ').grid(row=10)
            tk.Label(okno, text=round(stevilo.get(), 2)).grid(row=10, column=0)
        if mesto2 == 3:
            tk.Label(okno, text='                                                      ').grid(row=10)
            tk.Label(okno, text=round(stevilo.get() * 0.00621371, 2)).grid(row=10, column=0)
        if mesto2 == 4:
            tk.Label(okno, text='                                                      ').grid(row=10)
            tk.Label(okno, text=round(stevilo.get() * 32.8084, 2)).grid(row=10, column=0)
        if mesto2 == 5:
            tk.Label(okno, text='                                                      ').grid(row=10)
            tk.Label(okno, text=round(stevilo.get() * 393.701, 2)).grid(row=10, column=0)
    if mesto1 == 3:
        if mesto2 == 0:
            tk.Label(okno, text='                                                      ').grid(row=10)
            tk.Label(okno, text=round(stevilo.get() * 1.60934, 2)).grid(row=10, column=0)
        if mesto2 == 1:
            tk.Label(okno, text='                                                      ').grid(row=10)
            tk.Label(okno, text=round(stevilo.get() * 1609.34, 2)).grid(row=10, column=0)
        if mesto2 == 2:
            tk.Label(okno, text='                                                      ').grid(row=10)
            tk.Label(okno, text=round(stevilo.get() * 16093.4, 2)).grid(row=10, column=0)
        if mesto2 == 3:
            tk.Label(okno, text='                                                      ').grid(row=10)
            tk.Label(okno, text=round(stevilo.get(), 2)).grid(row=10, column=0)
        if mesto2 == 4:
            tk.Label(okno, text='                                                      ').grid(row=10)
            tk.Label(okno, text=round(stevilo.get() * 5280.00, 2)).grid(row=10, column=0)
        if mesto2 == 5:
            tk.Label(okno, text='                                                      ').grid(row=10)
            tk.Label(okno, text=round(stevilo.get() *  63360, 2)).grid(row=10, column=0)
    if mesto1 == 4:
        if mesto2 == 0:
            tk.Label(okno, text='                                                      ').grid(row=10)
            tk.Label(okno, text=round(stevilo.get() * 0.00030479, 2)).grid(row=10, column=0)
        if mesto2 == 1:
            tk.Label(okno, text='                                                      ').grid(row=10)
            tk.Label(okno, text=round(stevilo.get() * 0.3047999, 2)).grid(row=10, column=0)
        if mesto2 == 2:
            tk.Label(okno, text='                                                      ').grid(row=10)
            tk.Label(okno, text=round(stevilo.get() * 3.047999, 2)).grid(row=10, column=0)
        if mesto2 == 3:
            tk.Label(okno, text='                                                      ').grid(row=10)
            tk.Label(okno, text=round(stevilo.get() * 0.000189393, 2)).grid(row=10, column=0)
        if mesto2 == 4:
            tk.Label(okno, text='                                                      ').grid(row=10)
            tk.Label(okno, text=round(stevilo.get(), 2)).grid(row=10, column=0)
        if mesto2 == 5:
            tk.Label(okno, text='                                                      ').grid(row=10)
            tk.Label(okno, text=round(stevilo.get() *  12.0000060, 2)).grid(row=10, column=0)
    if mesto1 == 5:
        if mesto2 == 0:
            tk.Label(okno, text='                                                      ').grid(row=10)
            tk.Label(okno, text=round(stevilo.get() * 0.000025399986284, 2)).grid(row=10, column=0)
        if mesto2 == 1:
            tk.Label(okno, text='                                                      ').grid(row=10)
            tk.Label(okno, text=round(stevilo.get() * 0.025399986284, 2)).grid(row=10, column=0)
        if mesto2 == 2:
            tk.Label(okno, text='                                                      ').grid(row=10)
            tk.Label(okno, text=round(stevilo.get() * 0.0025399986284, 2)).grid(row=10, column=0)
        if mesto2 == 3:
            tk.Label(okno, text='                                                      ').grid(row=10)
            tk.Label(okno, text=round(stevilo.get() * 0.00001578281, 2)).grid(row=10, column=0)
        if mesto2 == 4:
            tk.Label(okno, text='                                                      ').grid(row=10)
            tk.Label(okno, text=round(stevilo.get() * 0.08333329, 2)).grid(row=10, column=0)
        if mesto2 == 5:
            tk.Label(okno, text='                                                      ').grid(row=10)
            tk.Label(okno, text=round(stevilo.get(), 2)).grid(row=10, column=0)

okno.mainloop()
