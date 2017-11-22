import time
import hashlib
import urllib.request
import os
import socket
import re
import json

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

#命令行输入
def input(str):
    input = input("input test:")
    print("your input:", input)
    return input

#文件读写
def fileReadwrite():
    fileobj = open("myfile.txt","a")
    for i in range(1,10):
        fileobj.writelines("hello world %s \n"%i)
    fileobj.close()
    fileobj = open("myfile.txt","r+")
    readstr = fileobj.read()
    print("file content:",readstr)
    fileobj.close()

#修改文件名
def fileRename():
    os.rename("testfile.txt", "myfile.txt")

#创建路径
def makeDir(path):
    if (not os.path.exists(path)):
        os.mkdir(path)

#删除路径
def deleteDir(path):
    if (os.path.exists(path)):
        os.rmdir(path)

#修改当前路径
def chdir(path):
    os.chdir(path)

#获取当前路径
def getcwd():
    return os.getcwd()


#遍历指定目录下的文件，并删除符合条件的文件
def deleteFile():
    dirList = os.listdir(os.getcwd())
    for file in dirList:
        print("file name:",file)
        if file=="test.txt":
            os.remove(file)

#模拟浏览器访问网页，返回网页html
def getHtml(weburl):
    webheader = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    req = urllib.request.Request(url=weburl, headers=webheader)
    webPage = urllib.request.urlopen(req)
    data = webPage.read()
    data = data.decode('UTF-8')
    return data

#通过图片url保存图片到指定的本地路径
def saveWebImg(imageurl, imagesavepath):
    urllib.request.urlretrieve(imageurl, imagesavepath)


#设置网络请求的timeinterval
def setNetworkTimeOut(time):
    socket.setdefaulttimeout(time)


#获取格式化时间(xxxx-xx-xx xx:xx:xx)
def getlocaltime():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


#JSON解析
def string2Json(string):
    return json.loads(string)

def dict2Json(dict):
    return json.loads(json.dumps(dict))

#正则表达式(regex)
def findByRegex(stringData, regex):
    #regex = r't[a-z]{1,}'
    pattern = re.compile(regex)
    return pattern.findall(stringData)
