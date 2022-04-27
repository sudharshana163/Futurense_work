import os
import sqlalchemy
import hashlib
import PyPDF2
from PyPDF2 import PdfFileReader, PdfFileWriter
from sqlalchemy import create_engine

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

import getpass

# ---------------Hash lib----------------

hash_fuc = hashlib.sha1()
message ="Python is great"
endoing_message = message.encode()
hash_fuc.update(endoing_message)
string = hash_fuc.hexdigest()
# print(string)
# --------------------Task-------------



files = os.listdir("C:/Users/pc/Desktop/GitHub/Futurense_work")

for x in files:
    if x.endswith(".pdf"):
        if PyPDF2.PdfFileReader(open("C:/Users/pc/Desktop/GitHub/Futurense_work/"+x, 'rb')).isEncrypted:
            continue
        else:
            with open("C:/Users/pc/Desktop/GitHub/Futurense_work/"+x, "rb") as in_file:
                input_pdf = PdfFileReader(in_file)

                output_pdf = PdfFileWriter()
                output_pdf.appendPagesFromReader(input_pdf)

                output_pdf.encrypt(user_pwd="timeline")

                with open("encoded_pdf.pdf", "wb") as out_file:
                    output_pdf.write(out_file)


