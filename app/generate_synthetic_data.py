import pandas as pd
import random

def generate_synthetic_data(n_rows=4000):
    # Subjects from the feeder documents
    subjects = [
        "Thermodynamics", "Fluid Mechanics", "Heat Transfer", "Manufacturing Processes",
        "Machine Design", "Mechanics of Materials", "Computer-Aided Design (CAD)", 
        "Control Systems", "Mechatronics", "Engineering Mechanics"
    ]
    
    # Teaching styles from the feeder document
    teaching_styles = [
        "Direct Teaching", "Indirect Teaching", "Discipline-Centered", "Teacher-Centered", 
        "Student-Centered", "Peer Teaching", "Problem Solving", "Group Approach",
        "Socratic", "Didactic", "Facilitative", "Expert", "Formal Authority",
        "Personal Model", "Facilitator", "Delegator", "Conservative", "Global",
        "Legislative", "Local", "Judicial", "Liberal", "Executive"
    ]
    
    # Learning styles from the feeder document
    learning_styles = [
        "Visual", "Auditory", "Kinesthetic", "Tactile", "Field-Independent",
        "Field-Dependent", "Reflective", "Impulsive", "Concrete", "Abstract", 
        "Sequential", "Global", "Active", "Intuitive"
    ]
    
    # Additional characteristics
    characteristics = ["Design-oriented", "Analytical", "Experimental"]
    lab_subject_options = ["Yes", "No"]
    subject_types = ["Core", "Elective"]
    requirements = ["Theoretical", "Lab"]  
    learning_abilities = ["High", "Medium", "Low"]
    backgrounds = ["UG", "PG", "PhD"]
    lab_facility_options = ["Available", "Not Available"]

    data = []
    for _ in range(n_rows):
        row = {
            "Subject Name": random.choice(subjects),
            "Characteristics": random.choice(characteristics),
            "Lab Subject": random.choice(lab_subject_options),
            "Type of Subject": random.choice(subject_types),
            "Duration": random.randint(1, 5) * 10,  # Duration in hours
            "Requirements": random.choice(requirements),
            "Learning Background": random.choice(backgrounds),
            "Learning Style": random.choice(learning_styles),
            "Learning Ability": random.choice(learning_abilities),
            "Teacher Experience": random.choice(["New", "Intermediate", "Experienced"]),
            "Teaching Pattern": random.choice(teaching_styles),
            "Lab Facility": random.choice(lab_facility_options)
        }
        data.append(row)

    df = pd.DataFrame(data)
    df.to_csv("data/synthetic_teaching_data.csv", index=False)
    print("Synthetic data generated and saved to data/synthetic_teaching_data.csv")

# Run the script
if __name__ == "__main__":
    generate_synthetic_data()
