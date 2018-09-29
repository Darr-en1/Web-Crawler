import urllib.request
response = urllib.request.urlopen('http://python.org/')
result = response.read().decode('utf-8')
if __name__ == '__main__':
    print(response.read().decode('utf-8')) #返回也买你

    print(response.geturl())        #返回URL，用于看是否有重定向
    print(response.getcode())       #返回回复的HTTP状态码
    print(response.info())          #返回元信息
