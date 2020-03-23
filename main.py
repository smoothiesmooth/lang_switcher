import tkinter as tk
from db import rus, eng

firstclick = True
txt = "Write your text here..."
colour = "#252336"

class Main(tk.Frame):
	def __init__(self, root):
		super().__init__(root)
		self.init_main()

	def init_main(self):
		def on_text_click(event):
			global firstclick
			if firstclick:
				firstclick = False
				text.delete("0.0", "end")

		def Rus():
			s = text.get("0.0", "end")
			s = s.lower()
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
			s = s.lower()
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

		def info():
			Info()

		button1 = tk.Button(
		    text="Rus",
		    width=10,
		    height=2,
		    bg="#201e2e",
		    fg="white",
			command=Rus,
			borderwidth=0,
		)

		button2 = tk.Button(
		    text="Eng",
		    width=10,
		    height=2,
		    bg="#201e2e",
		    fg="white",
			command=Eng,
			borderwidth=0,
		)
		info_b = tk.Button(
			image=photo,
			width=12,
			height=12,
			borderwidth=0,
			command=info,
		)

		label_rus = tk.Label(text='', wraplength=290, bg=colour, fg="#ff9500", font="menlo  9")
		label_eng = tk.Label(text='', wraplength=290, bg=colour, fg="#ff9500", font="menlo  9")
		text = tk.Text(bg="#302e47", fg="#ff9500", font="menlo  11", width=80, height=3, borderwidth=0)
		text.insert("0.0", 'Write text here')
		text.bind('<FocusIn>', on_text_click)
		scroll = tk.Scrollbar(command=text.yview)

		scroll.pack(side="right", fill="y")
		label_rus.place(x=10,y=100)
		label_eng.place(x=400,y=100)
		text.pack()
		button1.place(x=220,y=50)
		button2.place(x=400,y=50)
		info_b.place(x=0,y=385)

class Info(tk.Toplevel):
	def __init__(self):
		super().__init__(root)
		self.init_info()
	def init_info(self):
		self.title('info')
		self.iconbitmap(r'img\\icon.ico')
		self.geometry(f'350x100+430+300')
		self.configure(background=colour)
		self.resizable(False, False)
		self.grab_set()
		self.focus_set()
		self.label = tk.Label(self, text='''Lantcher by Gregor Zhilich
Version 0.0.5 beta''', bg=colour, fg="#ff9500")
		self.label.pack()


if __name__ == "__main__":
	root = tk.Tk()
	photo = tk.PhotoImage(file=r'img\\info.gif')
	app = Main(root)
	app.pack()
	root.title("Lantcher")
	root.iconbitmap(r'img\\icon.ico')
	root.geometry("700x400+300+100")
	root.resizable(False, False)
	root.configure(background=colour)
	root.mainloop()
