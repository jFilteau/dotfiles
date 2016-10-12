#!/usr/bin/env python
import psutil, subprocess, os

process_name = 'cmus'

for p in psutil.process_iter():
	if p.name() == process_name:
		p = subprocess.Popen('cmus-remote -Q', stdout=subprocess.PIPE, shell=True)
		p_info = p.stdout.read()
		artist = p_info.splitlines()[4]
		title = p_info.splitlines()[5]
		song_info = artist[11:] + ' - ' + title[10:]
		os.system('echo ' + song_info)
