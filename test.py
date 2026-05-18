import tkinter as tk
from tkinter import simpledialog

root = tk.Tk()
root.title("Test Window")
root.geometry("1000x800")

new_password = simpledialog.askstring("Input", "Enter your new password here:")

print("New Password:", new_password)
root.mainloop()