from db import rus, eng
import tkinter as tk

firstclick = True
def on_entry_click(event):
	global firstclick
	if firstclick: # if this is the first time they clicked it
		firstclick = False
		entry.delete(0, "end") # delete all the text in the entry

def Rus():
	s = entry.get()
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
	s = entry.get()
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
win.iconbitmap(r'icon.ico')
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
label_rus.place(x=10,y=80)
label_eng = tk.Label(text='', wraplength=290, bg="white", fg="black")
label_eng.place(x=400,y=80)
entry = tk.Entry(fg="black", width=50, borderwidth=1)
entry.insert(0, 'Write text here')
entry.bind('<FocusIn>', on_entry_click)
entry.pack()
inf = tk.Label(text="Beta 0.0.2, developed by Gregor Zhilich", bg="white", fg="black")
button1.place(x=220,y=30)
button2.place(x=400,y=30)
inf.place(x=0,y=380)

win.mainloop()
