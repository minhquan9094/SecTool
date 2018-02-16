import socket
import os
import sys
import optparse

def dictionaryFUNC():
    services = {'ftp':21,'ssh':22,'smtp':25,'http':80}
    print services['ftp']

def socket_recive(ipAddress,portAddress):
    socket.setdefaulttimeout(0.1)
    s=socket.socket()
    try:
        s.connect((ipAddress,portAddress))
    except Exception, e:
        print "         Error: " + str(e)
        return
    ans=s.recv(1024)
    print "  "+ ans

def check_SSH_port(ipAdd,portstartAdd,portendAdd):

    for i in range(portstartAdd,portendAdd+1):
        print "Checking %s : %d" % (ipAdd,i)
        socket_recive(ipAdd,i)




#check_SSH_port()
#print sys.argv[1]

# suat thong bao khi error
parser=optparse.OptionParser('usage %prog -M <mode> -H <target host> -p <target port>')

# add cac option:
##      1. mode
###         (1) : 1 ip
###         (2) : rangePort
##      2. Host
##      3. Port

parser.add_option('-M' , dest='tgtMode', type='string', help='specify mode for scan'
                                                             '(1): check 1 IP - 1 port'
                                                             '(2): check 1 IP - range port')
parser.add_option('-H' , dest='tgtHost', type='string', help='specify target host')
parser.add_option('-p' , dest='tgtPort' , type='string', help='specify target port')

# option for range IP
parser.add_option("--sH" , dest='startHost', type='string', help='specify start Host')
parser.add_option('--eH' , dest='endHost', type='string', help='specify end Host')

# option for range IP
parser.add_option("--sp" , dest='startPort', type='string', help='specify start Port')
parser.add_option('--ep' , dest='endPort', type='string', help='specify end Port')

# option for some port
parser.add_option('--ap' , dest='anyPort', type='string', help='specify any port[0-n]')


(options,args)=parser.parse_args()

tgtMode=options.tgtMode
tgtHost=options.tgtHost
tgtPort=options.tgtPort

endHost=options.endHost
startHost=options.startHost

startPort = options.startPort
endPort = options.endPort

anyPort= str(options.anyPort).split(",")


if (tgtMode == None):
    print parser.usage
    exit(0)
    
### (1): check 1 IP - 1 port
elif(tgtMode == "1"):
    if (tgtHost== None) | (tgtPort==None):
        print parser.usage
    else:
        print "Checking IP: %s port: %s" % (tgtHost,tgtPort)
        socket_recive(tgtHost,int(tgtPort))


#### (2): check 1 IP - range port
elif (tgtMode == "2"):
    if (startPort==None) | (endPort == None) | (tgtHost==None):
        print parser.usage
    else:
        print "Checking IP: %s in range port: %s -> %s " % (tgtHost,startPort,endPort)
        check_SSH_port(tgtHost,int(startPort),int(endPort))

#### (3): check 1 IP - any port
elif (tgtMode == "3"):
    if ((tgtHost==None) | (anyPort[0]== None)):
        print parser.usage
    else:
        print "Checking IP: %s in port: %s  " % (tgtHost,anyPort)
        for i in range(len(anyPort)):
            print "Checking IP: %s port: %s" % (tgtHost, anyPort[i])
            socket_recive(tgtHost, int(anyPort[i]))
