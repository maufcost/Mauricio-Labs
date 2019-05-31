function DoomsdayDeviceQuiz(questions) {
    this.score = 0;
    this.questions = questions;
    this.currentQuestionIndex = 0;
    this.numberOfMistakes = 0;
    this.MAX_NUM_OF_MISTAKES = 5; // Change to five later (after I add more questions)
}

DoomsdayDeviceQuiz.prototype.getQuestionBasedOnIndex = function() {
    return this.questions[this.currentQuestionIndex];
}

DoomsdayDeviceQuiz.prototype.hasEnded = function() {
    return this.currentQuestionIndex == this.questions.length;
}

DoomsdayDeviceQuiz.prototype.guess = function(selectedChoice) {

    if (this.getQuestionBasedOnIndex().isCorrectAnswer(selectedChoice)) {
        // Correct choice!
        this.score++;
    }else {
        // Incorrect choice! Let's add one mistake.
        document.getElementsByClassName("mistake-title")[this.numberOfMistakes].style.color = "red";
        this.numberOfMistakes++;
        audio.play();

        // Making background AJAX POST request to a view that will write the number
        // of mistakes to a txt file.
        makeAJAXPOSTRequest(this.numberOfMistakes);
    }

    // Checking if the number of mistakes has gotten to five, so that we can
    // send the email.
    if (this.numberOfMistakes == this.MAX_NUM_OF_MISTAKES) {
        location.href = redirect_user_url;
    }

    this.currentQuestionIndex++;
}

function makeAJAXPOSTRequest(numberOfMistakes) {

    var data = {"numberOfMistakes":numberOfMistakes}

    $.ajax({
        data: data,
        url: "process-mistake", // URL to redirect the user back to after the AJAX POST request.
        method: "POST",
        success: function(data) {
            console.log("This is a success message: " + data.message)
        },
        error: function(error) {
            console.log(error)
        }
    })
}
