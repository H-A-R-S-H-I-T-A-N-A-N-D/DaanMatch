from twilio.rest import Client
account_sid=""
auth_token = ''

client = Client(account_sid, auth_token)
numbers_to_message = ['+919837549166']
for number in numbers_to_message:
    client.messages.create(
                     body="Hello World From Twilio",
                     # from_='+12056277965',
                     from_='+18634501750',
                     to=number
                 )
