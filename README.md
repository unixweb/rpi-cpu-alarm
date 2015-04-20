# rpi-cpu-alarm
App for notify the CPU Temperature on Raspberry Pi via Mail<p>

<b>Install:<p></b> 

git clone https://github.com/unixweb/rpi-cpu-alarm<p>


<b>Define your Variables:<p></b>

mailserver = "XXXX.de"   	      Add your SMTP-Mailserver<p>
smtpport = 25             	    Add your SMTP-Mailserver Port mostly Port :25<p>
smtpuser = "XXXX"         	    Add your Username example :  myusername@gmail.com<p>
smtpasswd = "XXXXX"       	    Add your Password for SMTP-Mail Delivery<p>
recipient = "XXXX@XXXX.de"      Add your Mailaddresss example : myusername@gmail.com<p>
smtpsender = "alarm@XXXX.de"    Add your Mailaddress whatever you like<p>
alarmtemp =  55                 Change for testing to 20 only<p>

<b>Create Crontab Entry:<p></b>

vi /etc/cron.d/pi-alarm<p>
*/15 *   * * *  pi /usr/bin/python  /home/pi/rpi-cpu-alarm/alarm.py <p>
