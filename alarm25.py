#!/usr/bin/python

import os
import smtplib
import time
from email.mime.text import MIMEText

mailserver = "XXXX.de"
smtpport = 25
smtpuser = "XXXX"
smtpasswd = "XXXXX"
recipient = "XXXX@XXXX.de"
smtpsender = "alarm@XXXX.de"
alarmtemp =  25

day = repr(time.localtime()[2]) + "."+repr(time.localtime()[1])+"."+repr(time.localtime()[0])
zeit = repr(time.localtime()[3]) + ":" + repr(time.localtime()[4]) + ":"+ repr(time.localtime()[5])

def getCPUtemperature():
    res = os.popen('vcgencmd measure_temp').readline()
    return(res.replace("temp=","").replace("'C\n",""))

temp_float = float(getCPUtemperature())

if (temp_float > alarmtemp):
    server = smtplib.SMTP(mailserver, smtpport)
    server.login(smtpuser, smtpasswd)

    value = "Die aktuelle Temperatur des Raspberry Pi liegt bei "+ getCPUtemperature()+" Grad Celsius.\n Zeit: "+zeit+ " am " + day
    msg = MIMEText(value)
    msg['Subject'] = "[Warnung] Temperatur "+ getCPUtemperature()+" Grad!"
    msg['From'] = "RPi Temperature"
    msg['To'] = recipient
    server.sendmail(smtpsender, recipient, msg.as_string())
    server.quit()
