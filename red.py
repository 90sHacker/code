import textract
from datetime import datetime
from pathlib import Path
import sys
import os
import tabula
import tempfile
import pandas as pd
# from PyPDF2 import PdfReader
# import PyPDF2
# import pdf2txt
# import camelot
# import fitz

import pdfplumber
import csv

fp = Path('attachments')
np = Path('converted')

def check_file_name(file_name, keyword):
    """
    Checks a file name for a specified key
    """
    fn = file_name.lower()
    for key in keyword:
        if not fn.__contains__(key):
            return False
        #break
    return True

# dt = datetime.now()
# print(f'{dt.strftime("%Y")}{dt.strftime("%m")}{dt.strftime("%d")}')

# Ensure that directory containing pdf2txt.py is in PATH
# if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
#     # Works for macOS and linux; for Windows, semi-colon needs to be used as separator
#     os.environ["PATH"] = os.environ["PATH"] + ":" + sys._MEIPASS

# for path in fp.rglob('*.*'):
#     if path.stem != '.DS_Store':
#         path_parts = path.stem.split('_')
#         print(path_parts)
#         date = path_parts[0]
#         network = path_parts[1]
#         text = textract.process(str(path.absolute()))
#         # tabula.convert_into(path, f"converted/{path.stem}.txt", output_format="csv", pages='all')
#         # output_path = os.path.realpath(f"{path.stem}.txt")
#         # print(output_path)
#         if np.exists() == False:
#             np.mkdir()
#         np.joinpath(f'{date}.csv').write_bytes(text)

# for path in fp.rglob('*.*'):
#     if path.stem != '.DS_Store':
#         path_parts = path.stem.split('_')
#         print(path_parts)
#         date = path_parts[0]
#         network = path_parts[1]
#         # text = textract.process(str(path.absolute()))
#         # # tabula.convert_into(path, f"converted/{path.stem}.txt", output_format="csv", pages='all')
#         # # output_path = os.path.realpath(f"{path.stem}.txt")
#         # # print(output_path)
#         # if np.exists() == False:
#         #     np.mkdir()
#         # np.joinpath(f'{date}.csv').write_bytes(text)
#         if path.suffix == '.xlsx':
#             xl_file = pd.read_excel(path)
#             xl_file.to_csv(np.joinpath(f'{date}.csv'), index = None, header=True)

# Import the required Module

# Read a PDF File
# df = tabula.read_pdf("attachments/20220615.pdf", pages='all')[0]
# # convert PDF into CSV
# # temp = tempfile.NamedTemporaryFile(delete=False, suffix='.csv', dir='converted')
# # tabula.convert_into("attachments/20220615.pdf", Path(temp).absolute(), output_format="csv", pages='all')
# df.to_csv('converted/file.csv')
# # print(type(df))
# print(temp)

# for path in fp.glob('*.*'):
#     if path.stem != '.DS_Store':
#         path_parts = path.stem.split('_')
#         #print(path.with_name)
#         print(path_parts)
#         date = path_parts[0]
#         network = path_parts[1]
#         data_path = f'attachments/{path.stem}.csv'
#         tabula.convert_into(
#             path, data_path, output_format='csv', pages='all'
#         )
merged_path = f"attachments/20230301-20230326_mtn_merged_mnp.txt"
with open(merged_path, "a", newline="") as csv_file:
    #print('here')
    csv_writer = csv.writer(csv_file, 'unix')
    csv_writer.writerow(['MSISDN','DONOR_ID','RECIPIENT_ID','DATE_TIME_STAMP'])
    # csv_writer.writerow(['MSISDN','RECIPIENT_ID'])
for path in fp.rglob('*.*'):
    if path.stem != '.DS_Store':
        path_parts = path.stem.split('_')
        print(path_parts)
        date = path_parts[0]
        network = path_parts[1]
        print('In mnp aggregator...',date, network)
        #print(path.name)

        if check_file_name(path.name, ['mnp']):
            with open(merged_path, "a", newline="") as csv_file:
                #print('here')
                csv_writer = csv.writer(csv_file)
                #csv_writer.writerow(['MSISDN','DONOR_ID','RECIPIENT_ID','DATE_TIME_STAMP'])
                if network == 'mtn' and check_file_name(path.name, ['csv']):
                    with open(path) as mtn:
                        print(path.name)
                        csv_reader = csv.DictReader(mtn)
                        #csv_writer.writerow(csv_reader.fieldnames)
                        for row in csv_reader:
                            #print(row.values())
                            # csv_writer.writerow(row.values())
                            csv_writer.writerow([row['MSISDN'], row['DONOR_ID'], row['RECIPIENT_ID'], row['DATE_TIME_STAMP']])

        # with pdfplumber.open(path) as pdf:
        #     # Create a new CSV file for writing
        #     with open(data_path, "w", newline="") as csv_file:
        #         csv_writer = csv.writer(csv_file)

        #         # Iterate through all pages in the PDF
        #         for page in pdf.pages:
        #             # Extract the text from the page
        #             text = page.extract_text()
        #             # Split the text into lines
        #             lines = text.split("\n")
        #             # Write the lines to the CSV file
        #             for line in lines:
        #                 csv_writer.writerow([line])

        # pdffileobj=open(path,'rb')
        # pdfreader=PyPDF2.PdfFileReader(pdffileobj)
        # x=pdfreader.numPages
        # print(x)
        # pageobj=pdfreader.getPage(1)
        # text=pageobj.extractText()
        # file1 = open(data_path, 'a')
        # file1.writelines(text)

        # reader = PdfReader(path)
        # print(len(reader.pages))

        # file1 = open(path, 'a')
        # tables = camelot.read_pdf(file1)
        # tables[0].df
        # tables.export(data_path, f='csv')
        # tables[0].parsing_report

        # pdf_document = fitz.open(path)
        # with open(data_path, "w") as text_file:
        #     for page in pdf_document:
        #         # Extract the text from the page
        #         text = page.get_text("text")
        #         # Write the text to the text file
        #         text_file.write(text)

        # # Close the PDF document
        # pdf_document.close()