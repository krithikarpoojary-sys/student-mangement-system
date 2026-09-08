import sqlite3

def create_database():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            rollno TEXT UNIQUE,
            name TEXT,
            age INTEGER,
            gender TEXT,
            course TEXT,
            phone TEXT,
            email TEXT
        )
    """)

    conn.commit()
    conn.close()


def add_student(rollno, name, age, gender, course, phone, email):
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO students
        (rollno, name, age, gender, course, phone, email)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (rollno, name, age, gender, course, phone, email))

    conn.commit()
    conn.close()

def search_student(rollno):
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM students WHERE rollno=?",
        (rollno,)
    )

    student = cursor.fetchone()

    conn.close()

    return student
def update_student(rollno, name, age, gender, course, phone, email):
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE students
        SET name=?, age=?, gender=?, course=?, phone=?, email=?
        WHERE rollno=?
    """, (name, age, gender, course, phone, email, rollno))

    conn.commit()
    conn.close()
def delete_student(rollno):
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM students WHERE rollno=?",
        (rollno,)
    )

    conn.commit()
    conn.close()
def get_all_students():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")

    students = cursor.fetchall()

    conn.close()

    return students
def get_dashboard_data():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM students")
    total = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM students WHERE LOWER(gender)='male'")
    male = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM students WHERE LOWER(gender)='female'")
    female = cursor.fetchone()[0]

    conn.close()

    return total, male, female