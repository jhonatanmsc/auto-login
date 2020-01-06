'''
    Script de auto login na rede do ifpi campus central
    ===================================================

    Author: Jhonatanmsc
    Github: https://github.com/jhonatanmsc/auto-login
'''

import pdb

def load_env():
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

def internet_is_ok():
    # TODO: procurar uma forma de checkar se a internet esta pegando sem uso de libs externas
    pass

def login():
    # TODO: realizar POST para realizar login sem uso de libs externas
    pass

def main():
    env = load_env()
    
    while(not internet_is_ok()):
        print('Applying login...')
        login()
    else:
        print("Internet is ok.")

    print(env)


if __name__ == '__main__':
    main()