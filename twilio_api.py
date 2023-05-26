from twilio.rest import Client

account_sid = 'id'
auth_token = 'token'
client = Client(account_sid, auth_token)

twilio_phone = "+13158563199"
my_phone = "+5524988213416"


def send_sms():
    message = client.messages \
        .create(
             body="TESTE SMS",
             from_=twilio_phone,
             to=my_phone
         )

    print(message.status)


send_sms()
