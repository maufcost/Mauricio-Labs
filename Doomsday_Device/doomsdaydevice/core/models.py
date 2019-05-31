from django.db import models

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    choice1 = models.CharField(max_length=100, blank=False, null=False, default="choiceA")
    choice2 = models.CharField(max_length=100, blank=False, null=False, default="choiceB")
    choice3 = models.CharField(max_length=100, blank=False, null=False, default="choiceC")
    choice4 = models.CharField(max_length=100, blank=False, null=False, default="choiceD")
    correct_answer = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.title
