from api_manager import API_Manager

if __name__ == "__main__":
    target_muscle = input("Enter the target muscle group: ")
    difficulty_level = input("Enter the difficulty level: ")
    API_Manager.get_exercise_data(target_muscle, difficulty_level)
