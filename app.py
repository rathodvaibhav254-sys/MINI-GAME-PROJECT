from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Choices
choices = ["rock", "paper", "scissor"]

# Global scores
me = 0
bot = 0

@app.route("/", methods=["GET", "POST"])
def index():
    global me, bot

    # ✅ Default values (VERY IMPORTANT)
    result = ""
    bot_move = ""
    user_move = ""

    # When user plays
    if request.method == "POST":
        user_move = request.form.get("move")

        # Validate input
        if user_move not in choices:
            result = "Invalid move, try again"
            return render_template("index.html",
                                   result=result,
                                   bot_move=bot_move,
                                   me=me,
                                   bot=bot,
                                   user_move=user_move)

        # Bot move
        bot_move = random.choice(choices)

        # Game logic
        if user_move == bot_move:
            result = "It's a tie!"

        elif (user_move == "rock" and bot_move == "scissor") or \
             (user_move == "paper" and bot_move == "rock") or \
             (user_move == "scissor" and bot_move == "paper"):
            me += 1
            result = "You win this round!"

        else:
            bot += 1
            result = "Bot wins this round!"

        # Final winner check
        if me == 5:
            result = "🎉 You win the game!"
            me = 0
            bot = 0

        elif bot == 5:
            result = "🤖 Bot wins the game!"
            me = 0
            bot = 0

    # Always return page (GET + POST)
    return render_template("index.html",
                           result=result,
                           bot_move=bot_move,
                           me=me,
                           bot=bot,
                           user_move=user_move)

# Run server
if __name__ == "__main__":
    app.run(debug=True)