import tkinter as tk
from tkinter import ttk
from api_manager import API_Manager


data = API_Manager.filtered_exercises

def select_muscle_group(event):
    """return all available muscle groups in dropdown menu"""


def select_difficulty(event):
    """return all difficulty levels in dropdown menu"""


def get_exercises():
    """return all exercises matching the criteria and
    the instructions for all of them"""





window = tk.Tk()
window.title("FitnessProgram")

target_muscle = tk.StringVar(window)
mg_menu = ttk.Combobox(window, textvariable=target_muscle, values=muscles)
mg_menu.grid(row=0, column=0, padx=10, pady=10)

difficulty_level = tk.StringVar(window)
d_menu = ttk.Combobox(window, textvariable=difficulty_level, values=difficulty)
d_menu.grid(row=0, column=0, padx=10, pady=10)

get_instructions = tk.Button(window, text="Start training", command=get_exercises)
get_instructions.grid(row=1, column=0, columnspan=2, padx=10, pady=10)


window.mainloop()


