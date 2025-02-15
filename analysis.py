import pandas as pd
import matplotlib.pyplot as plt

# Load attendance data (assuming it's stored in attendance.csv)
file_path = "attendance.csv"  # Update with the actual file path
try:
    data = pd.read_csv(file_path)
except FileNotFoundError:
    print("Error: attendance.csv not found!")
    exit()

# Ensure correct column names
if "Name" not in data.columns or "Attendance" not in data.columns:
    print("Error: CSV file must contain 'Name' and 'Attendance' columns!")
    exit()

# Compute attendance percentage
total_classes = 30  # Modify as per your requirement
data["Attendance Percentage"] = (data["Attendance"] / total_classes) * 100

# Display summary statistics
print("\n--- Attendance Summary ---")
print(data.describe())

# Plot Attendance Bar Chart
plt.figure(figsize=(10, 5))
plt.bar(data["Name"], data["Attendance"], color="skyblue")
plt.xlabel("Students")
plt.ylabel("Attendance Days")
plt.title("Attendance Overview")
plt.xticks(rotation=45)
plt.show()

# Save updated data with attendance percentage
data.to_csv("updated_attendance.csv", index=False)
print("\nUpdated attendance data saved as 'updated_attendance.csv'")
