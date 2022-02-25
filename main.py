# -*- coding:utf-8 -*-
"""
cron: */20 * * * *
new Env('定时更改参数');
"""

from kipro_ql.ql_send import ql_send

msg = ql_send(path='kipro_ql/qlconf.toml')
print('msg')