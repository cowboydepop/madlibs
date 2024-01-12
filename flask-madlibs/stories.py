"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request


app = Flask(__name__)

compliments = compliments = [
    "awesome",
    "terrific",
    "fantastic",
    "neato",
    "fantabulous",
    "wowza",
    "oh-so-not-meh",
    "brilliant",
    "ducky",
    "coolio",
    "incredible",
    "wonderful",
    "smashing",
    "lovely",
]



@app.route("/")
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route("/hello")
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route("/greet")
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html", person=player, compliment=compliment)


@app.route("/game")
def show_madlib_form():
    """Show madlib form based on user request."""

    answer_value = request.args.get("answer")

    if answer_value == "no":
        return render_template("goodbye.html")
    elif answer_value == "yes":
        return render_template("game.html")


@app.route("/madlib")
def show_madlib():

    person = request.args.get("person")
    color = request.args.get("color")
    noun = request.args.get("noun")
    adjective = request.args.get("adjective")

    return render_template(
        "madlib.html", person=person, color=color, noun=noun, adjective=adjective
    )


