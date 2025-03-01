import tkinter as tk
from tkinter import ttk
import webbrowser
from math import floor

COLOR_BACKGROUND = "#151818"
COLOR_FOREGROUND = "#e1e5eb"
COLOR_BUTTON_BG = "#339999"
COLOR_BUTTON_HOVER = "#2b7a7a"
COLOR_BUTTON_FG = "#fff"
COLOR_PROGRESS_BG = "#00FF00"
COLOR_PROGRESS_TROUGH = "#27292b"
COLOR_ERROR_BG = "#151818"
COLOR_ERROR_TEXT = "#e1e5eb"
COLOR_LINK = "#1d72f2"

window = tk.Tk()
window.title("Взлом КАЗИНО")
window.geometry("400x250")
window.minsize(300, 200)
window.configure(bg=COLOR_BACKGROUND)

try:
    window.iconbitmap("icon.ico")
except tk.TclError:
    pass

style = ttk.Style()
style.theme_use('clam')
style.configure("TLabel", background=COLOR_BACKGROUND, foreground=COLOR_FOREGROUND, font=("Avenir", 12))
style.configure("TButton", background=COLOR_BUTTON_BG, foreground=COLOR_BUTTON_FG, font=("Avenir", 12), padding=10)
style.configure("black.Horizontal.TProgressbar", background=COLOR_PROGRESS_BG, troughcolor=COLOR_PROGRESS_TROUGH)
style.map("TButton", background=[("active", COLOR_BUTTON_HOVER)])

l1 = ttk.Label(window, text="Казино взломано на 14%", font=("Avenir", 14))
l1.grid(row=0, column=0, columnspan=2, pady=10, sticky="ew")

l2 = ttk.Label(window, text="Выкачано 12 050 руб. из 70 055 020 руб.", font=("Avenir", 14))
l2.grid(row=1, column=0, columnspan=2, pady=5, sticky="ew")

label3 = ttk.Label(window, text="Продолжить?", font=("Avenir", 14))
label3.grid(row=2, column=0, columnspan=2, pady=10, sticky="ew")

bar = ttk.Progressbar(window, length=350, style='black.Horizontal.TProgressbar')
bar['value'] = 28
bar.grid(row=3, column=0, columnspan=2, pady=10, sticky="ew")

def set_icon(window_obj):
    try:
        window_obj.iconbitmap("icon.ico")
    except tk.TclError:
        pass

def show_check_window():
    check_window = tk.Toplevel(window)
    check_window.title("Ваш чек")
    check_window.geometry("400x150")
    check_window.configure(bg=COLOR_BACKGROUND)
    set_icon(check_window)
    
    message = ttk.Label(check_window, text="Ваш чек в криптоботе, чтобы забрать деньги:", font=("Avenir", 12))
    message.pack(pady=10)
    link = tk.Label(check_window, text="http://t.me/CryptoBot?start=wallet", fg=COLOR_LINK, bg=COLOR_BACKGROUND, font=("Avenir", 12, "underline"), cursor="hand2")
    link.pack(pady=5)
    link.bind("<Button-1>", lambda e: window.clipboard_clear() or window.clipboard_append("http://t.me/CryptoBot?start=wallet"))
    close_button = ttk.Button(check_window, text="Закрыть", command=check_window.destroy)
    close_button.pack(pady=10)

def on_click():
    for i in range(28, 101):
        bar['value'] = i
        l1['text'] = f"Казино взломано на {i}%"
        l2['text'] = f"Выкачано {floor(i * 70552020 / 100)} руб. из 70 055 020 руб."
        window.update()
        window.after(50)
    l1['text'] = "Казино взломано на 159 УК РФ"
    webbrowser.open("https://www.youtube.com/watch?v=vTUP8eimDuY")
    show_check_window()

def on_no_click():
    new_window = tk.Toplevel(window)
    new_window.title("Ошибка")
    new_window.geometry("300x150")
    new_window.configure(bg=COLOR_ERROR_BG)
    set_icon(new_window)
    
    message = ttk.Label(new_window, text="Ты че, дурак чтоли?", foreground=COLOR_ERROR_TEXT, background=COLOR_ERROR_BG, font=("Avenir", 14))
    message.pack(pady=20)
    close_button = ttk.Button(new_window, text="Закрыть", command=new_window.destroy)
    close_button.pack(pady=10)

button_frame = ttk.Frame(window)
button_frame.grid(row=4, column=0, columnspan=2, pady=10, sticky="ew")
button_frame.grid_columnconfigure(0, weight=1, uniform="buttons")
button_frame.grid_columnconfigure(1, weight=1, uniform="buttons")

yes_button = ttk.Button(button_frame, text="Да", command=on_click)
yes_button.grid(row=0, column=0, padx=2, sticky="ew")

no_button = ttk.Button(button_frame, text="Нет", command=on_no_click)
no_button.grid(row=0, column=1, padx=2, sticky="ew")

window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_rowconfigure(0, weight=1)
window.grid_rowconfigure(1, weight=1)
window.grid_rowconfigure(2, weight=1)
window.grid_rowconfigure(3, weight=1)
window.grid_rowconfigure(4, weight=1)

window.mainloop()