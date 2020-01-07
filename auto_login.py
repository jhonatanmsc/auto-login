'''
    Script de auto login na rede do ifpi campus central
    ===================================================

    Author: Jhonatanmsc
    Github: https://github.com/jhonatanmsc/auto-login
'''

import pdb
import urllib
import urllib.parse
import urllib.request
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

def login(env):
    # TODO: check if works :D
    myssl = ssl.create_default_context()
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
    print('\nPS: to exit press CTRL-C...')
    print('Applying login as %s\n' % env['USERNAME'])
    while(True):
        try:
            res = login(env)
            print('%d - %s - %s' % (res.status, res.msg, res.getheader('Expires')))
            print('sleep for 5 min...')
            sleep(300)
        except Exception as e:
            print(e)
            sleep(5)
        

if __name__ == '__main__':
    main()