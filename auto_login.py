'''
    Script de auto login na rede do ifpi campus central
    ===================================================

    Author: Jhonatanmsc
    Github: https://github.com/jhonatanmsc/auto-login
'''

import pdb
import http.client as httplib
import urllib
import urllib.parse
import urllib.request
import datetime
import ssl
from time import sleep

def load_env():
    # TODO: in test fase
    env_vars = {}
    with open('.env') as f:
        for line in f:
            if line.startswith('#'):
                continue
            # if 'export' not in line:
            #     continue
            # Remove leading `export `, if you have those
            # then, split name / value pair
            # key, value = line.replace('export ', '', 1).strip().split('=', 1)
            key, value = line.strip().split('=', 1)
            # os.environ[key] = value  # Load to local environ
            env_vars[key.replace(' ', '')] = value.replace(' ', '')
    
    return env_vars

def is_online(env):
    conn = httplib.HTTPConnection(env['URL_TEST'], 80, timeout=5)
    try:
        conn.request("HEAD", "/")
        conn.close()
        return True
    except:
        conn.close()
        return False

def login(env):
    # TODO: check if works :D
    myssl = ssl.create_default_context();
    myssl.check_hostname=False
    myssl.verify_mode=ssl.CERT_NONE
    params = {
            'buttonClicked': env['BTN_CLICKED'],
            'err_flag': env['ERR_FLAG'],
            'err_msg': '',
            'info_flag': env['INFO_FLAG'],
            'info_msg': '',
            'redirect_url': '',	
            'network_name': env['NETWORK_NAME'],
            'username': 	env['USERNAME'],
            'password': 	env['PASSWORD']
        }
    query = urllib.parse.urlencode(params).encode("utf-8")
    res = urllib.request.urlopen(env['URL'], query, context=myssl)
    # pdb.set_trace()
    res.close()
    return res

def main():
    env = load_env()
    while(True):
        print('\nPS: to break press CTRL-C...')
        if(not is_online(env)):
            print('You is offline, applying login as %s...' % env['USERNAME'])
            try:
                res = login(env)
                print('%d - %s - %s' % (res.status, res.msg, res.getheader('Expires')))
            except Exception as e:
                print(e)
        else:
            print('You is logged as %s!' % env['USERNAME'])
        sleep(300)

if __name__ == '__main__':
    main()