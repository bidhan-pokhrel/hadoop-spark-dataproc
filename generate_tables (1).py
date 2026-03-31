import csv
import random
from datetime import datetime, timedelta

# Function to generate random dates
def random_date(start_date, end_date):
    time_between = end_date - start_date
    days = time_between.days
    random_days = random.randrange(days)
    return start_date + timedelta(days=random_days)

# Define date range for DOB (1985-01-01 to 2000-12-31)
start_date = datetime(1985, 1, 1)
end_date = datetime(2000, 12, 31)

# Sample names and course IDs
names = ["Alice Smith", "Bob Johnson", "Charlie Brown", "Diana Wilson", "Emma Davis",
         "Frank Miller", "Grace Lee", "Henry Clark", "Isabella Adams", "Jack Taylor"]
course_ids = ["CS101", "MATH201", "PHY301", "ENG401", "BIO501"]

# Generate Table A (StudentId, Name, DOB)
table_a = []
for i in range(1, 101):  # 100 students
    dob = random_date(start_date, end_date).strftime('%Y-%m-%d')
    table_a.append([i, random.choice(names), dob])

# Write Table A to CSV
with open('table_a.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['StudentId', 'Name', 'DOB'])
    writer.writerows(table_a)

# Generate Table B (StudentId, CourseId, Grade)
table_b = []
for i in range(1, 101):  # Each student has 1-3 courses
    num_courses = random.randint(1, 3)
    for _ in range(num_courses):
        table_b.append([i, random.choice(course_ids), round(random.uniform(60.0, 100.0), 1)])

# Write Table B to CSV
with open('table_b.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['StudentId', 'CourseId', 'Grade'])
    writer.writerows(table_b)