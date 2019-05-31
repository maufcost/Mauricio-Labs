function Question(title, choices, answer) {
    this.title = title;
    this.choices = choices;
    this.answer = answer;
}

Question.prototype.isCorrectAnswer = function(selectedChoice) {
    return selectedChoice == this.answer;
}
