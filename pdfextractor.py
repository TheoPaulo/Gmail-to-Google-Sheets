import re 
from pdfminer.high_level import extract_pages, extract_text

text = extract_text("/home/theopaulo/Documents/PythonFiles/GithubProjects/Gmail-to-Google-Sheets/report.pdf")

textList = text.split()
print(textList)

date = "Date = {} {}".format(textList[0], textList[1])
print(date)

debitCard = "Debit Card = {} {} {}".format(textList[51], textList[56], textList[101])
print(debitCard)

creditCard = "Credit Card = {} {} {}".format(textList[49], textList[54], textList[99])
print(creditCard)

cash = "Cash = {} {} {}".format(textList[50], textList[55], textList[100])
print(cash)

grossTotal = "Gross Total = {}".format(textList[20])
print(grossTotal)

refunds = "Refunds = {}".format(textList[55])
print(refunds)

transactionCount = "Transaction Count = {}".format(textList[39])
print(transactionCount)

averageTicket = "Average Ticket = {}".format(textList[47])
print(averageTicket)

itemCount = "Item Count = {}".format(textList[52])
print(itemCount)

itemsPerTicket = "Items Per Ticket = {}".format(textList[97])
print(itemsPerTicket)

print(textList.index("1.79"))



"""
print(text.replace("\n", " "))

matches2 = re.compile(r"(\d+|\d{1,3}(,\d{3})*)(\.\d+)?").findall(text)

pattern = re.compile(r"[0-9]+.{1}[0-9]{2}").findall(text)

matches1 = re.search('[0-9]{1,3}(,[0-9]{3})*\.[0-9]+', text)


match = re.search(r"\d{1,3}(,\d{3})*\.\d{2}", text)
i = 1

print(match)

while match:
    print("\nMatched string is", match.group(0))
    print("and it is " + str(i) + "in the list")
    i += 1
    
 
    # suffix to find the rest of the string.
    text = text[(match.end()):]
    match = re.search(r"\d{1,3}(,\d{3})*\.\d{2}", text)


#print(pattern)
"""

