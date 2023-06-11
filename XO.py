from tkinter import *
from tkinter import messagebox

pedram = Tk()
equation = StringVar()
equation.set("player X your turn")
player = "X"
h = Label(pedram, textvariable = equation,font = ("Tohoma",26),pady = 50 , padx = 20 , bg="#6f6f65")
h.grid(row = 3 , column = 1,columnspan = 3)

def printer(n):
    global player
    loc(n,player)
    if player == "X":
        player = "O"
        equation.set("player O your turn")
    elif player == "O":
        player = "X"
        equation.set("player X your turn")
    winer()
        
def loc(a,b):
    if a == "1" :
       if l1.get() == "":
          l1.set(b)
       else:
          printer(1)
    elif a == "2" :
       if l2.get() == "":
          l2.set(b)
       else:
          printer(2)
    elif a == "3" :
       if l3.get() == "":
          l3.set(b)
       else:
          printer(3)
    elif a == "4" :
       if l4.get() == "":
          l4.set(b)
       else:
          printer(4)
    elif a == "5" :
       if l5.get() == "":
          l5.set(b)
       else:
          printer(5)
    elif a == "6" :
       if l6.get() == "":
          l6.set(b)
       else:
          printer(6)
    elif a == "7" :
       if l7.get() == "":
          l7.set(b)
       else:
          printer(7)
    elif a == "8" :
       if l8.get() == "":
          l8.set(b)
       else:
          printer(8)
    elif a == "9" :
       if l9.get() == "":
          l9.set(b)
       else:
          printer(9)
def winer():
    if l1.get() == l2.get() == l3.get() and l1.get() != "":
       messagebox.showinfo("winner",f"player {l1.get()} wins!")
       pedram.quit()
    elif l4.get() == l5.get() == l6.get() and l4.get() != "":
       messagebox.showinfo("winner",f"player {l4.get()} wins!")
       pedram.quit()
    elif l7.get() == l8.get() == l9.get() and l7.get() != "":
       messagebox.showinfo("winner",f"player {l7.get()} wins!")
       pedram.quit()
    elif l1.get() == l4.get() == l7.get() and l1.get() != "":
       messagebox.showinfo("winner",f"player {l1.get()} wins!")
       pedram.quit()
    elif l2.get() == l5.get() == l8.get() and l2.get() != "":
       messagebox.showinfo("winner",f"player {l2.get()} wins!")
       pedram.quit()
    elif l3.get() == l6.get() == l9.get() and l3.get() != "":
       messagebox.showinfo("winner",f"player {l3.get()} wins!")
       pedram.quit()
    elif l1.get() == l5.get() == l9.get() and l1.get() != "":
       messagebox.showinfo("winner",f"player {l1.get()} wins!")
       pedram.quit()
    elif l3.get() == l5.get() == l7.get() and l3.get() != "":
       messagebox.showinfo("winner",f"player {l3.get()} wins!")
       pedram.quit()
    elif l1.get() != "" and l2.get() != "" and l3.get() != "" and l4.get() != "" and l5.get() != "" and l6.get() != "" and l7.get() != "" and l8.get() != "" and l9.get() != "":
       messagebox.showinfo("draw","game is draw")
       pedram.quit()
 
#textvariables
l1 = StringVar()
l2 = StringVar()
l3 = StringVar()
l4 = StringVar()
l5 = StringVar()
l6 = StringVar()
l7 = StringVar()
l8 = StringVar()
l9 = StringVar()
#loc
loc1 = Button(pedram,textvariable = l1, font = ("Tohoma",20),width=6,height=3,command = lambda:printer("1"),background="#a0fc4b")
loc1.grid(row = 0 , column = 1)
loc2 = Button(pedram,textvariable = l2, font = ("Tohoma",20),width=6,height=3,command = lambda:printer("2"),background="#a0fc4b")
loc2.grid(row = 0 , column = 2)
loc3 = Button(pedram,textvariable = l3, font = ("Tohoma",20),width=6,height=3,command = lambda:printer("3"),background="#a0fc4b")
loc3.grid(row = 0 , column = 3)
loc4 = Button(pedram,textvariable = l4, font = ("Tohoma",20),width=6,height=3,command = lambda:printer("4"),background="#a0fc4b")
loc4.grid(row = 1 , column = 1)
loc5 = Button(pedram,textvariable = l5, font = ("Tohoma",20),width=6,height=3,command = lambda:printer("5"),background="#a0fc4b")
loc5.grid(row = 1 , column = 2)
loc6 = Button(pedram,textvariable = l6, font = ("Tohoma",20),width=6,height=3,command = lambda:printer("6"),background="#a0fc4b")
loc6.grid(row = 1 , column = 3)
loc7 = Button(pedram,textvariable = l7, font = ("Tohoma",20),width=6,height=3,command = lambda:printer("7"),background="#a0fc4b")
loc7.grid(row = 2 , column = 1)
loc8 = Button(pedram,textvariable = l8, font = ("Tohoma",20),width=6,height=3,command = lambda:printer("8"),background="#a0fc4b")
loc8.grid(row = 2 , column = 2)
loc9 = Button(pedram,textvariable = l9, font = ("Tohoma",20),width=6,height=3,command = lambda:printer("9"),background="#a0fc4b")
loc9.grid(row = 2 , column = 3)


mainloop()

