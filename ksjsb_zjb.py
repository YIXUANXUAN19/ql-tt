#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
cron: 20 10 * * *
new Env('快手极速版-周周十五万');

@Time   : 2022/4/14 15:50
@Author : XuanYi
@File   : kszjb.py
@desc   :
每个账号每天都有一次助力机会，但是你一周内只能被同一账号助力一次

export ksjsbAssistance=''
变量：ksjsbAssistance 指定助力码,则所有账号只助力这个助力码
如果没有指定则车头每周助力一次作者，其他号根据排序来互相助力，首先助力排序靠前的号,能保证每个号都能被助力到，实现收益最大化

抓包：二选一
推荐完整cookie:  开头是 kpn=NEBULA; kpf=ANDROID_PHONE;，中间有 did=XXX; kuaishou.api_st=XXXXX;
也可以部分cookie：kuaishou.api_st=XXXXX; did=XXX;   可以只要 kuaishou.api_st=XXX; 但是如果有did的最好把did加上

ck变量格式：三选一
ksjsbCookie='ck'
可以放环境变量里，一个变量一个ck
也可以使用 export ksjsbCookie='ck1@ck2@ck3'
也可以使用 export ksjsbCookie='ck1&ck2&ck3'

可有可无变量：
自定义 User-Agent：export kszjbUA='XXXXX'
设置助力一个账号后的等待时间(默认5秒)：export kszjbWait='5'

如果助力顺序出问题，就删除 kszjb.py.json 文件，这个文件是记录谁给谁助力过的
"""
import os
import sys
import time

so_file_name39 = 'kszjb.cpython-39-x86_64-linux-gnu.so'
so_file_name38 = 'kszjb.cpython-38-x86_64-linux-gnu.so'
so_file_address = f'wget https://yixuanxuan19.github.io/ql-tt/Cython-ql/'


def print_error_info(e):
    print(f"出错了-- {e}")
    import importlib.machinery

    print("当前环境支持模块：", importlib.machinery.all_suffixes())
    sys.stdout.flush()

    version = os.popen('python3 --version').read().strip()
    print("当前python3版本：", version)
    sys.stdout.flush()

    print("当前pip版本：", os.popen('pip --version').read().strip())
    print("当前pip3版本：", os.popen('pip3 --version').read().strip())
    sys.stdout.flush()


if __name__ == '__main__':
    try:
        files = os.listdir()
        if so_file_name39 not in files and so_file_name38 not in files:
            version = os.popen('python3 --version').read().strip()
            print(f"当前版本：{version}")
            if '3.8' in version:
                so_file_address = f'{so_file_address}{so_file_name38}'
            else:
                so_file_address = f'{so_file_address}{so_file_name39}'
            os.popen(so_file_address + ' > /dev/null').read()
            time.sleep(2)
            print("请手动查看依赖是否下载完成\n文件名为：kszjb.cpython-XXX.so，如果下载失败，可以尝试再次运行此文件")
            sys.stdout.flush()
        from kszjb import main
        main()
    except ModuleNotFoundError as e:
        os.popen(f'rm -rf {so_file_name38} > /dev/null').read()
        os.popen(f'rm -rf {so_file_name39} > /dev/null').read()
        print_error_info(e)
    except ImportError as e:
        print_error_info(e)
        os.popen(f'rm -rf {so_file_name38} > /dev/null').read()
        os.popen(f'rm -rf {so_file_name39} > /dev/null').read()
