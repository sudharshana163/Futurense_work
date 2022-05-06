import os
import time
import PyPDF2
from PyPDF2 import PdfFileReader,PdfFileWriter
import time
import threading
l=[]
s=len(os.listdir("C:/Users/pc/Desktop/GitHub/Futurense_work/FILES-PDF/"))
def fun1():
    files = os.listdir("C:/Users/pc/Desktop/GitHub/Futurense_work/FILES-PDF/")

    for x in files:
        if x.endswith(".pdf"):
            if PyPDF2.PdfFileReader(open("C:/Users/pc/Desktop/GitHub/Futurense_work/FILES-PDF/" + x, 'rb')).isEncrypted:
                continue
            else:
                with open("C:/Users/pc/Desktop/GitHub/Futurense_work/FILES-PDF/" + x, "rb") as in_file:
                    input_pdf = PdfFileReader(in_file)

                    output_pdf = PdfFileWriter()
                    output_pdf.appendPagesFromReader(input_pdf)

                    output_pdf.encrypt(user_pwd="timeline")

                    with open("encoded"+str(x[:4])+".pdf", "wb") as out_file:
                        output_pdf.write(out_file)

for i in range(s):
    print(s)
    t1=threading.Thread(target=fun1)
    t1.start()
    t1.join()