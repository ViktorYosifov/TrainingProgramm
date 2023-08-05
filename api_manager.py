import requests
import json

with open("config.json") as conf:
    API_KEY = json.load(conf)["api_key"]


class API_Manager:
    @staticmethod
    def get_exercise_data(target_muscle, difficulty_level=None):
        api_url = "https://exercises-by-api-ninjas.p.rapidapi.com/v1/exercises"
        headers = {
            "X-RapidAPI-Key": API_KEY,
            "X-RapidAPI-Host": "exercises-by-api-ninjas.p.rapidapi.com",
        }
        if difficulty_level:
            params = {"muscle": target_muscle, "difficulty": difficulty_level}
        else:
            params = {"muscle": target_muscle}
        try:
            response = requests.get(api_url, headers=headers, params=params)
            response.raise_for_status()
            exercises_data = response.json()
        except requests.exceptions.RequestException as e:
            print(f"Failed to fetch data from the API. Error: {e}")
            return

        return exercises_data if exercises_data else None

    @staticmethod
    def get_image(query):
        url = f"https://unsplash.com/napi/search/photos?per_page=20&page=1&query={query}"

        payload = ""
        headers = {
            'Cookie': 'require_cookie_consent=false'
        }

        response = requests.request("GET", url, headers=headers, data=payload).json()
        image_url = response['results'][0]['urls']['raw']
        return image_url

    @staticmethod
    def return_html(target_muscle, difficulty_level):
        output = ""
        json_ = API_Manager.get_exercise_data(target_muscle, difficulty_level)
        for exercise in json_:
            output += f"<h1> Exercise: {exercise['name']} </h1>\n"
            url = API_Manager.get_image(exercise['name'])
            output += f"<img src=\"{url}\" alt=\"Italian Trulli\" style=\"width: 25%;\">"

            output += f"<p>Muscle group: {exercise['muscle']}, "
            output += f"Difficulty: {exercise['difficulty']} </p>"
            output += f"<p> Instructions: {exercise['instructions']} </p>"
            output += "<p>" + ("-" * 40) + "</p>"
            output += "<br>"

        with open(f"{target_muscle}_{difficulty_level}.html", "w") as file:
            file.write(output)


if __name__ == "__main__":
    API_Manager.return_html('biceps', 'beginner')
