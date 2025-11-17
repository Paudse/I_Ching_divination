
# folder = "./My_Wortschatz/"
folder = "./"
file = "I_Ching"
# file = "Eight_Trigrams"
de2ch = 1

###
foler_file_name = folder + file + ".txt"

###
import random
from termcolor import colored
import time
from datetime import datetime
import os
os.system('color')
os.system('mode con: cols=100 lines=20')

def test(foler_file_name):
	
	time_start = time.time()
	with open(foler_file_name, "r", encoding='utf-8') as f: 
		data = f.readlines()

	de = []
	ch = []
	item_line_num = 3
	for i in range (0,len(data)):
		if i%item_line_num == 0:
			de.append(data[i].replace('\n', ''))
		if i%item_line_num == 1:
			ch.append(data[i].replace('\n', ''))



	c = list(zip(de, ch))
	random.shuffle(c)
	de, ch = zip(*c)
	print(colored(de[0], 'yellow', attrs=['bold']))
	print('卦意:', ch[0])

if __name__ == '__main__':
	while True:
		print('-----------------------------------------------------')
		print('您所卜得之卦象為:')
		test(foler_file_name)
		print('-----------------------------------------------------')
		testing = input('按任意鍵卜下一卦...')




