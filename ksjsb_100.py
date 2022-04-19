#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
cron: 0 10 * * *
new Env('快手极速版-提现100');

@Time   : 2022/4/18 11:16
@Author : XuanYi
@File   : ksjsb100.py
@desc   :
助力码：如果不知道自己的助力码就先运行一次，会显示助力码
export ksjsbBoostId=''

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

"""

import os
import sys
import time

so_file_name39 = 'ksjsb100.cpython-39-x86_64-linux-gnu.so'
so_file_name38 = 'ksjsb100.cpython-38-x86_64-linux-gnu.so'
so_file_address = f'wget https://github.com/YIXUANXUAN19/ql-tt/blob/main/Cython-ql/'


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
            print("依赖下载完成，如果没有自动运行，请再次运行此文件\n") if os.popen('echo $?').read() == '0' else print("如果报错，请检查当前目录下是否存在 ksjsb100.cpython-XX-x86_64-linux-gnu.so 文件\n")
            sys.stdout.flush()
        from ksjsb100 import main
        main()
    except ModuleNotFoundError as e:
        print_error_info(e)
    except ImportError as e:
        print_error_info(e)
    except Exception as ex:
        os.popen(f'rm -rf {so_file_name38} > /dev/null').read()
        os.popen(f'rm -rf {so_file_name39} > /dev/null').read()
        print(f'出错了！--{ex} \n请尝试重新运行此文件，如果还是出错则有问题.')
        sys.stdout.flush()
