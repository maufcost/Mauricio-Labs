from django.core.management.base import BaseCommand, CommandError
import os
from crontab import CronTab

class Command(BaseCommand):
    help = 'Cron testing'

    def handle(self, *args, **options):
        # Initializes crontab.
        cron  = CronTab(user=True) # user=True

        # Adding a new cron job
        # job = cron.new(command='python <path_to>/example.py >>/tmp/out.txt 2>&1') # (template)
        job = cron.new(command="/Users/mauriciofigueiredomattoscosta/Documents/Warehouse/dev/Websites/django_env/bin/python3.7 /Users/mauriciofigueiredomattoscosta/Documents/Warehouse/dev/Websites/Doomsday_Device/doomsdaydevice/sendemail.py >>/tmp/out.txt 2>&1")

        # Setting up the job settings.
        job.minute.every(1) # Change to 5.

        cron.write()

        self.stdout.write(self.style.SUCCESS("Crontab Successfully setup!"))
