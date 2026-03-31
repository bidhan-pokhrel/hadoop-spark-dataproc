import sys
from datetime import datetime

def reducer():
    current_student_id = None
    table_a_records = []
    table_b_records = []

    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        # Parse the mapper output
        fields = line.split('\t')
        if len(fields) != 4:
            continue

        student_id, table_type, field1, field2 = fields

        # Group records by student_id
        if current_student_id is None:
            current_student_id = student_id

        if student_id != current_student_id:
            # Process the previous group
            process_group(current_student_id, table_a_records, table_b_records)
            # Reset for the new student_id
            table_a_records = []
            table_b_records = []
            current_student_id = student_id

        # Store records based on table type
        if table_type == 'A':
            table_a_records.append((field1, field2))  # (Name, DOB)
        elif table_type == 'B':
            table_b_records.append((field1, field2))  # (CourseId, Grade)

    # Process the last group
    if current_student_id:
        process_group(current_student_id, table_a_records, table_b_records)

def process_group(student_id, table_a_records, table_b_records):
    # Filter table_a records where DOB >= 1995-01-01
    cutoff_date = datetime(1995, 1, 1)
    valid_a_records = []
    for name, dob in table_a_records:
        try:
            dob_date = datetime.strptime(dob, '%Y-%m-%d')
            if dob_date >= cutoff_date:
                valid_a_records.append(name)
        except ValueError:
            continue

    # Perform the join
    for name in valid_a_records:
        for course_id, grade in table_b_records:
            print(f"{student_id},{name},{course_id},{grade}")

if __name__ == "__main__":
    reducer()