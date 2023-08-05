import tkinter as tk
from tkinter import ttk, messagebox
from api_manager import API_Manager

muscles = [
    "abdominals",
    "abductors",
    "adductors",
    "biceps",
    "calves",
    "chest",
    "forearms",
    "glutes",
    "hamstrings",
    "lats",
    "lower_back",
    "middle_back",
    "neck",
    "quadriceps",
    "traps",
    "triceps",
]

difficulty = [
    "-",
    "beginner",
    "intermediate",
    "expert",
]

def get_exercises():
    """return all exercises matching the criteria and
    the instructions for all of them"""
    try:
        API_Manager.return_html(target_muscle.get(), difficulty_level.get() if difficulty_level.get() != "-" else None)
        messagebox.showinfo(title="Result", message="Done!")

    except:
        messagebox.showinfo(title="Result", message="Such exercise does not exist")


window = tk.Tk()
window.title("FitnessProgram")

tk.Label(window,
         text="Muscle Group").grid(row=10, column=2, padx=60, pady=1)

target_muscle = tk.StringVar(window)
mg_menu = ttk.Combobox(window, textvariable=target_muscle, values=muscles)
mg_menu.grid(row=20, column=2, padx=60, pady=10)

tk.Label(window,
         text="Difficulty").grid(row=25, column=2, padx=60, pady=1)
difficulty_level = tk.StringVar(window)
d_menu = ttk.Combobox(window, textvariable=difficulty_level, values=difficulty)
d_menu.grid(row=30, column=2, padx=60, pady=10)

get_instructions = tk.Button(window, text="Start training", command=get_exercises)
get_instructions.grid(row=40, column=2, columnspan=2, padx=60, pady=10)


window.mainloop()
