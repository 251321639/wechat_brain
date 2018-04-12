import sqlite3
import json
import time
import os

conn = sqlite3.connect("mistakes_collection.db",check_same_thread=False)

def sql_match_result(question):
	right_answer=''
	sql_cmd = 'select * from mistake where question=' + question
	cursor = conn.execute(sql_cmd)
	for row in cursor:
		right_answer = row[2]
	if not right_answer=='' :
		return right_answer
	else:
		return False
	

def sql_write(quiz):
	with open('question-zh.hortor.net/question/bat/choose', encoding='utf-8') as f:
		time.sleep(1)
		response = json.load(f)
		f.close()
		os.remove('question-zh.hortor.net/question/bat/choose')
		question = quiz['data']['quiz']
		right_choose = int(response['data']['answer']) -1 
		answer = quiz['data']['options'][right_choose]
		print('将题目写入数据库中...')
		try:
			sql = "insert into mistake(question,answer)values('%s','%s')" % (question,answer)
			print(sql)
			conn.execute(sql)
			conn.commit()
			print('写入成功')
		except:
			print('该问题已存在数据库中，跳过')
