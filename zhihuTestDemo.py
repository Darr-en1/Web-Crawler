# -*- coding: utf-8 -*-
import os
import shutil

import requests
from lxml import html
'''
https://www.zhihu.com/question/20899988/answer/165536870

在此基础上做了点优化
'''
headers = {
    'Host': 'www.zhihu.com',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'Upgrade-Insecure-Requests': '1',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
}


def save(text, filename='temp', path='download'):
    fpath = os.path.join(path, filename)
    '''
    w
    打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
    wb
    以二进制格式打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
    '''
    with open(fpath, 'wb') as  f:
        print('output:', fpath)
        f.write(text)


def save_image(image_url):
    resp = requests.get(image_url)
    page = resp.content
    filename = image_url.split('zhimg.com/')[-1]
    save(page, filename)


def crawl(url):
    resp = requests.get(url, headers=headers)
    page = resp.content
    root = html.fromstring(page)
    image_urls = root.xpath('//img[@data-original]/@data-original')
    for image_url in image_urls:
        save_image(image_url)



def mkdir(path):
    folder = os.path.exists(path)

    if folder:
        shutil.rmtree(path)
    os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径
    print("---  new folder...  ---")
    print("---  OK  ---")

if __name__ == '__main__':
    mkdir("download")
    # 注意在运行之前，先确保该文件的同路径下存在一个download的文件夹, 用于存放爬虫下载的图片
    url = 'https://www.zhihu.com/question/26942050/answer/34817491'  # 有一双美腿是一种怎样的体验?
    crawl(url)
