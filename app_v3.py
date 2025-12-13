"""Module providing a function printing python version."""


def load_progress():
    with open("save_data.txt", "r") as file:
        data = file.read()
        values = data.split(",")
        cleanliness_score = int(values[0])
        spirit_energy = int(values[1])
        return cleanliness_score, spirit_energy


def intro():
    caretaker_name = input("Who approaches the shrine? ")
    print(f"Welcome, Caretaker {caretaker_name}")
    return caretaker_name


def shrine_adventure(caretaker_name):
    cleanliness_score, spirit_energy = load_progress()

    print(f"Current Shrine Cleanliness: {cleanliness_score}")
    print(f"Current Spirit Strength: {spirit_energy}")

    game_running = True

    while game_running == True:
        task = input("What task would you like to perform? ").lower()

        if task == "clean":
            cleanliness_score += 5
            print("You swept the dusty floors. The shrine brightens!")

            if cleanliness_score >= 20:
                print("The shrine is pure! The spirits are at peace.")
                game_running = False

        elif task == "meditate":
            spirit_energy += 10
            print("You sit in silence. Your spirit strengthens.")

        elif task == "leave":
            game_running = False

        else:
            print("The spirits are confused by your actions.")

    save_progress(cleanliness_score, spirit_energy)
    print(
        f"Goodbye, Caretaker {caretaker_name}. The shrine awaits your return.")


def save_progress(cleanliness_score, spirit_energy):
    with open("save_data.txt", "w") as file:
        file.write(f"{cleanliness_score}, {spirit_energy}")


if __name__ == "__main__":
    caretaker_name = intro()
    shrine_adventure(caretaker_name)
