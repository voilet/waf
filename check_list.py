# !/usr/bin/env python
#-*- coding: utf-8 -*-
#=============================================================================
#     FileName: check_list.py
#         Desc:
#       Author: 苦咖啡
#        Email: voilet@qq.com
#     HomePage: http://blog.kukafei520.net
#      Version: 0.0.1
#   LastChange: 2014-09-16
#      History: 
#=============================================================================
import requests

# while True:
headers = {
            'User-agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1) HTTrack'
        }
s = requests.get("http://bj.jumei.com/index.php?id=1 select * from user=1 limit 10", headers=headers)
print s.status_code
