import imaplib
import email
from email.header import decode_header
from datetime import datetime
from dateutil.parser import *

# account credentials
username = "bshobanke@terragonltd.com"
password = "grrgmlcgbsjzhnlz"

# create an IMAP4 class with SSL 
imap = imaplib.IMAP4_SSL("imap.gmail.com")
# authenticate
imap.login(username, password)

status, messages = imap.select("INBOX", readonly=False)

status, messages = imap.search(None, '(FROM "bshobanke2@gmail.com")')
print(messages)
print(messages[0])
# number of top emails to fetch
N = 3
# total number of emails
#messages = int(messages[0])
print(str(messages))

msgs = []

id = email.message_from_bytes(messages[0]).as_string()
id = id.strip()
id_array = id.split(' ')

print(id_array)

# for i in range(messages, messages-N, -1):
    # fetch the email message by ID
for message_id in id_array:
    res, msg = imap.fetch(message_id, "(RFC822)")

    msgs.append(msg[0][1])

for res in msgs:
    msg = email.message_from_bytes(res)
    date = decode_header(msg["Date"])[0][0]
    msg_date = parse(date).date()
    print(msg_date)


# for response in msg:
#     if isinstance(response, tuple):
#         # parse a bytes email into a message object
#         msg = email.message_from_bytes(response[1])
#         date = decode_header(msg["Date"])[0][0]
#         print(date)
#         print(isinstance(date, str))

#         then = parse(date).date()
#         print(then)
#         now = datetime.now().strftime('%Y-%m-%d')
        
#         if str(then) != str(now):
#             print('error')

        # ft = date.split(' ')
        # print(ft)
        # ct = ' '.join(ft[0:4])
        # print(ct)
        # dt = datetime.strptime(ct, '%Y-%m-%d')
        # print(dt)