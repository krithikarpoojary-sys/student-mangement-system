import tkinter as tk
from tkinter import ttk
import sqlite3
from database import (
    create_database,
    add_student,
    search_student,
    update_student,
    delete_student,
    get_all_students,
    get_dashboard_data,
)
from tkinter import messagebox
def search():
    student = search_student(roll_entry.get())
    if student:

        name_entry.delete(0, tk.END)
        age_entry.delete(0, tk.END)
        gender_entry.delete(0, tk.END)
        course_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)

        name_entry.insert(0, student[2])
        age_entry.insert(0, student[3])
        gender_entry.insert(0, student[4])
        course_entry.insert(0, student[5])
        phone_entry.insert(0, student[6])
        email_entry.insert(0, student[7])

    else:
        messagebox.showinfo("Search", "Student not found.")

def save_student():
    try:
        messagebox.showinfo("Step 1", "Button is working")

        add_student(
            roll_entry.get(),
            name_entry.get(),
            age_entry.get(),
            gender_entry.get(),
            course_entry.get(),
            phone_entry.get(),
            email_entry.get()
        )

        messagebox.showinfo("Step 2", "Student added successfully!")
        load_students()

    except Exception as e:
        messagebox.showerror("Database Error", str(e))
def update():
    update_student(
        roll_entry.get(),
        name_entry.get(),
        age_entry.get(),
        gender_entry.get(),
        course_entry.get(),
        phone_entry.get(),
        email_entry.get()
    )

    messagebox.showinfo(
        "Success",
        "Student updated successfully!"
    )
    load_students()
from tkinter import messagebox
def delete():

    messagebox.showinfo("Test", "Delete button clicked!")

    answer = messagebox.askyesno(
        "Delete",
        "Are you sure you want to delete this student?"
    )

    if answer:
        delete_student(roll_entry.get())

        messagebox.showinfo(
            "Success",
            "Student deleted successfully!"
        )
    load_students()
create_database()


# Main Window
window = tk.Tk()
window.title("Student Management System")
window.geometry("900x750")
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
dashboard = tk.Frame(window, bg="#D6EAF8")
dashboard.pack(pady=10)

total_label = tk.Label(
    dashboard,
    text="👨‍🎓 Total Students : 0",
    font=("Arial",12,"bold"),
    bg="#D6EAF8",
    fg="blue"
)
total_label.grid(row=0,column=0,padx=20)

male_label = tk.Label(
    dashboard,
    text="👨 Male : 0",
    font=("Arial",12,"bold"),
    bg="#D6EAF8",
    fg="green"
)
male_label.grid(row=0,column=1,padx=20)

female_label = tk.Label(
    dashboard,
    text="👩 Female : 0",
    font=("Arial",12,"bold"),
    bg="#D6EAF8",
    fg="deeppink"
)
female_label.grid(row=0,column=2,padx=20)
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
search_button = tk.Button(
    window,
    text="🔍 Search Student",
    command=search,
    bg="#3498DB",
    fg="white",
    font=("Arial", 12, "bold"),
    width=18
)

search_button.pack(pady=10)
from tkinter import messagebox
update_button = tk.Button(
    window,
    text="✏ Update Student",
    command=update,
    bg="orange",
    fg="white",
    font=("Arial", 12, "bold"),
    width=18
)

update_button.pack(pady=10)
delete_button = tk.Button(
    window,
    text="🗑 Delete Student",
    command=delete,
    bg="red",
    fg="white",
    font=("Arial", 12, "bold"),
    width=18
)

delete_button.pack(pady=10)
# Student Records Table
columns = ("Roll No", "Name", "Age", "Gender", "Course", "Phone", "Email")

student_table = ttk.Treeview(
    window,
    columns=columns,
    show="headings",
    height=8
)

for col in columns:
    student_table.heading(col, text=col)
    student_table.column(col, width=100)

student_table.pack(pady=20)
def select_student(event):

    selected = student_table.focus()

    if not selected:
        return

    values = student_table.item(selected, "values")

    roll_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    gender_entry.delete(0, tk.END)
    course_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)

    roll_entry.insert(0, values[0])
    name_entry.insert(0, values[1])
    age_entry.insert(0, values[2])
    gender_entry.insert(0, values[3])
    course_entry.insert(0, values[4])
    phone_entry.insert(0, values[5])
    email_entry.insert(0, values[6])
student_table.bind("<<TreeviewSelect>>", select_student)
def load_students():

    for row in student_table.get_children():
        student_table.delete(row)

    students = get_all_students()

    for student in students:
        student_table.insert(
            "",
            tk.END,
            values=(
                student[1],  # Roll No
                student[2],  # Name
                student[3],  # Age
                student[4],  # Gender
                student[5],  # Course
                student[6],  # Phone
                student[7],  # Email
            )
        )

def update_dashboard():

    total, male, female = get_dashboard_data()

    total_label.config(text=f"👨‍🎓 Total Students : {total}")
    male_label.config(text=f"👨 Male : {male}")
    female_label.config(text=f"👩 Female : {female}")

load_students()
update_dashboard()

window.mainloop()