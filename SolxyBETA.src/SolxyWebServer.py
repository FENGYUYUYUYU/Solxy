# File: SolxyWebServer.pyc (Python 3.12)

from flask import Flask, render_template_string
app = Flask(__name__)
index = (lambda : render_template_string('\n        <html>\n            <head>\n                <title>卡密BOT</title>\n            </head>\n            <body>\n                <h1>欢迎使用卡密BOT</h1>\n                <button onclick="location.href=\'/get_bot\'">获取卡密BOT</button>\n                <button onclick="location.href=\'/about_author\'">关于作者</button>\n                <button onclick="location.href=\'/buy_bot\'">购买卡密</button>\n            </body>\n        </html>\n    '))()
get_bot = (lambda : render_template_string('\n        <html>\n            <head>\n                <title>卡密BOT</title>\n            </head>\n            <body>\n                <h1>获取卡密BOT</h1>\n                <p>c37g24g7_k77-rp47--c57t-p24</p>\n                <button onclick="location.href=\'/\'">返回首页</button>\n            </body>\n        </html>\n    '))()
about_author = (lambda : render_template_string('\n        <html>\n            <head>\n                <title>关于作者</title>\n            </head>\n            <body>\n                <h1>关于作者</h1>\n                <p>星际文化：JacaScript后端开发架构师：KUN X</p>\n                <p>Solxy Pro强大的功能更新</p>\n                <p>[+]团队最新写入CL无视网易更新</p>\n                <p>[+]使用最新的RAS算法加密采用非对称加密方式，如果你要逆向分析此程序那么你可能会非常棘手</p>\n                <p>[+]服务器防火墙升级</p>\n                <p>[+]绕过最新的网易开端</p>\n                <button onclick="location.href=\'/\'">返回首页</button>\n            </body>\n        </html>\n    '))()
buy_bot = (lambda : render_template_string('\n        <html>\n            <head>\n                <title>购买卡密</title>\n            </head>\n            <body>\n                <h1>购买卡密</h1>\n                <p>本卡密仅需1.99r即可永久使用！由于服务器成本，算法的成本所以使用加密卡密，望谅解！</p>\n                <img src="https://via.placeholder.com/150" alt="支付图片">\n                <button onclick="location.href=\'/\'">返回首页</button>\n            </body>\n        </html>\n    '))()
if __name__ == '__main__':
    app.run(debug = True)
    return None
