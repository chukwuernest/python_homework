import sqlite3


with sqlite3.connect("../db/school.db") as conn: 
    print("Database created and connected successfully.")

    conn.execute("PRAGMA foreign_keys = 1")  
    cursor = conn.cursor()

    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Students (
            student_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL UNIQUE,
            age INTEGER,
            major TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Courses (
            course_id INTEGER PRIMARY KEY,
            course_name TEXT NOT NULL UNIQUE,
            instructor_name TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Enrollments (
            enrollment_id INTEGER PRIMARY KEY,
            student_id INTEGER,
            course_id INTEGER,
            FOREIGN KEY (student_id) REFERENCES Students (student_id),
            FOREIGN KEY (course_id) REFERENCES Courses (course_id)
        )
    """)

    print("Tables created successfully.")



def add_student(cursor, name, age, major):
    try:
        cursor.execute("INSERT INTO Students (name, age, major) VALUES (?, ?, ?)", (name, age, major))
    except sqlite3.IntegrityError:
        print(f" Student '{name}' is already in the database.")

def add_course(cursor, name, instructor):
    try:
        cursor.execute("INSERT INTO Courses (course_name, instructor_name) VALUES (?, ?)", (name, instructor))
    except sqlite3.IntegrityError:
        print(f" Course '{name}' is already in the database.")



with sqlite3.connect("../db/school.db") as conn:
    conn.execute("PRAGMA foreign_keys = 1")
    cursor = conn.cursor()

    add_student(cursor, 'Alice', 20, 'Computer Science')
    add_student(cursor, 'Bob', 22, 'History')
    add_student(cursor, 'Charlie', 19, 'Biology')

    add_course(cursor, 'Math 101', 'Dr. Smith')
    add_course(cursor, 'English 101', 'Ms. Jones')
    add_course(cursor, 'Chemistry 101', 'Dr. Lee')

    conn.commit()
    print("Sample data inserted successfully.")