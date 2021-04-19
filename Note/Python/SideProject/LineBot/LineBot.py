from sys import version as python_version
from cgi import parse_header, parse_multipart
import socketserver as socketserver
import http.server
from http.server import SimpleHTTPRequestHandler as RequestHandler
from urllib.parse import parse_qs
import json
import requests
import aiml



#Token
auth_token='oJ+WWI5mwRYYiliBK0qmFJiwh/NXHrVn2vhgoBULmGfeXOHjjRSqcLq0Wrvqh1lIw6M0pUdzcetNw67LTAHooexFMHWW1On6lSLhZE06ZDrQNe0QK8cfiDxfqjyHx/0zku93lyRRNl9COyxJ/nBKjQdB04t89/1O/w1cDnyilFU='

class MyHandler(RequestHandler):
    def do_HEAD(self):
        self.send_response(200)
        self.end_headers()

    def do_POST(self):

        #取得透過HTTP POST傳出的資料長度
        varLen = int(self.headers['Content-Length'])

        #大於0，意指有收到資料。
        if varLen > 0:
            #讀取收到的資料，資料為dict型態。
            post_data = self.rfile.read(varLen)

            #故使用json格式讀取。
            data = json.loads(post_data)

            #回應用的Token
            replyToken=data['events'][0]['replyToken']

            #傳出訊息的USER ID
            userId=data['events'][0]['source']['userId']

            #收到的訊息
            text=data['events'][0]['message']['text']

        text=text.lower()
        text=text.lstrip()
        print('收到訊息')
        print('User ID：'+userId)
        print('text：'+text)
        response = kernel.respond(text)

        if response=="":
            response='貼心提示，可以從選單上查看指令喔。'
        response=response.replace('\\n','\n')
        print("自動回覆訊息",response)



        #表頭處理
        self.do_HEAD()

        #手刻回應訊息格式。
        message = {
            "replyToken":replyToken,
            "messages": [
                    {
                        "type": "text", #回應訊息的型態。
                        "text": response
                    }
                ]
            }

        #準備要回傳給LINE API 的表頭處理
        hed = {'Authorization': 'Bearer ' + auth_token}
        #LINE  API的回傳用URL
        url = 'https://api.line.me/v2/bot/message/reply'
        #以POST送出給LINE API
        response = requests.post(url, json=message, headers=hed)

        #確認POST結果
        print(response)





#-------------------------------------------------------------------

kernel=aiml.Kernel()
kernel.learn('LineBot_AIML.xml')
print('AIML already...')
socketserver.TCPServer.allow_reuse_address = True
httpd = socketserver.TCPServer(('0.0.0.0', 8000), MyHandler)
print('Server already')
httpd.serve_forever()
