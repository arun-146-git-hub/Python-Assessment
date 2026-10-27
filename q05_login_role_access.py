""" Check username, password and role. """

correct_username = "admin"
correct_password = "python123"

username = input("Username: ")
if username == correct_username:
    password = input("Password: ")
    if password == correct_password:
        role = input("Role (admin/teacher/student): ").strip().lower()
        if role == "admin":
            print("Full Access")
        elif role == "teacher":
            print("Teacher Dashboard")
        elif role == "student":
            print("Student Dashboard")
        else:
            print("Invalid Role")
    else:
        print("Wrong Password")
else:
    print("Invalid Username")
