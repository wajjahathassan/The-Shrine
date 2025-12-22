"""Module providing a function printing python version."""

import os
import json
import random
from dotenv import load_dotenv
import google.generativeai as genai
load_dotenv()


class Shrine:
    def __init__(self):
        self.cleanliness_score = 0
        self.spirit_energy = 0
        self.inventory = {}

    def ask_ai(self):
        # Setup the AI
        genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
        model = genai.GenerativeModel("gemini-2.5-flash")

        # Ask for wisdom
        response = model.generate_content(
            """You are a wise ancient shrine caretaker in Korea.
            Give me one short sentence of mystical, comforting advice.""")

        # Return the answer
        return response.text

    def load_progress(self):
        try:
            with open("save_data.txt", "r") as file:
                data = json.load(file)
                self.cleanliness_score = data["cleanliness"]
                self.spirit_energy = data["energy"]
                self.inventory = data["inventory"]

        except (FileNotFoundError, ValueError, KeyError):
            self.cleanliness_score = 0
            self.spirit_energy = 0
            self.inventory = {}

    def add_item(self, item_name):
        if item_name in self.inventory:
            self.inventory[item_name] += 1

        else:
            self.inventory[item_name] = 1

        print(f"You obtained a {item_name}!")

    def remove_item(self, item_name):
        if item_name in self.inventory:
            self.inventory[item_name] -= 1

            if self.inventory[item_name] == 0:
                # This deletes the key completely!
                del self.inventory[item_name]

            print(f"Used 1 {item_name}!")

        else:
            print("You don't have that item")

    def clean(self):
        self.cleanliness_score += 5
        print("You swept the dusty floors. The shrine brightens!")

        roll = random.randint(1, 10)
        print(f"DEBUG: Rolled a {roll}")

        if roll > 7:
            self.add_item("Incense")

    def meditate(self):
        roll = random.randint(1, 10)

        if roll > 4:
            self.spirit_energy += 5
            print("You sit in silence. Your spirit strengthens.")

        else:
            print("You fell asleep!")

    def show_inventory(self):
        for key, value in sorted(self.inventory.items()):
            print(f"{key}: {value}")

    def buy_item(self, item_name, cost):
        if self.spirit_energy >= cost:
            self.spirit_energy -= cost
            self.add_item(item_name)

            print(f"Congratulations! You purchased a {item_name}.")

        else:
            print("Sorry! Not enough energy.")

    def save_progress(self):
        # Create a dictionary of everything we want to save
        data = {
            "cleanliness": self.cleanliness_score,
            "energy": self.spirit_energy,
            "inventory": self.inventory
        }

        with open("save_data.txt", "w") as file:
            json.dump(data, file)
            # json.dump(data, file) writes the dictionary to the file


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

            if my_shrine.cleanliness_score >= 50:
                print("The shrine is pure! The spirits are at peace.")
                game_running = False

        elif task == "meditate":
            my_shrine.meditate()

        elif task == "inventory":
            my_shrine.show_inventory()

        elif task == "shop":
            item_name = input("Which item do you wish to buy?")
            cost = int(input("How much offering does it require?"))
            my_shrine.buy_item(item_name, cost)

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
