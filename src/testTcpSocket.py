import socket
import time
import datetime


def tcptesting(server,port,timeout=5):
    s = socket.socket(
        socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)
    success = True
    try:
        s.connect((server, port))
    except Exception, e:
        success = False
    finally:
        s.close()
    return success

if __name__=="__main__":
    log="/tmp/tcptesting.log"
    server = "westfieldwifi.skyfii.com"
    port = 80
    f = open(log,'w+');
    testingtime = 7200
    for a in xrange(0,testingtime):
        if tcptesting(server,port):
            f.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " testing %s on tcp port %d is good\n" %(server,port))
        else:
            f.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " testing %s on tcp port %d is failed or timedout\n" %(server,port))
        time.sleep(1)
        f.flush()
    f.close()
