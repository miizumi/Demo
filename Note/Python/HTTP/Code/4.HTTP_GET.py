import sys
import socketserver
import http.server
from http.server import SimpleHTTPRequestHandler as RequestHandler
#此次範例新增引用
import time
from urllib.parse import urlparse   #轉換URL用


#函式-------------------------------------------------------------

class MyHandler(RequestHandler):
    #處理表頭的方法
    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-type","text/html")

        self.end_headers()
    def do_GET(self):
        #取得並解析完整的URL
        query=urlparse(self.path).query

        #上述方法取得的值長這樣。
        #path:   /?name=admin&password=123
        #query： name=admin&password=123


        #老師教學將宣告變數放在這，並先以byte字串表示，但其實不用做，只是方便同學理解。
        #name=b""
        #password=b""

        #當HTTP GET有收到值的時候作動
        if query!="":
            #取得資料，以下會取得URL中「?name=admin&password=123」的這段資料。   #翻譯：components=成分、零件
            query_components=dict(qc.split("=") for qc in query.split("&"))

            #宣告變數放入取得的值
            name=query_components["name"]           #取得name的值
            password=query_components["password"]   #取得password的值

        self.do_HEAD() #在這裡做表頭處理。

        #刻上要回傳的HTML格式與內容。-----------------------
        output=b""
        output+=b"<html><body>Hello name="
        #收到的資料要轉成UTF-8
        output+=name.encode('utf-8')
        output+=b",password="
        output+=password.encode('utf-8')
        output+=b"</body></html>"
        #刻到這裡結束，刻這種東西很累，盡量找其他IDE輔助完成較不會出錯。

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
