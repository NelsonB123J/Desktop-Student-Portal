from firebase_config import auth, db


email = "nelson@gmail.com"
password = "123456"

user = auth.sign_in_with_email_and_password(email, password)
uid = user["localId"]


student = db.child("students").child(uid).get().val()
student = student['Student_info']
student = eval(student)
name = student[0][1]
print("UID:", uid)
print(student, name)
