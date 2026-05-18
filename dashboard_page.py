import tkinter as tk
from Academic_Status import Academic_Status

class Dashboard(tk.Frame):
    def __init__(self, root, create_page=None, Logout=None, student_info=None, Result=None):
        super().__init__(root, bg="white")
        self.latest_gpa = Academic_Status(root,None,None, Result).latest_gpa
        self.cgpa = Academic_Status(root,None,None, Result).cgpa
        self.create_page = create_page
        self.Logout = Logout
        self.name = student_info[0][1]
        self.program = student_info[2][1]
        self.year = student_info[5][1]
        self.degree = student_info[6][1]


        tk.Label(self, text=f"Welcome {self.name}! 👋", 
                 font=("Segoe UI", 24, "bold"), 
                 bg="white", fg="#0C4A99").pack(padx=40,pady=(50, 20), anchor="nw")
        tk.Frame(self, height=1, bg="#A5A2A2").pack(padx=40,fill="x")

        self.widgets_frame = tk.Frame(self, bg="#FFFFFF")
        self.widgets_frame.pack(padx=40, pady=20, fill="both", expand=True)
        
        self.create_widget("🎓", "Program", f"{self.degree} {self.program} Year {self.year}", 0, 0)
        self.create_widget("⭐", "Latest GPA", self.latest_gpa, 0, 1)
        self.create_widget("⭐", "Cumulative GPA",self.cgpa, 0, 2)

        self.create_widget("👤", "Profile", None, 1, 0)
        self.create_widget("📖", "Courses", None, 1, 1)
        self.create_widget("📅", "Schedule", None, 1, 2)

        self.create_widget("✓", "Attendance", None, 2, 0)
        self.create_widget("📈", "Academic Status", None, 2, 1)
        self.create_widget("🚪", "Logout",None, 2, 2)


    def create_widget(self, icon, text, desc, row, column):
        widget_frame = tk.Frame(self.widgets_frame, bg="white", width=310, height=140, 
                                highlightbackground="#A5A2A2", highlightthickness=1)
        widget_frame.grid(row=row, column=column, padx=10, pady=10)
        widget_frame.pack_propagate(False)

        if text == "Program":
            tk.Label(widget_frame, text=f"{icon} {text}", 
                    font=("Segoe UI", 16, "bold"), bg="white", fg="#0C4A99").pack(anchor="nw", pady=(10,0), padx=20)
            tk.Label(widget_frame, text=desc, 
                    font=("Segoe UI", 12, "bold"), bg="white", fg="#0C4A99").pack(anchor="w", side="left", padx=20, pady=(10, 0))

        if text == "Latest GPA" or text == "Cumulative GPA":
            tk.Label(widget_frame, text=f"{icon} {text}", 
                    font=("Segoe UI", 16, "bold"), bg="white", fg="#0C4A99").pack(anchor="nw", pady=(10,0), padx=20)
            tk.Label(widget_frame, text=desc, 
                    font=("Segoe UI", 28, "bold"), bg="white", fg="#0C4A99").pack(anchor="w", padx=20,pady=(10, 0))
        if desc is None:
            icon_label = tk.Label(widget_frame, text=f"{icon}", 
                    font=("Segoe UI", 24, "bold"), bg="white", 
                    fg="#0C4A99")
            icon_label.pack(anchor="center", pady=(10,0), padx=20)
            
            text_label = tk.Label(widget_frame, text=f"{text}", 
                    font=("Segoe UI", 16, "bold"), bg="white", 
                    fg="#0C4A99")
            text_label.pack(anchor="center", pady=(10,0), padx=20)


            widget_frame.bind("<Button-1>", lambda e: self.create_page(text) if text != "Logout" else self.Logout())
            for widget in widget_frame.winfo_children():
                widget.bind("<Button-1>", lambda e: self.create_page(text) if text != "Logout" else self.Logout())

            widget_frame.bind("<Enter>", lambda e: widget_frame.config(height=150, width=320, bg="white", highlightbackground="#0A3671"))
            widget_frame.bind("<Leave>", lambda e: widget_frame.config(height=140, width=310, bg="white", highlightbackground="#A5A2A2"))

            for widget in widget_frame.winfo_children():
                        widget.bind("<Enter>", lambda e: widget_frame.config(height=150, width=320, bg="white", highlightbackground="#0A3671"))
                        widget.bind("<Leave>", lambda e: widget_frame.config(height=140, width=310, bg="white", highlightbackground="#A5A2A2"))

    


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Profile Test")
    root.geometry("1090x1024")
    Dashboard(root).pack(fill="both", expand=True)
    root.mainloop()