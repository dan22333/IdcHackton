#!/usr/bin/env python
import ImageProcessing as img
import TcpClient as tcp
import sys

def main():
    
    socket = tcp.Connect('127.0.0.1',1024)
    
    if len(sys.argv) == 3:
        img.StartImageProcessing(socket,int(sys.argv[1]),int(sys.argv[2]))
    else:
        img.StartImageProcessing(socket,1,1)
    return

if __name__ == '__main__':
  main()