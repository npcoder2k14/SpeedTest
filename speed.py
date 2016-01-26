import urllib2
import os,time,sys
from multiprocessing import *

def download(p):
     try:
        proxydict = {
                    "http" : "http://heed:ravi@"+p+":3128",
                    "https" : "http://edcguest:edcguest@"+p+":3128",
                    }
        #url = 'http://tvshows4mobile.com/download/16539'
        url = 'http://mirror2.internetdownloadmanager.com/idman625build10.exe?b=1&filename=idman625build10.exe'
        header = { 'User-Agent' : 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:43.0) Gecko/20100101 Firefox/43.0'}
        proxy = urllib2.ProxyHandler(proxydict)
        auth = urllib2.HTTPBasicAuthHandler()
        opener = urllib2.build_opener(proxy, auth, urllib2.HTTPHandler)
        urllib2.install_opener(opener)
        k = p.split(".")
        file1="."+str(k[3])+str(k[2])
        if(os.path.isfile(file1)):
            os.system("rm "+file1)
        #print "Connecting with %s ..." %(p)
        try :
            r = urllib2.urlopen(urllib2.Request(url, headers = header),timeout=10)
        except (KeyboardInterrupt,urllib2.socket.error,urllib2.URLError):
            print "proxy %s is down" %p
            return
        content_length = r.headers['content-length']
        session_data=0
        #print "Getting proxy status..."
        session_time=int(time.time())
        start_time=time.time()
        f = open(file1,"wb")
        data = r.read(1024)
        while data :
            f.write(data)
            session_data += len(data)
            if(int(time.time()) == int(session_time+10)):
                print "\rspeed for %s is %.2f KBps\n" %(p,session_data/(1024*(time.time()-start_time))),
                session_time+=10
            try:
                data=r.read(1024)
            except(KeyboardInterrupt,urllib2.URLError,urllib2.socket.error):
                print "some error occured in "+p
                return
        f.close()
        os.system("rm "+file1)
     except (KeyboardInterrupt,SystemExit,urllib2.URLError):
        sys.stdout.write("Some error occurred\n")
        if(os.path.isfile(".10026")):
            os.system("rm .10026")
        if(os.path.isfile(".10029")):
            os.system("rm .10029")
        if(os.path.isfile(".10030")):
            os.system("rm .10030")
        if(os.path.isfile(".10229")):
            os.system("rm .10229")
        if(os.path.isfile(".10329")):
            os.system("rm .10329")
        if(os.path.isfile(".10214")):
            os.system("rm .10214")
        return

def Main():
      print "Starting proxy test..."
      print "##############################################################"
      proxy=['172.31.102.29','172.31.100.29','172.31.103.29','172.31.100.26','172.31.100.30','172.31.102.14']
      try:
            p=Pool(6)
            p.map(download,proxy)
          #  os.system("clear")
      except (KeyboardInterrupt,SystemExit,urllib2.socket.error,urllib2.URLError):
            print "Some error occurred"
            if(os.path.isfile(".10026")):
                os.system("rm .10026")
            if(os.path.isfile(".10029")):
                os.system("rm .10029")
            if(os.path.isfile(".10030")):
                os.system("rm .10030")
            if(os.path.isfile(".10229")):
                os.system("rm .10229")
            if(os.path.isfile(".10329")):
                os.system("rm .10329")
            if(os.path.isfile(".10214")):
                os.system("rm .10214")
if __name__=="__main__" :
    Main()
