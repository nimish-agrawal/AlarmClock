import time
import os
import random

print 'Hello. I see you need my help.'

minutes = input('After how many minutes should I play the music?\n')
if(minutes == 1):
	print 'Alright do whatever you wanna do. A minute is all you\'ve got'
elif(minutes > 1):
	print 'Alright do whatever you wanna do. I\'ll play the song in ' + str(minutes) + ' minutes.'
else:
	print 'Invalid time entered.\nQuitting.'
	exit()

for i in range(minutes):
    time.sleep(60)
    if (minutes - i -1 == 1):
    	print 'Just one minute remaining!'
    else:
    	print str(minutes - i -1) + ' minutes remaining!'
print 'Okay. Time\'s up!'

while(1):
	track = random.choice(os.listdir("E:\Music\My Music\Music\Misc Collections\FIFA 15 (Soundtrack) (2014)"))
	# Make sure the file selected is a legit .mp3 file and not other file like album art or meta-data file
	if(track.endswith(".mp3")):
		break
# print str(track)
os.startfile("E:\Music\My Music\Music\Misc Collections\FIFA 15 (Soundtrack) (2014)\\" + track)
# os.startfile("wake_.mp3")