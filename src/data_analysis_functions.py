"""
Advanced Analysis Script - src/data_analysis_functions.py
Modular design with comprehensive analysis functions
"""
import os

def load_data(filename):
    """
    Generic loader that checks file extension
    """
    if filename.endswith('.csv'):
        return load_csv(filename)
    else:
        raise ValueError(f"Unsupported file type: {filename}")

def load_csv(filename):
    """
    Load CSV data using same technique as basic script
    """
    students = []
    
    with open(filename, 'r') as file:
        lines = file.readlines()
        
        # Skip header line
        for line in lines[1:]:
            # Split each line and strip whitespace
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

def analyze_data(students):
    """
    Return dictionary with multiple statistics
    """
    if not students:
        return {}
    
    # Extract grades list using list comprehension
    grades = [student['grade'] for student in students]
    
    # Calculate total students
    total_students = len(students)
    
    # Calculate average grade
    average_grade = sum(grades) / len(grades)
    
    # Calculate highest and lowest grades
    highest_grade = max(grades)
    lowest_grade = min(grades)
    
    # Count students by subject using dictionary
    subject_counts = {}
    for student in students:
        subject = student['subject']
        if subject in subject_counts:
            subject_counts[subject] += 1
        else:
            subject_counts[subject] = 1
    
    # Get grade distribution
    grade_distribution = analyze_grade_distribution(grades)
    
    # Return dictionary with all statistics
    return {
        'total_students': total_students,
        'average_grade': average_grade,
        'highest_grade': highest_grade,
        'lowest_grade': lowest_grade,
        'subject_counts': subject_counts,
        'grade_distribution': grade_distribution
    }

def analyze_grade_distribution(grades):
    """
    Count grades by letter grade ranges
    """
    # Initialize grade range counters
    grade_ranges = {
        'A (90-100)': 0,
        'B (80-89)': 0,
        'C (70-79)': 0,
        'D (60-69)': 0,
        'F (0-59)': 0
    }
    
    # Loop through grades and count each range using if/elif statements
    for grade in grades:
        if grade >= 90:
            grade_ranges['A (90-100)'] += 1
        elif grade >= 80:
            grade_ranges['B (80-89)'] += 1
        elif grade >= 70:
            grade_ranges['C (70-79)'] += 1
        elif grade >= 60:
            grade_ranges['D (60-69)'] += 1
        else:
            grade_ranges['F (0-59)'] += 1
    
    # Calculate total number of grades
    total_grades = len(grades)
    
    # Calculate percentages for each grade range and use .1f formatting
    distribution = {}
    for grade_range, count in grade_ranges.items():
        percentage = (count / total_grades) * 100 if total_grades > 0 else 0
        distribution[grade_range] = {
            'count': count,
            'percentage': percentage
        }
    
    return distribution

def save_results(results, filename):
    """
    Save detailed report
    """
    # Create output directory if needed
    output_dir = os.path.dirname(filename)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Format comprehensive report string
    report = "ADVANCED DATA ANALYSIS REPORT\n"
    report += "=" * 35 + "\n\n"
    
    # Include total students, average grade, highest/lowest grades
    report += f"Total number of students: {results['total_students']}\n"
    report += f"Average grade: {results['average_grade']:.1f}\n"
    report += f"Highest grade: {results['highest_grade']}\n"
    report += f"Lowest grade: {results['lowest_grade']}\n\n"
    
    # Include subject distribution with counts and percentages
    report += "Subject counts:\n"
    for subject, count in results['subject_counts'].items():
        percentage = (count / results['total_students']) * 100
        report += f"  {subject}: {count} students ({percentage:.1f}%)\n"
    
    # Include grade distribution with counts and percentages using .1f formatting
    report += "\nGrade Distribution:\n"
    for grade_range, data in results['grade_distribution'].items():
        report += f"  {grade_range}: {data['count']} students ({data['percentage']:.1f}%)\n"
    
    # Write formatted report to file
    with open(filename, 'w') as file:
        file.write(report)

def main():
    """
    Orchestrate the analysis using all functions
    """
    print("Starting advanced data analysis:")
    
    try:
        # Load data using load_data() function
        students = load_data('data/students.csv')
        
        # Print number of loaded records
        print(f"Loaded {len(students)} student records")
        
        # Analyze data using analyze_data() function
        results = analyze_data(students)
        
        # Print analysis complete message
        print("Analysis complete")
        
        # Save results using save_results() function
        save_results(results, 'output/analysis_report.txt')
        
        # Print completion message with filename
        print("Advanced analysis complete! Results saved to output/analysis_report.txt")
        
        # Print summary statistics
        print(f"\nSummary:")
        print(f"- Total students: {results['total_students']}")
        print(f"- Average grade: {results['average_grade']:.1f}")
        print(f"- Grade range: {results['lowest_grade']} - {results['highest_grade']}")
        print(f"- Subjects analyzed: {len(results['subject_counts'])}")
        
    except FileNotFoundError as e:
        print(f"Error: Could not find data file. {e}")
    except Exception as e:
        print(f"Error during analysis: {e}")

if __name__ == "__main__":
    main()
