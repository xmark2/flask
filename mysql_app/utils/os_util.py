import os

def mkdir(dirName):
	try:
		os.makedirs(dirName)
	except:
		pass

def write_file(file, msg,mode):
	with open(file,mode) as f:
		f.write(msg)