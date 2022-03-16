

import glob
import re
from random import randint,choice
from .get_repo import get_repo
from .utils.myfunc import get_toml
from .utils.util_ql import *

def get_conf():
    conf = []
    repo = get_repo()
    
    conf.append(['txsReadNum',str(randint(10,25)),'淘小说阅读数'])

    with open(sorted(glob.glob(f'/ql/log/{repo}_jx_factory_commodity/*.log'))[-1],'r',encoding='utf-8') as f:
        r = f.read()
    commodity = choice(re.findall('【(.*?)】',r))
    conf.append(['COMMODITY_NAME',commodity,'京喜工厂商品名'])
    
    return conf






def env_send(path='ql/qlconf.toml'):
    '''
    '''
    conf = get_conf()
    qlconfs = get_toml(path=path).get('青龙')
    for qlconf in qlconfs:
        for key in qlconf.keys():
            qlurl = qlconf.get('qlurl')
            qlid = qlconf.get('qlid')
            qlsecret = qlconf.get('qlsecret')
        token = ql_ini(qlurl,qlid,qlsecret)
        envs = ql_envs(qlurl,token)
        msg = []
        for name,value,app in conf:
            msg.append(send2ql(qlurl,token,envs,name,value,app))
    return msg