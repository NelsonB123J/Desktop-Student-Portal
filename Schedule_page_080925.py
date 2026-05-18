import tkinter as tk
from datetime import datetime, timedelta
from tkinter import font

class Schedule(tk.Frame):
    def __init__(self, root, create_page=None, schedule=None):
        super().__init__(root, bg="white")
        
        # Schedule data
        self.schedule = schedule
        # Track currently selected day (defaults to today)
        self.days_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        self.selected_day = datetime.now().strftime("%A")
        
        # Create UI elements
        self.create_widgets()
        self.update_today_schedule()
        
        # Update next class every minute
        self.update_next_class()
    
    def create_widgets(self):
        """Create the UI components"""
        # Title
        title_font = font.Font(family="Arial", size=20, weight="bold")
        title_label = tk.Label(self, text="Class Schedule", font=title_font, bg="white", fg="#003d99")
        title_label.pack(pady=10)
        
        # Day selector buttons
        days_frame = tk.Frame(self, bg="white")
        days_frame.pack(fill="x", padx=10)
        self.day_buttons = {}
        for d in self.days_order:
            b = tk.Button(days_frame, text=d[:3], width=6, relief="raised",
                          command=lambda day=d: self.show_day_schedule(day))
            b.pack(side="left", padx=3, pady=5)
            self.day_buttons[d] = b
        # "Today" quick button
        today_btn = tk.Button(days_frame, text="Today", width=6, bg="#0052cc", fg="white",
                              command=lambda: self.show_day_schedule(datetime.now().strftime("%A")))
        today_btn.pack(side="left", padx=8)
        
        # Next class section
        next_class_frame = tk.Frame(self, bg="#003d99", relief="raised", bd=2)
        next_class_frame.pack(fill="x", padx=20, pady=10)
        
        next_label = tk.Label(next_class_frame, text="Next Class:", font=("Arial", 12, "bold"), 
                              bg="#003d99", fg="white")
        next_label.pack(anchor="w", padx=15, pady=5)
        
        self.next_class_info = tk.Label(next_class_frame, text="Loading...", font=("Arial", 14, "bold"),
                                         bg="#003d99", fg="white", wraplength=400, justify="left")
        self.next_class_info.pack(anchor="w", padx=15, pady=(0, 15))
        
        # Today's (or selected day's) schedule frame
        schedule_frame = tk.Frame(self, bg="white")
        schedule_frame.pack(fill="both", expand=True, padx=20, pady=10)
        
        # Day header
        today_header = tk.Frame(schedule_frame, bg="#0052cc")
        today_header.pack(fill="x", pady=(0, 10))
        
        self.today_label = tk.Label(today_header, text="Selected Day's Schedule", font=("Arial", 14, "bold"), 
                                   bg="#0052cc", fg="white")
        self.today_label.pack(anchor="w", padx=10, pady=8)
        
        # Container for classes
        self.classes_container = tk.Frame(schedule_frame, bg="white")
        self.classes_container.pack(fill="both", expand=True)
        
        # Highlight initial selected day button
        self.highlight_selected_day()
    
    def update_today_schedule(self):
        """Initialize display with today's schedule (selects today)"""
        self.show_day_schedule(datetime.now().strftime("%A"))
    
    def highlight_selected_day(self):
        """Update button styles to reflect currently selected day"""
        for d, btn in self.day_buttons.items():
            if d == self.selected_day:
                btn.config(bg="#0052cc", fg="white", relief="sunken")
            else:
                btn.config(bg="SystemButtonFace", fg="black", relief="raised")
    
    def show_day_schedule(self, day):
        """Show schedule for the given day (called by buttons)"""
        self.selected_day = day
        self.today_label.config(text=f"{day}'s Schedule")
        self.highlight_selected_day()
        
        # Clear previous classes
        for widget in self.classes_container.winfo_children():
            widget.destroy()
        
        classes = self.schedule.get(day, [])
        if classes:
            for class_info in classes:
                class_frame = tk.Frame(self.classes_container, bg="white")
                class_frame.pack(fill="x", pady=8)
                
                time_label = tk.Label(class_frame, text=f"⏰ {class_info['time']}", 
                                     font=("Arial", 10), bg="white", fg="#333")
                time_label.pack(anchor="w")
                
                course_label = tk.Label(class_frame, text=f"📚 {class_info['course']}", 
                                       font=("Arial", 10, "bold"), bg="white", fg="#003d99")
                course_label.pack(anchor="w")
                
                location_label = tk.Label(class_frame, text=f"📍 {class_info['location']}", 
                                         font=("Arial", 9), bg="white", fg="#666")
                location_label.pack(anchor="w")
        else:
            no_class_label = tk.Label(self.classes_container, text="No classes that day", 
                                      font=("Arial", 11, "italic"), bg="white", fg="#999")
            no_class_label.pack(anchor="w", pady=20)
    
    def get_next_class(self):
        """Get the next upcoming class"""
        now = datetime.now()
        current_day = now.strftime("%A")
        current_time = now.time()
        
        days_order = self.days_order
        current_day_index = days_order.index(current_day)
        
        # Check today's remaining classes
        today_classes = self.schedule.get(current_day, [])
        for class_info in today_classes:
            start_time_str = class_info['time'].split(' - ')[0]
            start_time = datetime.strptime(start_time_str, "%I:%M %p").time()
            
            if current_time < start_time:
                return f"{class_info['course']} at {class_info['time']}", current_day
        
        # Check future days
        for i in range(1, 7):
            future_day_index = (current_day_index + i) % 7
            future_day = days_order[future_day_index]
            future_classes = self.schedule.get(future_day, [])
            
            if future_classes:
                first_class = future_classes[0]
                return f"{first_class['course']} at {first_class['time']}", future_day
        
        return "No upcoming classes this week", ""
    
    def update_next_class(self):
        """Update the next class display"""
        next_class, day = self.get_next_class()
        if day:
            self.next_class_info.config(text=f"{next_class}\n({day})")
        else:
            self.next_class_info.config(text=next_class)
        
        # Schedule next update in 60 seconds
        self.after(60000, self.update_next_class)



if __name__ == "__main__":
    root = tk.Tk()
    root.title("Profile Test")
    root.geometry("1090x1024")
    Schedule(root).pack(fill="both", expand=True)
    root.mainloop()