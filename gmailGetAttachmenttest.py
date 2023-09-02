# https://youtu.be/K21BSZPFIjQ
"""
Extract selected mails from your gmail account

1. Make sure you enable IMAP in your gmail settings
(Log on to your Gmail account and go to Settings, See All Settings, and select
 Forwarding and POP/IMAP tab. In the "IMAP access" section, select Enable IMAP.)

2. If you have 2-factor authentication, gmail requires you to create an application
specific password that you need to use. 
Go to your Google account settings and click on 'Security'.
Scroll down to App Passwords under 2 step verification.
Select Mail under Select App. and Other under Select Device. (Give a name, e.g., python)
The system gives you a password that you need to use to authenticate from python.

"""

# Importing libraries
import imaplib
import email
import os
from datetime import date

import yaml  #To load saved login credentials from a yaml file

def searchSinceTodayString():
    todaysDate = date.today().strftime("%d-%b-%Y") 
    return "SINCE \"" + todaysDate + "\""

def searchSubjectString(Subject):
    return 'SUBJECT \"' + Subject + '\"'

with open("credentials.yml") as f:
    content = f.read()
    
# from credentials.yml import user name and password
my_credentials = yaml.load(content, Loader=yaml.FullLoader)

#Load the user name and passwd from yaml file
user, password = my_credentials["user"], my_credentials["password"]

#URL for IMAP connection
imap_url = 'imap.gmail.com'

# Connection with GMAIL using SSL
my_mail = imaplib.IMAP4_SSL(imap_url)

# Log in using your credentials
my_mail.login(user, password)

# Select the Inbox to fetch messages
my_mail.select('Inbox')

#Define Key and Value for email search
#For other keys (criteria): https://gist.github.com/martinrusev/6121028#file-imap-search
#key = "SUBJECT"
#key = 'FROM'
#key = 'SINCE'

#value = '"THEO PAULO, see how to help boost your security level"'
#value = 'customerservice@emcom.bankofamerica.com'
#value = str(date.today())
#value = date.today().strftime("%d-%b-%Y")
#print(type(value))

#criteria = '(SUBJECT "THEO PAULO, see how to help boost your security level")'
criteria = "(" + searchSinceTodayString() + " " + searchSubjectString("Attachment Test Email") + ")"

#_, data = my_mail.search(None, key, value)  #Search for emails with specific key and value
_, data = my_mail.search(None, criteria)

mail_id_list = data[0].split()  #IDs of all emails that we want to fetch 

msgs = [] # empty list to capture all messages
#Iterate through messages and extract data into the msgs list
for num in mail_id_list:
    typ, data = my_mail.fetch(num, '(RFC822)') #RFC822 returns whole message (BODY fetches just body)
    msgs.append(data)

#Now we have all messages, but with a lot of details
#Let us extract the right text and print on the screen

#In a multipart e-mail, email.message.Message.get_payload() returns a 
# list with one item for each part. The easiest way is to walk the message 
# and get the payload on each part:
# https://stackoverflow.com/questions/1463074/how-can-i-get-an-email-messages-text-content-using-python

# NOTE that a Message object consists of headers and payloads.

for msg in msgs[::-1]:
    for response_part in msg:
        if type(response_part) is tuple:
            my_msg=email.message_from_bytes((response_part[1]))
            for part in my_msg.walk():
                if part.get_content_maintype() == 'multipart':
                    continue
                if part.get('Content-Disposition') is None:
                    continue

                filename = part.get_filename()
                att_path = os.path.join("/home/theopaulo/Documents/PythonFiles/GithubProjects/Gmail-to-Google-Sheets", filename)

                if not os.path.isfile(att_path):
                    fp = open(att_path, 'wb')
                    fp.write(part.get_payload(decode=True))
                    fp.close()
            #filename = my_msg.get_filename()
            #print(filename)
            #print(type(filename))
            #my_msg.get_filename()
            #my_msg.get_payload
            #print(my_msg['filename'])
            #print(my_msg['f'])
            #att_path = os.path.join("/Downloads", filename)

            #if not os.path.isfile(att_path):
            #    fp = open(att_path, 'wb')
            #    fp.write(my_msg.get_payload(decode=True))
            #    fp.close()
            
            print("_________________________________________")
            print ("subj:", my_msg['subject'])
            print ("from:", my_msg['from'])
            print ("body:")
            for part in my_msg.walk():  
                #print(part.get_content_type())
                if part.get_content_type() == 'text/plain':
                    print (part.get_payload())
            
