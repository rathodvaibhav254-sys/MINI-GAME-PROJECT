// Score variables
let me = 0;
let bot = 0;

// Choices
let choices = ["rock", "paper", "scissor"];

// Main function
function play(userMove) {

    // Generate bot move
    let botMove = choices[Math.floor(Math.random() * 3)];

    let result = "";

    // Game logic
    if (userMove === botMove) {
        result = "It's a tie!";
    }
    else if (
        (userMove === "rock" && botMove === "scissor") ||
        (userMove === "paper" && botMove === "rock") ||
        (userMove === "scissor" && botMove === "paper")
    ) {
        me++;
        result = "You win this round!";
    }
    else {
        bot++;
        result = "Bot wins this round!";
    }

    // Check final winner
    if (me === 5) {
        result = "🎉 You win the game!";
        me = 0;
        bot = 0;
    }
    else if (bot === 5) {
        result = "🤖 Bot wins the game!";
        me = 0;
        bot = 0;
    }

    // Update DOM
    document.getElementById("result").innerText = result;
    document.getElementById("botMove").innerText = "Bot chose: " + botMove;
    document.getElementById("me").innerText = me;
    document.getElementById("bot").innerText = bot;
}