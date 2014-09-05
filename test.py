#!/usr/bin/env python
#-*- coding: utf-8 -*-
#=============================================================================
#     FileName: test.py
#         Desc:
#       Author: 苦咖啡
#        Email: voilet@qq.com
#     HomePage: http://blog.kukafei520.net
#      Version: 0.0.1
#   LastChange: 2014-09-01
#      History: 
#=============================================================================

import pcap
import dpkt
import sys
from multiprocessing import Process, Queue, Pool
import time
import multiprocessing, Queue
import os
from time import sleep
from random import randint

#初始化ip库
from api.QQWry import *
from check_data import hack_filter, hackerinfo
#导入白名单
from config.whiteurl import *

pc = pcap.pcap("eth0")    #注，参数可为网卡名，如eth0
pc.setfilter('tcp port 80')    #设置监听过滤器


tt = IPSearch('/home/jm/hacker/api/QQWry.Dat')


class Producer(multiprocessing.Process):
    def __init__(self, queue):
        multiprocessing.Process.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            self.queue.put('one product')
            print multiprocessing.current_process().name + str(os.getpid()) + ' produced one product, the no of queue now is: %d' %self.queue.qsize()
            sleep(randint(1, 3))


class Consumer(multiprocessing.Process):
    def __init__(self, queue):
        multiprocessing.Process.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            d = self.queue.get(1)
            if d != None:
                print multiprocessing.current_process().name + str(os.getpid()) + ' consumed  %s, the no of queue now is: %d' %(d,self.queue.qsize())
                sleep(randint(1, 4))
                continue
            else:
                break

#create queue
queue = multiprocessing.Queue(40)

if __name__ == "__main__":
    print 'come on baby ... 哇咔咔~'
    #create processes
    processed = []
    for i in range(3):
        processed.append(Producer(queue))
        processed.append(Consumer(queue))

    #start processes
    for i in range(len(processed)):
        processed[i].start()
    print processed
    #join processes
    for i in range(len(processed)):
        processed[i].join()





