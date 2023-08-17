import tkinter as tk
import time

def update_time():
    current_time = time.ctime()
    time_label.config(text=current_time)
    root.after(1000, update_time)  # Uruchamia update_time() co 1000 ms (1 sekunda)

root = tk.Tk()
root.title("Digital clock")

time_label = tk.Label(root, text="", font=("Helvetica", 24))
time_label.pack(pady=20)

update_time()  # Uruchamia funkcję aktualizującą czas

root.mainloop()




