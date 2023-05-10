import imaplib
import email
import os

# TODO: Ler emails enviados,apenas suporte, dos dois nobreaks.
# establish connection with Gmail
server = "imap.gmail.com"
imap = imaplib.IMAP4_SSL(server)

# instantiate the username and the password
username = "alertanobreakfloresta@gmail.com"
password = os.getenv("EMAIL_PASSWORD")

# login into the gmail account
imap.login(username, password)

# select the e-mails
res, messages = imap.select('"[Gmail]/E-mails enviados"')

# calculates the total number of sent messages
print(messages[0])
messages = int(messages[0])

# determine the number of e-mails to be fetched
n = 3

# iterating over the e-mails
for i in range(messages, messages - n, -1):
    res, msg = imap.fetch(str(i), "(RFC822)")
    for response in msg:
        if isinstance(response, tuple):
            msg = email.message_from_bytes(response[1])

            # getting the sender's mail id
            From = msg["From"]

            # getting the subject of the sent mail
            subject = msg["Subject"]

            # printing the details
            print("From : ", From)
            print("subject : ", subject)

# TODO: Guardar status.

# TODO: Enviar SMS.
