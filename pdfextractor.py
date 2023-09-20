import re 
from pdfminer.high_level import extract_text
from googleSheetsWriter import googleSheetsWriter

#report path = "/home/theopaulo/Documents/PythonFiles/GithubProjects/Gmail-to-Google-Sheets/report.pdf"


def pdfExtractor(filePath: str):
    text = extract_text(filePath)
    textList = text.split()
    date = "{} {} {}".format(textList[0], textList[1], textList[3])

    debitCardRow1 = textList[51]

    debitCardRow2 = textList[56]

    debitCardRow3 = textList[101]

    creditCardRow1 = textList[49]

    creditCardRow2 = textList[54]

    creditCardRow3 = textList[99]

    cashRow1 = textList[50]

    cashRow2 = textList[55]

    cashRow3 = textList[100]

    grossTotal = textList[20]

    refunds = textList[55]

    transactionCount = textList[39]

    averageTicket = textList[47]

    itemCount = textList[52]

    itemsPerTicket = textList[97]

    return([[date, debitCardRow1, creditCardRow1, cashRow1, grossTotal, refunds, transactionCount, averageTicket, itemCount, itemsPerTicket],
                ["", debitCardRow2, creditCardRow2, cashRow2],
                ["", debitCardRow3, creditCardRow3, cashRow3]
            ])

if __name__ == "__main__":
    googleSheetsWriter(pdfExtractor("/home/theopaulo/Documents/PythonFiles/GithubProjects/Gmail-to-Google-Sheets/report.pdf"))

#code for if you want data to be in the same cell
"""
date = "{} {} {}".format(textList[0], textList[1], textList[3])
print(date)

debitCard = "{}\n{}\n{}".format(textList[51], textList[56], textList[101])
print(debitCard)

creditCard = "{}\n{}\n{}".format(textList[49], textList[54], textList[99])
print(creditCard)

cash = "{}\n{}\n{}".format(textList[50], textList[55], textList[100])
print(cash)

grossTotal = "{}".format(textList[20])
print(grossTotal)

refunds = "{}".format(textList[55])
print(refunds)

transactionCount = "{}".format(textList[39])
print(transactionCount)

averageTicket = "{}".format(textList[47])
print(averageTicket)

itemCount = "{}".format(textList[52])
print(itemCount)

itemsPerTicket = "{}".format(textList[97])
print(itemsPerTicket)
"""
