import sv_ttk
import easygui as eg
import tkinter as tk
from tkinter import *
from tkinter import messagebox, filedialog, Button, ttk

from main import remove_almost

root = tk.Tk()
root.title("滤镜去除")
root.geometry('200x240') # window size
root.resizable(0, 0)
sv_ttk.use_dark_theme()


file_path = ""
def select_file():
    global file_path
    file_path = filedialog.askopenfilename()


file_select = ttk.Button(root, text="选择关卡文件", command=select_file)

file_select.place(x=20, y=20, anchor='w')

filt = tk.BooleanVar()
remove_filter = ttk.Checkbutton(root, text="去除滤镜",variable=filt)
remove_filter.place(x=20, y=60, anchor='w')

flash = tk.BooleanVar()
remove_flash = ttk.Checkbutton(root, text="去除闪屏", variable=flash)
remove_flash.place(x=20, y=100, anchor='w')

HallOfMirrors = tk.BooleanVar()
remove_HallOfMirrors = ttk.Checkbutton(root, text="去除HallOfMirrors", variable=HallOfMirrors)
remove_HallOfMirrors.place(x=20, y=140, anchor='w')

bloom = tk.BooleanVar()
remove_bloom = ttk.Checkbutton(root, text="去除bloom", variable=bloom)
remove_bloom.place(x=20, y=180, anchor='w')


def start():
    if file_path == "":
        messagebox.showerror("错误", "请选择关卡文件")
        return
    if not filt.get() and not flash.get() and not HallOfMirrors.get() and not bloom.get():
        messagebox.showerror("错误", "请选择至少一个选项")
        return
    remove_almost(file_path, filt.get(), flash.get(), HallOfMirrors.get(), bloom.get())
    messagebox.showinfo("成功", "处理完成")


process = ttk.Button(root, text="处理", command=start)
process.place(x=20, y=220, anchor='w')


root.mainloop()