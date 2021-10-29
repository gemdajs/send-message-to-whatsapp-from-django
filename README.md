# send message to whatsapp from django using twilio

## Setup
Get SID and Auth Token keys from https://console.twilio.com/us1/account/manage-account/general-settings under keys and crednetials
install twilio by 
`pip install twilio`

## run
`
wa_service = WhatsAppService()
resp = wa_service.send('+2348187654321', 'Hello there!', attachment='https://existing.link/to-your-media-file.ext')

`