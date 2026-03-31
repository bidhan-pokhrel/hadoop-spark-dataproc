import sys
from datetime import datetime

def mapper():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        # Split the line based on CSV format
        fields = line.split(',')

        # Determine if the input is from table_a or table_b based on number of fields
        if len(fields) == 3 and fields[0] != 'StudentId':  # table_a: StudentId,Name,DOB
            student_id, name, dob = fields
            try:
                # Validate DOB format
                datetime.strptime(dob, '%Y-%m-%d')
                print(f"{student_id}\tA\t{name}\t{dob}")
            except ValueError:
                continue  # Skip invalid DOB
        elif len(fields) == 3 and fields[0] != 'StudentId':  # table_b: StudentId,CourseId,Grade
            student_id, course_id, grade = fields
            try:
                float(grade)  # Validate grade
                print(f"{student_id}\tB\t{course_id}\t{grade}")
            except ValueError:
                continue  # Skip invalid grade

if __name__ == "__main__":
    mapper()