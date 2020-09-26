#Author:Ahmed Mohiy
#27-08-2017
#for Android only
import time
import androidhelper
import os
def clear():
    #to clear the screen
    os.system("clear")
droid = androidhelper.Android()
#this is the main thing ^
def x(n=raw_input):
    droid.ttsSpeak(n)
    droid.makeToast(n)
#line = droid.dialogGetInput("Welcome to the\nVoice Application","Enter your name:")
#msg = "Hello, %s" % (line.result,)
clear()
droid.makeToast("Welcome to XMV")
#lets edit it
start=("Enter what you want me to read:")
droid.ttsSpeak(start)
fmsg=droid.dialogGetInput("-------Main Message------",start)


def sign():
    print """
 ___     ___ __     __  __     __
 \  \   /  /|  \   /  |\  \   /  /
  \  \_/  / |   \ /   | \  \ /  /
   \     /  | |\ V /| |  \  V  /
   /  _  \  | | \ / | |   \   /
  /  / \  \ | |  V  | |    \ /
 /__/   \__\|_|     |_|     V
 
 #XMMR12  Modern  Voice 
                        application\n    
    """
#done already lol
sign()
choice=(fmsg.result)
#todo make if
if (choice.lower()=="e" or choice.lower()=="exit"):
        choice="Exiting now"
        x(choice)
else:
    x(choice)
    while (True):    
        tmsg=droid.dialogGetInput('',start)
        choice=(tmsg.result)
        if (choice.lower()=="e" or choice.lower()=="exit"):
            choice="Exiting now"
            x(choice)
            break
        x(choice)
clear()

#last test
#Lets Test ^.^
