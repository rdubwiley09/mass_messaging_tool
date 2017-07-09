from Twilio.rest import Client
from datetime import datetime

def validate_list(df):
    if 'number' in df:
        return True
    else:
        return False

def message_list(twilioID, twilioNumber, twilioKey, df, userID, message):
    client = Client(twilioID, twilioKey)
    messageLog = []
    for i, row in df.iterrows():
        message = client.messages.create(
            to=row['number'],
            from=twilioNumber,
            body = messages
        )
        print(dir(message))
        messageLog.append({
            'id': message.sid,
            'to': row['number'],
        })
    log = {
        'userID': userID,
        'from': twilioNumber,
        'time': datetime.now(),
        'messages': messageLog
    }
    return log
