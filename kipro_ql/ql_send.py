

from .myfunc import get_toml
from .util_ql import *
from .ql_sample import get_conf

def ql_send(path='ql/qlconf.toml'):
    conf = get_conf()
    qlconfs = get_toml(path=path).get('青龙')
    for qlconf in qlconfs:
        for key in qlconf.keys():
            exec(f'{key} = "{qlconf.get(key)}"')
        token = ql_ini(qlurl,qlid,qlsecret)
        envs = ql_envs(qlurl,token)
        msg = []
        for name,value,app in conf:
            msg.append(send2ql(qlurl,token,envs,name,value,app))
    return msg

