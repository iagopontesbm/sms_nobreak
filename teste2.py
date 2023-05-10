import imaplib
import os

imap_ssl_host = 'imap.gmail.com'
imap_ssl_port = 993
username = "alertanobreakfloresta@gmail.com"
password = os.getenv("EMAIL_PASSWORD")
server = imaplib.IMAP4_SSL(imap_ssl_host, imap_ssl_port)

server.login(username, password)
server.select("INBOX")

status, data = server.search(None, 'ALL')
for num in data[0].split():
    status, data = server.fetch(num, '(BODY[HEADER.FIELDS (SUBJECT DATE FROM TO)])')
    email_msg = data[0][1]
    print(email_msg)
