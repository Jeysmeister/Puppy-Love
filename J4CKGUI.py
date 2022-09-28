from tkinter import *
from Lexical import lexical_analyzer
from Syntax import SyntaxAnalyzer


compiler = Tk()
compiler.title('J4CK COMPILER')
compiler.geometry('1920x1080')
compiler.attributes('-fullscreen', True)
compiler.configure(background = 'black')


def func1(evt=None):
    lexicaloutput.configure(state='normal')
    errors.configure(state='normal')
    errors.delete('1.0', END)
    lexicaloutput.delete("1.0", END)
    sourcecode = data.get("1.0", END)
    lexres, lexcheck, lexerror, tokens, lineno, datatypez, semantokens, idencheck = lexical_analyzer(sourcecode)
    lexicaloutput.insert(END, lexres)
    errors.insert(END, lexerror)
    if lexcheck is True:
        syntaxerrors,semanerrors,synerror = SyntaxAnalyzer(tokens, lineno,semantokens,datatypez,idencheck)
        syntaxerrorsstr = str(syntaxerrors)
        errors.insert(END, syntaxerrorsstr)
        if syntaxerrors == 'No Syntax Error':
            if semanerrors != 0:
                errors.insert(END, semanerrors)
            else:
                errors.insert(END,"\nNo Semantic Error")
    lexicaloutput.configure(state='disabled')
    errors.configure(state='disabled')

j4ck = Label(compiler, text = "J4CK", fg = "white", bg = "black", font = ("Courier New", 70, 'bold')).place(x=115, y=5)
sc = Label(compiler, text = "Source code", fg = "white", bg = "black", font=("Courier New", 15, 'bold')).place(x=1775, y=5)
er = Label(compiler, text = "Errors", fg = "white", bg = "black", font=("Courier New", 15, 'bold')).place(x=1810, y=680)
le = Label(compiler, text = "Lexemes", fg = "white", bg = "black", font=("Courier New", 15, 'bold')).place(x=10, y=220)

datacontainer = Frame(compiler,relief = "sunken")
data = Text(datacontainer, width = 103, height=25, font=("Courier New", 17), bg = "black", fg = "#FFFFFF", insertbackground='white', undo=True, wrap="none", borderwidth=1)
datavsb = Scrollbar(datacontainer, orient="vertical", command=data.yview)
datahsb = Scrollbar(datacontainer, orient="horizontal", command=data.xview)
datacontainer.place(x=450, y=33)
data.grid(row=0, column=0, sticky="nsew")
datavsb.grid(row=0, column=1, sticky="ns")
datahsb.grid(row=1, column=0, sticky="ew")

lexoutcontainer = Frame(compiler, relief="sunken")
lexicaloutput = Text(lexoutcontainer, width = 30, height=32, font=("Courier New", 17), bg = "black", fg = "#FFFFFF", wrap="none", borderwidth=1)
lexicaloutput.configure(state='disabled')
lexoutvsb = Scrollbar(lexoutcontainer, orient="vertical", command=lexicaloutput.yview)
lexouthsb = Scrollbar(lexoutcontainer, orient="horizontal", command=lexicaloutput.xview)
lexoutcontainer.place(x=5, y=250)
lexicaloutput.grid(row=0, column=0, sticky="nsew")
lexoutvsb.grid(row=0, column=1, sticky="ns")
lexouthsb.grid(row=1, column=0, sticky="ew")

errorcontainer = Frame(compiler, relief="sunken")
errors = Text(errorcontainer, width = 103, height=13.5, font=("Courier New", 17), bg = "black", fg = "#FFFFFF", wrap="none", borderwidth=1)
errors.configure(state='disabled')
errorsvsb = Scrollbar(errorcontainer, orient="vertical", command=errors.yview)
errorshsb = Scrollbar(errorcontainer, orient="horizontal", command=errors.xview)
errorcontainer.place(x=450, y=710)
errors.grid(row=0, column=0, sticky="nsew")
errorsvsb.grid(row=0, column=1, sticky="ns")
errorshsb.grid(row=1, column=0, sticky="ew")

compile_button = Button(compiler, text ="COMPILE / <F5>", fg = "white", bg = "grey", font=("Courier New", 15, 'bold'), command=func1, padx=70, pady=30).place(x=65, y=120)
compiler.bind('<F5>', func1)

compiler.mainloop()
