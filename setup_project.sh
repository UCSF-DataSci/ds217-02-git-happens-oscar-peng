#!/bin/bash
# Create project strucutre
echo "Setting up project structure..."
mkdir -p src data output 
echo "Project structure created."

# Create .gitignore file
cat > .gitignore << 'EOF'
# Python cache files
__pycache__/
*.pyc

# Data and secrets
data/
output/
.env
*.key

# IDE files
.vscode/
.idea/
EOF
echo ".gitignore created."

# Create requirements.txt file
cat > requirements.txt << 'EOF'
# DataSci 217 - Lecture 02 Assignment Requirements
# Git Workflow, CLI Automation, and Python Data Processing

# Core Python packages (built-in, no external dependencies required)
# This assignment focuses on fundamental Python concepts and file I/O

# Testing framework
pytest>=7.0.0

# Optional: For enhanced development experience
# pathlib (built-in since Python 3.4)
# json (built-in)
# csv (built-in)
# subprocess (built-in)
# os (built-in)
# sys (built-in)

# Note: This assignment is designed to use only Python standard library
# to focus on core programming concepts without external dependencies
EOF
echo "requirements.txt created."

# Create students.csv in the data directory (NOT root directory)
echo "Creating students.csv in data directory..."
cat > data/students.csv << 'EOF'
name,age,grade,subject
Alice,20,85,Math
John,22,90,Science
Bob,19,92,History
Elena,21,88,Math
Diana,20,95,Science
Dylan,23,80,History
Jim,22,78,Math
Jason,21,85,Science
Kate,20,89,History
EOF
echo "students.csv created in data/ directory."

# Create data_analysis.py template
echo "Creating Python template files..."
cat > src/data_analysis.py << 'EOF'
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
EOF

# Create data_analysis_functions.py template
cat > src/data_analysis_functions.py << 'EOF'
"""
Advanced Analysis Script - src/data_analysis_functions.py
Modular design with comprehensive analysis functions
"""
import os

def load_data(filename):
    """
    Generic loader that checks file extension
    
    Args:
        filename (str): Path to data file
        
    Returns:
        list: Loaded data
    """
    # TODO: Check if filename ends with '.csv'
    # TODO: If CSV, call load_csv() function
    # TODO: If not CSV, raise ValueError with unsupported file type message
    # TODO: Return loaded data
    pass

def load_csv(filename):
    """
    Load CSV data using same technique as basic script
    
    Args:
        filename (str): Path to CSV file
        
    Returns:
        list: List of student records as dictionaries
    """
    # TODO: Read the CSV file line by line using open() and readlines()
    # TODO: Skip header line using lines[1:]
    # TODO: Split each line using line.strip().split(',')
    # TODO: Convert age and grade to integers using int()
    # TODO: Create student dictionaries with name, age, grade, subject
    # TODO: Return list of student dictionaries
    pass

def analyze_data(students):
    """
    Return dictionary with multiple statistics
    
    Args:
        students (list): List of student data
        
    Returns:
        dict: Dictionary containing various statistics
    """
    # TODO: Handle empty students list case
    # TODO: Extract grades list from students using list comprehension
    # TODO: Calculate total students using len()
    # TODO: Calculate average grade using sum() and len()
    # TODO: Calculate highest grade using max()
    # TODO: Calculate lowest grade using min()
    # TODO: Count students by subject using dictionary or loop
    # TODO: Get grade distribution using analyze_grade_distribution()
    # TODO: Return dictionary with all statistics
    pass

def analyze_grade_distribution(grades):
    """
    Count grades by letter grade ranges
    
    Args:
        grades (list): List of numeric grades
        
    Returns:
        dict: Grade distribution counts and percentages
    """
    # TODO: Initialize grade range counters for A, B, C, D, F
    # TODO: Create grade ranges: A (90-100), B (80-89), C (70-79), D (60-69), F (0-59)
    # TODO: Loop through grades and count each range
    # TODO: Use if/elif statements to categorize grades
    # TODO: Calculate total number of grades
    # TODO: Calculate percentages for each grade range
    # TODO: Use .1f formatting for percentages
    # TODO: Return dictionary with counts and percentages
    pass

def save_results(results, filename):
    """
    Save detailed report
    
    Args:
        results (dict): Analysis results
        filename (str): Output filename
    """
    # TODO: Create output directory if needed using os.makedirs()
    # TODO: Format comprehensive report string
    # TODO: Include total students, average grade, highest/lowest grades
    # TODO: Include subject distribution with counts and percentages
    # TODO: Include grade distribution with counts and percentages
    # TODO: Use f-strings with .1f formatting for decimal numbers
    # TODO: Write formatted report to file
    pass

def main():
    """
    Orchestrate the analysis using all functions
    """
    print("Starting advanced data analysis...")
    
    # TODO: Load data using load_data() function
    # TODO: Print number of loaded records
    # TODO: Analyze data using analyze_data() function
    # TODO: Print analysis complete message
    # TODO: Save results using save_results() function
    # TODO: Print completion message with filename
    # TODO: Print summary statistics (total, average, grade range, subjects)
    # TODO: Add error handling with try/except for FileNotFoundError
    # TODO: Add general exception handling

if __name__ == "__main__":
    main()
EOF

echo "Python template files created in src/ directory."

echo "Setup complete!"