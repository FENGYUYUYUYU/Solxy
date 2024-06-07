# File: Solxy.pyc (Python 3.12)

import requests
import time
import random
import re
from flask import Flask, render_template_string
from threading import Thread
from colorama import init, Fore, Style
from datetime import datetime
import sys
init(autoreset = True)

def check_internet_connection():
    urls = [
        'http://www.google.com',
        'http://www.baidu.com',
        'http://www.bing.com']
    for url in urls:
        response = requests.get(url, timeout = 5)
        if response.status_code == 200:
            return True
# WARNING: Decompyle incomplete


def validate_cookies(cookies):
    pattern = re.compile('^{"sauth_json":".*"}$')
    return bool(pattern.match(cookies))


def current_time():
    return datetime.now().strftime('%H:%M:%S')

app = Flask(__name__)
server_info = (lambda : server_pid = random.randint(0x9184E72A000L, 0x5AF3107A3FFFL)html_content = f'''\n    服务器IP：127.0.0.1，端口号：25565，<br>\n    服务器IP由华为云支持，<br>\n    华为云服务器PID编号：{server_pid}<br>\n    @@华为云服务器授权\n    <button onclick="showInfo()">华为云服务器信息</button>\n    <div id="info" style="display:none;">华为云服务器提供代理IP：127.0.0.1 华为云CSS加密技术</div>\n    <script>\n    function showInfo() {{\n        document.getElementById("info").style.display = "block";\n    }}\n    </script>\n    '''render_template_string(html_content))()

