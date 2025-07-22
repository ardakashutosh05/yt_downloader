from tkinter import *
from tkinter import filedialog
from moviepy.editor import VideoFileClip
from pytube import YouTube
import shutil
import os

# ----- Functions -----
def select_path():
    # Allows user to select a folder
    path = filedialog.askdirectory()
    path_label.config(text=path)

def download_file():
    try:
        # Get the YouTube link and path
        get_link = link_field.get()
        user_path = path_label.cget("text")

        if not get_link:
            screen.title('Please enter a valid YouTube link!')
            return

        if not user_path or user_path == "Select Path For Download":
            screen.title("Please select a path first!")
            return

        # Update window title
        screen.title('Downloading...')

        # Download video
        mp4_video = YouTube(get_link).streams.get_highest_resolution().download()
        vid_clip = VideoFileClip(mp4_video)
        vid_clip.close()

        # Move the file to selected path
        shutil.move(mp4_video, user_path)
        screen.title('Download Complete! Download Another File...')

    except Exception as e:
        screen.title('Error: Download Failed')
        print("Error:", e)

# ----- GUI Setup -----
screen = Tk()
screen.title('YouTube Downloader')
canvas = Canvas(screen, width=500, height=500)
canvas.pack()

# Logo image
try:
    logo_img = PhotoImage(file='yt.png')
    logo_img = logo_img.subsample(2, 2)  # Resize
    canvas.create_image(250, 80, image=logo_img)
except Exception as e:
    print("Image Load Failed:", e)

# Link input
link_label = Label(screen, text="Enter Download Link: ", font=('Arial', 15))
link_field = Entry(screen, width=40, font=('Arial', 15))

# Path selection
path_label = Label(screen, text="Select Path For Download", font=('Arial', 15))
select_btn = Button(screen, text="Select Path", bg='red', padx=22, pady=5,
                    font=('Arial', 15), fg='white', command=select_path)

# Download button
download_btn = Button(screen, text="Download File", bg='green', padx=22, pady=5,
                      font=('Arial', 15), fg='white', command=download_file)

# Add widgets to canvas
canvas.create_window(250, 170, window=link_label)
canvas.create_window(250, 220, window=link_field)
canvas.create_window(250, 280, window=path_label)
canvas.create_window(250, 330, window=select_btn)
canvas.create_window(250, 390, window=download_btn)

# Start the app
screen.mainloop()
