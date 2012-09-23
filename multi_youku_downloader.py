import urllib,urllib2
import sys
import re
from subprocess import Popen
address = 'http://www.flvcd.com/parse.php?'
agent = 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.6; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3'
start = 1

def fetchLink(url):
    global start
    """fetch link for the input parameters"""
    para = {'flag' : '', 'format' : '', 'kw' : url}
    req = address + urllib.urlencode(para)
    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', agent)]
    data = opener.open(req).read().decode('gb2312')
    # print re.findall("if\(copyToClipboard\('(http.*)'\)\)\{alert",data)
    links = re.findall("(http.*)\s*<[A-Z]>",data)
    #info = re.findall(".{5,20}(.*?)",data)[0]
    info = start
    start = start+1
    for (index,link) in enumerate(links):
        print link
        Popen(['wget','-c', link, '-U', agent,'-O', str(info) + '_' + str(index+1) + '.flv']).wait()


def main():
    global start
    """main method"""
    # tudou.com
    # fetchLink("http://www.tudou.com/programs/view/xHeuSl-QKAI/tid=-1&aid=4573&pid=41010010&oid=100957&isNielson=0")
    # youku.com
    #fetchLink("http://v.youku.com/v_show/id_XNzkyMzk1NDg=.html")
    if len(sys.argv) >= 1:
	start = int(sys.argv[2])
	file_handle = open(sys.argv[1])
	lines = file_handle.readlines()
	for line in lines:
		fetchLink(line)


if __name__ == "__main__":
    main()
