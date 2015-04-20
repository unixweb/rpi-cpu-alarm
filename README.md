# rpi-cpu-alarm
App for notify the CPU Temperature on Raspberry Pi via Mail

Install: 

git clone https://github.com/unixweb/rpi-cpu-alarm


Define your Variables:

mailserver = "XXXX.de"   	Add your SMTP-Mailserver
smtpport = 25             	Add your SMTP-Mailserver Port mostly Port :25
smtpuser = "XXXX"         	Add your Username example :  myusername@gmail.com
smtpasswd = "XXXXX"       	Add your Password for SMTP-Mail Delivery
recipient = "XXXX@XXXX.de"      Add your Mailaddresss example : myusername@gmail.com
smtpsender = "alarm@XXXX.de"    Add your MAiladdress if you like
alarmtemp =  55                 Change for testing to 20 only

Create Crontab Entry:

*/15 *   * * *  pi /usr/bin/python  /home/pi/rpi-cpu-alarm/alarm.py 
