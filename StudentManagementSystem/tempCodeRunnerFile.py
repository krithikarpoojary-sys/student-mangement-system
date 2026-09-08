import tkinter as tk
from database import create_database, add_student

# Create Database
create_database()
def save_student():

    add_student(
        roll_entry.get(),
        name_entry.get(),
        age_entry.get(),
        gender_entry.get(),
        course_entry.get(),
        phone_entry.get(),
        email_entry.get()
    )

    print("Student Saved")

# Main Window
window = tk.Tk()
window.title("Student Management System")
window.geometry("800x600")
window.configure(bg="#D6EAF8")

# Title
title = tk.Label(
    window,
    text="🎓 Student Management System",
    font=("Arial", 22, "bold"),
    bg="#D6EAF8",
    fg="#2C3E50"
)
title.pack(pady=20)

# Form Frame
form_frame = tk.Frame(window, bg="#D6EAF8")
form_frame.pack(pady=10)

# Roll Number
tk.Label(form_frame, text="Roll No", bg="#D6EAF8", font=("Arial", 11, "bold")).grid(row=0, column=0, padx=10, pady=10)
roll_entry = tk.Entry(form_frame, width=25)
roll_entry.grid(row=0, column=1)

# Name
tk.Label(form_frame, text="Name", bg="#D6EAF8", font=("Arial", 11, "bold")).grid(row=1, column=0, padx=10, pady=10)
name_entry = tk.Entry(form_frame, width=25)
name_entry.grid(row=1, column=1)

# Age
tk.Label(form_frame, text="Age", bg="#D6EAF8", font=("Arial", 11, "bold")).grid(row=2, column=0, padx=10, pady=10)
age_entry = tk.Entry(form_frame, width=25)
age_entry.grid(row=2, column=1)

# Gender
tk.Label(form_frame, text="Gender", bg="#D6EAF8", font=("Arial", 11, "bold")).grid(row=3, column=0, padx=10, pady=10)
gender_entry = tk.Entry(form_frame, width=25)
gender_entry.grid(row=3, column=1)

# Course
tk.Label(form_frame, text="Course", bg="#D6EAF8", font=("Arial", 11, "bold")).grid(row=4, column=0, padx=10, pady=10)
course_entry = tk.Entry(form_frame, width=25)
course_entry.grid(row=4, column=1)

# Phone
tk.Label(form_frame, text="Phone", bg="#D6EAF8", font=("Arial", 11, "bold")).grid(row=5, column=0, padx=10, pady=10)
phone_entry = tk.Entry(form_frame, width=25)
phone_entry.grid(row=5, column=1)

# Email
tk.Label(form_frame, text="Email", bg="#D6EAF8", font=("Arial", 11, "bold")).grid(row=6, column=0, padx=10, pady=10)
email_entry = tk.Entry(form_frame, width=25)
email_entry.grid(row=6, column=1)

add_button = tk.Button(
    window,
    text="➕ Add Student",
    command=save_student,
    bg="green",
    fg="white",
    font=("Arial", 12, "bold"),
    width=18
)

add_button.pack(pady=20)

window.mainloop()