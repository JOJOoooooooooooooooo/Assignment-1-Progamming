import tkinter as tk
from PIL import ImageTk, Image
import pygame
import threading
from tkinter import Canvas
import adventureclass



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
#my_img = ImageTk.PhotoImage(Image.open("TheHoppit2.jpg"))
#my_label = tk.Label(image=my_img)
#my_label.pack()

#Creating gif background
gif_frames = []

frame_delay = 0


def ready_gif():
    global frame_delay

    
    gif_file = Image.open('TheHoppit3.gif')

    for i in range(0, gif_file.n_frames):
        
        gif_file.seek(i)
        gif_frames.append(gif_file.copy())

    frame_delay = gif_file.info['duration']
    
    play_gif()

frame_count = -1

def play_gif():
    global frame_count, current_frame

    if frame_count >= len(gif_frames) -1:
        frame_count = -1
        play_gif()

    else: 
        frame_count += 1

        current_frame = ImageTk.PhotoImage(gif_frames[frame_count])
        gif_lb.config(image=current_frame)
        
        

        win.after(frame_delay, play_gif)

gif_lb = tk.Label(win)
gif_lb.pack(fill=tk.BOTH)

threading.Thread(target=ready_gif).start()




#creating radio button options

TextChose = tk.Text(win, height=1, width=20 )
TextChose.pack() 
TextChose.insert(tk.END, '  CHOOSE A CLASS')


def rb():
    if option.get() == 1:
        result = "Hobbit"
    elif option.get() == 2:
        result = "Human"
    elif option.get() == 3:
        result = "Elf"
    elif option.get() == 4:
        result = "Dwarf"
    label.config(text=f'You have selected:  {result}')

option = tk.IntVar()
rb1 = tk.Radiobutton(win, text = "Hobbit" , variable=option , value = 1,command=rb)
rb1.pack()
   
rb2 = tk.Radiobutton(win, text = "Human" , variable=option , value = 2,command=rb)
rb2.pack()

rb3 = tk.Radiobutton(win, text = "Elf        " , variable=option , value = 3,command=rb)
rb3.pack()

rb4 = tk.Radiobutton(win, text = "Dwarf  " , variable=option , value = 4,command=rb)
rb4.pack()

label = tk.Label(text="Your Class:")
label.pack()

#creating background music
pygame.mixer.init() # the order for inside the brackets would go ( 44100, -16, 2, 2048) Frequency, size, channels, buffer

pygame.mixer.music.load("The Company of Heroes.wav") 
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1) #-1 so that every time the song ends it will play it again


#creating SStart and Quit Buttons
button_start= tk.Button(win, text= "Start Game", command=win.quit)
button_start.pack()
button_quit = tk.Button(win, text= "Quit Game", command= win.quit)
button_quit.pack()




win.mainloop()

