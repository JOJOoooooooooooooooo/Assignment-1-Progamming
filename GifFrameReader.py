import tkinter as tk
from PIL import ImageTk, Image
import pygame 
import threading

win = tk.Tk()
win.geometry = ("600x393")

gif_frames = []

frame_delay = 0


def ready_gif():
    global frame_delay

    print('Started')
    gif_file = Image.open('TheHoppit3.gif')

    for i in range(0, gif_file.n_frames):
        
        gif_file.seek(i)
        gif_frames.append(gif_file.copy())

    frame_delay = gif_file.info['duration']
    print('Completed')
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

win.mainloop()