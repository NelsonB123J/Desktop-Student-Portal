import tkinter as tk
import datetime





class Attendance(tk.Frame):
      def __init__(self, root, create_page=None, course_attend_list=None):
        self.courses = course_attend_list if course_attend_list is not None else [
                  "ASE GST 201",
                  "ENT 201",
                  "MTH 201",
                  "MTH 205",
                  "SEN 201",
                  "COS 201",
                  "ASE CSC 201",
                  "ASE CSC 203",
                  "IFT 201",
                  "CSC 201",
                  ]
        self.time = [
                  "09:00",
                  "11:00",
                  "02:00"
                  ]

        super().__init__(root)
        self.create_page = create_page
        self.configure(bg="#FFFFFF")
        
        self.current_row = 1   
        self.rows_today = 0
        self.current_date = datetime.date.today()


        tk.Label(self, text="Attendance Page", 
                 font=("Segoe UI", 24, "bold"), 
                 bg="#FFFFFF", fg="#0C4A99").pack(padx=40,pady=(50, 20), anchor="nw")
        tk.Frame(self, height=1, bg="#A5A2A2").pack(padx=40,fill="x")

        self.table_frame = tk.Frame(self, bg="#FFFFFF")
        self.table_frame.pack(padx=40, pady=20, fill="both", expand=True)

        self.create_header("Date", column=0)
        self.create_header("Course", column=1)
        self.create_header("Time", column=2)
        self.create_header("Attendance", column=3)
        self.add_row()
        
      def add_row(self):
            row = self.current_row
            
            self.create_label( "",row = row,column =0)
            self.create_button("Select course",row = row,column =1)
            self.create_button("Pick time",row = row,column =2)
            self.create_toggle( "",row = row,column =3)

            self.current_row += 1
      def create_header(self, text, column):
                  header_frame = tk.Frame(self.table_frame, bg="white", width=200, height=80, 
                                    highlightbackground="#A5A2A2", highlightthickness=1)
                  header_frame.grid(row=0, column=column, padx=10, pady=10)
                  header_frame.pack_propagate(False)

                  # if text in ["Date","Course","Time","Attendance"]:
                  tk.Label(header_frame, text=text,
                              font=("Segoe UI", 16, "bold"), bg="white", fg="#0C4A99").pack(anchor="nw", pady=(10,0), padx=20 )
                  if text == "Course":
                              tk.Label(header_frame, text="Select course", 
                              font=("Segoe UI", 12, "bold"), bg="white", fg="#0C4A99").pack(anchor="nw", pady=(5,0), padx=20 )
                  if text == "Time":
                              tk.Label(header_frame, text="Pick time",
                              font=("Segoe UI", 12, "bold"), bg="white", fg="#0C4A99").pack(anchor="nw", pady=(5,0), padx=20 )
      def on_time_selected(self):
            if self.rows_today < 3:
                  self.add_row()
                  self.rows_today += 1
            else:
                  self.current_date += datetime.timedelta(days=1)
                  self.rows_today = 1
                  self.add_row()

      def create_label(self,  text,  row, column):
                  label_frame = tk.Frame(self.table_frame, bg="white", width=200, height=50, 
                                    highlightbackground="#A5A2A2", highlightthickness=1)
                  label_frame.grid(row=row, column=column, padx=10, pady=10)
                  label_frame.pack_propagate(False)
                  
                  if text == "":
                        current_date = datetime.date.today().strftime("%d/%m/%Y")
                        tk.Label(label_frame, text=current_date, 
                                    font=("Segoe UI", 16, "bold"), bg="white", fg="#0C4A99").pack(anchor="nw", pady=(10,0), padx=20)
            
      def create_button(self, text, row, column):
                  button_frame = tk.Frame(self.table_frame, bg="white", width=200, height=50, 
                                    highlightbackground="#A5A2A2", highlightthickness=1)
                  button_frame.grid(row=row, column=column, padx=10, pady=10)
                  button_frame.pack_propagate(False)
                  
                  if text == "Select course":
                        selected = tk.StringVar(value="Select course")
                        option = tk.OptionMenu(button_frame, selected, *self.courses)
                        option.config( font=("Segoe UI", 16, "bold"), bg="white", fg="#0C4A99", highlightthickness=0)
                        option.pack(anchor="nw", pady=(10,0), padx=20)
                  elif text == "Pick time":
                        selected = tk.StringVar(value="Pick time")
                        option = tk.OptionMenu(button_frame, selected, *self.time,command=lambda _: self.on_time_selected())
                        option.config( font=("Segoe UI", 16, "bold"), bg="white", fg="#0C4A99", highlightthickness=0)
                        option.pack(anchor="nw", pady=(10,0), padx=20)
            
      def create_toggle(self, text, row, column):
                  toggle_frame = tk.Frame(self.table_frame, bg="white", width=200, height=50, 
                                    highlightbackground="#A5A2A2", highlightthickness=1)
                  toggle_frame.grid(row=row, column=column, padx=10, pady=10)
                  toggle_frame.pack_propagate(False)


                  
                  state = tk.BooleanVar(value=False)

                  canvas = tk.Canvas(toggle_frame,width=50,height=26,bg="white",highlightthickness=0)
                  canvas.pack(pady=12)

                  
                  circle = canvas.create_oval(2, 2, 24, 24, fill="#0C4A99", outline="")

                  def toggle(event=None):
                        if state.get():
                              canvas.config(bg="white")
                              canvas.coords(circle, 2, 2, 24, 24)
                              canvas.itemconfig(circle, fill="#0C4A99")
                              state.set(False)
                        else:
                              canvas.config(bg="#0C4A99")
                              canvas.coords(circle, 26, 2, 48, 24)
                              canvas.itemconfig(circle, fill="white")
                              state.set(True)

                  canvas.bind("<Button-1>", toggle)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Profile Test")
    root.geometry("1090x1024")
    Attendance(root, create_page=None).pack(fill="both", expand=True)
    root.mainloop()