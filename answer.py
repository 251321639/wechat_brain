import json
import requests
import webbrowser
import urllib.parse
import sqlite3
import sql
import time
import os
import adbshell
import bs4
import watchdog

from bs4 import BeautifulSoup
from watchdog.observers import Observer
from watchdog.events import *

def read_question(f):
	time.sleep(1)
	response = json.load(f)
	f.close()
	os.remove('question.hortor.net/question/bat/findQuiz')
	question = response['data']['quiz']
	options = response['data']['options']
	sql_result=sql.sql_match_result('"%s"' % question)
	if sql_result:
		print('Question: '+question)
		print('绝对正确答案:%s' % sql_result)
		while not os.path.exists('question.hortor.net/question/bat/choose'):
			time.sleep(0.5)
			adbshell.tap('option' + str(options.index(sql_result)))
	else:
		count_base(question, options)
	return response


#搜索答案并输出
def count_base(question,choices):
    print('\n-- 题目搜索结果包含选项词频计数法 --\n')
    # 搜索答案
    req = requests.get(url='http://www.baidu.com/s', params={'wd':question})
    counts = []
    print('Question: '+question)

    for i in range(len(choices)):
        counts.append(req.text.count(choices[i]))
	
	#输出答案
    counts = list(map(int, counts))
    index_max = counts.index(max(counts))
    index_min = counts.index(min(counts))
    print(counts)
    if counts == [0,0,0,0]:
        print("这题不会...")

    elif '不' in question:
        print('**请注意此题可能为否定题,否定题选第一个选项**')
        print("答案可能是：{0} 或者 {1}".format(choices[index_min],choices[index_max]))
    else:
        print("答案是：{0}".format(choices[index_max]))
    print(index_max)
    while not os.path.exists('question.hortor.net/question/bat/choose'):
        time.sleep(0.5)
        adbshell.tap('option' + str(index_max))

#监听文件
class FileEventHandler(FileSystemEventHandler):
	def __init__(self):
		FileSystemEventHandler.__init__(self)
	
	def on_created(self,event):
		global quiz
		if event.src_path.split('/')[-1] == 'findQuiz':
			with open('question.hortor.net/question/bat/findQuiz', encoding='utf-8') as f:
				quiz=read_question(f)
		elif event.src_path.split('/')[-1] == 'choose':
			sql.sql_write(quiz)
		elif event.src_path.split('/')[-1] == 'fightResult':
			print('本局结束')
			time.sleep(3)
			adbshell.back()
			time.sleep(3)
			adbshell.tap('start')

if __name__ == "__main__":
	observer = Observer()
	event_handler = FileEventHandler()
	observer.schedule(event_handler,'question.hortor.net/question/bat/',True)
	print('-----答题器已运行，请开始排位-----')
	observer.start()
	try:
		while True:
			time.sleep(1)
	except KeyboardInterrup:
		observer.stop()
	observer.join()
