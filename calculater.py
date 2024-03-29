# PROGRAMME DE CALCULATRICE A FAIRE EN EXECUTABLE
#- Resolution de l'ecran
# 2-Definition des bouttons 
# 3- Affichage des Bouttons
# 4-la boucle d'affichage des bounton
# 5- les fonctions

# vveullez bien lire le redme


#importation
import tkinter as tk

# les focntion
def click_btn(event):
    global expression
    text=event.widget.cget('text')
    if text=='=':
        try:
            result = str(eval(expression))
            expression = result
            display_var.set(result)
        except Exception as e:
            expression=''
            display_var.set('Error')
    elif text=='c':
        expression =''
        display_var.set(expression)

# definition de la fenetre
expression=""
app = tk.Tk()
app.title('MA CALCULATRICE')
app.geometry('300x500')
app.configure(bg='lightgray')

# champs de saisir et recup de resultats
display_var = tk.StringVar()
display = tk.Entry(app,textvariable=display_var,font=('Helvetica',20),bd=10,insertwidth=4,width=15,justify='right')
display.grid(row=0,column=0,columnspan=4,padx=10,pady=10)

# définition des bouton et leur position
display.grid(row=0,column=0,columnspan=4,padx=10,pady=10)
buttons = [('7',1,0),('8',1,1),('9',1,2),('/',1,3),
           ('4',2,0),('5',2,1),('6',2,2),('*',2,3),
           ('1',3,0),('2',3,1),('3',3,2),('-',3,3),
           ('c',4,0),('0',4,1),('=',4,2),('+',4,3)]

for (text,row,col) in buttons:
    btn = tk.Button(app,text=text,font=('Helvetica',15),padx=20,pady=20,bg='gray',
                    fg='white')
    btn.grid(row=row,column=col,padx=5,pady=5,sticky='nsew')
    btn.bind('<Button-1>',click_btn)
#maintenir la fentre afficher
app.mainloop()

