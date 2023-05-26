import imaplib
import email
from email.header import decode_header
import os

# Leitura do id do ultimo email armazenado
with open("email_id.txt") as data:
    ultimo_email = int(data.read())

print(ultimo_email)

# TODO: Ler emails enviados,apenas suporte, dos dois nobreaks.
# Criação conexão com Gmail via IMAP
imap_ssl_host = 'imap.gmail.com'
imap_ssl_port = 993
username = "alertanobreakfloresta@gmail.com"  # user
password = os.getenv("EMAIL_PASSWORD")  # password
server = imaplib.IMAP4_SSL(imap_ssl_host, imap_ssl_port)


# Login GMAIL
server.login(username, password)

# Seleção pasta para verificação
server.select('"[Gmail]/E-mails enviados"')
# Filtro de pesquisa dos email
filtro_pesquisa = '(TO "suporte@fcisa.com.br" SUBJECT "Modo Bateria")'
server.search("utf-8", filtro_pesquisa)

# Lista de mensagens
status, data = server.search("utf-8", filtro_pesquisa)
id_mensagens = [int(x.decode("utf-8")) for x in data[0].split()[-50:]]
# print(status, data[0].split()[-5:])
print(id_mensagens)

status_nobreak = False

# Verificação se o id dos emails é maior que o ultimo_email, se sim altera status nobreak
for id_mensagem in id_mensagens:
    if id_mensagem > ultimo_email:
        status_nobreak = True
        # Armazenar id ultimo email
        with open("email_id.txt", "w") as data:
            data.write(str(id_mensagem))

# TODO: Enviar SMS.
if status_nobreak:
    print("Enviar mensagem")
