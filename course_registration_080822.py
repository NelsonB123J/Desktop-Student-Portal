import tkinter as tk
from tkinter import messagebox, font

MIN_CU = 18
MAX_CU = 24



class CourseRegistrationApp(tk.Frame):
    def __init__(self, parent, switch_page=None, registered_courses=None):
        COURSES = registered_courses if registered_courses else []
        super().__init__(parent, bg="#3b82f6")

        # Colors
        self.primary_blue = "#3b82f6"
        self.accent_blue = "#2563eb"
        self.bg_white = "#ffffff"

        # Fonts
        self.header_font = font.Font(size=16, weight="bold")
        self.normal_font = font.Font(size=11)
        self.small_font = font.Font(size=10)

        # Content frame (white on blue background)
        content = tk.Frame(self, bg=self.bg_white, bd=0)
        content.pack(fill="both", expand=True, padx=24, pady=24)

        header = tk.Label(
            content,
            text="Semester Course Registration",
            font=self.header_font,
            bg=self.bg_white,
            fg=self.accent_blue
        )
        header.pack(pady=(14, 6))

        hint = tk.Label(
            content,
            text=f"Select courses (required load: {MIN_CU} - {MAX_CU} credit units)",
            bg=self.bg_white,
            font=self.small_font
        )
        hint.pack()

        self.course_vars = []

        list_frame = tk.Frame(content, bg=self.bg_white)
        list_frame.pack(pady=12, padx=14, fill="both", expand=True)

        left_col = tk.Frame(list_frame, bg=self.bg_white)
        right_col = tk.Frame(list_frame, bg=self.bg_white)
        left_col.pack(side="left", fill="both", expand=True, padx=(0, 12))
        right_col.pack(side="left", fill="both", expand=True)

        for idx, (code, cu) in enumerate(COURSES):
            var = tk.IntVar(value=0)
            parent_col = left_col if idx % 2 == 0 else right_col

            cb = tk.Checkbutton(
                parent_col,
                text=f"{code} — {cu} CU",
                variable=var,
                command=self.update_total,
                bg=self.bg_white,
                fg="#0f172a",
                selectcolor=self.bg_white,
                font=self.normal_font,
                activebackground=self.bg_white,
                anchor="w"
            )
            cb.pack(anchor="w", pady=6)

            self.course_vars.append((var, code, cu))

        summary = tk.Frame(content, bg=self.bg_white)
        summary.pack(pady=(6, 0))

        self.total_label = tk.Label(
            summary,
            text="Total Credit Units: 0",
            font=self.normal_font,
            bg=self.bg_white
        )
        self.total_label.pack()

        self.validation_label = tk.Label(
            summary,
            text="",
            font=self.small_font,
            bg=self.bg_white
        )
        self.validation_label.pack()

        actions = tk.Frame(content, bg=self.bg_white)
        actions.pack(pady=10)

        self.select_all_btn = tk.Button(
            actions,
            text="Select All",
            command=self.select_all,
            bg=self.accent_blue,
            fg="white",
            activebackground="#1d4ed8",
            relief="flat",
            padx=8,
            pady=6
        )
        self.select_all_btn.grid(row=0, column=0, padx=8)

        self.clear_all_btn = tk.Button(
            actions,
            text="Clear All",
            command=self.clear_all,
            bg="#64748b",
            fg="white",
            activebackground="#475569",
            relief="flat",
            padx=8,
            pady=6
        )
        self.clear_all_btn.grid(row=0, column=1, padx=8)

        self.register_btn = tk.Button(
            actions,
            text="Register Selected Courses",
            command=self.register,
            state="disabled",
            bg="#059669",
            fg="white",
            activebackground="#047857",
            relief="flat",
            padx=10,
            pady=7
        )
        self.register_btn.grid(row=0, column=2, padx=12)

        # Result + registered courses section (UNCHANGED)
        bottom = tk.Frame(content, bg=self.bg_white)
        bottom.pack(padx=10, pady=(6, 12), fill="both", expand=True)

        self.result_text = tk.Text(
            bottom,
            height=6,
            state="disabled",
            bg="#f8fafc",
            bd=0
        )
        self.result_text.pack(side="left", fill="both", expand=True, padx=(0, 8))

        reg_frame = tk.Frame(bottom, bg=self.bg_white)
        reg_frame.pack(side="right", fill="y")

        reg_label = tk.Label(
            reg_frame,
            text="Registered Courses",
            bg=self.bg_white,
            font=self.small_font,
            fg=self.accent_blue
        )
        reg_label.pack(anchor="nw")

        self.registered_listbox = tk.Listbox(
            reg_frame,
            height=8,
            bg="#f8fafc",
            bd=0,
            width=28
        )
        self.registered_listbox.pack(pady=(6, 0))

        # Registration history (unchanged)
        self.registration_history = []

        self.update_total()

    # ================= LOGIC (UNCHANGED) ================= #

    def update_total(self):
        total = sum(var.get() * cu for var, _, cu in self.course_vars)
        self.total_label.config(text=f"Total Credit Units: {total}")

        if total < MIN_CU:
            self.validation_label.config(
                text=f"Minimum {MIN_CU} CUs required",
                fg="#dc2626"
            )
            self.register_btn.config(state="disabled")

        elif total > MAX_CU:
            self.validation_label.config(
                text=f"Maximum {MAX_CU} CUs allowed",
                fg="#dc2626"
            )
            self.register_btn.config(state="disabled")

        else:
            self.validation_label.config(
                text="Load is valid — you may register",
                fg="#059669"
            )
            self.register_btn.config(state="normal")

    def select_all(self):
        for var, _, _ in self.course_vars:
            var.set(1)
        self.update_total()

    def clear_all(self):
        for var, _, _ in self.course_vars:
            var.set(0)
        self.update_total()

    def register(self):
        selected = [(code, cu) for var, code, cu in self.course_vars if var.get()]
        total = sum(cu for _, cu in selected)

        if not selected:
            messagebox.showwarning(
                "No Selection",
                "Please select at least one course."
            )
            return

        selected_lines = [f"{code} ({cu} CU)" for code, cu in selected]

        msg = (
            "You have registered the following courses:\n\n"
            + "\n".join(selected_lines)
            + f"\n\nTotal: {total} CU"
        )

        messagebox.showinfo("Registration Confirmed", msg)

        # Result pane
        self.result_text.config(state="normal")
        self.result_text.delete("1.0", tk.END)
        self.result_text.insert(tk.END, msg)
        self.result_text.config(state="disabled")

        # Registered courses list
        self.registered_listbox.delete(0, tk.END)
        for code, cu in selected:
            self.registered_listbox.insert(
                tk.END, f"{code} — {cu} CU"
            )

        self.registration_history.append({
            "courses": selected_lines,
            "total": total
        })
