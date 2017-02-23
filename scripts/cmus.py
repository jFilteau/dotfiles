#!/usr/bin/env python
import subprocess

proc = subprocess.Popen('cmus-remote -Q', stdout=subprocess.PIPE, shell=True)
status = proc.stdout.read()
proc_info = status.splitlines()
try:
    if proc_info[0].find('stopped') >= 0 or proc_info[0].find('paused') >= 0:
        print(proc_info[0])
    else:
        artist = proc_info[4][11:]

        if proc_info[5].find('album') >= 0:
            album = proc_info[5][10:]
            title = proc_info[6][10:]
            song_info = artist + ' - ' + title + ' (' + album + ')'
        else:
            title = proc_info[5][10:]
            song_info = artist + ' - ' + title

        print(song_info)

except IndexError:
    print('')
