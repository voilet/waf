# !/usr/bin/env python
#-*- coding: utf-8 -*-
#=============================================================================
#     FileName: send.py
#         Desc:
#       Author: 苦咖啡
#        Email: voilet@qq.com
#     HomePage: http://blog.kukafei520.net
#      Version: 0.0.1
#   LastChange: 2014-09-04
#      History: 
#=============================================================================
#
# import amqplib.client_0_8 as amqp
# def main():
#     server = {'host':'192.168.49.5', 'userid':'voilet', 'password':'voilet', 'ssl': False}
#     x_name = 'snort'
#
#     conn = amqp.Connection( server['host'],
#                 userid=server['userid'],
#                 password=server['password'],
#                 ssl=server['ssl'])
#
#     ch = conn.channel()
#     ch.access_request('/hacker_filter', active=True, write=True)
#     ch.exchange_declare(exchange=x_name, type='fanout', durable=True, auto_delete=False)
#
#     while True:
#         msg_body = raw_input('>')
#         msg = amqp.Message(msg_body, content_encoding='UTF-8')
#         msg.properties['delivery_mode'] = 2
#         ch.basic_publish(msg, x_name)
#
#         if msg_body == 'quit':
#             retry = False
#
#     ch.close()
#     conn.close()
# if __name__ == '__main__':
#     main()


import pika
import sys

credentials = pika.PlainCredentials("voilet", "voilet")
conn_params = pika.ConnectionParameters("192.168.49.5", credentials=credentials)
connection = pika.BlockingConnection(conn_params)

channel = connection.channel()
channel.exchange_declare(exchange='/snort', type='direct')

channel.basic_publish(exchange='snort',
                      routing_key="snort",
                      body="hello")

# print " [x] Sent %r:%r" % (routing_key, message)
connection.close()