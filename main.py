# -*- coding:utf-8 -*-
"""
cron: */10 * * * *
new Env('定时更改参数');
"""

from kipro_ql.env_sample import env_send
from kipro_ql.task_sample import run_task

msg = [*env_send(path='kipro_ql/qlconf.toml'),*run_task()]

print(msg)