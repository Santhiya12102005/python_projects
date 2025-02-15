import matplotlib.pyplot as plt

# Manually set values
total_students = 50  # Change this as needed
present_students = 40  # Change this as needed

# Calculate absent students
absent_students = total_students - present_students

# Labels and data
labels = ["Present", "Absent"]
sizes = [present_students, absent_students]
colors = ["green", "red"]

# Plot the pie chart
plt.figure(figsize=(6, 6))
plt.pie(sizes, labels=labels, autopct="%1.1f%%", colors=colors, startangle=140, wedgeprops={"edgecolor": "black"})

# Title
plt.title("Class Attendance Percentage")

# Display the chart
plt.show()
