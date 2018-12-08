import os
import sys




# OS Compatibility : Coloring
if sys.platform.startswith('win'):
    R, B, Y, C, W = '\033[1;31m', '\033[1;37m', '\033[93m', '\033[1;30m', '\033[0m'
    try:
        import win_unicode_console, colorama
        win_unicode_console.enable()
        colorama.init()
    except:
        print('[-] Error: Coloring libraries not installed')
        R, B, Y, C, W = '', '', '', '', ''
else:
    R, B, Y, C, W = '\033[1;31m', '\033[1;37m', '\033[93m', '\033[1;30m', '\033[0m'
def header():
    print('''%s
  ____    _    ____  _   ___   __
 / ___|  / \  |  _ \| | | \ \ / /
| |  _  / _ \ | |_) | |_| |\ V / 
| |_| |/ ___ \|  __/|  _  | | |  
 \____/_/   \_\_|   |_| |_| |_|  
                                              /|              
         %sBy Raji Abdulgafar - @_mrgaphy%s    \|%s          #GAPHY %s 
        '''%(Y, B, R, C, W))
       
url = str(sys.argv[1])
def httpHeader():
	#req = os.system("curl http://api.hackertarget.com/httpheaders/?q=" + url)
	#headers = ['Server', 'x-runtime','user-agent','content-type','content-encoding', 'Via', 'X-Powered-By', 'X-Country-Code']
	#for header in headers:
	#	try:
	#		req = os.system("curl http://api.hackertarget.com/httpheaders/?q=" + url)

	#		print '%s: %s' % (header, req)
	#	except Exception, error:
	#		print '%s: Not found' % header
	os.system("curl http://api.hackertarget.com/httpheaders/?q=" + url)
def ip():
	os.system("ping " + url)
# Reverse ip lookup
def reverseHackTarget():

	os.system("curl http://api.hackertarget.com/reverseiplookup/?q=" + url)
# traceroute
def traceRoute():

	os.system("curl http://api.hackertarget.com/mtr/?q=" + url)
# wHOIS LOokup
def whoIs():

	os.system("curl http://api.hackertarget.com/whois/?q=" + url)
# DNS Lookup
def dns():

	os.system("curl http://api.hackertarget.com/dnslookup/?q=" + url)
# Reverse DNS lookup
def reverseDns():

	os.system("curl http://api.hackertarget.com/reversedns/?q=" + url)
#GeoIP Lookup
def geoIp():

	os.system("curl http://api.hackertarget.com/geoip/?q=" + url)
# port scan
def nmap():

	os.system("curl http://api.hackertarget.com/nmap/?q=" + url)

def findSharedServer():

	os.system("curl http://api.hackertarget.com/findshareddns/?q=" + url)

def pageLinks():

	os.system("curl http://api.hackertarget.com/pagelinks/?q=" + url)
def gaphy():
	header()
	httpHeader()
	reverseHackTarget()
	traceRoute()
	nmap()
	#reverseDns()
	dns()
	whoIs()
	pageLinks()


if __name__ == '__main__': gaphy()
