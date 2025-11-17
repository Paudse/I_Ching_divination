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
	return [de[0], ch[0]]





@app.route("/", methods=["GET", "POST"])
def index():
    if "index" not in session:
        session["index"] = 0  # 初始化

    if request.method == "POST":
        # texts = read_file()
        # 按下按鈕，切換到下一段文字
        session["index"] += 1
        texts = read_file()

    texts = read_file()
    current_text1 = texts[0]
    current_text2 = texts[1]
    return render_template("index.html", text1=current_text1, text2=current_text2)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))