
import glob
import re
from random import randint,choice

def get_conf():
    conf = []
    repo = 'gys619_jdd_'
    
    conf.append(['txsReadNum',str(randint(5,30)),'淘小说阅读数'])

    with open(sorted(glob.glob(f'/ql/log/{repo}jx_factory_commodity/*.log'))[-1],'r',encoding='utf-8') as f:
        r = f.read()
    commodity = choice(re.findall('【(.*?)】',r))
    conf.append(['COMMODITY_NAME',commodity,'京喜工厂商品名'])
    
    return conf
