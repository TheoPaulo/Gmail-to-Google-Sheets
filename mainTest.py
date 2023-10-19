from gmailAPIGetAttachmenttest import APIgetReportAttachmentFromEmail
from googleSheetsWriter import googleSheetsWriter
from pdfextractor import pdfExtractor
import schedule
import os
import time

def getEmailAndWriteSheet():
    try:
        os.remove("/home/theopaulo/Documents/PythonFiles/GithubProjects/Gmail-to-Google-Sheets/report.pdf")
    except:
        pass
    APIgetReportAttachmentFromEmail()

    googleSheetsWriter(pdfExtractor("/home/theopaulo/Documents/PythonFiles/GithubProjects/Gmail-to-Google-Sheets/report.pdf"))

def printSchedulerVerification():
    print("scheduler working")

if __name__ == "__main__":

    schedule.every().day.at("07:00").do(getEmailAndWriteSheet)
    
    while 1:
        schedule.run_pending()
        time.sleep(1)


