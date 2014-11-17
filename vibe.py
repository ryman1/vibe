import androidhelper as android
import time


def speaklen(len):
	droid.ttsSpeak(str(pulselen))
	time.sleep(.5)

def vibe(pl, sl, tl):
	vibestarttime = time.time()
	while True:
		droid.vibrate(pl)
		time.sleep(sl)
		if time.time()- vibestarttime > tl:
			 break

		
	

droid = android.Android()
droid.vibrate(5000)		
pulselen = 1000.0
sleeplen = .2
interval = .5
scriptstarttime = time.time()
runtime = scriptstarttime

while runtime - scriptstarttime < 15:

	vibe(pulselen, sleeplen, interval)
		
	

	