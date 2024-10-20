#from tkinter import *
import subprocess

def download_video(url, output_format='mp4', output_path='C:/Users/hrish/OneDrive/Desktop/%(title)s.mp4'):
    command = ['yt-dlp', '-f', output_format, '-o', output_path, url]
    try:
        subprocess.run(command, check=True)
        print(f"Video downloaded successfully and saved to {output_path}")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

# Example usage
video_url = input("enter the url:")
download_video(video_url)

# yt-dlp -f 'bestvideo[ext=mp4][height<=2160]+bestaudio[ext=m4a]/bestvideo[ext=mp4][height<=1440]+bestaudio[ext=m4a]/bestvideo[ext=mp4][height<=1080]+bestaudio[ext=m4a]'https://www.youtube.com/watch?v=KWh0-WmsMy kvideo_URL

'''
from tkinter import *
import pytube


# Functions
def download():
    video_url = url.get()
    try:
        youtube = pytube.YouTube(video_url)
        video = youtube.streams.first()
        video.download("C:/Users/iwanh/Desktop/MP4_MP3s")
        notif.config(fg="green", text="Download complete")
    except Exception as e:
        print(e)
        notif.config(fg="red", text="Video could not be downloaded")


# Main Screen
master = Tk()
master.title("Youtube Video Downloader")

# Labels
Label(master, text="Youtube Video Converter", fg="red", font=("Calibri", 15)).grid(sticky=N, padx=100, row=0)
Label(master, text="Please enter the link to your video below : ", font=("Calibri", 15)).grid(sticky=N, row=1, pady=15)
notif = Label(master, font=("Calibri", 12))
notif.grid(sticky=N, pady=1, row=4)
# Vars
url = StringVar()
# Entry
Entry(master, width=50, textvariable=url).grid(sticky=N, row=2)
# Button
Button(master, width=20, text="Download", font=("Calibri", 12), command=enter).grid(sticky=N, row=3, pady=15)
master.mainloop()
'''


