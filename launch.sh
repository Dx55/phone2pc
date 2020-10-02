#/bin/bash
BASEDIR='/var/mobile'
IP='192.168.1.4'
#idke I don't use android or some thin
#SCREENSHOT_LOCATION='/storage/emulated/0/Pictures/Screenshots'
SCREENSHOT_LOCATION='/var/mobile/Media/DCIM/100APPLE'

while true;
do
ssh mobile@$IP python3 $BASEDIR/monitor.py
scp mobile@$IP:$BASEDIR/filename filename
scp mobile@$IP:/$SCREENSHOT_LOCATION/$(cat filename) screen
# do sometin idke
feh -F screen
done
