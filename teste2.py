import imaplib
import email
from email.header import decode_header
import os

imap_ssl_host = 'imap.gmail.com'
imap_ssl_port = 993
username = "alertanobreakfloresta@gmail.com"
password = os.getenv("EMAIL_PASSWORD")
server = imaplib.IMAP4_SSL(imap_ssl_host, imap_ssl_port)

server.login(username, password)
server.select('"[Gmail]/E-mails enviados"')
# server.search("utf-8", '(TO "suporte@fcisa.com.br" SUBJECT "Modo Bateria")')

status, data = server.search("utf-8", '(TO "suporte@fcisa.com.br" SUBJECT "Modo Bateria")')

print(status, data[0].split()[-5:])

id_mensagens = [x.decode("utf-8") for x in data[0].split()[-5:]]

for num in id_mensagens:
    status, msg = server.fetch(num, '(RFC822)')
    msg = msg[0][1]
    message = email.message_from_bytes(msg)
    # print(message)
    subject = str(decode_header(message["subject"])[0][0])[1:]
    print(num)
    print(f'Assunto: {subject}')
    print(f'De: {message["from"]}')
    print(f'Para: {message["to"]}')
    print(f'{message.get_payload()[:30]}\n')
