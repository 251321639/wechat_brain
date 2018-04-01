# Python知乎答题王答题器

## 效果
<img width="30%" src="./images/result.png">


## 原理说明

1. 通过 Charles抓包，获取 https://question.hortor.net/question/bat/ 返回的json数据，并保存成文件
<img width="50%" src="./images/findQuiz.png">

2. 通过watchdog监测question.hortor.net/question/bat/目下文件的变化，去响应对应的方法
```
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
			print('fightresult')
			time.sleep(3)
			adbshell.back()
			time.sleep(3)
			adbshell.tap('start')
```

3.获取题目后，如果题目在数据库中，直接返回答案。否则通过百度搜索题目信息，并统计选项出现的次数，出现的最多的选项就当作答案。

4.通过adb shell input tab 模拟点击选项(自动版的只在小米6上试过)

- [使用说明](https://github.com/251321639/wechat_brain/wiki/%E8%AF%A6%E7%BB%86%E4%BD%BF%E7%94%A8%E6%95%99%E7%A8%8B)




