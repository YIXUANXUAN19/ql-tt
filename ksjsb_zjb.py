#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
cron: 20 10 * * *
new Env('快手极速版-周周十五万');

变量：ksjsbAssistance 指定助力码
export ksjsbAssistance='助力码'
----------------------------------
ck格式需要包含 did 和 kuaishou.api_st :  did=XXX; kuaishou.api_st=XXXXX;

ck变量格式：三选一
可以放环境变量里，一个变量一个ck  ksjsbCookie='ck'
也可以使用 export ksjsbCookie='ck1@ck2@ck3'
也可以使用 export ksjsbCookie='ck1&ck2&ck3'

设置每个账号的间隔时间，设为为0则不等待，默认10秒
export kszjbWait='0'
"""
import os
import sys
import requests

so_file_name39 = 'kszjb.cpython-39-x86_64-linux-gnu.so'
so_file_name38 = 'kszjb.cpython-38-x86_64-linux-gnu.so'
so_file_address = f'https://yixuanxuan19.github.io/ql-tt/Cython-ql/'


def print_error_info(e):
    print(f"出错了-- {e}")
    import importlib.machinery

    print("当前环境支持模块：", importlib.machinery.all_suffixes())
    sys.stdout.flush()

    version = os.popen('python3 --version').read().strip()
    print("当前python3版本：", version)
    sys.stdout.flush()

    print("当前pip3版本：", os.popen('pip3 --version').read().strip())
    sys.stdout.flush()


def download_file(url, times=0, i=0):
    print(f"-- {i + 1} 正在尝试下载依赖文件，请稍等...")
    sys.stdout.flush()
    if i > times:
        print(f"\n下载失败！\n请尝试重试或者手动下载文件到同一目录 {url}")
        sys.stdout.flush()
        exit()
        return
    try:
        res = requests.get(url)
        if len(res.content) <= 0:
            download_file(url, times, i + 1)
        else:
            with open(url.split("/")[-1], 'wb') as f:
                f.write(res.content)
            print("依赖下载完成")
            sys.stdout.flush()
            return res
    except Exception as e:
        print(f"下载出错了--{e}--正在重试")
        sys.stdout.flush()
        download_file(url, times, i + 1)


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
            download_file(so_file_address, times=3)
            # os.popen(so_file_address + ' > /dev/null').read()
            # time.sleep(2)
            # print("请手动查看依赖是否下载完成\n文件名为：kszjb.cpython-XXX.so，如果下载失败，可以尝试再次运行此文件")
        from kszjb import main

        main()
    except ModuleNotFoundError as e:
        download_file(so_file_address, times=3)
        print_error_info(e)
    except ImportError as e:
        print_error_info(e)
        download_file(so_file_address, times=3)
