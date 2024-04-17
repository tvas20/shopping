from tkinter import *
import gerItens

# create root window
root = Tk()
root.geometry('1440x1024')

# adding a label to the root window
textcod = (Label(root, text="Codigo: ")).grid()
textnom = (Label(root, text="Nome: ")).grid()
textpre = (Label(root, text="Preço: ")).grid()

# adding Entry Field
iocod = (Entry(root, width=10)).grid(column=1, row=0)
ionom = (Entry(root, width=10)).grid(column=1, row=1)
iopre = (Entry(root, width=10)).grid(column=1, row=2)

def pre(a,b,c):
    gerItens.addItem(a,b,c)

# botão voltar
backbutton = (Button(root, text='Voltar')).grid(column=0, row=3) #falta o command
#botão de salvar
savebutton = (Button(root, text='Salvar',command=lambda: pre(iocod.get(),ionom.get(),iopre.get()))).grid(column=1, row=3)

# Tkinter event loop
root.mainloop()