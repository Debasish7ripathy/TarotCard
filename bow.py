import tkinter as tk
import tkinter.ttk as ttk
import webbrowser

def open_url():
    url = entry.get()
    webbrowser.open_new(url)

root = tk.Tk()
root.title("Minimal Web Browser")

frame = ttk.Frame(root)
frame.pack(padx=10, pady=10)

label = ttk.Label(frame, text="Enter URL:")
label.grid(row=0, column=0)

entry = ttk.Entry(frame, width=40)
entry.grid(row=0, column=1)

button = ttk.Button(frame, text="Go", command=open_url)
button.grid(row=0, column=2, padx=5)

root.mainloop()
