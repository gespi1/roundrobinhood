from config import ConfigList, Config
import os

# Determines Environment using PYTHON_ENV variable in the system, and uses $PYTON_ENV.cfg as the apps config file
cfgList = ConfigList()
if os.environ.get('PYTHON_ENV'):
    ENV = os.environ['PYTHON_ENV']
    cfgList.append(Config(file('conf/{0}.cfg'.format(ENV))))
else:
    cfgList.append(Config(file('conf/default.cfg')))

# print cfgList.getByPath('yo.keys.env')

# Plaid Keys
PLAID_KEY_CLIENT_ID = cfgList.getByPath('plaid.key.env')
PLAID_KEY_ENV = cfgList.getByPath('plaid.key.env')
PLAID_KEY_SECRET = cfgList.getByPath('plaid.key.secret')
PLAID_KEY_PUBLIC_KEY = cfgList.getByPath('plaid.key.public_key')
PLAID_KEY_PRODUCTS = cfgList.getByPath('plaid.key.products')
