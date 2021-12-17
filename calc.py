from tkinter import *
a="" #string variable to store the expression
# button functionality
def click(num):
    global a
    a=a+str(num)
    e.set(a)

def presseq():
    try:
        global a
        total=str(eval(a))
        e.set(total)
        a=""

    except:
        e.set("Error")
        expression=""
def click_clear():
    global a
    a=""
    e.set("")

if __name__ == "__main__":
    root=Tk()
    root.title("Calculator")
    root.geometry("360x360")

    text = Label(root, text="Calculator By Adi",fg="Blue")
    text.place(x=140,y=310)

    e=StringVar()
    e1 = Entry(root,textvariable=e)
    e1.place(width=360,height=150)
    #operations frame
    frame=Frame(root)
    frame.place(x=315,y=150)
    # numbers frame
    frame1=Frame(root)
    frame1.place(x=0,y=150)
    #creating and placing the buttons inside frame
    b1 =Button(frame,height=2,width=4,text="+",command=lambda:click("+"))
    b1.grid(row=10,column=180,padx=5,pady=0)
    b2 = Button(frame,height=2,width=4,text="-",command=lambda:click("-"))
    b2.grid(row=11,column=180,padx=5,pady=0)
    b3 = Button(frame,height=2,width=4,text="*",command=lambda:click("*"))
    b3.grid(row=12,column=180,padx=5,pady=0)
    b4 = Button(frame,height=2,width=4,text="/",command=lambda:click("/"))
    b4.grid(row=13,column=180,padx=5,pady=0)
    b5 = Button(frame,height=2,width=4,text="=",command=lambda:presseq())
    b5.grid(row=14,column=180,padx=5,pady=0)

    b12 = Button(frame1,height=2,width=10,text="clear",command=lambda:click_clear())
    b12.grid(row=12,column=140,padx=0,pady=0)
    #placing numbers
    b6 = Button(frame1,height=2,width=10,text="1",command=lambda:click("1"))
    b6.grid(row=10,column=140,padx=0,pady=0)
    b7 = Button(frame1,height=2,width=10,text="2",command=lambda:click("2"))
    b7.grid(row=10,column=141,padx=0,pady=0)
    b8 =Button(frame1,height=2,width=10,text="3",command=lambda:click("3"))
    b8.grid(row=10,column=142,padx=0,pady=0)
    b8 = Button(frame1,height=2,width=10,text="4",command=lambda:click("4"))
    b8.grid(row=10,column=143,padx=0,pady=0)

    b6 = Button(frame1,height=2,width=10,text="5",command=lambda:click("5"))
    b6.grid(row=11,column=140,padx=0,pady=0)
    b7 = Button(frame1,height=2,width=10,text="6",command=lambda:click("6"))
    b7.grid(row=11,column=141,padx=0,pady=0)
    b8 = Button(frame1,height=2,width=10,text="7",command=lambda:click("7"))
    b8.grid(row=11,column=142,padx=0,pady=0)
    b9 = Button(frame1,height=2,width=10,text="8",command=lambda:click("8"))
    b9.grid(row=11,column=143,padx=0,pady=0)

    b10 = Button(frame1,height=2,width=10,text="9",command=lambda:click("9"))
    b10.grid(row=12,column=141,padx=0,pady=0)
    b11 =Button(frame1,height=2,width=10,text="0",command=lambda:click("0"))
    b11.grid(row=12,column=142,padx=0,pady=0)
    b13 =Button(frame1,height=2,width=10,text=".",command=lambda:click("."))
    b13.grid(row=12,column=143,padx=0,pady=0)
    
    root.mainloop()