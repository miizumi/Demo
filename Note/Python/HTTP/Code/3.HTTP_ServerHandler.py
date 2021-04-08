import sys

import socketserver
import http.server
from http.server import SimpleHTTPRequestHandler as RequestHandler


#函式-------------------------------------------------------------

#繼承原先的HTTP反應類別
class MyHandler(RequestHandler):
    #重寫原有的回應方法，此方法會在被網頁要求回應的時候啟動。
    def do_GET(self):
        self.send_response(200)                     #回傳一個正確的回應。
        self.send_header("Content-type","text/html")#設定反應格式為文字。

        self.end_headers()  #HTTP表頭處理完畢
        print(self.wfile)   #這是回傳給網頁要求的相關變數

        output=b""      #這邊宣告新的變數裡面放新的網頁內容，並轉成Byte字串
        output+=b"<html><body>Successfull!!!</body></html>" #這裡還不能使用中文
        self.wfile.write(output)    #寫入新的網頁內容


#主要程式內容--------------------------------------------------------


if sys.argv[1:]:
    port=int(sys.argv[1])
else:
    port = 8888


print('Server Listening on port %s'% port)
socketserver.TCPServer.allow_reuse_address=True

#宣告主體，記得要換上新的反應類別。
httpd=socketserver.TCPServer(('0.0.0.0',port),MyHandler)

try:
    httpd.serve_forever()
except:
    print('關閉伺服器')
    #一樣用完要記得關閉
    httpd.server_close()
