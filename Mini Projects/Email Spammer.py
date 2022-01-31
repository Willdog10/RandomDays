from ast import Str
import smtplib
import string
import time
import random
from email.mime.text import MIMEText
#Open a file for reading

me = 'goalsinmind15@gmail.com' # change to your email
p_reader = open('smith143','rb') # edit for your password
cipher = p_reader.read()
recipients = ['ashley.nicole0499@gmail.com'] # enter recipients here


def spamEveryMinute():
    while (True):
        fp = open('message.txt', 'rb')
        #multipart class is for multiple recipients
        msg = MIMEText(fp.read(), 'plain', 'utf-8')
        fp.close()

        thread_number = random.randint(0, 10000)
        msg['Subject'] = 'Header''Minutely Spam Report (randomizer: ' + str (thread_number + ')', 'utf-8')
        msg['From'] = me
        msg['To'] = 'ashley.nicole0499@gmail.com'.join(recipients)

        s = smtplib.SMTP(host='smtp.gmail.com', port=587)
        s.ehlo()
        s.starttls()
        s.ehlo()
        s.login(me, cipher)
        s.sendmail(me, recipients, msg.as_string())

        print ;'Email sent to: ashley.nicole0499@gmail.com+ ', 
        s.quit()
        time.sleep(10) # change rate of fire here

