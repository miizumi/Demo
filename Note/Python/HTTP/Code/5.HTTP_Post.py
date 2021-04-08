import sys
import time
import socketserver
import http.server
from http.server import SimpleHTTPRequestHandler as RequestHandler
#本次新增引用函式庫
from urllib.parse import parse_qs


#函式-------------------------------------------------------------

class MyHandler(RequestHandler):
    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-type","text/html")

        self.end_headers()
    def do_POST(self):
        #取得傳遞來的資料長度
        varLen=int(self.headers["Content-Length"])

        #當HTTP POST有收到值的時候作動
        if varLen>0:
            #取得並解析完整的URL
            query_components=parse_qs(self.rfile.read(varLen),keep_blank_values=1)

            print(query_components)
            #取值放入變數
            name=query_components[b"name"][0]
            password=query_components[b"password"][0]



        self.do_HEAD()

        #刻上要回傳的HTML格式與內容。

        output=b""
        output+=b"<html><body>Hello name="
        #收到的資料要轉成UTF-8
        output+=name
        output+=b",password="
        output+=password
        output+=b"</body></html>"

        self.wfile.write(output)


#主要程式內容--------------------------------------------------------


if sys.argv[1:]:
    port=int(sys.argv[1])
else:
    port = 8888


print('Server Listening on port %s'% port)
socketserver.TCPServer.allow_reuse_address=True

httpd=socketserver.TCPServer(('0.0.0.0',port),MyHandler)

try:
    httpd.serve_forever()
except:
    print('關閉伺服器')
    httpd.server_close()
