# !/usr/bin/env python
#-*- coding: utf-8 -*-
#=============================================================================
#     FileName: receive.py
#         Desc:
#       Author: 苦咖啡
#        Email: voilet@qq.com
#     HomePage: http://blog.kukafei520.net
#      Version: 0.0.1
#   LastChange: 2014-09-04
#      History: 
#=============================================================================
import json, time, os
import pika
import multiprocessing, Queue
# from check_data import hackerinfo, hack_filter



class Producer(multiprocessing.Process):
    def __init__(self, queue):
        multiprocessing.Process.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            # print "进行循环"
            self.queue.put("voilet")


class Consumer(multiprocessing.Process):
    def __init__(self, queue):
        multiprocessing.Process.__init__(self)
        self.queue = queue

    def run(self):
        credentials = pika.PlainCredentials("voilet", "voilet")
        conn_params = pika.ConnectionParameters("192.168.49.5", credentials=credentials)
        connection = pika.BlockingConnection(conn_params)

        channel = connection.channel()
        channel.exchange_declare(exchange='/snort', type='direct')
        channel.basic_consume(callback_a,
                          queue="snort",
                          no_ack=True)
        channel.start_consuming()

def callback_a(ch, method, properties, body):
    print "Queue  %r %s" % (body, os.getpid())
    # #截取url以便白名单验证
    # s = json.loads(body,)
    # print s
    # print json.dumps(s)
    # get_data_url = s["uri"].split("?")[0]
    # print get_data_url, os.getpid()

    # check_data = hack_filter(s)
    # result = check_data.run()
    #
    # if result["status"] and get_data_url not in url_list:
    #
    #     hack_data = hackerinfo(http, result["acl"], src_ip, src_time)
    #     hack_status = hack_data.run()
    #
    #     print hack_status


#create queue
queue = multiprocessing.Queue(40)



if __name__ == '__main__':
    # main()
    #create processes
    processed = []
    for i in range(10):
        processed.append(Producer(queue))
        processed.append(Consumer(queue))

    #start processes
    for i in range(len(processed)):
        processed[i].start()

    #join processes
    for i in range(len(processed)):
        processed[i].join()


