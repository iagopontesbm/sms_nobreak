import imaplib
import os

imap_ssl_host = 'imap.gmail.com'
imap_ssl_port = 993
username = "alertanobreakfloresta@gmail.com"
password = os.getenv("EMAIL_PASSWORD")
server = imaplib.IMAP4_SSL(imap_ssl_host, imap_ssl_port)

server.login(username, password)
# server.select('INBOX')

result = server.list()

for folder in result[1]:
    print(folder.decode('utf-8'))
