import random
import datetime
import smtplib

# Creating List Out of Quotes.txt
with open("quotes.txt","r") as quotes_file:
    data = [line.strip() for line in quotes_file.readlines()]

# Generating Random Quotes from Quotes List
random_quote = random.choice(data)


# LogIn Details
my_email = "saadhasssan47@gmail.com"
my_password = "mdmw hqvb iafm egbe"
receiver_emails = ["saifqaiser101@gmail.com","mrusman4578@gmail.com","webdevcoder409@gmail.com"]

# Sending Mail Function
def motivation_thursday():
    now = datetime.datetime.now()
    if now.strftime("%A") == "Thursday":
        with smtplib.SMTP("smtp.gmail.com") as new_server:
            new_server.starttls()
            new_server.login(user=my_email , password=my_password)
            new_server.sendmail(from_addr=my_email , to_addrs=receiver_emails , msg=f"Subject:Thursday MotivationQuotation\n\n{random_quote}")
motivation_thursday()