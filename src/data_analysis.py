#!/usr/bin/env python3
"""Basic Data Analysis Script"""

import os

def load_students(filename):
    """Load student data from CSV."""
    # TODO: Open file, read lines, skip header
    # TODO: Split each line by comma
    # TODO: Return list of student data
    students = []
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
        
            # Skip the header line
            for line in lines[1:]:
                # Split CSV line and strip whitespace
                data = line.strip().split(',')
            
                # Create student dictionary
                student = {
                    'name': data[0],
                    'age': int(data[1]),
                    'grade': int(data[2]),
                    'subject': data[3]
                }
                students.append(student)

    except FileNotFoundError:
        print(f"Error: File {filename} not found.")
    except Exception as e:
        print(f"Error reading {filename}: {e}")
    
    return students

'''
# Example usage
# print(load_students('data/students.csv'))
'''

def calculate_average_grade(students):
    """Calculate average grade."""
    # TODO: Sum all grades
    # TODO: Divide by number of students
    total_grade = sum(student['grade'] for student in students)
    average = total_grade / len(students) if students else 0
    return average

'''
# Example usage
print(calculate_average_grade(load_students('data/students.csv')))
'''

def count_math_students(students):
    """Count students in Math."""
    # TODO: Count students where subject is Math
    math_students = [student for student in students if student['subject'] == 'Math']
    return len(math_students)

'''
# Example usage
print(count_math_students(load_students('data/students.csv')))
'''

def generate_report(total, average, math_count):
    """Generate report string."""
    # TODO: Create formatted string with results
    # TODO: Use f-strings with .1f for decimals
    report = (
        f"Total Students: {total}\n"
        f"Average Grade: {average:.1f}\n"
        f"Math Students: {math_count}\n"
    )
    return report

'''
# Example usage
students = load_students('data/students.csv')
total = len(students)
average = calculate_average_grade(students)
math_count = count_math_students(students)
print(generate_report(total, average, math_count))
'''

def save_report(report, filename):
    """Save report to file."""
    # TODO: Create output directory if needed
    # TODO: Write report to file
    if not os.path.exists('output'):
        os.makedirs('output')

    with open(filename, 'w') as file:
        file.write("Basic Data Analysis\n")
        file.write("=" * 30 + "\n")
        file.write(report)

    print(f"Report saved to {filename}")

'''
# Example usage
students = load_students('data/students.csv')
total = len(students)
average = calculate_average_grade(students)
math_count = count_math_students(students)
report = generate_report(total, average, math_count)
save_report(report, 'output/analysis_report.txt')
'''

def main():
    # TODO: Load data
    # TODO: Calculate statistics
    # TODO: Generate and save report
    students = load_students('data/students.csv')
    total = len(students)
    average = calculate_average_grade(students)
    math_count = count_math_students(students)
    report = generate_report(total, average, math_count)
    save_report(report, 'output/analysis_report.txt')

if __name__ == "__main__":
    main()