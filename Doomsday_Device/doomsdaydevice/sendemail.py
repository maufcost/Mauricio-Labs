import os
import smtplib
import datetime
from email.message import EmailMessage

numberOfMistakes = 0
MAXIMUM_NUMBER_OF_MISTAKES = 5 # Change
# Cron creates its OWN shell with the use specified through which it will run
# (Still figuring out how to access the shell created by cron).
EMAIL_ADDRESS = os.environ.get("EMAIL_USER")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")
MISTAKES_FILE_PATH = os.path.environ("MISTAKES_FILE_PATH")

msg = EmailMessage()

msg["Subject"] = "Your mom!"
msg["From"] = EMAIL_ADDRESS
msg["To"] = ["Put the list of recipient emails here"]
msg.set_content("You suck!") # Fallback.
msg.add_alternative("""
    <!DOCTYPE html>
    <html>
        <body style='background-color: black;'>
            <h1 style='color: red;'>There is no way you have not strangled at least one stripper!</h1>
        </body>
    </html>
""", subtype="html")

# Opening file with the number of mistakes
try:
    with open(os.path.environ("MISTAKES_FILE_PATH"), "r") as f:
        numberOfMistakes = int(f.read())
except FileNotFoundError:
    pass # No mistakes yet (but the cron keep checking every five minutes).

# Checking if the number of mistakes equals five
if numberOfMistakes == MAXIMUM_NUMBER_OF_MISTAKES:
    now = datetime.datetime.now()

    # Checking if it is 5PM to send the e-mail.
    if now.hour >= 17:
        # Let's send the email!
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            # Logging in to the email server.
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

            # Sending email.
            smtp.send_message(msg)

            # Resetting buttocks.txt file to 0 again.
            os.remove(MISTAKES_FILE_PATH)
            with open(MISTAKES_FILE_PATH, "w") as f:
                f.write(str(0))
