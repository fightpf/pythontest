from tkinter import *
from tkinter import filedialog as fd
import pytube


def do_asksaveasfile():
    x.set('下載中')
    files = [('video Document', '*.mp4')]
    video_link=url1.get()
    download_title=pytube.YouTube(video_link).title
    file = fd.asksaveasfile(mode='a',initialfile=download_title ,filetypes = files, defaultextension = files)
    location = file.name[0:len(file.name)-len(download_title)-4]
    pytube.YouTube(video_link).streams.first().download(location)
    x.set('下載完成') 

#print(f.composition(True)[0])
#分子式f.empirical
window=Tk()
window.title("YouYueDownLoad")
window.geometry("800x450")
window.configure(background="#FFFFFF")
text1=Label(window,
                   text="請輸入網址",
                   font="Helvetica 20",
                   width=30,
                   bg="#FFFFFF").pack(pady=10)
url1=Entry(window,width=50)
url1.insert(1,'https://www.youtube.com/watch?v=yN6Ic2EJ1d0')
url1.pack(pady=20)
x=StringVar()
label2=Label(window,
            textvariable=x,
            font="Helvetica 20 bold",
            bg="#FFFFFF").pack(pady=20)
save_file_botton=Button(window,
                text="下載位置",
                width=10,
                command=do_asksaveasfile,
                font="Helvetica 20 ",
                fg="white",
                bg="#000000"
                ).place(relx=0.5,rely=0.95,anchor="s")
                
              
window.mainloop()

