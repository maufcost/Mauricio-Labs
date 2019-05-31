import requests, json
from core.models import Question
from django.core.management.base import BaseCommand

class Command(BaseCommand):
     help = """ Loads questions to Django's sqlite database. """

     def handle(self, *args, **kwargs):
         """
         Evoked when we execute manage.py on this command.
         """

         # Getting and loading questions from JSON to Django models.
         url = "https://raw.githubusercontent.com/maufcost/Maurice-Labs/master/Doomsday_Device/questions.json"
         httpResponse = requests.get(url)
         json_data = httpResponse.json()

         for instance in json_data:

             # Instantiating the Question class.
             Question.objects.create(title=instance["text"],
                                     choice1=instance["choices"][0],
                                     choice2=instance["choices"][1],
                                     choice3=instance["choices"][2],
                                     choice4=instance["choices"][3],
                                     correct_answer=instance["correct_answer"])
         # Displaying success message.
         self.stdout.write(self.style.SUCCESS("All the questions were successfully loaded to Django's database."))
