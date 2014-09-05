# !/usr/bin/env python
#-*- coding: utf-8 -*-
#=============================================================================
#     FileName: todo.py
#         Desc:
#       Author: 苦咖啡
#        Email: voilet@qq.com
#     HomePage: http://blog.kukafei520.net
#      Version: 0.0.1
#   LastChange: 2014-09-03
#      History: 
#=============================================================================
import pika

def mqClient_rcv():
    credentials = pika.PlainCredentials("voilet", "voilet")
    conn_params = pika.ConnectionParameters("192.168.49.5", credentials=credentials)
    connection = pika.BlockingConnection(conn_params)

    channel = connection.channel()
    channel.exchange_declare(exchange='/snort', type='direct')

    #here we create 2 temp queues

    channel.basic_consume(callback_a,
                          queue="snort",
                          no_ack=True)
    channel.start_consuming()

def callback_a(ch, method, properties, body):
    print "Queue A Received %r" % (body,)

# def callback_b(ch, method, properties, body):
#     print "Queue B Received %r" % (body,)

mqClient_rcv()