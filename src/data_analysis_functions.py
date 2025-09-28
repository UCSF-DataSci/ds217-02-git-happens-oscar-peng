#!/usr/bin/env python3
"""Advanced Data Analysis with Functions"""

def load_data(filename):
    """Load data from CSV file."""
    # TODO: Check file extension
    # TODO: Call appropriate loader
    if not filename.endswith('.csv'):
        raise ValueError("Unsupported file format. Please provide a CSV file.")

    return load_csv(filename)

def load_csv(filename):
    """Load CSV data."""
    # TODO: Same technique as basic script
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

def analyze_data(students):
    """Analyze student data."""
    # TODO: Calculate multiple statistics
    # TODO: Count students by subject
    # TODO: Return dictionary of results
    results = {}
    if not students:
        return results
    grades = [student['grade'] for student in students]
    results['num_students'] = len(students)
    results['average'] = sum(grades) / len(grades)
    results['max'] = max(grades)
    results['min'] = min(grades)
    results['grade_distribution'] = analyze_grade_distribution(grades)

    math_subject_counts = {}
    math_students = [student for student in students if student['subject'] == 'Math']
    math_subject_counts['Math'] = len(math_students)
    results['math_subject_counts'] = math_subject_counts

    science_subject_counts = {}
    science_students = [student for student in students if student['subject'] == 'Science']
    science_subject_counts['Science'] = len(science_students)
    results['science_subject_counts'] = science_subject_counts

    history_subject_counts = {}
    history_students = [student for student in students if student['subject'] == 'History']
    history_subject_counts['History'] = len(history_students)
    results['history_subject_counts'] = history_subject_counts
    return results

def analyze_grade_distribution(grades):
    """Count grades by letter grade."""
    # TODO: Count A (90-100), B (80-89), etc.
    if not grades:
        return {}
    
    # Count grades by ranges
    distribution = {
        'A (90-100)': 0,
        'B (80-89)': 0,
        'C (70-79)': 0,
        'D (60-69)': 0,
        'F (0-59)': 0
    }
    
    for grade in grades:
        if grade >= 90:
            distribution['A (90-100)'] += 1
        elif grade >= 80:
            distribution['B (80-89)'] += 1
        elif grade >= 70:
            distribution['C (70-79)'] += 1
        elif grade >= 60:
            distribution['D (60-69)'] += 1
        else:
            distribution['F (0-59)'] += 1
    
    return distribution

def save_results(results, filename):
    """Save detailed results."""
    # TODO: Format and write comprehensive report
    with open(filename, 'w') as file:
        file.write("Student Data Analysis Report\n")
        file.write("============================\n")
        file.write(f"Basic Analytics:\n")
        file.write(f"Average Grade: {results['average']:.1f}\n")
        file.write(f"Highest Grade: {results['max']}\n")
        file.write(f"Lowest Grade: {results['min']}\n")
        file.write(f"Total Students: {results['num_students']}\n\n")
        file.write("Grade Distribution:\n")
        for grade_range, count in results['grade_distribution'].items():
            file.write(f"{grade_range}: {count}\n")
        file.write("\nStudents by Subject:\n")
        for subject, count in results['math_subject_counts'].items():
            file.write(f"{subject}: {count}\n")
        for subject, count in results['science_subject_counts'].items():
            file.write(f"{subject}: {count}\n")
        for subject, count in results['history_subject_counts'].items():
            file.write(f"{subject}: {count}\n")

def main():
    # TODO: Orchestrate the analysis
    students = load_data('data/students.csv')
    results = analyze_data(students)
    save_results(results, 'output/advanced_analysis_report.txt')

if __name__ == "__main__":
    main()