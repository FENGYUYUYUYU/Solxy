# File: SolxyFix.pyc (Python 3.12)

import time
import random
from colorama import init, Fore, Style
init()

def print_server_connection_info():
    print(Fore.BLUE + '[Solxy Fix]服务器登陆中' + Style.RESET_ALL)
    time.sleep(3)
    print('请选择服务器的编号：')
    print('1.花雨庭')


def main():
    print(Fore.BLUE + '欢迎使用Solxy Fix Pro' + Style.RESET_ALL)
    print(Fore.BLUE + '软件作者：KUN X' + Style.RESET_ALL)
    print(Fore.GREEN + '公告：Solxy Fix是以https://github.con/Dingless1337/netease-launcer-reloadsd为基础开发的网易我的世界开端工具箱（闭源），认证服务器有RIP提供，请勿利用Solxy Fix作弊等操作。' + Style.RESET_ALL)
    time.sleep(2)
    print(Fore.BLUE + 'version 1.0服务器连接成功，请输入登陆方式的编号' + Style.RESET_ALL)
    print(Fore.BLUE + '1.sauth Cookies登陆' + Style.RESET_ALL)
    print(Fore.BLUE + '2.4399登陆' + Style.RESET_ALL)
    choice = input('请输入选择登陆方式的编号: ')
# WARNING: Decompyle incomplete

if __name__ == '__main__':
    main()
    return None
