waf
===
使用pcap和dpkt抓包解包
对80端口数据进行过滤
时时分析，匹配规则打印当次请求所有信息

使用方法
===
修改waf2.2.py中需要抓取网卡的名称
安装python pypcap和dpkt模块

python waf2.2.py即可

效果图如下
===
![sec](http://blog.kukafei520.net/wp-content/uploads/2014/09/waf.jpg)

这里要非常感谢"魏哲"同学，在我遇到抓包大流量问题时给出的解决方法，非常感谢
https://blog.weizhe.net/?p=296

