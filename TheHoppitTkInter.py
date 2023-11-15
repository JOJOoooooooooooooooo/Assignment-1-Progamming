import tkinter as tk
from PIL import ImageTk, Image

#creating the window
win = tk.Tk()
win.geometry = ("400x400")
win.title('THE HOPPIT')


#Text for the window
TextTitle = tk.Text(win, height=5, width=30 )
TextTitle.grid(row=0 , column=0)
TextTitle.insert(tk.END, 'Welcome to "THE HOPPIT" ')

#retrieving text
tt = TextTitle.get('1.0' , 'end')

print(tt)

#creating radio button options
option = tk.IntVar()
rb1 = tk.Radiobutton(win, text = "Hobbit" , variable=option , value = 1)
rb1.grid(row=1 , column=0)

rb2 = tk.Radiobutton(win, text = "Human" , variable=option , value = 2)
rb2.grid(row=2 , column=0)

rb3 = tk.Radiobutton(win, text = "Elf" , variable=option , value = 3)
rb3.grid(row=3 , column=0)

rb4 = tk.Radiobutton(win, text = "Dwarf" , variable=option , value = 4)
rb4.grid(row=4 , column=0)








button_quit = tk.Button(win, text= "Quit Game", command= win.quit)
button_quit.grid(row=5 , column=0)




win.mainloop()

