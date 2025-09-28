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
#!/usr/bin/env python3
"""Basic Data Analysis Script"""

def load_students(filename):
    """Load student data from CSV."""
    # TODO: Open file, read lines, skip header
    # TODO: Split each line by comma
    # TODO: Return list of student data
    pass

def calculate_average_grade(students):
    """Calculate average grade."""
    # TODO: Sum all grades
    # TODO: Divide by number of students
    pass

def count_math_students(students):
    """Count students in Math."""
    # TODO: Count students where subject is Math
    pass

def generate_report(total, average, math_count):
    """Generate report string."""
    # TODO: Create formatted string with results
    # TODO: Use f-strings with .1f for decimals
    pass

def save_report(report, filename):
    """Save report to file."""
    # TODO: Create output directory if needed
    # TODO: Write report to file
    pass

def main():
    # TODO: Load data
    # TODO: Calculate statistics
    # TODO: Generate and save report
    pass

if __name__ == "__main__":
    main()
EOF

# Create data_analysis_functions.py template
cat > src/data_analysis_functions.py << 'EOF'
#!/usr/bin/env python3
"""Advanced Data Analysis with Functions"""

def load_data(filename):
    """Load data from CSV file."""
    # TODO: Check file extension
    # TODO: Call appropriate loader
    pass

def load_csv(filename):
    """Load CSV data."""
    # TODO: Same technique as basic script
    pass

def analyze_data(students):
    """Analyze student data."""
    # TODO: Calculate multiple statistics
    # TODO: Return dictionary of results
    pass

def analyze_grade_distribution(grades):
    """Count grades by letter grade."""
    # TODO: Count A (90-100), B (80-89), etc.
    pass

def save_results(results, filename):
    """Save detailed results."""
    # TODO: Format and write comprehensive report
    pass

def main():
    # TODO: Orchestrate the analysis
    pass

if __name__ == "__main__":
    main()
EOF

echo "Python template files created in src/ directory."

echo "Setup complete!"