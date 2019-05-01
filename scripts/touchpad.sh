#!/bin/bash
id=`xinput list --id-only "ETPS/2 Elantech Touchpad"`
xinput --set-prop $id "Synaptics Two-Finger Scrolling" 1 1
