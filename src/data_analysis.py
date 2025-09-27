"""
Basic Analysis Script - src/data_analysis.py
Read CSV file line by line and calculate basic statistics
"""
import os

def load_students(filename):
    """
    Read CSV and return list of student data
    
    Args:
        filename (str): Path to CSV file
        
    Returns:
        list: List of student records as dictionaries
    """
    # TODO: Read the CSV file line by line using open() and readlines()
    # TODO: Skip the header line when reading CSV: lines[1:]
    # TODO: Split CSV lines: line.strip().split(',')
    # TODO: Convert strings to integers: int(value)
    # TODO: Create student dictionaries with name, age, grade, subject
    # TODO: Return list of student data
    pass

def calculate_average_grade(students):
    """
    Calculate and return average grade
    
    Args:
        students (list): List of student data
        
    Returns:
        float: Average grade
    """
    # TODO: Calculate sum of all grades
    # TODO: Divide by number of students
    # TODO: Handle empty list case
    pass

def count_math_students(students):
    """
    Count students in Math subject
    
    Args:
        students (list): List of student data
        
    Returns:
        int: Number of math students
    """
    # TODO: Count students where subject is "Math"
    # TODO: Return the count
    pass

def generate_report():
    """
    Create formatted report string
    
    Returns:
        str: Formatted analysis report
    """
    # TODO: Load student data using load_students()
    # TODO: Calculate total students using len()
    # TODO: Calculate average grade using calculate_average_grade()
    # TODO: Count math students using count_math_students()
    # TODO: Count students by all subjects using a loop or dictionary
    # TODO: Format report string with f-strings
    # TODO: Use .1f formatting for decimal numbers
    # TODO: Return formatted report
    pass

def save_report(report, filename):
    """
    Write report to file
    
    Args:
        report (str): Report content
        filename (str): Output filename
    """
    # TODO: Create output directory if it doesn't exist using os.makedirs()
    # TODO: Open file for writing
    # TODO: Write report string to file
    pass

def main():
    """
    Orchestrate the analysis
    """
    print("Starting basic data analysis...")
    
    # TODO: Generate report using generate_report()
    # TODO: Save report using save_report()
    # TODO: Print completion message
    # TODO: Add error handling with try/except

if __name__ == "__main__":
    main()
