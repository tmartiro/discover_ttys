#!/usr/bin/env python
''' Author: Tigran Martirosyan, mail:  tmartiro at gmail.com'''
import serial
import subprocess

'''Find serial ports'''
popen = subprocess.Popen("dmesg | awk '/ttyS/ {print $4}'", shell=True, stdout=subprocess.PIPE)
tty_devices = popen.stdout.read().split('\n')

if len(tty_devices) < 1:
 print "no device is found"
 exit(1)

'''Testing serial ports'''
for device in tty_devices:
  s = serial.Serial(port='/dev/' + device, timeout=2)
  s.write(b"\x04\x50\x02\x46\x03\x13")
  out = s.read()
  if len(out) > 0 and out == '\x06':
        print "/dev/" + device
        s.close()
        exit(0)
  s.close()
