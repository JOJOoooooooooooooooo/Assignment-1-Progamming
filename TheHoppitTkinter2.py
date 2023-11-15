import tkinter as tk
from PIL import ImageTk, Image
import pygame 


#creating the window
win = tk.Tk()
win.geometry = ("600x393")
win.title('The Hoppit')


#Text for the window
TextTitle = tk.Text(win, height=1, width=30 )
TextTitle.pack() 
TextTitle.insert(tk.END, '     WELCOME TO THE HOPPIT ')

#retrieving text
tt = TextTitle.get('1.0' , 'end')

print(tt)

#creating image
my_img = ImageTk.PhotoImage(Image.open("TheHoppit2.jpg"))
my_label = tk.Label(image=my_img)
my_label.pack()





#creating radio button options

TextChose = tk.Text(win, height=1, width=20 )
TextChose.pack() 
TextChose.insert(tk.END, '  CHOSE A CLASS')


option = tk.IntVar()
rb1 = tk.Radiobutton(win, text = "Hobbit" , variable=option , value = 1)
rb1.pack()

rb2 = tk.Radiobutton(win, text = "Human" , variable=option , value = 2)
rb2.pack()

rb3 = tk.Radiobutton(win, text = "Elf        " , variable=option , value = 3)
rb3.pack()

rb4 = tk.Radiobutton(win, text = "Dwarf  " , variable=option , value = 4)
rb4.pack()





#creating background music
pygame.mixer.init() # the order for inside the brackets would go ( 44100, -16, 2, 2048) Frequency, size, channels, buffer

pygame.mixer.music.load("The Company of Heroes.wav") 
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1) #-1 so that every time the song ends it will play it again


#creating SStart and Quit Buttons
button_start= tk.Button(win, text= "Start Game", command=win.quit)
button_start.pack(pady= 12)
button_quit = tk.Button(win, text= "Quit Game", command= win.quit)
button_quit.pack()




win.mainloop()

