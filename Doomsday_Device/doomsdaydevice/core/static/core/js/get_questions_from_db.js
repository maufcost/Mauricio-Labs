// Getting the questions and storing them in a JS variable.
for (i = 0; i < NUMBER_OF_QUESTIONS; i++) {

    // Getting the title
    title = document.getElementById("hidden_title_q" + i).textContent;

    // Getting the choices
    choices = [];
    for (j = 0; j < NUMBER_OF_CHOICES; j++) {
        cid = "hidden_choice" + (j + 1) + "_q" + i;
        c = document.getElementById(cid).textContent;
        choices.push(c);
    }

    // Getting the correct answer.
    hidden_answer = document.getElementById("hidden_answer_q" + i).textContent; // include?!
    questions.push(new Question(title, choices, hidden_answer));
}
