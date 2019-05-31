from .models import Question
from django.shortcuts import render
from django.http import JsonResponse

def home(request):
    questions = Question.objects.all()
    return render(request, "core/home.html", {"questions":questions})

def processMistake(request):
    if request.POST and request.is_ajax():
        # Getting the data (number of mistakes) from the AJAX POST request.
        numberOfMistakes = request.POST.get("numberOfMistakes")

        # Checking if file exists.
        try:
            numberOfMistakes = 0
            with open("mistakes_file.txt", "r") as f: # Throws.
                # The file exists (mistakes were already made).
                numberOfMistakes = int(f.read())
                numberOfMistakes += 1

            # Write new number of mistakes to the file.
            with open("mistakes_file.txt", "w") as f:
                f.write(str(numberOfMistakes))

        except FileNotFoundError:
            # The file does not exist (first mistake made).
            with open("mistakes_file.txt", "w") as f:
                f.write(str(1))

        return JsonResponse({"message":"Number of mistakes successfully updated in the file."})

def doomsdayDeviceActivated(request):
    return render(request, "core/doomsday.html")
