from db import rus, eng
import tkinter as tk

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
	label = tk.Label(text=f'{out}')
	label.pack(pady=60)

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
	label = tk.Label(text=f'{out}')
	label.pack(pady=60)

win = tk.Tk()
win.title("Lang Switcher")
win.geometry("700x400")
win.iconbitmap(r'icon.ico')
button2 = tk.Button(
    text="Rus",
    width=10,
    height=2,
    bg="grey",
    fg="white",
	command=Rus,
)
button1 = tk.Button(
    text="Eng",
    width=10,
    height=2,
    bg="grey",
    fg="white",
	command=Eng,
)
entry = tk.Entry(fg="black", width=50)
entry.pack()
inf = tk.Label(text="Beta 0.0.1, developed by Gregor Zhilich")
button1.place(x=400,y=30)
button2.place(x=220,y=30)
inf.place(x=0,y=380)

win.mainloop()
