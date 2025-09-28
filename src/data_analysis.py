"""
Basic Analysis Script - src/data_analysis.py
Read CSV file line by line and calculate basic statistics
"""
import os

def load_students(filename):
    """
    Read CSV and return list of student data
    """
    students = []
    
    with open(filename, 'r') as file:
        lines = file.readlines()
        
        # Skipping the header line index = 0
        for line in lines[1:]:
            # Split CSV line and strip whitespace
            data = line.strip().split(',')

            # Convert age and grade to integers and create student dictionary
            student = {
                'name': data[0],
                'age': int(data[1]),
                'grade': int(data[2]),
                'subject': data[3]
            }
            students.append(student)
    
    return students

def calculate_average_grade(students):
    """
    Calculate and return average grade
    """
    if not students:
        return 0.0
    
    total_grade = sum(student['grade'] for student in students)
    return total_grade / len(students)

def count_math_students(students):
    """
    Count students in Math subject
    """
    count = 0
    for student in students:
        if student['subject'] == 'Math':
            count += 1
    return count

def generate_report():
    """
    Create formatted report string
    """
    # Load student data
    students = load_students('data/students.csv')
    
    # Calculate total students
    total_students = len(students)
    
    # Calculate average grade
    average_grade = calculate_average_grade(students)
    
    # Count math students
    math_students = count_math_students(students)
    
    # Count students by all subjects
    subject_counts = {}
    for student in students:
        subject = student['subject']
        if subject in subject_counts:
            subject_counts[subject] += 1
        else:
            subject_counts[subject] = 1
    
    # Format report string using f-strings
    report = "BASIC DATA ANALYSIS REPORT\n"
    report += "=" * 30 + "\n\n"
    
    report += f"Total number of students: {total_students}\n"
    report += f"Average grade: {average_grade:.1f}\n\n"
    
    report += "Subject counts:\n"
    for subject, count in subject_counts.items():
        report += f"  {subject}: {count} students\n"
    
    report += f"\nMath students specifically: {math_students}\n"
    
    return report

def save_report(report, filename):
    """
    Write report to file
    """
    # Create output directory if it doesn't exist
    if not os.path.exists('output'):
        os.makedirs('output')

    # Open file for writing and write report string
    with open(filename, 'w') as file:
        file.write(report)

def main():
    """
    Orchestrate the analysis
    """
    print("Starting basic data analysis...")
    
    # Generate report
    report = generate_report()
        
    # Save report
    save_report(report, 'output/analysis_report.txt')
        
    # Print completion message
    print("Analysis complete! Results saved to output/analysis_report.txt")
    print("\nReport Preview:")
    print("-" * 40)
    print(report)

if __name__ == "__main__":
    main()
