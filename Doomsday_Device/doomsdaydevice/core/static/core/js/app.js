// Creating a quiz.
var doomsdayDeviceQuiz = new DoomsdayDeviceQuiz(questions);

function displayDoomsdayQuiz() {
    // Displays the quiz
    if (doomsdayDeviceQuiz.hasEnded()) {
        // Showing the final score if the quiz has ended.
        showFinalScore();
    }else {
        // The quiz has not ended yet.

        // Showing the current question title.
        var element = document.getElementById("question");
        element.innerHTML = doomsdayDeviceQuiz.getQuestionBasedOnIndex().title;

        // Showing the current question choices.
        var choices = doomsdayDeviceQuiz.getQuestionBasedOnIndex().choices;
        for (i = 0; i < choices.length; i++) {
            var element = document.getElementById("choice" + (i + 1));
            element.innerHTML = choices[i];
            updateChoiceAction("btn" + (i + 1), choices[i]);
        }

        // Showing the progress.
        showProgress();
    }
}

function showFinalScore() {
    // Shows your scores after the quiz has ended.
    var finalHTML = "<h1>Result</h1>";
    finalHTML += "<h2>Score: " + doomsdayDeviceQuiz.score + "</h2>";
    var element = document.getElementById("quiz");
    element.innerHTML = finalHTML;
}

function updateChoiceAction(id, aGuess) {
    // Gives a specific action for each choice for the current displayed question.

    // Getting the button that has the id of 'id'.
    var button = document.getElementById(id);

    // Setting an action for each choice of the current displaying question.
    button.onclick = function() {
        doomsdayDeviceQuiz.guess(aGuess);
        displayDoomsdayQuiz();
    }
}

function showProgress() {
    // Showing the quiz progress, such as "Question 1 of 3", "Question 2 of 3", etc.
    var currentQuestionNumber = doomsdayDeviceQuiz.currentQuestionIndex + 1;
    var element = document.getElementById("progress");
    element.innerHTML = "Question " + currentQuestionNumber + " of " + doomsdayDeviceQuiz.questions.length;
}

// Displays the quiz for the first time.
displayDoomsdayQuiz()
