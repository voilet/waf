# !/usr/bin/env python
#-*- coding: utf-8 -*-
#=============================================================================
#     FileName: acl.py
#         Desc:
#       Author: 苦咖啡
#        Email: voilet@qq.com
#     HomePage: http://blog.kukafei520.net
#      Version: 0.0.1
#   LastChange: 2014-09-01
#      History: 
#=============================================================================

args = [
    "\.\./",
    "\:\$",
    "\$\{",
    "select.+(from|limit)",
    "(?:(union(.*?)select))",
    "having|rongjitest",
    "sleep\((\s*)(\d*)(\s*)\)",
    "benchmark\((.*)\,(.*)\)",
    "base64_decode\(",
    "(?:from\W+information_schema\W)",
    "(?:(?:current_)user|database|schema|connection_id)\s*\(",
    "(?:etc\/\W*passwd)",
    "into(\s+)+(?:dump|out)file\s*",
    "group\s+by.+\(",
    "xwork.MethodAccessor",
    "(?:define|eval|file_get_contents|include|require|require_once|shell_exec|phpinfo|system|passthru|preg_\w+|execute|echo|print|print_r|var_dump|(fp)open|alert|showmodaldialog)\(",
    "xwork\.MethodAccessor",
    "(gopher|doc|php|glob|file|phar|zlib|ftp|ldap|dict|ogg|data)\:\/",
    "java\.lang",
    "\$_(GET|post|cookie|files|session|env|phplib|GLOBALS|SERVER)\[",
    "\<(iframe|script|body|img|layer|div|meta|style|base|object|input)",
    "(onmouseover|onerror|onload)\=",
]

cookie_acl = [
    "\.\./",
    "\:\$",
    "\$\{",
    "select.+(from|limit)",
    "(?:(union(.*?)select))",
    "having|rongjitest",
    "sleep\((\s*)(\d*)(\s*)\)",
    "benchmark\((.*)\,(.*)\)",
    "base64_decode\(",
    "(?:from\W+information_schema\W)",
    "(?:(?:current_)user|database|schema|connection_id)\s*\(",
    "(?:etc\/\W*passwd)",
    "into(\s+)+(?:dump|out)file\s*",
    "group\s+by.+\(",
    "xwork.MethodAccessor",
    "(?:define|eval|file_get_contents|include|require|require_once|shell_exec|phpinfo|system|passthru|preg_\w+|execute|echo|print|print_r|var_dump|(fp)open|alert|showmodaldialog)\(",
    "xwork\.MethodAccessor",
    "(gopher|doc|php|glob|file|phar|zlib|ftp|ldap|dict|ogg|data)\:\/",
    "java\.lang",
    "\$_(GET|post|cookie|files|session|env|phplib|GLOBALS|SERVER)\[",
]

post_acl = [
    "\.\./",
    "select.+(from|limit)",
    "(?:(union(.*?)select))",
    "having|rongjitest",
    "sleep\((\s*)(\d*)(\s*)\)",
    "benchmark\((.*)\,(.*)\)",
    "base64_decode\(",
    "(?:from\W+information_schema\W)",
    "(?:(?:current_)user|database|schema|connection_id)\s*\(",
    "(?:etc\/\W*passwd)",
    "into(\s+)+(?:dump|out)file\s*",
    "group\s+by.+\(",
    "xwork.MethodAccessor",
    "(?:define|eval|file_get_contents|include|require|require_once|shell_exec|phpinfo|system|passthru|preg_\w+|execute|echo|print|print_r|var_dump|(fp)open|alert|showmodaldialog)\(",
    "xwork\.MethodAccessor",
    "(gopher|doc|php|glob|file|phar|zlib|ftp|ldap|dict|ogg|data)\:\/",
    "java\.lang",
    "\$_(GET|post|cookie|files|session|env|phplib|GLOBALS|SERVER)\[",
    "\<(iframe|script|body|img|layer|div|meta|style|base|object|input)",
    "(onmouseover|onerror|onload)\=",
]

url_list = [
    "\.(svn|htaccess|bash_history)",
    "\.(bak|inc|old|mdb|sql|backup|java|class)$",
    "(vhost|bbs|host|wwwroot|www|site|root|hytop|flashfxp).*.rar",
    "(phpmyadmin|jmx-console|jmxinvokerservlet)",
    "java\.lang",
    "/(attachments|upimg|images|css|uploadfiles|html|uploads|templets|static|template|data|inc|forumdata|upload|includes|cache|avatar)/(\\w+).(php|jsp)",
]

useragent = ["(HTTrack|harvest|audit|dirbuster|pangolin|nmap|sqln|-scan|hydra|Parser|libwww|BBBike|sqlmap|w3af|owasp|Nikto|fimap|havij|PycURL|zmeu|BabyKrokodil|netsparker|httperf|bench)"]



