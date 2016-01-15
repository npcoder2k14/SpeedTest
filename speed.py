import urllib2
import os,time
def download(p):
        proxydict = {
                    "http" : "http://edcguest:edcguest@"+p+":3128" 
                    }
        url = 'http://tvshows4mobile.com/download/17447'
        header = { 'USER_AGENT' : 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:43.0) Gecko/20100101 Firefox/43.0'}
        proxy = urllib2.ProxyHandler(proxydict)
        auth = urllib2.HTTPBasicAuthHandler()
        opener = urllib2.build_opener(proxy, auth, urllib2.HTTPHandler)
        urllib2.install_opener(opener)
        print "Connecting with %s ..." %(p)
        try : 
            r = urllib2.urlopen(urllib2.Request(url, headers = header),timeout=10)
        except:
            print "proxy %s is down" %p  
            return     
        content_length = r.headers['content-length']
        session_data=0
        print "Getting proxy status..."
        start_time=time.time()
        f = open("file12346.3gp","wb")
        data = r.read(1024)
        while data :
            f.write(data)
            session_data += len(data)
            if(int(time.time()) == int(start_time+10)):
                break
            data=r.read(1024)
        f.close()
        speed=session_data/(1024*10.0)
        print "Speed for %s is %.2f KBps" %(p,speed)
        os.system("rm file12346.3gp")

def Main():
        print "Starting proxy test..."
        print "##############################################################"
        proxy=['172.31.102.29','172.31.103.29','172.31.100.29','172.31.102.14','172.31.100.30','172.31.100.26']
        
        for element in proxy:
            download(element)


if __name__=="__main__" :
    Main()


