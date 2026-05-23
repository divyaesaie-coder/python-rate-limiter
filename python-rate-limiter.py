#Rate Limiter (Backend Logic)

import time
count=0
while True:
	input("Press enter to send a request:")
	if count<3:
		count+=1
		print("Request sent:")
	else:
		print("Limit exceeded,Waiting a Minute....")
		time.sleep(60)
		count=0
