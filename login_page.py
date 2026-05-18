import tkinter as tk
from firebase_config import auth, db

class LoginPage(tk.Frame):
    def __init__(self, parent, on_login_success=None):
        super().__init__(parent, bg="#FFFFFF")
        self.on_login_success = on_login_success


        main_frame = tk.Frame(self, bg="#FFFFFF", bd=3, relief="raised")
        main_frame.pack(anchor="center", expand=True)
        center_frame = tk.Frame(main_frame, bg="#FFFFFF", padx=60, pady=40)
        center_frame.pack(anchor="center", expand=True)


        tk.Label(
            center_frame,
            text="📚 ASE STUDENT PORTAL",
            font=("Segoe UI", 28, "bold"),
            bg="#FFFFFF",
            fg="#0C4A99"
        ).pack(pady=(0, 10))

        tk.Label(
            center_frame,
            text="Please log in to continue",
            font=("Segoe UI", 14),
            bg="#FFFFFF",
            fg="#666666"
        ).pack(pady=(0, 40))


        tk.Label(
            center_frame,
            text="Email",
            font=("Segoe UI", 12, "bold"),
            bg="#FFFFFF",
            fg="#0C4A99",
            anchor="w"
        ).pack(fill="x", pady=(0, 5))

        self.email_entry = tk.Entry(
            center_frame,
            font=("Segoe UI", 14),
            width=30,
            bd=1,
            relief="solid"
        )
        self.email_entry.pack(pady=(0, 20), ipady=8)
        self.email_entry.focus()


        tk.Label(
            center_frame,
            text="Password",
            font=("Segoe UI", 12, "bold"),
            bg="#FFFFFF",
            fg="#0C4A99",
            anchor="w"
        ).pack(fill="x", pady=(0, 5))

        self.password_entry = tk.Entry(
            center_frame,
            font=("Segoe UI", 14),
            width=30,
            show="*",
            bd=1,
            relief="solid"
        )
        self.password_entry.pack(pady=(0, 10), ipady=8)


        self.error_label = tk.Label(
            center_frame,
            text="",
            fg="red",
            bg="#FFFFFF",
            font=("Segoe UI", 10)
        )
        self.error_label.pack(pady=(5, 20))


        self.login_button = tk.Button(
            center_frame,
            text="Sign In",
            font=("Segoe UI", 14, "bold"),
            bg="#0C4A99",
            fg="white",
            bd=0,
            padx=50,
            pady=12,
            command=lambda: (self.login()),
            cursor="hand2"
        )
        self.login_button.pack(pady=(10, 0))


        self.bind('<Return>', lambda e: (self.login()))
        self.email_entry.bind('<Return>', lambda e: (self.login()))
        self.password_entry.bind('<Return>', lambda e: (self.login()))

    def login(self):
        email = self.email_entry.get().strip()
        password = self.password_entry.get().strip()

        if not email or not password:
            self.error_label.config(text="Please enter both email and password")
            return

        try:
            user = auth.sign_in_with_email_and_password(email, password)
            uid = user["localId"]
            idToken = user['idToken']
            student = db.child("students").child(uid).get().val()
            Courses = db.child("Courses").get().val()




            if self.on_login_success:
                self.on_login_success(student, Courses, uid, idToken)
        except Exception as e:
            self.error_label.config(text="Invalid email or password")
            if e == "HTTPSConnectionPool(host='www.googleapis.com', port=443): Max retries exceeded with url: /identitytoolkit/v3/relyingparty/verifyPassword?key=AIzaSyDe7GodG9CY9DGNhbep7c2stRBe7dxwoFE (Caused by NewConnectionError('<urllib3.connection.HTTPSConnection object at 0x0000022F49165FD0>: Failed to establish a new connection: [Errno 11001] getaddrinfo failed'))":
                self.error_label.config(text="No internet Connection")
            print("Login error:", e)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Student Portal Login")
    root.geometry("1160x1024")
    root.configure(bg="#FFFFFF")

    login_page = LoginPage(root)
    login_page.pack(fill="both", expand=True)

    root.mainloop()