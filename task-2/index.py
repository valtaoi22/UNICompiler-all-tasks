from tkinter import *
from tkinter import filedialog,messagebox
from pytube import YouTube,Playlist
import os

#functionality Part

def download():
    got_path=filedialog.askdirectory()
    link_url=text.get()

    if check.get()==1:

        yt=YouTube(link_url)
        yt.streams.get_highest_resolution().download(got_path)
        messagebox.showinfo('Success','Downloading is succesfull')
        os.startfile(got_path)

    if check.get()==2:
        yt_playlist=Playlist(link_url)
        for videos in yt_playlist.videos:
            videos.streams.get_highest_resolution().download(got_path)

        messagebox.showinfo('Success','Complete Playlist is downloaded succesfully')
        os.startfile(got_path)
root = Tk()

root.title('Youtube Video Downloader')
root.config(bg='red4')

outerframe = Frame(root, bd=5)
outerframe.grid(row=0, column=0, pady=30, padx=30)

logoImage = PhotoImage(file='logo.png')
logoLabel = Label(outerframe, image=logoImage)
logoLabel.grid(row=0, column=0, pady=20)

innerframe = LabelFrame(outerframe, text='DOWNLOAD', font=('arial black', 14, 'bold'))
innerframe.grid(row=1, column=0, pady=30)
radioImage = PhotoImage(file='video.png')
check=IntVar()
videoradioButton = Radiobutton(innerframe, image=radioImage, text='  Single Video', compound=LEFT,variable=check,value=1,
                               font=('arial', 12, 'bold')
                               , relief='solid')
videoradioButton.grid(row=0, column=0, padx=20, pady=20)

playlistImage = PhotoImage(file='playlist.png')
playlistradioButton = Radiobutton(innerframe, image=playlistImage, text='  Playlist', compound=LEFT,variable=check,value=2,
                                  font=('arial', 12, 'bold')
                                  , relief='solid')
playlistradioButton.grid(row=0, column=1, padx=20, pady=20)

text = StringVar()
url_entryField = Entry(outerframe, width=60, font=('arial', 14, 'bold'), justify=CENTER, textvariable=text, fg='gray')
url_entryField.grid(row=2, column=0, padx=10, pady=30)
text.set('Enter URL')


def click(event):
    url_entryField.delete(0, END)
    url_entryField.config(fg='black')


url_entryField.bind('<Button-1>', click)

downloadImage = PhotoImage(file='download.png')
downloadButton = Button(outerframe, image=downloadImage, bg='red4',command=download)
downloadButton.grid(row=3, column=0, pady=30)

root.mainloop()