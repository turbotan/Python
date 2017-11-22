import time
import hashlib
import urllib.request

def getCurrectTimeSeconds() :
    return int(time.time())

def md5(str):
    return  hashlib.md5(str.encode(encoding="utf-8")).hexdigest()


def httpRequst(url, params):
    postdata = urllib.parse.urlencode(params).encode('utf-8')
    requestHeader = {'User-Agent': 'Fieldworks/1.1 (iPhone; iOS 11.1.2; Scale/2.00)'}
    req = urllib.request.Request(url=url, data=postdata, headers=requestHeader)
    result = urllib.request.urlopen(req)
    return result.read()

def httpRequst(url):
    requestHeader = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36'}
    req = urllib.request.Request(url=url, headers=requestHeader)
    result = urllib.request.urlopen(req)
    return result.read()