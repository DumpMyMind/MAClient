#!/usr/bin/env python
# coding:utf-8
# general registration helper(tw)
# Contributor:
#      fffonion        <fffonion@gmail.com>
from _prototype import plugin_prototype
import random
import time
import sys
import os
import sys
import httplib2
from cross_platform import *
import maclient_network
if PYTHON3:
    raw_input = input
from xml2dict import XML2Dict
__plugin_name__ = 'invitation tool'
__author = 'fffonion'
__version__ = 0.33
hooks = {}
extra_cmd = {"reg":"reg_gen"}
def reg_gen(plugin_vals):
    def do(*args):
        loc = plugin_vals['loc']
        po = plugin_vals['poster']
        logger = plugin_vals['logger']
        if 'player' not in plugin_vals:
            logger.error('玩家信息还没有初始化')
            return
        invid = hex(int(plugin_vals['player'].id))[2:]
        cnt = 0
        logger.warning('如果连续注册遇到code 500\n请明天再试\n或者使用VPN或代理连接(MAClient会在启动时自动读取IE代理)')
        print(du8('招待码 = %s' % invid))
        while True:
            po.cookie = ''
            po.post('check_inspection')
            if loc not in ['jp', 'my']:
                po.post('notification/post_devicetoken', postdata = 'S=nosessionid&login_id=&password=&app=and&token=')
            # s=raw_input('session: ').lstrip('S=').strip()
            # print po.cookie
            while True:
                uname, pwd = '', ''
                while len(uname) < 4 or len(uname) > 14:
                    uname = raw_input('user-name: ')
                while len(pwd) < 8 or len(pwd) > 14:
                    pwd = raw_input('password: ')
                if loc == 'sg':
                    p = 'email=%s@%s&invitation_id=%s&login_id=%s&param=&password=%s&password_confirm=%s&platform=1&param=%s' % (
                        uname, random.choice(['google.com', 'yahoo.com', 'live.com']), invid, uname, pwd, pwd, 
                        '35' + (''.join([str(random.randint(0, 9)) for i in range(10)]))
                        )
                else:
                    p = 'invitation_id=%s&login_id=%s&password=%s&param=%s' % (invid, uname, pwd, '35' + (''.join([str(random.randint(0, 9)) for i in range(10)])))
                # print maclient_network.encode_param(p)
                r, d = po.post('regist', postdata = p)
                if(XML2Dict.fromstring(d).response.header.error.code != '0'):
                    print(XML2Dict.fromstring(d).response.header.error.message)
                    continue
                break
            GET_header = po.header
            GET_header.update({'Cookie':po.cookie})
            # httplib2.Http().request(maclient_network.serv[loc]+'tutorial/next?step=100&resume_flg=1',headers=GET_header)
            # my server add scenario_id=0
            time.sleep(2.328374)
            po.post('tutorial/save_character', postdata = 'country=%s&name=%s' % (random.choice('123'), uname))
            time.sleep(2.123123)
            po.post('tutorial/next', postdata = 'S=%s&step=%s' % (po.cookie, 1000))
            time.sleep(2.123123)
            po.post('tutorial/next', postdata = 'S=%s&step=%s' % (po.cookie, 7025))
            time.sleep(3.123123)
            resp, ct = po.post('tutorial/next', postdata = 'S=%s&step=%s' % (po.cookie, 8000))
            if loc in ['kr', 'sg']:
                # httplib2 doesn't follow redirection in POSTs
                resp, ct = httplib2.Http().request(maclient_network.serv[loc] + 'mainmenu?fl=1', headers = GET_header)
            if len(ct) > 8000:
                cnt += 1
                print('Success. (%d done)' % cnt)
            else:
                print('Error occured.')
            time.sleep(2.232131)
            if raw_input('exit?(y/n)') == 'y':
                print(du8("请重新登录 relogin(rl) 来刷新玩家信息!"))
                break

    return do
    # po.post('tutorial/next?step=100&resume_flg=1')
    # clipboard.SetClipboardText(maclient_network.encode_param(p))
    # raw_input(maclient_network.encode_param('S=%s&step=%s'%(po.cookie,7025)))
    # clipboard.SetClipboardText(maclient_network.encode_param('S=%s&step=%s'%(po.cookie,7025)))
    # raw_input(maclient_network.encode_param('S=%s&step=%s'%(po.cookie,8000)))
    # clipboard.SetClipboardText(maclient_network.encode_param('S=%s&step=%s'%(po.cookie,8000)))
