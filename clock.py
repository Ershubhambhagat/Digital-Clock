print("JAI SHREE RAM")
from tkinter import messagebox
from tkinter import * 
import time
import random
root=Tk()
root.title("Digital Clock")
root.geometry("452x300+300+220")
root.resizable(0,0)
root.config(bg="black")
###############################___DEF CLOCK___################################################33
def clock():
    h=str(time.strftime("%H"))
    m=str(time.strftime("%M"))
    s=str(time.strftime("%S")) 
    #print(h,m,s)
    hlab.config(text=h)
    mlab.config(text=m)
    slab.config(text=s)
    hlab.after(200,clock)
##################################___NOW FUN START___###############

#####################___THIS IS ONLY COLOR NAME___#############################################
colors = ['red', 'blue', 'yellow', 'pink', 'black', 'snow', 'ghost white', 'white smoke', 'gainsboro', 'floral white',
          'old lace','linen', 'antique white', 'papaya whip', 'blanched almond', 'bisque', 'peach puff',
          'navajo white', 'lemon chiffon', 'mint cream', 'azure', 'alice blue', 'lavender',
          'lavender blush', 'misty rose', 'dark slate gray', 'dim gray', 'slate gray',
          'gray14', 'gray15', 'gray16', 'gray17', 'gray18', 'gray19','gray20', 'gray21', 'gray22', 'gray23', 'gray24','gray25', 'gray26', 'gray27', 'gray28','gray29', 'gray30', 'gray31', 'gray32', 'gray33', 'gray34', 'gray35', 'gray36', 'gray37','gray38', 'gray39', 'gray40',
          'light slate gray', 'gray', 'light grey', 'midnight blue', 'navy', 'cornflower blue', 'dark slate blue',
          'slate blue', 'medium slate blue', 'light slate blue', 'medium blue', 'royal blue', 'blue',
          'dodger blue', 'deep sky blue', 'sky blue', 'light sky blue', 'steel blue', 'light steel blue',
          'light blue', 'powder blue', 'pale turquoise', 'dark turquoise', 'medium turquoise', 'turquoise',
          'cyan', 'light cyan', 'cadet blue', 'medium aquamarine', 'aquamarine', 'dark green', 'dark olive green',
          'dark sea green', 'sea green', 'medium sea green', 'light sea green', 'pale green', 'spring green',
          'lawn green', 'medium spring green', 'green yellow', 'lime green', 'yellow green',
          'forest green', 'olive drab', 'dark khaki', 'khaki', 'pale goldenrod', 'light goldenrod yellow',
          'light yellow', 'yellow', 'gold', 'light goldenrod', 'goldenrod', 'dark goldenrod', 'rosy brown',
          'indian red', 'saddle brown', 'sandy brown','dark salmon', 'salmon', 'light salmon', 'orange', 'dark orange',
          'coral', 'light coral', 'tomato', 'orange red', 'red', 'hot pink', 'deep pink', 'pink', 'light pink',
          'pale violet red', 'maroon', 'medium violet red', 'violet red',
          'medium orchid', 'dark orchid', 'dark violet', 'blue violet', 'purple', 'medium purple']
def col(): 
    fg=random.choice(colors)
    by.config(fg=fg)
    by.after(300,col)
colors2 = ['dark slate gray', 'dim gray', 'slate gray',
          'light slate gray', 'gray']
def col2():
    bg=random.choice(colors2)
    by.config(bg=bg)
    by.after(600,col2)
Aro=Label(root,text="₯-----↬",font=50,bg="black",fg="red")
Aro.place(x=230,y=0)
################################___FOR FUN END__##############################################

#######################___HOUR LABEL___###########################
hlab=Label(root,text="12",font=("times new roman",50,"bold"),bd=15,bg="red",fg="white")
hlab.place(x=50,y=30)

h_lab=Label(root,text="Hour",font=("times new roman",20,"bold"),width=6,height=1,bg="#0875B7",fg="white")
h_lab.place(x=50,y=150)
######################___MINUTE LABEL___#################################
mlab=Label(root,text="12",font=("times new roman",50,"bold"),bd=15,bg="red",fg="white")
mlab.place(x=170,y=30)

m_lab=Label(root,text="Minute",font=("times new roman",18,"bold"),width=7,height=1,bg="#0875B7",fg="white")
m_lab.place(x=170,y=150)
######################___SECOND LABEL___#################################
slab=Label(root,text="12",font=("times new roman",50,"bold"),bd=15,bg="red",fg="white")
slab.place(x=290,y=30)

s_lab=Label(root,text="Second",font=("times new roman",18,"bold"),width=7,height=1,bg="#0875B7",fg="white")
s_lab.place(x=290,y=150)
###############################___INPUT TO OUTPUT___#########################################
def pri():    
    printt=disval.get()
    by.config(text=printt)
    by.after(200,pri)
#################################___RIGHT CORNER INPUT BOX___#################################3
disval=StringVar()
disval.set("SHUBHAM")
disply=Entry(root,bg='gray',bd=5,fg='white',textvariable=disval)
disply.place(x=310,y=0)
####################___NAME DISPLY ON BUTTON___#############################################
by=Button(root,text=" ",font=("times new roman",25,"bold"),width=17,height=1,bg="red",bd=5,fg="gold",
activebackground="#0875B7",command=pri)
by.place(x=50,y=200)
##################################___CALLING FUNCTION___#####################################
clock()
pri()
col2()
col()
root.mainloop()
##############################___Er.ShubhamBhagat@gmail.com___###################################
