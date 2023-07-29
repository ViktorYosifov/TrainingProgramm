import requests
import json

with open("config.json") as conf:
	API_KEY = json.load(conf)['api_key']

class API_Manager:

	@staticmethod
	def get_exercise_data():

		api_url = "https://exercises-by-api-ninjas.p.rapidapi.com/v1/exercises"
		headers = {'Authorization': f'Bearer {API_KEY}'}

		target_muscle = input("Enter the target muscle group: ")
		difficulty_level = input("Enter the difficulty level: ")

		params = {
			'muscle': target_muscle,
			'difficulty': difficulty_level
		}
		try:
			response = requests.get(api_url, headers=headers, params=params)
			response.raise_for_status()
			exercises_data = response.json()
		except requests.exceptions.RequestException as e:
			print(f"Failed to fetch data from the API. Error: {e}")
			exit()


		filtered_exercises = []
		for exercise in exercises_data:
			if exercise.get('muscle', '').lower() == target_muscle.lower() and exercise.get('difficulty', '').lower() == difficulty_level.lower():
				filtered_exercises.append(exercise)

		if filtered_exercises:
			print("Exercises for you: ")
			for exercise in filtered_exercises:
				print(f"Exercise: {exercise['name']}")
				print(f"Muscle group: {exercise['muscle']}")
				print(f"Difficulty: {exercise['difficulty']}")
				print(f"Instructions: {exercise['instructions']}")
				print("-" * 40)
		else:
			print("We don't have such an exercise.Sorry!")





