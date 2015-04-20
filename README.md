# rpi-cpu-alarm
App for notify the CPU Temperature on Raspberry Pi via Mail

Install: 

git clone https://github.com/unixweb/rpi-cpu-alarm

Create Crontab Entry:

*/15 *   * * *  pi /usr/bin/python  /home/pi/rpi-cpu-alarm/alarm.py 
