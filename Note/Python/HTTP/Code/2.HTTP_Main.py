import sys
if (sys.version_info >(3,0)):
    import socketserver
    import http.server
    from http.server import SimpleHTTPRequestHandler as RequestHandler
else:
    import SocketServer as socketserver
    import BaseHTTPServer
    from SimpleHTTPServer import SimpleHttpRequestHandler as RequestHandler
#檢查是否有被給予參數
if sys.argv[1:]:
    #有參數即接收參數的數值去指定port
    port=int(sys.argv[1])
else:
    #預設 8888
    port = 8888

#顯示收到的port
print('Server Listening on port %s'% port)

#能改善佔據Port而產生的問題
socketserver.TCPServer.allow_reuse_address=True

#宣告主體
#參數((Host,Port),Handler)
httpd=socketserver.TCPServer(('0.0.0.0',port),RequestHandler)

#正式上線
try:
    #這段Code執行會出現無限迴圈，等待網頁的請求。
    #需要離開時按下CTRL+C即可
    httpd.serve_forever()
except:
    print('關閉伺服器')
    #一樣用完要記得關閉
    httpd.server_close()
