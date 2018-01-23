from watchdog.observers import Observer
from watchdog.events import *
import time

class FileEventHandler(FileSystemEventHandler):
	def __init__(self):
		FileSystemEventHandler.__init__(self)
	
	def on_moved(self,event):
		if event.is_directory:
			print("directory moved from {0} to {1}".format(event.src_path,event.dest_path))
		else:
			print("file moved from {0} to {1}".format(event.src_path,event.dest_path))
	
	def on_created(self,event):
		if event.is_directory:
			print("directory created:{0}".format(event.src_path))
		else:
			print("file created:{0}".format(event.src_path))
	
	def on_modified(self,event):
		if event.src_path.split('\\')[-1] == 'findQuiz':
			print("findQuiz")
		else:
			print("file modified:{0}".format(event.src_path))

if __name__ == "__main__":
	observer = Observer()
	event_handler = FileEventHandler()
	observer.schedule(event_handler,r"d:\src\answer\question.hortor.net\question\bat",True)
	observer.start()
	try:
		while True:
			time.sleep(1)
	except KeyboardInterrup:
		observer.stop()
	observer.join()