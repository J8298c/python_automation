import subprocess
import os


def runHoneybee():
    retval = os.getcwd()
    print 'current working dir is %s' % retval
    path = '../../dev/honeybee'
    os.chdir(path)
    newRetVal = os.getcwd()
    print 'current working dir is %s' % newRetVal
    subprocess.call('ls')
    var = raw_input("would you like to run git fetch y/n: ")
    print "you entered", var

    if (var.lower() == 'yes') or (var.lower == 'y'):
        gitFetch()
        print('yopu answeed yes')

    # subprocess.call('gulp', shell=True)
    
 

def gitFetch():
	subprocess.call('git pull', shell=True)
	return

def startWeb():
	subprocess.Popen(cmd2.split())
	subprocess.call('npm start')

runHoneybee()

