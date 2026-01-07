import pandas as pd
import matplotlib.pyplot as plt

# Load data
try:
    df = pd.read_csv("students.csv")
except FileNotFoundError:
    print("File not found. Please check the file path.")
    exit()

# Data Cleaning
df.dropna(inplace=True)

# Basic Analysis
avg_score_gender = df.groupby("Gender")["Exam_Score"].mean()
print("Average Score by Gender:")
print(avg_score_gender)

# Visualization 1: Bar Chart
avg_score_gender.plot(kind='bar')
plt.title("Average Exam Score by Gender")
plt.xlabel("Gender")
plt.ylabel("Average Score")
plt.tight_layout()
plt.savefig("avg_score_by_gender.png")
plt.show()

# Visualization 2: Line Chart
plt.plot(df["Study_Hours"], df["Exam_Score"], marker='o')
plt.title("Study Hours vs Exam Score")
plt.xlabel("Study Hours")
plt.ylabel("Exam Score")
plt.tight_layout()
plt.savefig("study_hours_vs_score.png")
plt.show()
