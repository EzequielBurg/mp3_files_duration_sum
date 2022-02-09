import os
from mutagen.mp3 import MP3
import datetime

def get_formatted_time(time):
	return str(datetime.timedelta(seconds=time)).split('.')[0]

def main():
	path = str(input())

	files = os.listdir(path)

	total_files_time = 0 

	for f in files:
		if f.endswith('.mp3'):
			filePath = path + '/' + f
			audio = MP3(filePath)
			length = audio.info.length
			total_files_time += length

	print("This folder has " + get_formatted_time(total_files_time) + " of music!" )


print('Type the path from here you want to sum the duration of mp3 files:')

main()
