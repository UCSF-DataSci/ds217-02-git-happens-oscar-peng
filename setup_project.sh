#!/bin/bash
# Create project strucutre
echo "Setting up project structure..."
mkdir -p src data output 
echo "Project structure created."

# Make script executable
chmod +x setup_project.sh
echo "Script made executable."

# Create .gitignore file
cat > .gitignore << 'EOF'
# Python cache files
__pycache__/
*.pyc

# Data and secrets
data/*.csv
.env
*.key

# IDE files
.vscode/
.idea/

# Track important files
!data/processed/important_results.csv
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

EOF

# Create data_analysis_functions.py template
cat > src/data_analysis_functions.py << 'EOF'

EOF

echo "Python template files created in src/ directory."

echo "Setup complete!"