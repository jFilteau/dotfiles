#!/usr/bin/env python
import subprocess, os

proc = subprocess.Popen("xrandr | grep '*'", stdout=subprocess.PIPE, shell=True)
res = proc.stdout.read().split()[0]
lock = '/home/justin/.i3/lock.png'
TMPBG = '/tmp/screen.png'

os.system('convert -size ' + res + ' xc:none ' + TMPBG)
os.system('ffmpeg -f x11grab -video_size ' + res + ' -y -i $DISPLAY -i ' + lock + ' -filter_complex "boxblur=5:1,overlay=(main_w-overlay_w)/2:(main_h-overlay_h)/2" -vframes 1 ' + TMPBG + ' -loglevel quiet')
os.system('i3lock -i ' + TMPBG)
os.system('rm ' + TMPBG)