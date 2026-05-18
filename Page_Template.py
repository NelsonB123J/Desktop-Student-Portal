import tkinter as tk

class Dashboard(tk.Frame):
    def __init__(self, root, create_page=None):
        super().__init__(root, bg="white")





if __name__ == "__main__":
    root = tk.Tk()
    root.title("Profile Test")
    root.geometry("1090x1024")
    Dashboard(root).pack(fill="both", expand=True)
    root.mainloop()