from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("500x600")
root.title("DRAWING SHAPES")


    


canvas = Canvas(root , width=900 , height=490 , bg = "white" , highlightbackground = "grey")
canvas.pack()





label1 = Label(root  ,text = "CHOOSE THE COLOUR   : ")
label1.place(relx =0.42  , rely =0.95 , anchor = CENTER)

ffillcolor = ["red" , "green" , "yellow" , "blue" , "orange" , "lightblue" , "pink", "purple" , "lightgreen" , "brown"]
colordropdown = ttk.Combobox(root  ,state = "readonly" , values = ffillcolor  ,width = 10)
colordropdown.place(relx =0.65  , rely =0.95 , anchor = CENTER)






#...............................................................

label2 = Label(root  ,text = "START X : ")
label2.place(relx =0.09 , rely =0.9 , anchor = CENTER)

list1 = [10,50,100,200,300,400,500,600,800,900]
startx = ttk.Combobox(root  ,state = "readonly" , values =list1  ,width = 4)
startx.place(relx =0.21 , rely =0.9, anchor = CENTER)



label3 = Label(root  ,text = "START Y : ")
label3.place(relx =0.34  , rely =0.9 , anchor = CENTER)

list1 = [10,50,100,200,300,400,500,600,800,900]
starty = ttk.Combobox(root  ,state = "readonly" , values =list1  ,width = 4)
starty.place(relx =0.45 , rely =0.9, anchor = CENTER)



label4 = Label(root  ,text = "END X : ")
label4.place(relx =0.58  , rely =0.9 , anchor = CENTER)

list1 = [10,50,100,200,300,400,500,600,800,900]
endx = ttk.Combobox(root  ,state = "readonly" , values =list1  ,width = 4)
endx.place(relx =0.69 , rely =0.9, anchor = CENTER)



label5 = Label(root  ,text = "END Y : ")
label5.place(relx =0.82  , rely =0.9 , anchor = CENTER)

list1 = [10,50,100,200,300,400,500,600,800,900]
endy = ttk.Combobox(root  ,state = "readonly" , values =list1  ,width = 4)
endy.place(relx =0.93 , rely =0.9, anchor = CENTER)



keypress = ""

def circle(event):
    oldx = startx.get()
    oldy = starty.get()
    newx = endx.get()
    newy = endy.get()
    keypress = "c"
    draw(keypress , oldx, oldy, newx, newy)

def rectangle(event):
    oldx = startx.get()
    oldy = starty.get()
    newx = endx.get()
    newy = endy.get()
    keypress = "r"
    draw(keypress, oldx, oldy, newx, newy)
    
def line(event):
    oldx = startx.get()
    oldy = starty.get()
    newx = endx.get()
    newy = endy.get()
    keypress = "l"
    draw(keypress, oldx, oldy, newx, newy)
    

def draw( keypress ,  oldx , oldy  ,newx , newy):
    global ffillcolor
    colorr = ffillcolor

    
    if (keypress == "c"):
        circlee = canvas.create_oval(oldx , oldy  ,newx , newy , width = 3 , fill = colorr)
        
    if(keypress == "r"):
        rectanglee = canvas.create_rectangle(oldx , oldy  ,newx , newy , width  =3, fill = colorr)
        
    if(keypress =="l"):
        linee = canvas.create_line(oldx , oldy  ,newx , newy , width = 3,  fill = colorr)
        
    
    
root.bind("<c>" ,circle ) 
root.bind("<r>" ,rectangle ) 
root.bind("<l>" ,line )   
    
root.mainloop()