import numpy as np
import skfuzzy as fuzz
from sklearn.mixture import GaussianMixture
import pickle

def recommend_teaching_and_learning_style(cluster, learning_ability):
    # Advanced fuzzy logic-based recommendations based on clusters
    recommendations = {
        0: {
            "teaching_style": ["Direct Instruction", "Problem Solving", "Demonstration"],
            "learning_style": ["Active", "Kinesthetic", "Concrete"]
        },
        1: {
            "teaching_style": ["Inquiry-Based", "Socratic Method", "Facilitator"],
            "learning_style": ["Reflective", "Visual", "Field-Independent"]
        },
        2: {
            "teaching_style": ["Cooperative Learning", "Peer Tutoring", "Discussion"],
            "learning_style": ["Auditory", "Global", "Abstract"]
        },
        3: {
            "teaching_style": ["Project-Based Learning", "Experiential Learning", "Facilitator"],
            "learning_style": ["Intuitive", "Sequential", "Active"]
        },
        4: {
            "teaching_style": ["Traditional Lecture", "Expert Instruction", "Didactic"],
            "learning_style": ["Tactile", "Field-Dependent", "Concrete"]
        },
        5: {
            "teaching_style": ["Problem-Based Learning", "Hands-On Activities", "Simulation"],
            "learning_style": ["Visual-Spatial", "Collaborative", "Critical Thinker"]
        }
    }

    # Define fuzzy membership functions for confidence levels
    x_ability = np.arange(0, 1.1, 0.1)  # Ranges from 0.0 to 1.0 in steps of 0.1
    low_ability = fuzz.trimf(x_ability, [0.0, 0.0, 0.5])
    medium_ability = fuzz.trimf(x_ability, [0.3, 0.5, 0.7])
    high_ability = fuzz.trimf(x_ability, [0.5, 1.0, 1.0])

    # Normalize `learning_ability` to [0, 1] for fuzzy evaluation
    if learning_ability == 0:
        fuzzy_value = fuzz.interp_membership(x_ability, low_ability, 0.0)
    elif learning_ability == 0.5:
        fuzzy_value = fuzz.interp_membership(x_ability, medium_ability, 0.5)
    else:
        fuzzy_value = fuzz.interp_membership(x_ability, high_ability, 1.0)

    # Get the recommended styles based on the cluster
    recommended_styles = recommendations.get(cluster, {
        "teaching_style": ["General"],
        "learning_style": ["General"]
    })
    confidence = fuzzy_value  # Use the calculated fuzzy value as the confidence

    return {
        "teaching_style": recommended_styles["teaching_style"],
        "learning_style": recommended_styles["learning_style"],
        "confidence": confidence
    }
