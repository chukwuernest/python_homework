import sqlite3

with sqlite3.connect("../db/school.db") as conn: 
  
 print("database created and connected successfully.")

cursor = conn.cursor()

cursor.execute("""
 Create Table If Not Exists Student(
     student_id INTEGER PRIMARY KEY,
     name TEXT NOT NULL UNIQUE,
     age INTEGER,
     major TEXT
     )
     """)

cursor.execute("""
 Create Table If Not Exists course(
     course_id INTEGER PRIMARY KEY,
     course_name TEXT NOT NULL UNIQUE,
     instructor_name Text 
     )
     """)

cursor.execute("""
 Create Table If Not Exists Enrollments(
     enrollment_id INTEGER PRIMARY KEY,
     student_id INTEGER,
     course_id INTEGER,
     FOREIGN KEY (student_id) REFERENCES Students (student_id),
     FOREIGN KEY (course_id) REFERENCES Course (course_id)
     )
     """)

print("Table Create Successfully")

   