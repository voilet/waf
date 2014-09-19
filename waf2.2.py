#!/usr/bin/env python
#-*- coding: utf-8 -*-
#=============================================================================
#     FileName: voilet.py
#         Desc:
#       Author: 苦咖啡
#        Email: voilet@qq.com
#     HomePage: http://blog.kukafei520.net
#      Version: 0.0.1
#   LastChange: 2014-09-09
#      History: 
#=============================================================================

import pcap
import dpkt
import time


#初始化ip库
from check_data import hack_filter, hackerinfo
#导入白名单
from config.whiteurl import *

def callback(jdr, data):
    eth = dpkt.ethernet.Ethernet(data)
    ip = eth.data
    tcp = ip.data
    src_ip = '%d.%d.%d.%d' % tuple(map(ord, list(eth.data.src)))
    src_time = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(jdr + 28800))
    try:
        if tcp.dport == 80:

            http = dpkt.http.Request(tcp.data)

            #截取url以便白名单验证
            get_data_url = http.uri.split("?")[0]
            #print http.uri
            check_data = hack_filter(http)
            result = check_data.run()

            if result["status"] and get_data_url not in url_list:

                hack_data = hackerinfo(http, result["acl"], src_ip, src_time)
                hack_status = hack_data.run()

                print hack_status

    except Exception, e:
        #print e
        pass


if __name__ == '__main__':

    pc = pcap.pcap('p2p1')
    pc.setfilter('tcp port 80')
    pc.loop(0, callback)
    print 'All subprocesses done.'
