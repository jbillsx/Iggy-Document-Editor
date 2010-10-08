# Server program

from socket import *
from random import choice
import string

alphabet = 'abcdefghijklmnopqrstuvwxyz123456789'
# Set the socket parameters
host = ""
port = 8971
buf = 1024
addr = (host,port)
i=-1


def GenPasswd():
    newpasswd=""
    chars = string.letters + string.digits
    for x in range(8):
        newpasswd = newpasswd + choice(chars)
    return newpasswd
def GenPasswd2():
    newpasswd=""
    chars = string.letters + string.digits
    for x in range(10):
        newpasswd = newpasswd + choice(chars)
    return newpasswd

class Doc:
    docid="D+1234"
    name="DEMO"
    def setid(self,strvar):
        self.docid=strvar

class Blip:
    blipid="B+!1234"
    text="DEMO TEXT"
    docid=""
    user=""
    def setus(self,name):
        self.user=name
    def setid(self,strvar):
        self.blipid=strvar
    def setdocid(self,newdoc):
        self.docid=newdoc
    def settext(self,newtext):
        self.text=newtext
newdoc=[]
i2=-1
blipnew=[]
# Create socket and bind to address
UDPSock = socket(AF_INET,SOCK_DGRAM)
UDPSock.bind(addr)


# Receive messages
while 1:
	data,addr = UDPSock.recvfrom(buf)
	if not data:
		print "Client has exited!"
		break
	else:
                newdata=data.split(":")
                if newdata[0]=="DOC":
                    if newdata[1]=="NEW":
                        i+=1
                        newdoc.append(Doc())
                        randstr=GenPasswd()
                        newdoc[i].setid(randstr)
                        print "\nAdded new document at'", newdoc[i].docid,"'"
                        UDPSock.sendto(newdoc[i].docid,addr)
                    if newdata[1]=="LIST":
                        for doc in newdoc:
                            print doc.docid
                            UDPSock.sendto(doc.docid,addr)
                if newdata[0]=="BLIP":
                    if newdata[1]=="GET":
                            for blip in blipnew:
                                if blip.blipid==newdata[2]:
                                    if blip.user!=newdata[3]:
                                        UDPSock.sendto(blip.text,addr)
                    if newdata[1]=="LIST":
                        for blip in blipnew:
                            if blip.docid==newdata[2]:
                                print blip.text
                                UDPSock.sendto(blip.text,addr)
                                print blip.blipid
                                UDPSock.sendto(blip.blipid,addr)
                    if newdata[1]=="NUMS":
                        number=0
                        for blip in blipnew:
                            if blip.docid==newdata[2]:
                                number=number+1
                                
                        print number
                        UDPSock.sendto(str(number),addr)
                    if newdata[1]=="ADD":
                        i2+=1
                        blipnew.append(Blip())
                        randstr=GenPasswd2()
                        blipnew[i2].setid(randstr)
                        blipnew[i2].setdocid(newdata[2])
                        print "\nAdded new blip at'", blipnew[i2].blipid,"'"
                        UDPSock.sendto(blipnew[i2].blipid,addr)
                    if newdata[1]=="UPDATE":
                        for blip in blipnew:
                            if blip.blipid==newdata[2]:
                                blip.setus(newdata[4])
                                main=newdata[3].split("\"")
                                blip.settext(main[2])
                                print "\nchanged text to '"+newdata[3]+"'"
                                UDPSock.sendto("done",addr)
                                

# Close socket
UDPSock.close()
