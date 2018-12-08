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
	base = os.system("curl http://api.hackertarget.com/httpheaders/?q=" + url)
	return base
def ip():
	base = os.system("ping " + url)
	return base
# Reverse ip lookup
def reverseHackTarget():
	base = os.system("curl http://api.hackertarget.com/reverseiplookup/?q=" + url)
	return base
# traceroute
def traceRoute():
	base = os.system("curl http://api.hackertarget.com/mtr/?q=" + url)
	return base
# wHOIS LOokup
def whoIs():
	base = os.system("curl http://api.hackertarget.com/whois/?q=" + url)
	return base
# DNS Lookup
def dns():
	base = os.system("curl http://api.hackertarget.com/dnslookup/?q=" + url)
	return base
# Reverse DNS lookup
def reverseDns():
	base = os.system("curl http://api.hackertarget.com/reversedns/?q=" + url)
	return base
#GeoIP Lookup
def geoIp():
	base = os.system("curl http://api.hackertarget.com/geoip/?q=" + url)
	return base
# port scan
def nmap():
	base = os.system("curl http://api.hackertarget.com/nmap/?q=" + url)
	return base
def findSharedServer():
	base = os.system("curl http://api.hackertarget.com/findshareddns/?q=" + url)
	return base
def pageLinks():
	base = os.system("curl http://api.hackertarget.com/pagelinks/?q=" + url)
	return base
# Generating reports in HTML format
def generateHTML():
	create = """<!DOCTYPE html>
<html>
<head>
  <title>R3C0N1Z3R Report</title>
</head>
<body>
 <center> <h1>R3C0N1Z3R Report - [{}]</h1></center>
 <strong>HTTP header information</strong>
	<pre>{}</pre>
    <strong>Trace Route</strong>
    <pre>{}</pre> 
  <strong>Whois Information</strong>
	<pre>{}</pre>
	<strong>DNS server record</strong>
	<pre>{}</pre>
	<strong><Nmap- running services/strong>
	<pre>{}</pre>
	<strong>Website on the same server</strong>
	<pre>{}</pre>
	<strong>Reverse IP Address</strong>
	<pre>{}</pre>
	<strong>Page Links</strong>
	<pre>{}</pre><hr>
	<center> All Right Reserved &copy; <strong>R3CON1Z3R</strong></center>
 
</body>
</html>
    """.format(url,httpHeader(),traceRoute(),whoIs(),dns(),nmap(),findSharedServer(),reverseHackTarget(),pageLinks())	
	return create
# Saving the report
def saveHTML():
	saveFile = open(url + '.html', 'w')
	saveFile.write(generateHTML())
	saveFile.close()
	print('{}[+] HTML Report Successfully Generated{}'.format(Y, C))
	print('{}[+] File saved as {}{}.html{}'.format(Y, R, url, C))
	print('{}[+] R3CON1Z3R Operation Completed!{}'.format(Y, W))

def gaphy():
	header()
	saveHTML()


if __name__ == '__main__': gaphy()
