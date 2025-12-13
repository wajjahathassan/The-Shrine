"""Module providing a function printing python version."""

# 1. INPUT: Prompt the user for their name to personalize the experience
caretaker_name = input("Who approaches the shrine? ")

# 2. OUTPUT: Greet the user using an f-string for dynamic text
print(f"Welcome, Caretaker {caretaker_name}")

# 3. VARIABLE INITIALIZATION: Set the starting game state
# We start at 0 because the shrine is currently dirty.
cleanliness_score = 0
spirit_energy = 0

# 4. OUTPUT: Display the current score to the user
print(f"Current Shrine Cleanliness: {cleanliness_score}")

# 9. LOOP INITIALIZATION:
# Set a boolean flag to True so the 'while' loop starts and keeps running.
game_running = True

# 10. GAME LOOP:
# The main application loop that continues until the user explicitly chooses to exit.
while game_running == True:

    # 5. INPUT SANITIZATION:
    # Prompt the user and immediately convert input to lowercase to ensure case-insensitive matching.
    task = input("What task would you like to perform? ").lower()

    # 6. CONDITIONAL LOGIC: Check if the user's input matches a specific command
    if task == "clean":

        # 7a. EXPLICIT ASSIGNMENT (Commented out for reference):
        # Manually calculates the sum and re-assigns it. Common in older languages.
        ### cleanliness_score = cleanliness_score + 5 ###

        # 7b. COMPOUND ASSIGNMENT:
        # Pythonic shorthand to update the variable in-place. Preferred for readability.
        cleanliness_score += 5

        # 8a. FEEDBACK: meaningful response to the user's action
        print("You swept the dusty floors. The shrine brightens!")

        # 8b. NESTED CONDITIONAL (WIN STATE CHECK):
        # Check if the win condition is met immediately after the state change.
        if cleanliness_score >= 20:

            # 8c. GAME OVER LOGIC (VICTORY):
            # Notify the user and terminate the game loop by updating the control flag.
            print("The shrine is pure! The spirits are at peace.")
            game_running = False

    # 11a. CONDITIONAL BRANCH (SECONDARY MECHANIC):
    # Check if the user selects the 'meditate' action to build a different resource.
    elif task == "meditate":

        # 11b. STATE UPDATE (RESOURCE ACCUMULATION):
        # Increment the spirit_energy variable.
        spirit_energy += 10
        print("You sit in silence. Your spirit strengthens.")

    # 11c. CONDITIONAL BRANCH (EXIT STRATEGY):
    # Check specifically if the user wants to quit the application.
    elif task == "leave":

        # 12. STATE MODIFICATION (LOOP TERMINATION):
        # Flip the flag to False. The loop will finish this iteration, check the flag, and then stop.
        game_running = False

    # 13. FALLBACK / ERROR HANDLING:
    # A catch-all 'else' block to handle any input that the program doesn't recognize.
    else:
        print("The spirits are confused by your actions.")

# 14. GRACEFUL EXIT:
# This runs only after the loop ends, confirming to the user that the program closed correctly.
print(f"Goodbye, Caretaker {caretaker_name}. The shrine awaits your return.")
