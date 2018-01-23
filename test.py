import json
import sqlite3
import sql


conn = sqlite3.connect("mistakes_collection.db")
print('Opened database successfully')

'''创建数据库'''

'''
try:
	conn.execute('''CREATE TABLE MISTAKE
			(ID INTEGER PRIMARY KEY,
			QUESTION TEXT UNIQUE,
			ANSWER TEXT NOT NULL);''')
	print('Table created successfully')
except:
	print('Table mistake already exists please ignore')
def get_right_answer(findQuiz,choose):
with open('question.hortor.net/question/bat/findQuiz', encoding='utf-8') as findQuiz,\
	open('question.hortor.net/question/bat/choose', encoding='utf-8') as choose:
	dit = json.load(findQuiz)
	question = dit['data']['quiz']
	choose = json.load(choose)['data']['option']
	right_answer = dit['data']['options'][choose]
	print('问题:%s' % question)
	print('正确答案：%s' % right_answer)
	#写入数据库
	try:
		sql = "insert into mistake(question,answer)values('%s','%s')" % (question,right_answer)
		conn.execute(sql)
		conn.commit()
		print('Insert question successfully')
	except:
		print('This question already exists please ignore')
'''


cursor = conn.execute("select id,question,answer from mistake")
#sql = "delete from mistake where id =135 "
#conn.execute(sql)
#conn.commit()
for row in cursor:
	print('ID = ', row[0])
	print('QUESTION = ', row[1])
	print('ANSWER = ', row[2])
print('Select Operation done successfully')




		











#with open('question.hortor.net/question/bat/findQuiz',encoding='utf-8') as f:
#	print(json.load(f)['data']['quiz'],end='')
		