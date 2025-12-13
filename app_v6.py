"""Module providing a function printing python version."""

import random


class Shrine:
    def __init__(self):
        self.cleanliness_score = 0
        self.spirit_energy = 0

    def load_progress(self):
        try:
            with open("save_data.txt", "r") as file:
                data = file.read()
                values = data.split(",")
                self.cleanliness_score = int(values[0])
                self.spirit_energy = int(values[1])

        except (FileNotFoundError, ValueError, IndexError):
            self.cleanliness_score = 0
            self.spirit_energy = 0

    def clean(self):
        self.cleanliness_score += 5
        print("You swept the dusty floors. The shrine brightens!")

    def meditate(self):
        roll = random.randint(1, 10)

        if roll > 5:
            self.spirit_energy += 10
            print("You sit in silence. Your spirit strengthens.")

        else:
            print("You fell asleep!")

    def save_progress(self):
        with open("save_data.txt", "w") as file:
            file.write(f"{self.cleanliness_score}, {self.spirit_energy}")


def intro():
    caretaker_name = input("Who approaches the shrine? ")
    print(f"Welcome, Caretaker {caretaker_name}")
    return caretaker_name


def shrine_adventure(caretaker_name):
    my_shrine = Shrine()

    my_shrine.load_progress()

    print(f"Current Shrine Cleanliness: {my_shrine.cleanliness_score}")
    print(f"Current Spirit Strength: {my_shrine.spirit_energy}")

    game_running = True

    while game_running == True:
        task = input("What task would you like to perform? ").lower()

        if task == "clean":
            my_shrine.clean()

            if my_shrine.cleanliness_score >= 20:
                print("The shrine is pure! The spirits are at peace.")
                game_running = False

        elif task == "meditate":
            my_shrine.meditate()

        elif task == "leave":
            game_running = False

        else:
            print("The spirits are confused by your actions.")

    my_shrine.save_progress()
    print(
        f"Goodbye, Caretaker {caretaker_name}. The shrine awaits your return.")


if __name__ == "__main__":
    caretaker_name = intro()
    shrine_adventure(caretaker_name)
