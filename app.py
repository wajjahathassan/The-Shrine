"""
This module initializes the Flask web server and
defines the main routes for the Shrine Caretaker application.
"""

from flask import Flask, render_template, redirect, request, jsonify

from app_v11 import Shrine

app = Flask(__name__)

item_names = {"Sword": "🗡️", "Incense": "🥢",
              "Banana": "🍌", "Arrow": "🏹", "Apple": "🍎", "Grapes": "🍇"}
item_prices = {"Sword": 15, "Incense": 10,
               "Banana": 5, "Arrow": 10, "Apple": 5, "Grapes": 5, "Curious Spirit": 0}


@app.route("/")
def home():
    my_shrine = Shrine()
    my_shrine.load_progress()
    return render_template("index.html", shrine=my_shrine, items=item_names, prices=item_prices)


@app.route("/about")
def about_me():
    my_shrine = Shrine()
    my_shrine.load_progress()
    item_name = "Curious Spirit"
    reward_given = False
    if item_name not in my_shrine.inventory:
        my_shrine.add_item(item_name)
        my_shrine.save_progress()
        reward_given = True

    return render_template("about.html", shrine=my_shrine, reward=reward_given)


@app.route("/clean", methods=["POST"])
def clean_action():
    my_shrine = Shrine()
    my_shrine.load_progress()
    my_shrine.clean()
    my_shrine.save_progress()
    return redirect("/")


@app.route("/meditate", methods=["POST"])
def meditate_mat():
    my_shrine = Shrine()
    my_shrine.load_progress()
    my_shrine.meditate()
    my_shrine.save_progress()
    return redirect("/")


@app.route("/merchant", methods=["POST"])
def entering_shop():
    my_shrine = Shrine()
    my_shrine.load_progress()

    # Get the data from the form
    item_name = request.form.get("item_name")
    cost = int(request.form.get("cost"))

    my_shrine.buy_item(item_name, cost)
    my_shrine.save_progress()
    return redirect("/")


@app.route("/sell", methods=["POST"])
def sell_item():
    my_shrine = Shrine()
    my_shrine.load_progress()

    # Get the data from the form
    item_name = request.form.get("item_name")
    cost = int(request.form.get("cost"))

    # Checking if we actually have the item to sell!
    if item_name in my_shrine.inventory:
        # 1. Remove the item
        my_shrine.remove_item(item_name)
        # 2. Add the cost to spirit_energy
        my_shrine.spirit_energy += cost

    my_shrine.save_progress()
    # OLD: return redirect("/")
    # NEW: Returns just the data we need!
    return jsonify({
        "success": True,
        "new_energy": my_shrine.spirit_energy,
        "new_count": my_shrine.inventory.get(item_name, 0)
    })


@app.route("/ask_wisdom", methods=["POST"])
def get_wisdom():
    my_shrine = Shrine()
    my_shrine.load_progress()

    # Gets the text string from the logic file
    wisdom_text = my_shrine.ask_ai()

    # Passes that text string to the template with the label 'advice'
    return render_template("index.html", shrine=my_shrine, response=wisdom_text, items=item_names, prices=item_prices)


if __name__ == "__main__":
    app.run(debug=True)
