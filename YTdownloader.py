import tkinter as tk
from pytube import YouTube
import time

window = tk.Tk()
window.title("YT Downloader") # 視窗名
window.minsize(width=500, height=200,) # 視窗大小
window.configure(bg="#D4BBBD") # 視窗顏色
window.resizable(width=False, height=False) # 鎖定視窗

bgcolor = "black"
fgcolor = "white"


# 設定當按鈕被按下
def mp4button_clicked():
    if entry.get() == "" :
        label.config(text="請輸入網址!!!!!",font=("Arial", 24, "bold"),fg="red")
    elif DL.get() == "" :
        label2.config(text="請輸入下載位址!!!!!", font=("Arial", 24, "bold"),fg="red")
    else:
        link = str(entry.get()) # 取得網址
        yt = YouTube(link) # Hi YT
        opp = str(DL.get())

        label.config(text=yt.title, font=("Arial", 14, "bold"),fg="black") # 更新文字格
        label2.config(text="下載位址", font=("Arial", 14, "bold"), padx=5, pady=5, bg="gray", fg="black")  # 更新文字格 
        MP4button.config(text="MP4 Downloading...")   # 更新按鈕文字

        ytmp4 = yt.streams.get_highest_resolution() #影像檔直接載最頂的    
        ytmp4.download(output_path=opp) # 開始下載         

        MP4button.config(text="MP4 Download Complete")   # 下載中，更新按鈕文字
        time.sleep(0.5)
        MP4button.config(text="MP4 Download")   # 下載完成，更新按鈕文字
    

def mp3button_clicked():
    if entry.get() == "" :
        label.config(text="請輸入網址!!!!!",font=("Arial", 24, "bold"),fg="red")
    elif DL.get() == "" :
        label2.config(text="請輸入下載位址!!!!!", font=("Arial", 24, "bold"),fg="red")
    else:
        link = str(entry.get()) # 取得網址
        yt = YouTube(link) # Hi YT
        opp = str(DL.get())

        label.config(text=yt.title, font=("Arial", 14, "bold"),fg="black") # 更新文字格
        label2.config(text="下載位址", font=("Arial", 14, "bold"), padx=5, pady=5, bg="gray", fg="black")  # 更新文字格 
        MP3button.config(text="MP3 Downloading...")   # 更新按鈕文字

        ytmp3 = yt.streams.filter().get_audio_only() #取得音樂檔
        ytmp3.download(output_path=opp,filename=yt.title+".mp3") #下載檔案同時轉檔  
   
        MP3button.config(text="MP3 Download Complete")   # 下載中，更新按鈕文字
        time.sleep(0.5)
        MP3button.config(text="MP3 Download")   # 下載完成，更新按鈕文字

   

#刪除網址
def reset_link():
    entry.delete(0,10000)


        



# 設定文字格
label = tk.Label(text="請輸入網址", font=("Arial", 14, "bold"), padx=5, pady=5, bg="gray", fg="black")  
label.pack() #創建文字格
    
#設定輸入區域
entry = tk.Entry(width=30, font=("Arial", 14, "bold"), bg=bgcolor, fg=fgcolor)
entry.insert(0,string="")
entry.pack()


#設定reset按鈕
reset = tk.Button(text="Reset", font=("Arial", 8, "bold"), padx=5, pady=5, bg="pink", fg="black", command=reset_link)
reset.pack()

#設定下載按鈕
MP4button = tk.Button(text="MP4 Download", font=("Arial", 14, "bold"), padx=20, pady=5, bg="orange", fg="black", command=mp4button_clicked)
MP4button.pack()

MP3button = tk.Button(text="MP3 Download", font=("Arial", 14, "bold"), padx=20, pady=5, bg="navy", fg=fgcolor, command=mp3button_clicked)
MP3button.pack()


#設定下載位址說明文字
label2 = tk.Label(text="下載位址", font=("Arial", 14, "bold"), padx=5, pady=5, bg="gray", fg="black")  # 設定文字格
label2.pack() 

#設定下載位址
DL = tk.Entry(width=30, font=("Arial", 14, "bold"), bg=bgcolor, fg=fgcolor)
DL.insert(0,string="C:/Users/user/Downloads") #預設路徑
DL.pack()

#循環主程式
window.mainloop()





