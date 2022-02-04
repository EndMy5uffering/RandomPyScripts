import os

RESET = '\033[0m'
CLEAR_SCREEN = '\033[2J'

def getColor(r=0, g=0, b=0):
	return '\033[38;2;' + str(r) + ';' + str(g) + ';' + str(b) + 'm';
	
def getColorBG(r=0, g=0, b=0):
	return '\033[48;2;' + str(r) + ';' + str(g) + ';' + str(b) + 'm';

def getDataInFolder(folder, keyword):
	data = {}
	file_count = 0
	folder_Count = 0
	file_size = 0
	color = getColorBG(106, 176, 76) + getColor(19, 15, 64)
	fcolor = getColorBG(240, 147, 43) + getColor(30, 39, 46)
	pcolor = getColorBG(41, 128, 185) + getColor(30, 39, 46) 
	w = color + keyword + RESET
	for (root, dirs, files) in os.walk(folder):
		folder_Count = folder_Count + 1
		if keyword in root:
			print(pcolor+'Path:'+RESET, w.join(root.split(keyword)), RESET,' ')
		for f in files:
			file_count = file_count + 1
			file_size += os.path.getsize(root + '\\' + f)
			if keyword in f:
				print(fcolor + 'File:' + RESET, w.join(root.split(keyword)) + '\\' + w.join(f.split(keyword)), RESET,' ')
	
	kb = file_size/1000
	mb = kb/1000
	gb = mb/1000
	print()
	print('Read:', folder_Count, 'folders and', file_count, 'files with full size:', '{:.2f}'.format(file_size), 'B', '{:.2f}'.format(kb), 'KB', '{:.2f}'.format(mb), 'MB', '{:.2f}'.format(gb), 'GB')
	return data

	
if __name__=='__main__':
	os.system('cls')
	c = getColorBG(255,255,255)+getColor(0,0,0)
	folder = input(c+'Folder to search in:'+RESET+' ')
	keyword = input(c+'Looking for:'+RESET+' ')
	data = getDataInFolder(folder, keyword)
	x = input()