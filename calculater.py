from tkinter import *
 
root = Tk()
root.geometry("444x650")
root.title("Calculator by Bhavesh")
root.wm_iconbitmap(r"C:\Users\Lenovo\Downloads\hnet.com-image.ico") 

value=StringVar()
value.set("")
screen = Entry(root,textvariable=value,font="lucida 30 bold")
screen.pack(fill=X,ipadx=8,pady=10,padx=1)


def click(event):
	text=event.widget.cget("text")
	print(text)
	if text == "=":
		if value.get().isdigit():
			ans=int(value.get())
		else:
			try:


				ans=eval(screen.get())
			except Exception as e:
				print(e)
				ans="ERROR"


			value.set(ans)
			screen.update()


	elif text=="C":
		value.set(" ")
		screen.update()
	else:
		value.set(value.get()+text)
		screen.update() 


f= Frame(root,bg="grey")
b= Button(f,text="9",padx=28,pady=10,font="lucida 20 bold")
b.pack(side=LEFT,padx=15,pady=5)
b.bind("<Button-1>", click)

b= Button(f,text="8",padx=28,pady=10,font="lucida 20 bold")
b.pack(side=LEFT,padx=15,pady=5)
b.bind("<Button-1>", click)

b= Button(f,text="7",padx=28,pady=10,font="lucida 20 bold")
b.pack(side=LEFT,padx=15,pady=5)
b.bind("<Button-1>", click)
f.pack()

f= Frame(root,bg="grey")
b= Button(f,text="6",padx=28,pady=10,font="lucida 20 bold")
b.pack(side=LEFT,padx=15,pady=5)
b.bind("<Button-1>", click)

b= Button(f,text="5",padx=28,pady=10,font="lucida 20 bold")
b.pack(side=LEFT,padx=15,pady=5)
b.bind("<Button-1>", click)

b= Button(f,text="4",padx=28,pady=10,font="lucida 20 bold")
b.pack(side=LEFT,padx=15,pady=5)
b.bind("<Button-1>", click)
f.pack()

f= Frame(root,bg="grey")
b= Button(f,text="3",padx=28,pady=10,font="lucida 20 bold")
b.pack(side=LEFT,padx=15,pady=5)
b.bind("<Button-1>", click)

b= Button(f,text="2",padx=28,pady=10,font="lucida 20 bold")
b.pack(side=LEFT,padx=15,pady=5)
b.bind("<Button-1>", click)

b= Button(f,text="1",padx=28,pady=10,font="lucida 20 bold")
b.pack(side=LEFT,padx=15,pady=5)
b.bind("<Button-1>", click)
f.pack()

f= Frame(root,bg="grey")
b= Button(f,text="0",padx=29,pady=10,font="lucida 20 bold")
b.pack(side=LEFT,padx=15,pady=15)
b.bind("<Button-1>", click)

b= Button(f,text="+",padx=29,pady=10,font="lucida 20 bold")
b.pack(side=LEFT,padx=15,pady=5)
b.bind("<Button-1>", click)

b= Button(f,text="-",padx=29,pady=10,font="lucida 21 bold")
b.pack(side=LEFT,padx=15,pady=5)
b.bind("<Button-1>", click)
f.pack()

f= Frame(root,bg="grey")
b= Button(f,text="*",padx=29,pady=10,font="lucida 20 bold")
b.pack(side=LEFT,padx=15,pady=5)
b.bind("<Button-1>", click)

b= Button(f,text="/",padx=28,pady=10,font="lucida 20 bold")
b.pack(side=LEFT,padx=15,pady=5)
b.bind("<Button-1>", click)

b= Button(f,text="%",padx=28,pady=10,font="lucida 20 bold")
b.pack(side=LEFT,padx=15,pady=5)
b.bind("<Button-1>", click)
f.pack()


f= Frame(root,bg="grey")
b= Button(f,text="=",padx=29 ,pady=10,font="lucida 20 bold")
b.pack(side=LEFT,padx=15,pady=5)
b.bind("<Button-1>", click)

b= Button(f,text=".",padx=28,pady=10,font="lucida 20 bold")
b.pack(side=LEFT,padx=15,pady=5)
b.bind("<Button-1>", click)

b= Button(f,text="C",padx=28,pady=10,font="lucida 20 bold")
b.pack(side=LEFT,padx=15,pady=5)
b.bind("<Button-1>", click)
f.pack()

root.mainloop()
