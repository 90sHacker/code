import textract
import tempfile
import boto3
import os
from pathlib import Path

fp = Path('attachments')
s3 = boto3.resource('s3')
# bucket = s3.Bucket('data-lake-v3')

# s3.meta.client.download_file('data-lake-v3', 'raw_batch_data/dnd_blacklist/email_raw/telco=airtel/20220615.txt', 'attachments/')

your_bucket = s3.Bucket('data-lake-v2')

# Iterate All Objects in Your S3 Bucket Over the for Loop
for s3_object in your_bucket.objects.all():
   
    #Use this statement if your files are available directly in your bucket. 
    # your_bucket.download_file(s3_object.key, filename_with_extension)

    #use below three line ONLY if you have sub directories available in S3 Bucket
    #Split the Object key and the file name.
    #parent directories will be stored in path and Filename will be stored in the filename
  
    path, filename = os.path.split(s3_object.key)

    #Create sub directories if its not existing
    if path == 'raw_batch_data/dnd_blacklist/email_raw/telco=airtel':
    #   os.makedirs(path)
      
      #Download the file in the sub directories or directory if its available.
      print(path, filename)
      file_name = Path(filename)
      if file_name.suffix != '.pdf': 
        your_bucket.download_file(s3_object.key, 'attachments/' + filename)

for path in fp.rglob('*.*'):
  if path.stem != '.DS_Store':
    text = textract.process(str(path.absolute()))
    temp = tempfile.NamedTemporaryFile(delete=False, suffix='.txt', dir=fp)
    temp.write(text)
    data_path = temp.name

    try:
      final_data_path = f'raw_batch_data/dnd_blacklist/email_raw/telco=airtel/{path.stem}.csv'
      data_write = your_bucket.upload_file(data_path, final_data_path)

      print('Upload successful!')
      print("Data Path ==> {} ... \n".format(final_data_path))
      print("Final data object ", data_write)

      Path(data_path).unlink()
    except FileNotFoundError:
      print('File not found')

    path.unlink()