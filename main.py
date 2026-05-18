import tkinter as tk
import os
import sys
import ast
from login_page import LoginPage
from dashboard_page import Dashboard
from Academic_Status import Academic_Status
from attendance_page import Attendance
from Schedule_page_080925 import Schedule
from Profile_page_080852 import Profile
from course_registration_080822 import CourseRegistrationApp

root = tk.Tk()
root.title("Student Portal")
root.geometry("1440x1024")
root.configure(bg="#FFFFFF")
bundle_dir = os.path.dirname(os.path.abspath(__file__))
logo = os.path.join(bundle_dir, "ase_logo.ico")
root.iconbitmap(logo)

r = 5
main_frame = tk.Frame(root, bg="#FFFFFF")
main_frame.pack(fill="both", expand=True)

current_active = None
buttons = {}
pages = {}

def create_page(page_name):
    global current_active
    for page in pages.values():
        page.pack_forget()
    if page_name in pages:
        pages[page_name].pack(fill="both", expand=True)
        current_active = page_name
        for name, btn in buttons.items():
            if name == current_active:
                btn.config(bg="#0A3671")
            else:
                btn.config(bg="#0C4A99")

def show_main_app(student_data, Courses, uid, idToken):
    global r
    
    Student_info = ast.literal_eval(student_data['Student_info'])
    print(Student_info)
    Result = ast.literal_eval(student_data['Result'])
    Courses = ast.literal_eval(Courses)

    def filter_schedule_for_program(courses, program_name):
        filtered_schedule = {}

        for day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday']:
            day_courses = []

            for course in courses.get(day, []):
                if program_name in course.get('program', set()):
                    day_courses.append({
                        'time': course['time'],
                        'course': course['course'],
                        'location': course['location']
                    })

            if day_courses:
                filtered_schedule[day] = day_courses

        return filtered_schedule
    def get_courses_by_program(timetable, program_name):
        credit_unit = 2
        courses = []

        for day, schedules in timetable.items():
            for entry in schedules:
                if program_name in entry["program"]:
                    course_tuple = (entry["course"], credit_unit)
                    if course_tuple not in courses:
                        courses.append(course_tuple)

        return courses
    def get_course_list(Courses, program_name=None):
        course_set = set()

        for day in Courses.values():
            for entry in day:
                if program_name is None or program_name in entry['program']:
                    course_set.add(entry['course'])

        return sorted(course_set)



    schedule = filter_schedule_for_program(
        Courses,
        Student_info[2][1]
    )
    course_regist_list = get_courses_by_program(Courses, Student_info[2][1])
    course_attend_list = get_course_list(Courses, Student_info[2][1])


    

    for widget in main_frame.winfo_children():
        widget.destroy()


    global Side_Bar
    Side_Bar = tk.Frame(main_frame, bg="#0C4A99", width=280)
    Side_Bar.pack(side="left", fill="y")
    Side_Bar.pack_propagate(False)

    Side_Bar_Title = tk.Frame(Side_Bar, bg="#0C4A99", height=120)
    Side_Bar_Title.pack(fill="x", padx=20, pady=20)

    tk.Label(Side_Bar_Title, text="📚 STUDENT", font=("Segoe UI", 18, "bold"), bg="#0C4A99", fg="#FFFFFF").pack(anchor="w", padx=20, pady=(20, 0))
    tk.Label(Side_Bar_Title, text="PORTAL", font=("Segoe UI", 14), bg="#0C4A99", fg="#E8F0F8").pack(anchor="w", padx=20, pady=(5, 20))


    pages["Dashboard"] = Dashboard(main_frame, create_page, Logout, Student_info, Result)
    pages["Profile"] = Profile(main_frame, create_page, Student_info, uid, idToken)
    pages["Academic Status"] = Academic_Status(main_frame, create_page, Student_info, Result)
    pages["Attendance"] = Attendance(main_frame, create_page, course_attend_list)
    pages["Schedule"] = Schedule(main_frame, create_page, schedule)
    pages["Courses"] = CourseRegistrationApp(main_frame, create_page, course_regist_list)

    def Side_Bar_Buttons(text, icon, page_name):
        btn = tk.Button(
            Side_Bar,
            text=f"{icon}  {text}",
            bg="#0C4A99",
            fg="White",
            font=("Segoe UI", 16, "bold"),
            anchor="w",
            relief="flat",
            cursor="hand2",
            command=lambda: create_page(page_name) if page_name != "Logout" else Logout()
        )
        btn.pack(fill="x", padx=10, pady=5)
        buttons[page_name] = btn
        btn.bind("<Enter>", lambda e: btn.config(bg="#0A3671"))
        btn.bind("<Leave>", lambda e: btn.config(bg="#0A3671" if page_name == current_active else "#0C4A99"))


    Side_Bar_Buttons("Dashboard", "🏠", "Dashboard")
    Side_Bar_Buttons("Profile", "👤", "Profile")
    Side_Bar_Buttons("Courses", "📚", "Courses")
    Side_Bar_Buttons("Schedule", "📅","Schedule")
    Side_Bar_Buttons("Attendance", "✓", "Attendance")
    Side_Bar_Buttons("Academic Status", "🎓", "Academic Status")
    Side_Bar_Buttons("Logout", "🚪", "Logout")


    create_page("Dashboard")
def Logout():
    for widget in main_frame.winfo_children():
        widget.destroy()
    login_page = LoginPage(main_frame, show_main_app)
    login_page.pack(fill="both", expand=True)


login_page = LoginPage(main_frame, show_main_app)
login_page.pack(fill="both", expand=True)

root.mainloop()