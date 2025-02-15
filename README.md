Attendance Tracker Project

Overview

This project is a simple Attendance Tracker Application designed for college students using Python. It consists of three main components:

GUI Attendance Tracker (Tkinter, Pandas, Matplotlib)

Data Analysis (Pandas, CSV Handling)

Data Visualization (Matplotlib - Bar Chart & Pie Chart)

1️⃣ GUI Attendance Tracker

Features

✔ Add students to the list✔ Mark attendance for each student✔ View attendance data in a listbox✔ Display an Attendance Overview Bar Chart✔ Save & update attendance data✔ Simple and user-friendly Tkinter GUI

Technologies Used

Python

Tkinter (GUI)

Pandas (Data handling)

Matplotlib (Graph plotting)

How to Run?

Install dependencies if not installed:

pip install pandas matplotlib

Run the Python script:

python attendance_tracker.py

2️⃣ Data Analysis (CSV Handling)

Features

✔ Reads attendance data from a CSV file✔ Computes attendance percentage for each student✔ Displays summary statistics (Mean, Min, Max, etc.)✔ Saves updated attendance data to a new CSV file

Technologies Used

Pandas (Data manipulation)

How to Run?

Ensure you have attendance.csv in the same directory.

Run the Python script:

python attendance.py

The script will generate a new file: updated_attendance.csv

3️⃣ Data Visualization (Graphs)

Features

✔ Bar Chart - Displays student attendance overview✔ Pie Chart - Shows Present vs Absent percentage✔ Customizable for different attendance data

Technologies Used

Matplotlib (Graph generation)

How to Run?

📊 Bar Chart for Attendance

Run the script:

python analysis.py

🥧 Pie Chart for Attendance Percentage

Modify the script to set total_students and present_students manually.

Run the script:

python percentage.py

The Pie Chart will show the percentage of present & absent students.
