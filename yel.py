import imaplib, email
from pathlib import Path
from typing_extensions import Self
import boto3
import os, tempfile
import textract
from datetime import datetime
import chardet

email_user = "bshobanke@terragonltd.com"
email_pass = "uedijmdxacoxmlos"
att_dir = Path('./attachments')
s3 = boto3.client('s3')
dt = datetime.now()

def get_body(msgs):
    if msgs.is_multipart():
        return get_body(msgs.get_payload(0))

    else:
        return msgs.get_payload(None, True)

def get_attachments(msg):
    for part in msg.walk():
        if part.get_content_maintype() == 'multipart':
            continue
        
        if part.get('Content-disposition') is None:
            continue

        file_name = Path(part.get_filename())

        if bool(file_name):
            file_path = att_dir / file_name
            if str(file_path.suffix) in ['.txt', '.xls', '.csv']:
                if att_dir.exists() == False:
                    att_dir.mkdir()
                # file_path.write_bytes(part.get_payload(decode=True))
                # with open(file_name, 'wb') as f:
                #     # s3.upload_fileobj(f, 'sample-bucket-90210', file_name)
                #     os.readlink()
                #     s3.Bucket('sample-bucket-90210').put_object(Key=f'{file_name}', Body=f)
                temp = tempfile.NamedTemporaryFile(delete=False, suffix=file_name.suffix)
                # tf.write(part.get_payload(decode=True))
                # print(name, fd)

                
                # tf_path.write_bytes(part.get_payload(decode=True))
                
                temp.write(part.get_payload(decode=True))
                # tf_path = Path(temp.name).with_suffix(file_name.suffix)

                # with open(tf_path, 'rb') as rawdata:
                #     result = chardet.detect(rawdata.read(100000))
                # print(result)
                # # if tf_path.suffix != '.txt':
                # result = chardet.detect(tf_path.read_bytes())
                # print(result['encoding'])
                text = textract.process(temp.name)
                demp = tempfile.NamedTemporaryFile(delete=False, suffix='.txt')
                demp.write(text)
                # temp.close()
                # tf_path.unlink()
                # tf_path.write_bytes(text)
                # # df.write(text)
                with open(Path(demp.name), "rb") as f:
                    s3.upload_fileobj(f, 'sample-bucket-90210', f'{dt.strftime("%Y")}{dt.strftime("%m")}{dt.strftime("%d")}.txt')
                # # upload_files(Path(df))
                # # upload_files(tf_path)
        return None

def upload_files(file_path):
    s3 = boto3.client("s3")
    dt = datetime.now()

    s3.upload_file(
    Filename=file_path,
    Bucket="sample-bucket-90210",
    Key=f'{dt.strftime("%Y")}{dt.strftime("%m")}{dt.strftime("%d")}.txt',
    )

def search(value, con):
    result, data = con.search(None, value)
    return data

def get_emails(result_bytes):
    msgs = []
    for num in result_bytes[0].split():
        typ, data = mail.fetch(num, "(RFC822)")
        msgs.append(data[0][1])
    return msgs


mail = imaplib.IMAP4_SSL("imap.gmail.com",993)
mail.login(email_user, email_pass)
mail.select('INBOX')

data = search('(FROM "Rajesh Chopra")', mail)
msgs = get_emails(data)

for msg in msgs:
    # print(get_body(email.message_from_bytes(msg)))
    get_attachments(email.message_from_bytes(msg))