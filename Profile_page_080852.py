import tkinter as tk
import requests
from tkinter import messagebox, simpledialog
from firebase_config import db, auth, firebaseConfig



class Profile(tk.Frame):
    def __init__(self, root, create_page=None, student_info=None, uid=None, idToken=None):
        super().__init__(root)
        self.root = root
        self.uid = uid
        self.idToken = idToken
        self.configure(bg="#0d6efd")

        self.card_padx = 28
        self.card_pady = 28

        # ================= STUDENT DATA =================
        self.data = {
            "Name": student_info[0][1],
            "Matric Number": student_info[1][1],
            "Programme": student_info[2][1],
            "School Email": student_info[3][1],
            "Academic Session": student_info[4][1],
            "Year of Study": student_info[5][1],
            "Degree": student_info[6][1],
            "Faculty": student_info[7][1],
        }

        self.edit_mode = False
        self.entries = {}
        self.field_labels = {}

        # ================= CARD =================
        card = tk.Frame(self, bg="white", bd=0)
        card.place(relx=0.5, rely=0.5, anchor="center")
        card.configure(padx=self.card_padx, pady=self.card_pady)

        # ================= HEADER =================
        header = tk.Frame(card, bg="white")
        header.grid(row=0, column=0, columnspan=4, sticky="ew", pady=(0, 12))
        header.columnconfigure(0, weight=1)

        title = tk.Label(
            header,
            text="Student Profile",
            bg="white",
            fg="#0b1a2b",
            font=(None, 20, "bold")
        )
        title.grid(row=0, column=0, sticky="w")

        actions = tk.Frame(header, bg="white")
        actions.grid(row=0, column=1, sticky="e")

        self.edit_btn = tk.Button(
            actions,
            text="Edit",
            command=self.toggle_edit,
            bg="#0d6efd",
            fg="white",
            padx=12,
            relief="flat",
            cursor="hand2"
        )
        self.edit_btn.pack(side="left", padx=(0, 8))

        self.change_pass_btn = tk.Button(
            actions,
            text="Change Password",
            command=self.change_password,
            bg="#f1f3f5",
            fg="#0b1a2b",
            padx=12,
            relief="flat",
            cursor="hand2"
        )
        self.change_pass_btn.pack(side="left")

        # ================= DETAILS =================
        details_frame = tk.Frame(card, bg="white")
        details_frame.grid(row=1, column=0, columnspan=4, sticky="nsew")
        details_frame.columnconfigure(2, weight=1)

        kinds = {
            "Name": "user",
            "Matric Number": "id",
            "Programme": "program",
            "School Email": "email",
            "Academic Session": "session",
            "Year of Study": "level",
            "Degree": "degree",
            "Faculty": "faculty",
        }

        row_idx = 0
        for key in self.data:
            icon = self._make_icon(details_frame, kinds.get(key, "dot"))
            icon.grid(row=row_idx, column=0, sticky="w", padx=(0, 8), pady=6)

            lbl_key = tk.Label(
                details_frame,
                text=key,
                anchor="w",
                bg="white",
                fg="#2b5f9e",
                font=(None, 10, "bold")
            )
            lbl_key.grid(row=row_idx, column=1, sticky="w", pady=6)

            lbl_val = tk.Label(
                details_frame,
                text=self.data[key],
                anchor="w",
                bg="white",
                fg="#111",
                font=(None, 10)
            )
            lbl_val.grid(row=row_idx, column=2, sticky="w", pady=6)

            self.field_labels[key] = lbl_val
            row_idx += 1

        note = tk.Label(
            card,
            text="Use Edit to update profile information",
            bg="white",
            fg="#666",
            font=(None, 9)
        )
        note.grid(row=2, column=0, columnspan=4, sticky="w", pady=(12, 0))

    # ================= ICONS =================
    def _make_icon(self, parent, kind):
        c = tk.Canvas(parent, width=20, height=20, bg="white", highlightthickness=0)

        if kind == "user":
            c.create_oval(4, 2, 16, 14, fill="#cfe8ff", outline="#9fc7ff")
            c.create_oval(6, 6, 14, 14, fill="#9fc7ff", outline="")
        elif kind == "id":
            c.create_rectangle(2, 3, 18, 15, outline="#9fc7ff", fill="#eaf6ff")
            c.create_line(4, 7, 16, 7, fill="#9fc7ff")
        elif kind == "program":
            c.create_rectangle(3, 4, 17, 14, fill="#eaf6ff", outline="#9fc7ff")
            c.create_line(4, 8, 16, 8, fill="#9fc7ff")
        elif kind == "level":
            c.create_polygon(10, 3, 15, 10, 5, 10, fill="#d6ecff", outline="#9fc7ff")
        elif kind == "session":
            c.create_rectangle(3, 3, 17, 15, fill="#fff4e6", outline="#ffd59e")
            c.create_text(10, 9, text="25", fill="#b07200", font=(None, 7))
        elif kind == "faculty":
            c.create_rectangle(3, 6, 17, 14, fill="#eaf6ff", outline="#9fc7ff")
            c.create_line(3, 9, 17, 9, fill="#9fc7ff")
        elif kind == "email":
            c.create_rectangle(3, 4, 17, 14, fill="#eaf6ff", outline="#9fc7ff")
            c.create_line(3, 4, 10, 9, 17, 4, fill="#9fc7ff")
        else:
            c.create_oval(4, 4, 16, 16, fill="#eaf6ff", outline="#9fc7ff")

        return c

    # ================= EDIT LOGIC =================
    def toggle_edit(self):
        if not self.edit_mode:
            self.enter_edit_mode()
        else:
            self.save_changes()

    def enter_edit_mode(self):
        self.edit_mode = True
        self.edit_btn.configure(text="Save")

        for key, lbl in self.field_labels.items():
            entry = tk.Entry(lbl.master, width=40)
            entry.insert(0, lbl.cget("text"))
            entry.grid(row=lbl.grid_info()["row"], column=2, sticky="w", pady=6)
            self.entries[key] = entry
            lbl.grid_forget()

    def save_changes(self):
        for key, entry in self.entries.items():
            new_value = entry.get().strip()
            self.data[key] = new_value

            lbl = tk.Label(
                entry.master,
                text=new_value,
                anchor="w",
                bg="white",
                fg="#111",
                font=(None, 10)
            )
            lbl.grid(row=entry.grid_info()["row"], column=2, sticky="w", pady=6)
            self.field_labels[key] = lbl
            entry.destroy()

        self.entries.clear()
        self.edit_mode = False
        self.edit_btn.configure(text="Edit")

        student_info = [
            ["Name:", self.data["Name"]],
            ["Matric Number:", self.data["Matric Number"]],
            ["Programme:", self.data["Programme"]],
            ["School Email:", self.data["School Email"]],
            ["Academic Session:", self.data["Academic Session"]],
            ["Year of Study:", self.data["Year of Study"]],
            ["Degree:", self.data["Degree"]],
            ["Faculty:", self.data["Faculty"]],
        ]

        if self.uid:
            db.child("students").child(self.uid).child("Student_info").set(str(student_info))

        messagebox.showinfo("Saved", "Profile changes have been saved.")


    def change_password(self):

        confirm = messagebox.askyesno(
            "Change Password",
            f"Are you sure you want to change your password"
        )

        if not confirm:
            return
        new_password = simpledialog.askstring("Input", "Enter your new password here:")
        if new_password is None:
            return

        def change_password(id_token, new_password):
            url = (
                "https://identitytoolkit.googleapis.com/v1/accounts:update"
                f"?key={firebaseConfig['apiKey']}"
            )

            payload = {
                "idToken": id_token,
                "password": new_password,
                "returnSecureToken": True
            }

            response = requests.post(url, json=payload)

            if response.status_code != 200:
                raise Exception(response.text)

            return response.json()
        try:
            change_password(self.idToken, new_password)
            messagebox.showinfo("Password",f"Password is been changed to {new_password}")
        except Exception as e:
            messagebox.showerror("Error: ",e)


# ================= TEST =================
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Profile Test")
    root.geometry("900x500")

    test_student_info = [
        ["Name:", "Binta Abimiku"],
        ["Matric Number:", "25/01SC02"],
        ["Programme:", "Computer Science"],
        ["School Email:", "binta@ase.edu.ng"],
        ["Academic Session:", "2025/2026"],
        ["Year of Study:", "2"],
        ["Degree:", "B Sc."],
        ["Faculty:", "Faculty of Science and Computing"],
    ]

    Profile(root, student_info=test_student_info, uid="TEST_UID").pack(fill="both", expand=True)
    root.mainloop()
