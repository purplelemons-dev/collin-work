
from twilio.rest import Client
from twilio.twiml import voice_response
from env import SID, AUTH, FROM

MESSAGE = "This is an automated {type} from Collin College to let you know that \
Summer and Fall registration is now open. There will be registration labs this \
week at the McKinney Campus on Wednesday the 26th and Thursday the 27th. \
These labs will be held in the Multipurpose Room at the Welcome Center. If you \
have any questions, you may come on campus to speak with an Enrollment Specialist."

client = Client(SID, AUTH)

def send_call(number:str):
    call = voice_response.VoiceResponse()
    call.pause(length=4)
    call.say(MESSAGE.format(type="call"))
    client.calls.create(to=number, from_=FROM, twiml=call)

def send_text(number:str):
    client.messages.create(to=number, from_=FROM, body=MESSAGE.format(type="text message"))

phonenums:list[str] = []

with open("numbers.txt", "r") as f:
    for line in f:
        line = line.strip().replace("-", "").replace("(", "").replace(")", "").replace(" ", "").replace(",", "")
        if len(line) == 10:
            line = f"+1{line}"
            phonenums.append(line)
        else:
            print(f"Invalid number: {line}")

for num in phonenums:
    send_call(num)
