from db import rus, eng
import tkinter as tk

firstclick = True
txt = "Write your text here..."

def on_text_click(event):
	global firstclick
	if firstclick: # if this is the first time they clicked it
		firstclick = False
		text.delete("0.0", "end") # delete all the text in the text

def Rus():
	s = text.get("0.0", "end")
	out = ''
	input = []
	output = []
	for i in s:
		input.append(i)
	for c in input:
		output.append(rus[c])
	for x in output:
		out+=x
		label_rus.config(text=f'{out}')

def Eng():
	s = text.get("0.0", "end")
	out = ''
	input = []
	output = []
	for i in s:
		input.append(i)
	for c in input:
		output.append(eng[c])
	for x in output:
		out+=x
	label_eng.config(text=f'{out}')

win = tk.Tk()
win.title("Lang Switcher")
win.geometry("700x400")
win.iconbitmap(r'img\\icon.ico')
win.resizable(width=False, height=False)
win.configure(background="white")

button1 = tk.Button(
    text="Rus",
    width=10,
    height=2,
    bg="lightgrey",
    fg="white",
	command=Rus,
	borderwidth=0,
)

button2 = tk.Button(
    text="Eng",
    width=10,
    height=2,
    bg="lightgrey",
    fg="white",
	command=Eng,
	borderwidth=0,
)

label_rus = tk.Label(text='', wraplength=290, bg="white", fg="black")
label_eng = tk.Label(text='', wraplength=290, bg="white", fg="black")
text = tk.Text(fg="black", font="courier", width=80, height=3, borderwidth=0.5)
text.insert("0.0", 'Write text here')
text.bind('<FocusIn>', on_text_click)
inf = tk.Label(text="Beta 0.0.3, developed by Gregor Zhilich", bg="white", fg="black")
scroll = tk.Scrollbar(command=text.yview)

scroll.pack(side="right", fill="y")
label_rus.place(x=10,y=100)
label_eng.place(x=400,y=100)
text.pack()
button1.place(x=220,y=50)
button2.place(x=400,y=50)
inf.place(x=0,y=380)

win.mainloop()
