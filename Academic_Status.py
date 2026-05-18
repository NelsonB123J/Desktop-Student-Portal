import tkinter as tk
import Print
from tkinter import messagebox
from tkinter import ttk

class Academic_Status(tk.Frame):
    def __init__(self, root, create_page=None, student_info=None, Result=None):
        super().__init__(root, bg="white")
        data = Result[list(Result.keys())[-1]]['Semester 1']
        data2 = Result[list(Result.keys())[-1]]['Semester 2']
        self.Result = Result

        self.create_ui(Result, list(Result.keys()))
        total_points = 0
        total_credits = 0
        self.gpa1 = self.calculate_gpa(data)
        self.gpa2 = self.calculate_gpa(data2)

        self.cgpa = self.calculate_cumulative_gpa()
        self.latest_gpa = self.calculate_gpa(data) if data2 == [] else self.calculate_gpa(data2)

        self.student_info = student_info



    def create_ui(self, Result, Years):

        data = Result[list(Result.keys())[-1]]['Semester 1']
        data2 = Result[list(Result.keys())[-1]]['Semester 2']
        self.data = data
        self.data2 = data2
        self.Years = Years
        self.active_year = None


        self.canvas = tk.Canvas(self, bg="white", highlightthickness=0)
        scrollbar = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=scrollbar.set)

        scrollbar.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)


        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)

        main = tk.Frame(self.canvas, bg="white")
        self.main_window = self.canvas.create_window((0, 0), window=main, anchor="nw")
        self.canvas.bind("<Configure>", self._configure_canvas)


        tk.Label(
            main,
            text="Academic Status",
            font=("Segoe UI", 24, "bold"),
            bg="white",
            fg="#0C4A99"
        ).pack(padx=40, pady=(50, 20), anchor="nw")

        tk.Frame(main, height=1, bg="#A5A2A2").pack(padx=40, fill="x")

        cards_frame = tk.Frame(main, bg="white")
        cards_frame.pack(fill="x", pady=15, padx=40)
    
        self.create_widget(cards_frame, "⭐", "Latest GPA", 
        self.calculate_gpa(self.data) if self.data2 == [] else self.calculate_gpa(self.data2), 0, 1)
        self.create_widget(cards_frame, "⭐", "Cumulative GPA", self.calculate_cumulative_gpa(), 0, 2)

        grades_frame = tk.Frame(main, bg="white")
        grades_frame.pack(fill="x", pady=(0, 10), padx=40)

        tk.Label(
            grades_frame,
            text="Grades",
            font=("Segoe UI", 20, "bold"),
            bg="white",
            fg="#0C4A99"
        ).pack(side="left", anchor="w")

        grades_combobox = ttk.Combobox(grades_frame, values=self.Years, 
                                       state="readonly", font=("Segoe UI", 18), foreground="#0C4A99", 
                                       background="white", width=10)
        grades_combobox.pack(side="right", anchor="e")
        grades_combobox.set("Select Year")

        Result_frame = tk.Frame(main, bg="white")
        Result_frame.pack(fill="both", expand=True)

        def on_select(event):
            self.active_year = grades_combobox.get()
            for widget in Result_frame.winfo_children():
                widget.destroy()
            tk.Label(
                Result_frame,
                text="First Semester",
                font=("Segoe UI", 20, "bold"),
                bg="white",
                fg="#0C4A99"
            ).pack(anchor="w", pady=(0, 10), padx=40)

            self.data = Result[grades_combobox.get()]['Semester 1']
            self.data2 = Result[grades_combobox.get()]['Semester 2']
            self.create_table(Result_frame, Result[grades_combobox.get()]['Semester 1'])

            tk.Label(
                Result_frame,
                text="Second Semester",
                font=("Segoe UI", 20, "bold"),
                bg="white",
                fg="#0C4A99"
            ).pack(anchor="w", pady=(0, 10), padx=40)

            self.create_table(Result_frame, Result[grades_combobox.get()]['Semester 2'])

        

            tk.Label(
                Result_frame,
                text=f"""First Semester GPA: {self.calculate_gpa(self.data)}
    Second Semester GPA: {self.calculate_gpa(self.data2)}
    Cumulative GPA: {self.calculate_cumulative_gpa()}""",
                font=("Segoe UI", 18, "bold"),
                bg="white",
                fg="#0C4A99",
                justify="left"
            ).pack(anchor="w", pady=(0, 10), padx=40)


            print_button = tk.Button(
                Result_frame,
                text="Print Result",
                font=("Segoe UI", 14, "bold"),
                bg="#0C4A99",
                fg="white",
                relief="raised",
                padx=20,
                pady=10,
                command=self.print_transcript)
            print_button.pack(pady=(20, 20), padx=40, anchor="w")


            main.update_idletasks()
            self.canvas.config(scrollregion=(0, 0, main.winfo_reqwidth(), main.winfo_reqheight()))

        grades_combobox.bind("<<ComboboxSelected>>", on_select)
        main.update_idletasks()
        self.canvas.config(scrollregion=(0, 0, main.winfo_reqwidth(), main.winfo_reqheight()))


    def create_widget(self, parent, icon, text, desc, row, column):
        widget_frame = tk.Frame(
            parent,
            bg="white",
            width=310,
            height=140,
            highlightbackground="#A5A2A2",
            highlightthickness=1
        )
        widget_frame.pack(side="left", padx=10, pady=10)
        widget_frame.pack_propagate(False)

        tk.Label(
            widget_frame,
            text=f"{icon} {text}",
            font=("Segoe UI", 16, "bold"),
            bg="white",
            fg="#0C4A99"
        ).pack(anchor="nw", pady=(10, 0), padx=20)

        tk.Label(
            widget_frame,
            text=desc,
            font=("Segoe UI", 28, "bold"),
            bg="white",
            fg="#0C4A99"
        ).pack(anchor="w", padx=20, pady=(10, 0))


    def create_table(self, parent, data):
        table = tk.Frame(parent, bg="white")
        table.pack(fill="both", expand=True, padx=40, pady=(0, 20))

        table.columnconfigure(0, weight=2)
        table.columnconfigure(1, weight=1)
        table.columnconfigure(2, weight=1)
        table.columnconfigure(3, weight=1)

        headers = ["Course Code", "Credits", "Score", "Grade"]

        for col, text in enumerate(headers):
            tk.Label(
                table,
                text=text,
                font=("Segoe UI", 20, "bold"),
                bg="#eef2ff",
                fg="#0C4A99",
                anchor="w"
            ).grid(row=0, column=col, padx=5, pady=5, sticky="ew")

        for row_id, row in enumerate(data, start=1):
            grade = self.grade_calc(float(row[2]))
            display_row = row + [grade]
            for col, value in enumerate(display_row):
                tk.Label(
                    table,
                    text=value,
                    font=("Segoe UI", 16),
                    bg="white",
                    fg="#0C4A99",
                    anchor="w"
                ).grid(row=row_id, column=col, padx=5, pady=4, sticky="ew")


    def grade_calc(self, score):
        if score >= 70:
            return "A"
        elif score >= 60:
            return "B"
        elif score >= 50:
            return "C"
        elif score >= 40:
            return "D"
        else:
            return "F"

    def calculate_gpa(self, data):
        total_points = 0
        total_credits = 0
        grade_points = {'A': 5.0, 'B': 4.0, 'C': 3.0, 'D': 2.0, 'F': 0.0}

        for course in data:
            credits = float(course[1])
            score = float(course[2])
            grade = self.grade_calc(score)
            points = grade_points.get(grade, 0)

            total_points += points * credits
            total_credits += credits

        gpa = total_points / total_credits if total_credits > 0 else 0
        return round(gpa, 2)
    
    def calculate_cumulative_gpa(self):
        total_points = 0
        total_credits = 0
        grade_points = {'A': 5.0, 'B': 4.0, 'C': 3.0, 'D': 2.0, 'F': 0.0}

        for year in self.Result.values():
            for semester in year.values():
                for course in semester:
                    credits = float(course[1])
                    score = float(course[2])
                    grade = self.grade_calc(score)
                    points = grade_points.get(grade, 0)

                    total_points += points * credits
                    total_credits += credits

        cumulative_gpa = total_points / total_credits if total_credits > 0 else 0
        return round(cumulative_gpa, 2)

    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def _configure_canvas(self, event):
        self.canvas.itemconfig(self.main_window, width=event.width)

    def print_transcript(self):
        for row in self.data:
            grade = self.grade_calc(float(row[2]))
            row.append(grade)
        for row in self.data2:
            grade = self.grade_calc(float(row[2]))
            row.append(grade)
        Print.create_transcript(self.calculate_gpa(self.data), self.calculate_gpa(self.data2), self.cgpa, self.data, self.data2, self.student_info, self.active_year)
        messagebox.showinfo("Result", "Result has been printed to the downloads folder.")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Profile Test")
    root.geometry("1090x1024")

    Academic_Status(root).pack(fill="both", expand=True)

    root.mainloop()
