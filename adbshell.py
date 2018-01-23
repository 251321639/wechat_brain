import os

conf = {
	"start" : {
		"x" : 620,
		"y" : 1800,
	},
	"option0":{
		"x" : 540,
		"y" : 1040,
	},
	"option1":{
		"x" : 540,
		"y" : 1230,
	},
	"option2":{
		"x" : 540,
		"y" : 1420,
	},
	"option3":{
		"x" : 540,
		"y" : 1610,
	}
}

def tap(option):
	os.popen('adb shell input tap {0} {1}'.format(conf[option]['x'],conf[option]['y']))

def back():
	os.popen('adb shell input keyevent 4')
