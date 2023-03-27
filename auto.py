import imaplib
import base64
import os
import email
from pathlib import Path

# email_user = input('Email: ')
# email_pass = input('Password: ')

email_user = "bshobanke@terragonltd.com"
email_pass = "uedijmdxacoxmlos"
path_file = Path('/files')

mail = imaplib.IMAP4_SSL("imap.gmail.com",993)

mail.login(email_user, email_pass)

# print(mail.list())
print(mail.select('Inbox'))

type, data = mail.search(None, '(FROM "Rajesh Chopra")')
# print(data)
items = data[0].split()

att_path_list = []

for mail_id in items:
    resp, data = mail.fetch(mail_id, "(RFC822)")
    mail_body = data[0][1]
    # print(mail_body)
    mail_string = mail_body.decode('utf-8')
    mailed = email.message_from_string(mail_string)
    print(mailed)
    temp = mail.store(mail_id, '+FLAGS', '\\Seen')
    # mail.expunge()

    if mailed.get_content_maintype != 'multipart':
        continue

    print ("["+mailed["From"]+"] :" + mailed["Subject"])

    for part in mailed.walk():
        # if part.get_content_maintype() == 'multipart':
        #     continue
        # if part.get('Content-Disposition') is None:
        #     continue

        filename = part.get_filename()
        att_path = os.path.join(path_file, filename)

        if not os.path.isfile(att_path):
            fp = open(att_path, 'wb')
            fp.write(part.get_payload(decode=True))
            fp.close()
        att_path_list.append(att_path)

    print(att_path_list)

mail.close()