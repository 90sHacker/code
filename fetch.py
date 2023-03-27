import imaplib, email
import textract
from pathlib import Path
from email.header import decode_header
from datetime import datetime
from dateutil.parser import *
import chardet

class FetchEmail():

    def __init__(self, mail_server, username, password):
        self.connection = imaplib.IMAP4_SSL(mail_server)

        self.connection.login(username, password)
        self.connection.select('Inbox', readonly=False)

    def close_connection(self):
        """
        Close connection to the IMAP server
        """
        self.connection.close()

    def search(self, value, key='FROM'):
        """
        Search the Mailbox for matching messages
        """
        result, data = self.connection.search(None, f'({key} "{value}")')
        if result == 'OK':
            return data

    def fetch_recent_email(self, value, key='FROM'):
        """
        Retrieve the most recent email for a search criterion
        """
        msgs = []
        result, messages = self.connection.search(None, f'({key} "{value}")')

        #get the id's of the messages as a string
        id = email.message_from_bytes(messages[0]).as_string()

        #create an array of id's and pick the last element which is the most recent
        id = id.strip()
        id_array = id.split(' ')
        # message = id_array[-1]
        for message in id_array:
            if result == 'OK':
                try:
                    res, data = self.connection.fetch(str(message), "(RFC822)")
                except:
                    print("No email found")
                    self.close_connection()
                    exit()
                
                msgs.append(data[0][1])
                response, data = self.connection.store(str(message), '+FLAGS', '\\Seen')

        return msgs

    def download_attachments(self, value, key='FROM', download_folder="attachments"):
        """
        Download the attachments for the recent email
        """

        att_err = "No current email found."
        att_dir = "No attachment found"

        msgs = self.fetch_recent_email(value, key)
        for response in msgs:
            msg = email.message_from_bytes(response)
            date = decode_header(msg["Date"])[0][0]
            then = parse(date).date()
            # print(then)
            # now = datetime.now().strftime('%Y-%m-%d')
            # print(now)
            # if str(then) != str(now):
            #     return att_err

            for part in msg.walk():
                if part.get_content_maintype() == 'multipart':
                    continue
                
                if part.get('Content-disposition') is None:
                    continue
                
                file_name = Path(part.get_filename())
                if bool(file_name):
                    att_dir = Path(download_folder)
                    file_path = att_dir / file_name
                    if str(file_path.suffix) in ['.txt', '.xls', '.csv']:
                        if value.__contains__('mtn'):
                            if self.check_file_name(file_name.stem, ['mnp']):
                                #convert file to .txt
                                #upload to s3 as specified name format
                                pass
                            if self.check_file_name(file_name.stem, ['dnd']):
                                #convert file to .txt
                                #upload to s3 as specified name format
                                pass

                        elif value.__contains__('airtel'):
                            if self.check_file_name(file_name.stem, ['mnp']):
                                #convert file to .txt
                                #upload to s3 as specified name format
                                pass
                            if self.check_file_name(file_name.stem, ['dnd']):
                                #convert file to .txt
                                #upload to s3 as specified name format
                                pass

                        elif value.__contains__('9mobile'):
                            if self.check_file_name(file_name.stem, ['mnp']):
                                #convert file to .txt
                                #upload to s3 as specified name format
                                pass
                            if self.check_file_name(file_name.stem, ['dnd']):
                                #convert file to .txt
                                #upload to s3 as specified name format
                                pass
                        
                        else:
                            if att_dir.exists() == False:
                                att_dir.mkdir()
                            file_path.write_bytes(part.get_payload(decode=True))
                            # with open(file_path, 'rb') as rawdata:
                            #     result = chardet.detect(rawdata.read(100000))
                            #     print(result)
                            self.convert_files(att_dir)
    
        if(isinstance(att_dir, Path)):
            return att_dir.absolute()

        return att_dir

    def check_file_name(self, file_name, keyword):
        """
        Checks a file name for a specified key
        """
        fn = file_name.lower()
        for key in keyword:
            if fn.__contains__(key):
                return True
            break
        return False

    def convert_files(self, file_path, convert_folder="converted"):
        """
        File conversion to .txt
        """
        con_dir = Path(convert_folder)
        for path in file_path.rglob('*.*'):
            print(path)
            if path.stem != '.DS_Store':
                text = textract.process(str(path.absolute()))
                print(path.absolute())
                if con_dir.exists() == False:
                    con_dir.mkdir()
                con_dir.joinpath(f'{path.stem}.txt').write_bytes(text)

if __name__ == '__main__':
    mail = FetchEmail('imap.gmail.com', 'bshobanke@terragonltd.com', 'uedijmdxacoxmlos')
    respond = mail.download_attachments('Rajesh Chopra')
    print(respond)

    mail.close_connection()