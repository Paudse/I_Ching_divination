from flask import Flask, render_template, request, redirect, url_for, session

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
app = Flask(__name__)
app.secret_key = "your_secret_key"  

def read_file():
	
	time_start = time.time()
	with open(foler_file_name, "r", encoding='utf-8') as f: 
		data = f.readlines()

	t1 = []
	t2 = []
	t3 = []
	item_line_num = 4
	for i in range (0,len(data)):
		if i%item_line_num == 0:
			t1.append(data[i].replace('\n', ''))
		if i%item_line_num == 1:
			t2.append(data[i].replace('\n', ''))
		if i%item_line_num == 2:
			t3.append(data[i].replace('\n', ''))



	c = list(zip(t1, t2, t3))
	random.shuffle(c)
	t1, t2, t3 = zip(*c)
	print(colored(t1[0], 'yellow', attrs=['bold']))
	print('卦象:', t2[0])
	print('卦意:', t3[0])
	return [t1[0], t2[0], t3[0]]

@app.route("/", methods=["GET", "POST"])
def index():
    texts = read_file()
    current_text1 = texts[0]
    current_text2 = texts[1]
    current_text3 = texts[2]
    return render_template("index.html", text1=current_text1, text2=current_text2, text3=current_text3)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))