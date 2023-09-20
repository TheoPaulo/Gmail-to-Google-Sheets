from gmailGetAttachmenttest import getReportAttachmentFromEmail
from googleSheetsWriter import googleSheetsWriter
from pdfextractor import pdfExtractor


if __name__ == "__main__":
    getReportAttachmentFromEmail()

    googleSheetsWriter(pdfExtractor("/home/theopaulo/Documents/PythonFiles/GithubProjects/Gmail-to-Google-Sheets/report.pdf"))

