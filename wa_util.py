from twilio.rest import Client

class WhatsAppService:

    def send(self, recipient, message, attachment=None):
        account_sid = '<TWILIO_ACCOUNT_SID>'
        auth_token = '<TWILIO_AUTH_TOKEN>'
        client = Client(account_sid, auth_token)

        wa_from = 'whatsapp:+2348123456789' # verified whatsapp business number
        wa_to = 'whatsapp:' + recipent # recipent number

        if attachment:
            message = client.messages.create(
                body=message,
                from_=wa_from,
                to=wa_to,
                media_url=attachment
            )

            return message.sid
        else:
            message = client.messages.create(
                body=message,
                from_=wa_from,
                to=wa_to
            )
            return message.sid


