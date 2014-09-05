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
import time
import re
import json

#初始化ip库
from api.QQWry import *
from check_data import hack_filter, hackerinfo
#导入白名单
from config.whiteurl import *
import pika


pc = pcap.pcap("eth0")    #注，参数可为网卡名，如eth0
pc.setfilter('tcp port 80')    #设置监听过滤器


credentials = pika.PlainCredentials("voilet", "voilet")
# credentials = pika.PlainCredentials("snort", "6a0d92e5a89034069686987f421736d0")
# conn_params = pika.ConnectionParameters("localhost", credentials=credentials)
conn_params = pika.ConnectionParameters("192.168.49.5", credentials=credentials)
connection = pika.BlockingConnection(conn_params)

channel = connection.channel()
channel.exchange_declare(exchange='/snort', type='direct')


for ts, buf in pc:    #ptime为收到时间，pdata为收到数据

    eth = dpkt.ethernet.Ethernet(buf)
    ip = eth.data
    tcp = ip.data
    src_ip = '%d.%d.%d.%d' % tuple(map(ord, list(eth.data.src)))
    src_time = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(ts + 28800))
    try:
        if tcp.dport == 80:

            http = dpkt.http.Request(tcp.data)
            if http.body:
                data = {"uri": http.uri, "headers": http.headers, "http_body": http.body, "body": True,
                        "src_time": src_time, "src_ip": src_ip, "method": "POST", "host": http.headers["host"]}

            else:
                data = {"uri": http.uri, "headers": http.headers, "body": False,
                        "src_time": src_time, "src_ip": src_ip, "method": "GET", "host": http.headers["host"]}

            channel.basic_publish(exchange='snort',
                      routing_key="snort",
                      body=json.dumps(data))

    except:pass

connection.close()