def main():
    if not check_internet_connection():
        print(Fore.RED + '无法连接服务器！')
        sys.exit()
    card_key = input('请输入卡密激活：')
    if card_key != 'c37g24g7_k77-rp47--c57t-p24':
        print(Fore.RED + '卡密无效')
        sys.exit()
    print(Fore.BLUE + '\n  _____       __              ____       __       \n / ___/____  / /  ____  __   / __ )___  / /_____ _\n \\__ \\/ __ \\/ / |/_/ / / /  / __  / _ \\/ __/ __ `/\n/___/ / /_/ / />  </ /_/ /  / /_/ /  __/ /_/ /_/ / \n/____/\\____/_/_/|_|\\__, /  /_____/\\___/\\__/\\__,_/  \n                  /____/                           \n    ')
    time.sleep(10)
    print(Fore.BLUE + 'Solxy Pro正在连接服务器【Verion Beta】')
    time.sleep(5)
    print(Fore.RED + '[+]最新的CL绕过网易更新')
    print(Fore.RED + '[+]使用RAS算法加密，如果你要逆向分析此程序，那么你会非常棘手')
    print(Fore.RED + '[+]更新服务器的漏洞，修复已知的Bug')
    cookies = input('请输入Cookies账号：')
    if not validate_cookies(cookies):
        print(Fore.RED + 'Cookies账号有误！')
        sys.exit()
    time.sleep(5)
    print(Fore.BLUE + f'''[{current_time()}] [main/INFO]: Loading tweak class name net.minecraftforge.fml.common.launcher.FMLTweaker''')
    print(Fore.BLUE + f'''[{current_time()}] [main/INFO]: Using primary tweak class name net.minecraftforge.fml.common.launcher.FMLTweaker''')
    print(Fore.BLUE + f'''[{current_time()}] [main/INFO]: Loading tweak class name optifine.OptiFineForgeTweaker''')
    time.sleep(0.5)
    print(Fore.BLUE + f'''[{current_time()}] [main/INFO]: Calling tweak class net.minecraftforge.fml.common.launcher.FMLTweaker''')
    print(Fore.BLUE + f'''[{current_time()}] [main/INFO]: Forge Mod Loader version 14.23.5.2859 for Minecraft 1.12.2 loading''')
    print(Fore.BLUE + f'''[{current_time()}] [main/INFO]: Java is Java HotSpot(TM) 64-Bit Server VM, version 1.8.0_301, running on Windows 10:amd64:10.0, installed at C:\\Program Files\\Java\\jre1.8.0_301''')
    time.sleep(0.5)
    print(Fore.BLUE + f'''[{current_time()}] [main/INFO]: Searching C:\\Users\\Administrator\\Desktop\\.minecraft\\mods for mods''')
    print(Fore.BLUE + f'''[{current_time()}] [main/INFO]: Loading tweaker guichaguri.betterfps.tweaker.BetterFpsTweaker''')
    print(Fore.BLUE + f'''[{current_time()}] [main/INFO]: Loading tweaker org.spongepowered.asm.launch.MixinTweaker''')
    print(Fore.BLUE + f'''[{current_time()}] [main/WARN]: Found FMLCorePluginContainsFMLMod marker in 进花雨庭必备1.jar. This is not recommended, @Mods should be in a separate jar from the coremod.''')
    print(Fore.BLUE + f'''[{current_time()}] [main/WARN]: The coremod base.coremod.TransformerTrigger does not have a MCVersion annotation, it may cause issues with this version of Minecraft''')
    time.sleep(1)
    print(Fore.BLUE + f'''[{current_time()}] [main/WARN]: The coremod germmod (base.coremod.TransformerTrigger) is not signed!''')
    time.sleep(1)
    print(Fore.BLUE + f'''[{current_time()}] [main/INFO]: [optifine.OptiFineForgeTweaker:dbg:56]: OptiFineForgeTweaker: acceptOptions''')
    print(Fore.BLUE + f'''[{current_time()}] [main/INFO]: [optifine.OptiFineForgeTweaker:dbg:56]: OptiFineForgeTweaker: injectIntoClassLoader''')
    time.sleep(1)
    print(Fore.BLUE + f'''[{current_time()}] [main/INFO]: [optifine.OptiFineClassTransformer:dbg:242]: OptiFine ClassTransformer''')
    print(Fore.BLUE + f'''[{current_time()}] [main/INFO]: [optifine.OptiFineClassTransformer:dbg:242]: OptiFine ZIP file: C:\\Users\\Administrator\\Desktop\\.minecraft\\libraries\\optifine\\OptiFine\\1.12.2_HD_U_G5\\OptiFine-1.12.2_HD_U_G5.jar''')
    print(Fore.BLUE + f'''[{current_time()}] [main/INFO]: Loading tweak class name net.minecraftforge.fml.common.launcher.FMLInjectionAndSortingTweaker''')
    print(Fore.BLUE + f'''[{current_time()}] [main/INFO]: Loading tweak class name guichaguri.betterfps.tweaker.BetterFpsTweaker''')
    time.sleep(1)
    print(Fore.BLUE + f'''[{current_time()}] [main/INFO]: Loading tweak class name org.spongepowered.asm.launch.MixinTweaker''')
    print(Fore.BLUE + f'''[{current_time()}] [main/INFO]: SpongePowered MIXIN Subsystem Version=0.8 Source=file:/C:/Users/Administrator/Desktop/.minecraft/mods/New%20Atry%20Plus%205.0%20Crack%20by%20.jar Service=LaunchWrapper Env=CLIENT''')
    print(Fore.BLUE + f'''[{current_time()}] [main/DEBUG]: Instantiating coremod class TransformerLoader''')
    time.sleep(0.5)
    print(Fore.BLUE + f'''[{current_time()}] [main/WARN]: The coremod net.ccbluex.liquidbounce.injection.forge.TransformerLoader does not have a MCVersion annotation, it may cause issues with this version of Minecraft''')
    print(Fore.BLUE + f'''[{current_time()}] [main/WARN]: The coremod TransformerLoader (net.ccbluex.liquidbounce.injection.forge.TransformerLoader) is not signed!''')
    server_choice = input('请选择服务器编号(1.花雨庭）：')
    if server_choice == '1':
        print(Fore.BLUE + f'''[{current_time()}] [main/WARN]: The coremod net.ccbluex.liquidbounce.injection.forge.TransformerLoader does not have a MCVersion annotation, it may cause issues with this version of Minecraft''')
        print(Fore.BLUE + f'''[{current_time()}] [main/WARN]: The coremod TransformerLoader (net.ccbluex.liquidbounce.injection.forge.TransformerLoader) is not signed!''')
        print(Fore.BLUE + f'''[{current_time()}] [main/DEBUG]: Enqueued coremod TransformerLoader''')
        print(Fore.BLUE + f'''[{current_time()}] [main/WARN]: Tweak class name optifine.OptiFineForgeTweaker has already been visited -- skipping''')
        print(Fore.BLUE + f'''[{current_time()}] [main/INFO]: Loading tweak class name net.minecraftforge.fml.common.launcher.FMLDeobfTweaker''')
        print(Fore.BLUE + f'''[{current_time()}] [main/INFO]: Calling tweak class net.minecraftforge.fml.common.launcher.FMLInjectionAndSortingTweaker''')
        print(Fore.BLUE + f'''[{current_time()}] [main/INFO]: Calling tweak class net.minecraftforge.fml.relauncher.CoreModManager$FMLPluginWrapper''')
    time.sleep(5)
# WARNING: Decompyle incomplete

if __name__ == '__main__':
    main()
    return None
