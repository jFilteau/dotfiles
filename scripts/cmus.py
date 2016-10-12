#!/usr/bin/env python
import psutil, subprocess, os

process_name = 'cmus'

for p in psutil.process_iter():
	if p.name() == process_name:
		p = subprocess.Popen('cmus-remote -Q', stdout=subprocess.PIPE, shell=True)
		p_info = p.stdout.read().splitlines()
		status = p_info[0][7:]
		artist = p_info[4]
		title = p_info[5]
		song_info = artist[11:] + ' - ' + title[10:]
		if status == 'playing':
			os.system('echo ' + song_info)
