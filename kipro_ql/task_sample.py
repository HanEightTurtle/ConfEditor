

import subprocess
import glob
from datetime import datetime

from .get_repo import get_repo

def check_ck():
    repo = get_repo()
    logs = [sorted(log_lst)[-1] for folder in glob.glob(f'/ql/log/{repo}*') if (log_lst:=glob.glob(f'{folder}/*.log'))]
    pd = False
    for log in logs:
        log_time = datetime.strptime(log[-23:-4],'%Y-%m-%d-%H-%M-%S')
        tcha = (datetime.now()-log_time).total_seconds()/60
        if tcha<10:
            with open(log,'r',encoding='utf-8') as f:
                r = f.read()
            if 'cookie已失效' in r:
                pd = True
                break
    if pd:
        p = subprocess.Popen('task /ql/scripts/gys619_jdd_main_wskey.py',
                            shell=True,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT,
                            encoding='utf-8'
                            )
        a = p.communicate()[0]
        msg = 'cookie失效，已更新'
    else:
        msg = 'cookie有效'
    return msg
        
        
        
def run_task():
    '''
    '''
    msg = [check_ck()]
    return msg
    