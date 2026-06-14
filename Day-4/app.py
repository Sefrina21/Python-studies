from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Create database and table
def init_db():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        email TEXT,
        course TEXT,
        marks REAL,
        status TEXT
    )
    """)

    conn.commit()
    conn.close()

init_db()

# Home Page
@app.route("/")
def home():
    return render_template("index.html")


# Add Student
@app.route("/add", methods=["POST"])
def add_student():

    name = request.form["name"]
    age = request.form["age"]
    email = request.form["email"]
    course = request.form["course"]
    marks = float(request.form["marks"])

    if marks >= 85:
        status = "Selected"
    else:
        status = "Waiting List"

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO students
    (name, age, email, course, marks, status)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (name, age, email, course, marks, status))

    conn.commit()
    conn.close()

    return redirect("/students")


# View Students
@app.route("/students")
def students():

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    data = cursor.fetchall()

    conn.close()

    return render_template("students.html", students=data)


# Delete Student
@app.route("/delete/<int:id>")
def delete_student(id):

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM students WHERE id=?",
        (id,)
    )

    conn.commit()
    conn.close()

    return redirect("/students")


if __name__ == "__main__":
    app.run(debug=True)
