

import glob
import re
from random import randint,choice
from .get_repo import get_repo
from .utils.myfunc import get_toml
from .utils.util_ql import *

def get_msg(qlconfs):
    msg = []
    repo = get_repo()
    
    msg.append(send2ql_remark(qlconfs, 'self', 'txsReadNum',str(randint(10,25)),'淘小说阅读数'))

    with open(sorted(glob.glob(f'/ql/log/{repo}jd_jxgckc/*.log'))[-1],'r',encoding='utf-8') as f:
        r = f.read()
    commodity = choice(re.findall('【(.*?)】',r))
    msg.append(send2ql_remark(qlconfs, 'ql1', 'COMMODITY_NAME',commodity,'京喜工厂商品名'))
    
    return msg




def send2ql_remark(qlconfs,ql,name,value,app):
    qlurl = qlconfs.get(ql).get('qlurl')
    qlid = qlconfs.get(ql).get('qlid')
    qlsecret = qlconfs.get(ql).get('qlsecret')
    token = qlconfs.get(ql).get('token')
    envs = qlconfs.get(ql).get('envs')
    return send2ql(qlurl,token,envs,name,value,app)


def env_send(path='qlconf.toml'):
    '''
    '''
    qlconfs = get_toml(path=path)
    qls = qlconfs.keys()
    for ql in qls:
        qlurl = qlconfs.get(ql).get('qlurl')
        qlid = qlconfs.get(ql).get('qlid')
        qlsecret = qlconfs.get(ql).get('qlsecret')
        token = ql_ini(qlurl,qlid,qlsecret)
        envs = ql_envs(qlurl,token)
        qlconfs[ql]['token'] = token
        qlconfs[ql]['envs'] = envs

    msg = get_msg(qlconfs)
    return msg